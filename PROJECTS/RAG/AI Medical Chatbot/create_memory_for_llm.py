# # Load raw pdfs
# # Create Chunks
# # Create Vector Embeddings
# # Store embeddings in FAISS


# from pathlib import Path

# from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS


# BASE_DIR = Path(__file__).resolve().parent
# DATA_PATH = BASE_DIR / "data"

# # Load Raw PDFs

# def load_pdf_files(data):
#     loader = DirectoryLoader(str(data) , glob="*.pdf" , loader_cls=PyPDFLoader)
#     documents = loader.load()
#     return documents


# documents = load_pdf_files(data=DATA_PATH)
# print("Length of PDF Pages:", len(documents))


# # Create Chunks 
# def create_chunks(extracted_data):
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500 , chunk_overlap = 50)
#     text_chunks = text_splitter.split_documents(extracted_data)
#     return text_chunks

# text_chunks = create_chunks(extracted_data = documents)
# print("Length of Text Chunks : " , len(text_chunks))


# # Create Vector Embeddings

# def get_embedding_model():
#     embedding_model = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-minilm-l6-v2")
#     return embedding_model

# embedding_model = get_embedding_model()


# # Store embeddings in FAISS

# DB_FAISS_PATH  = "vectorstore/db_faiss"

# db = FAISS.from_documents(text_chunks , embedding_model)
# db.save_local(str(DB_FAISS_PATH))

# print("FAISS vector database created successfully! ")
# print("Saved at : "  ,DB_FAISS_PATH)
      

