import openai
from dotenv import load_dotenv
import os

load_dotenv("./.env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Importações necessárias
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool  # Para definir ferramentas customizadas
from agno.storage.sqlite import SqliteStorage  # Para armazenar pedidos e estoque
import sqlite3  # Para inicializar o banco de dados
from typing import Dict, List, Optional
from pydantic import BaseModel


# Inicialize o banco de dados SQLite para estoque e pedidos
DB_FILE = "lanchonete.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Tabela de estoque
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS estoque (
            item TEXT PRIMARY KEY,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
        """
    )

    # Tabela de pedidos
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pedidos (
            pedido_id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id TEXT NOT NULL,
            nome TEXT NOT NULL,
            remetente TEXT NOT NULL,
            itens TEXT NOT NULL,
            status TEXT NOT NULL,
            total REAL NOT NULL
        )
        """
    )

    # Tabela de feedback dos clientes
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS feedback (
            feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id TEXT NOT NULL,
            tipo TEXT NOT NULL,         -- 'anotacao', 'sugestao', 'reclamacao'
            mensagem TEXT NOT NULL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    # Insira itens iniciais no estoque se a tabela estiver vazia
    cursor.execute("SELECT COUNT(*) FROM estoque")
    if cursor.fetchone()[0] == 0:
        itens_iniciais = [
            ("Hambúrguer", 15.0, 50),
            ("Batata Frita", 8.0, 100),
            ("Refrigerante", 5.0, 200),
            ("Sorvete", 7.0, 30),
            ("Sanduíche Vegetariano", 12.0, 40),
        ]
        cursor.executemany(
            "INSERT INTO estoque (item, preco, quantidade) VALUES (?, ?, ?)",
            itens_iniciais,
        )

    conn.commit()
    conn.close()


init_db()  # Inicialize o DB na primeira execução


# Defina ferramentas customizadas para o agente
@tool
def get_menu() -> Dict[str, Dict[str, float]]:
    """Retorna o cardápio completo com itens, preços e estoque disponível."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT item, preco, quantidade FROM estoque")
    menu = {
        row[0]: {"preco": row[1], "quantidade": row[2]} for row in cursor.fetchall()
    }
    conn.close()
    return menu


@tool
def check_stock(item: str) -> int:
    """Verifica a quantidade disponível no estoque para um item específico."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT quantidade FROM estoque WHERE item = ?", (item,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0


def _check_stock(item: str) -> int:
    """Função auxiliar para verificar a quantidade disponível no estoque."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT quantidade FROM estoque WHERE item = ?", (item,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0


class PedidoItem(BaseModel):
    item: str
    quantidade: int


@tool
def place_order(
    cliente_id: str, nome: str, remetente: str, itens: List[PedidoItem]
) -> int:
    """
    Registra um novo pedido. Itens é uma lista de PedidoItem {'item': str, 'quantidade': int}.
    Recebe nome e remetente do cliente. Retorna o ID do pedido.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    total = 0.0
    itens_str = []
    for i in itens:
        item = i.item
        qtd = i.quantidade
        if _check_stock(item) < qtd:
            raise ValueError(f"Estoque insuficiente para {item}")
        preco = get_menu().get(item, {}).get("preco", 0)
        total += preco * qtd
        itens_str.append(f"{item}: {qtd}")

    cursor.execute(
        "INSERT INTO pedidos (cliente_id, nome, remetente, itens, status, total) VALUES (?, ?, ?, ?, ?, ?)",
        (cliente_id, nome, remetente, ", ".join(itens_str), "pendente", total),
    )
    pedido_id = cursor.lastrowid

    # Atualize estoque
    for i in itens:
        update_stock(i.item, -i.quantidade)

    conn.commit()
    conn.close()
    return pedido_id


@tool
def update_stock(item: str, delta: int) -> None:
    """Atualiza o estoque de um item adicionando/subtraindo a quantidade (delta pode ser negativo)."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE estoque SET quantidade = quantidade + ? WHERE item = ?", (delta, item)
    )
    conn.commit()
    conn.close()


@tool
def check_order_status(pedido_id: int) -> Dict[str, str]:
    """Verifica o status de um pedido pelo ID."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT status, itens, total, nome, remetente FROM pedidos WHERE pedido_id = ?",
        (pedido_id,),
    )
    result = cursor.fetchone()
    conn.close()
    if result:
        return {
            "status": result[0],
            "itens": result[1],
            "total": result[2],
            "nome": result[3],
            "remetente": result[4],
        }
    return {"error": "Pedido não encontrado"}


@tool
def save_feedback(cliente_id: str, tipo: str, mensagem: str) -> str:
    """
    Salva um feedback do cliente (anotação, sugestão ou reclamação) para consulta futura pelo gestor.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO feedback (cliente_id, tipo, mensagem) VALUES (?, ?, ?)",
        (cliente_id, tipo, mensagem),
    )
    conn.commit()
    conn.close()
    return "Feedback registrado com sucesso. Obrigado por compartilhar!"


# Configuração do Agente Agno
armazenamento = SqliteStorage(
    table_name="sessao_lanchonete", db_file=DB_FILE
)  # Para histórico de conversas

agente_atendente = Agent(
    name="Atendente Lanchonete",
    model=OpenAIChat(id="gpt-3.5-turbo"),  # Troque para modelo disponível
    tools=[
        get_menu,
        check_stock,
        place_order,
        update_stock,
        check_order_status,
        save_feedback,
    ],
    instructions=[
        "Você é um atendente de lanchonete amigável e humanizado.",
        "Busque conhecer o cliente, pergunte nome, preferências e registre o pedido vinculado ao nome e remetente.",
        "Ao registrar um pedido, sempre utilize a ferramenta informando todos os parâmetros obrigatórios: cliente_id, nome, remetente e a lista de itens e quantidades (itens).",
        "Nunca tente registrar um pedido sem a lista de itens (itens). Sempre confirme os itens do pedido com o cliente antes de chamar a ferramenta.",
        "Ao chamar a ferramenta place_order, forneça os itens como uma lista de objetos no formato [{'item': nome_do_item, 'quantidade': quantidade}], por exemplo: [{'item': 'Hambúrguer', 'quantidade': 2}, {'item': 'Batata Frita', 'quantidade': 1}].",
        "Saúde o cliente e ofereça o cardápio se necessário.",
        "Sugira itens relacionados (ex: batata frita com hambúrguer).",
        "Confirme o pedido antes de registrar.",
        "Após registrar o pedido, informe ao cliente o número do pedido (pedido_id) gerado.",
        "Ao registrar um pedido usando a ferramenta, sempre forneça o identificador do cliente e a lista de itens e quantidades.",
        "Sempre que listar os itens do pedido do cliente, informe o valor individual de cada item e o valor total do pedido.",
        "Atualize o estoque após pedidos.",
        "Se estoque baixo, sugira alternativas.",
        "Mantenha o tom conversacional e empático.",
        "Use ferramentas para consultar menu, estoque e pedidos.",
        "Se o cliente quiser deixar uma anotação, sugestão ou reclamação, utilize a ferramenta de feedback para registrar e garantir que o gestor possa consultar depois.",
    ],
    storage=armazenamento,  # Para manter contexto multi-turn
    add_history_to_messages=True,
    num_history_runs=10,  # Manter histórico recente
    markdown=True,  # Respostas formatadas
    debug_mode=True,  # Para depuração
)


# Função para integração com WhatsApp
def processar_mensagem_whatsapp(remetente: str, shortname: str, body: str):
    """
    Processa uma mensagem recebida do WhatsApp e retorna a resposta do agente.
    Usa o id do remetente como session_id e user_id para garantir memória individual.
    """
    # O agente vai vincular o usuário pelo remetente_id
    resposta = agente_atendente.run(
        body,
        session_id=remetente,  # Memória individual por usuário
        user_id=remetente,
        # Opcional: pode adicionar dados extras do usuário se desejar
        user_data={"remetente": remetente, "shortname": shortname},
    )
    return resposta.content


# # Loop principal para interagir com o usuário
# if __name__ == "__main__":
#     print("Bem-vindo à Lanchonete! Como posso ajudar? (Digite 'sair' para encerrar)")
#     # Simulação: substitua pelo loop do seu chat WhatsApp
#     while True:
#         remetente_id = input("ID do cliente (WhatsApp): ")
#         if remetente_id.lower() == "sair":
#             break
#         name = input("Nome: ")
#         shortname = input("Apelido: ")
#         body = input("Mensagem recebida: ")
#         resposta = processar_mensagem_whatsapp(remetente_id, name, shortname, body)
#         print(f"Atendente: {resposta}")
