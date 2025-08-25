from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app

from agno.storage.sqlite import SqliteStorage

import openai
from dotenv import load_dotenv
import os

load_dotenv("./.env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

storage = SqliteStorage(table_name="history", db_file="./db/agent_domsweet.db")


def EstoqueTool():
    """
    Retorna o estoque atual de salgadinhos e bebidas.
    """
    estoque = {
        "salgadinho": {"preco": 12.0, "qtd": 20},
        "coxinha": {"preco": 8.0, "qtd": 15},
        "coca-cola": {"preco": 5.0, "qtd": 10},
        "suco de laranja": {"preco": 6.0, "qtd": 8},
        "pão de queijo": {"preco": 4.0, "qtd": 25},
        "pastel de carne": {"preco": 7.0, "qtd": 12},
    }
    return estoque


instructions = """
        Você é um atendente de padaria, Seu trabalho é atender aos clientes com
        elegancia e simpatia, sempre buscando a melhor solução para suas necessidades.
        
        Se o cliente solicitar algum produto, verifique a disponibilidade no estoque e informe o preço.

        Caso nao exista, informe que o produto não está disponível e pergunte se ele deseja visualizar 
        os itens disponiveis.

        Quando for exibir o estoque, faca em formato de linha. um item por linha e o valor.
        Exiba apenas itens disponíveis no estoque.

        Se o cliente solicitar o valor total de um pedido, some os valores dos itens e informe o total.

        Quando voce for responder o cliente, sempre use um tom amigável e educado.
        se for exibir itens e valores, utilize uma abordagem do tipo: "Aqui estão os itens disponíveis no estoque:" 
        "Verifique se estão de acordo com o que você precisa."
        Se o cliente solicitar algo que não está relacionado ao estoque, utilize um tom de desculpas e informe que não pode ajudar com isso.

        """

agent = Agent(
    model=OpenAIChat(id="gpt-3.5-turbo"),
    tools=[EstoqueTool],
    instructions=instructions,
    storage=storage,
    show_tool_calls=True,
    markdown=True,
    monitoring=True,
)

app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("domsweet:app", reload=True)
