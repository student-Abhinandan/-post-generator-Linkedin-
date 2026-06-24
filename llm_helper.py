from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("Groq_Api_key"),
    model="llama-3.3-70b-versatile",
    max_tokens=200,
    )

if __name__ == "__main__":
    response = llm.invoke("what are the ingredient in the samosha")
    print(response.content)