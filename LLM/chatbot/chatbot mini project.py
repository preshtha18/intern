import streamlit as st
from llama_cpp import Llama
from sentence_transformers import SentenceTransformer, util
import mysql.connector

MODEL_PATH = "./deepseek-llm-7b.Q4_K_M.gguf"
llm = Llama(model_path=MODEL_PATH)

sentence_model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

document_embeddings = sentence_model.encode(documents, convert_to_tensor=True)

def generate_response(prompt):
    response = llm(prompt, max_tokens=100)
    return response["choices"][0]["text"].strip()

def semantic_search(query, documents, document_embeddings):
    query_embedding = sentence_model.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, document_embeddings, top_k=1)
    return documents[hits[0][0]['corpus_id']]

def fetch_products():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MYSQL@123Pre",
        database="product_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT product_id, product_name, product_description FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products

products = fetch_products()
product_embeddings = sentence_model.encode([product[2] for product in products], convert_to_tensor=True)

def product_search(query, products, product_embeddings):
    query_embedding = sentence_model.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, product_embeddings, top_k=5)
    results = [(products[hit['corpus_id']][0], products[hit['corpus_id']][1]) for hit in hits[0]]
    return results

# Streamlit App
st.title("DeepSeek Chat Application (No Hugging Face)")

user_input = st.text_input("Ask a question:")
if st.button("Get Response"):
    response = generate_response(user_input)
    st.write("Chatbot Response:")
    st.write(response)

st.subheader("Search in Documents")
query = st.text_input("Enter search query:")
if st.button("Search Documents"):
    result = semantic_search(query, documents, document_embeddings)
    st.write("Search Result:")
    st.write(result)

st.subheader("Product Search")
product_query = st.text_input("Search for a product:")
if st.button("Search Products"):
    product_results = product_search(product_query, products, product_embeddings)
    st.write("Matching Products:")
    for product in product_results:
        st.write(f"Product ID: {product[0]}, Product Name: {product[1]}")
