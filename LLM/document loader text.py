from langchain_community.document_loaders import TextLoader
from transformers import pipeline

file_path = r"C:\Users\preshtha\PycharmProjects\PythonProject2\data\document_loader_ai_ml.txt"
loader = TextLoader(file_path)
documents = loader.load()

text_content = "\n".join([doc.page_content for doc in documents])

print("Text file loaded successfull!")

qa_model = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", device="cpu")

while True:
    user_input = input("\n Enter Your prompt(Or type 'exit' to quite):" )

    if user_input.lower() == 'exit':
        break

    print("\n Generating response....\n")

    response = qa_model(f"Document content:\n{text_content[:1000]}\n\nUser Question: {user_input}",
                        max_new_tokens=200,
                        do_sample=True,
                        truncation=True)

    print("Generated Text:", response[0]['generated_text'])