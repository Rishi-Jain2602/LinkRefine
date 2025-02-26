from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    max_retries=2,
)
client = Groq()