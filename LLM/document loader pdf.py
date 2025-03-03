from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

file_path = r"C:\Users\preshtha\PycharmProjects\PythonProject2\data\document_loader_test.pdf"
loader = PyPDFLoader(file_path)
documents = loader.load()

qa_model = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", device="cpu")

text_content = "\n".join([doc.page_content for doc in documents])

print("PDF load successfully!")

while True:
    user_input = input("\n Enter your prompt (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

    print("\n Generating reponse...")

    response = qa_model(f"Document content:\n{text_content[:1000]}\n\nUser Question: {user_input}",
                        max_new_tokens=200,
                        do_sample=True,
                        truncation=True)
    print("📝 Generated Text:", response[0]['generated_text'])