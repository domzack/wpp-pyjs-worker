import os
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Seção Reference com páginas conhecidas
reference_pages = [
    "agents/agent",
    "teams/team",
    "workflows/workflow",
    "workflows-v2/workflow-v2",
    "models/model",
    "knowledge/knowledge",
    "vector-databases/vector-db",
    "embedders/embedder",
    "memory/memory",
    "storage/storage",
    "rerankers/reranker",
    "chunking/chunking",
    "document-reader/document-reader",
]

# Pasta de saída
OUTPUT_DIR = "agno_docs_mdx_content"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# Função para extrair e salvar conteúdo da div .mdx-content
def extract_reference_content(page_path):
    url = f"https://docs.agno.com/reference/{page_path}"
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
    filename = os.path.join(OUTPUT_DIR, f"reference_{page_path.replace('/', '__')}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"✅ reference/{page_path} salvo com sucesso!")


# Loop pelas páginas da seção Reference
for page_path in reference_pages:
    extract_reference_content(page_path)
