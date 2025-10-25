from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "sample_docs.csv"
FAISS_PATH = BASE_DIR / "model" / "vector_index.faiss"
DOCS_PATH = BASE_DIR / "model" / "docs.pkl"
