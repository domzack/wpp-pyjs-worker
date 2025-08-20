import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import os

# URL base da documentação
BASE_URL = "https://docs.agno.com/examples"

# Estrutura completa da documentação
sections = {
    "getting-started": [
        "introduction",
        "basic-agent",
        "agent-with-tools",
        "agent-with-knowledge",
        "agent-with-storage",
        "agent-team",
        "structured-output",
        "custom-tools",
        "research-agent",
        "research-workflow",
        "image-agent",
        "image-generation",
        "video-generation",
        "audio-agent",
        "agent-state",
        "agent-context",
        "agent-session",
        "user-memories",
        "retry-functions",
        "human-in-the-loop",
    ],
    "agents": [
        "finance-agent",
        "tweet-analysis-agent",
        "eval-agent",
        "image-agent",
        "audio-agent",
        "video-agent",
        "multimodal-agent",
        "rag-agent",
        "reasoning-agent",
        "memory-agent",
        "storage-agent",
        "tools-agent",
        "vector-db-agent",
        "context-agent",
        "agent-state",
        "observability-agent",
        "testing-agent",
    ],
    "teams": [
        "team-coordination",
        "team-collaboration",
        "team-finance",
        "team-research",
        "team-multimodal",
    ],
    "workflows": [
        "workflow-basic",
        "workflow-finance",
        "workflow-research",
        "workflow-multimodal",
        "workflow-memory",
        "workflow-tools",
        "workflow-storage",
    ],
    "workflows-v2": [
        "workflow-v2-intro",
        "workflow-v2-finance",
        "workflow-v2-research",
        "workflow-v2-multimodal",
    ],
    "applications": ["streamlit-dashboard", "fastapi-server", "agent-cli", "agent-api"],
    "streamlit-apps": [
        "streamlit-finance",
        "streamlit-research",
        "streamlit-multimodal",
    ],
    "evals": ["eval-performance", "eval-memory", "eval-tools", "eval-storage"],
}

# Pasta onde os arquivos Markdown serão salvos
OUTPUT_DIR = "agno_docs_markdown"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# Função para baixar e converter cada página
def fetch_and_convert(section, page):
    url = f"{BASE_URL}/{section}/{page}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Erro ao acessar {url}: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Título da página
    title_tag = soup.find("title")
    title = title_tag.text.strip() if title_tag else page.replace("-", " ").title()

    # Conteúdo principal
    content_div = soup.find("main") or soup.find("article") or soup.body
    if not content_div:
        print(f"⚠️ Conteúdo não encontrado em {url}")
        return

    # Converter HTML para Markdown
    markdown = f"# {title}\n\n" + md(str(content_div), heading_style="ATX")

    # Nome do arquivo
    filename = os.path.join(OUTPUT_DIR, f"{section}__{page}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"✅ {section}/{page} convertido com sucesso!")


# Executar para todas as seções e páginas
for section, pages in sections.items():
    for page in pages:
        fetch_and_convert(section, page)
