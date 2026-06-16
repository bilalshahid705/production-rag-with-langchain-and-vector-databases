from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever        
from langchain.schema import Document
import os
from dotenv import load_dotenv

load_dotenv()

embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

