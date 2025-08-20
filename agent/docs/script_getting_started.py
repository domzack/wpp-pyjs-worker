import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import os

# Base da documentação
BASE_URL = "https://docs.agno.com/examples"

# Estrutura das seções e páginas
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

# Pasta de saída
OUTPUT_DIR = "agno_docs_mdx_content"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# Função para extrair e salvar conteúdo da div .mdx-content
def extract_mdx_content(section, page):
    url = f"{BASE_URL}/{section}/{page}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Erro ao acessar {url}: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    mdx_div = soup.find("div", class_="mdx-content")

    if not mdx_div:
        print(f"⚠️ .mdx-content não encontrada em {url}")
        return

    markdown = md(str(mdx_div), heading_style="ATX")
    filename = os.path.join(OUTPUT_DIR, f"{section}__{page}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"✅ {section}/{page} salvo com sucesso!")


# Loop por todas as páginas
for section, pages in sections.items():
    for page in pages:
        extract_mdx_content(section, page)
