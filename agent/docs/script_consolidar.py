import os
from pathlib import Path

ROOT = Path(r"./agno")
OUT = Path(r"./AGNO.md")
EXCLUDE_DIRS = {"node_modules", ".git", ".venv", ".venvs", "__pycache__"}
EXTS = {".md", ".mdx", ".markdown"}


def is_excluded(path: Path):
    return any(part in EXCLUDE_DIRS for part in path.parts)


def gather_files(root: Path):
    files = []
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in EXTS and not is_excluded(p):
            files.append(p)
    return sorted(files)


def read_file(path: Path):
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="latin-1")
        except Exception as e:
            return f"_Erro ao ler {path}: {e}_"


def main():
    if not ROOT.exists():
        print(f"❌ Diretório não encontrado: {ROOT}")
        return
    OUT.parent.mkdir(parents=True, exist_ok=True)
    files = gather_files(ROOT)
    if not files:
        print("⚠️ Nenhum arquivo .md/.mdx encontrado em docs/agno")
        return

    with OUT.open("w", encoding="utf-8") as out:
        out.write("# Agno — Documentação Consolidada\n\n")
        out.write(f"_Gerado de: {ROOT.resolve()}_\n\n")
        for p in files:
            rel = p.relative_to(ROOT)
            out.write(f"---\n\n## {rel}\n\n")
            content = read_file(p)
            out.write(content.strip() + "\n\n")
    print(f"✅ Consolidado gerado em: {OUT}")


if __name__ == "__main__":
    main()
