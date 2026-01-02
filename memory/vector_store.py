from chromadb import Client

client = Client()
collection = client.get_or_create_collection("research_memory")

def save_memory(text: str):
    collection.add(documents=[text], ids=[str(hash(text))])
