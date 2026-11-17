import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv(override=True)
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

name = os.environ["INDEX_NAME"]   # your existing index name from .env

pc.delete_index(name)
pc.create_index(
    name=name,
    dimension=1536,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1"),
)
print(pc.describe_index(name))