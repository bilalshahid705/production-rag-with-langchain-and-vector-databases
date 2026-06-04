from dotenv import load_dotenv
from openai.types.responses import response
from importlib.metadata import version

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

core_version = version("langchain-core")
lg_version = version("langgraph")

print(f"LangChain Core Version: {core_version}")
print(f"LangGraph Version: {lg_version}")


def main():

   # Test OpenAI
   llm_openai = ChatOpenAI(
      model="gpt-4o-mini",
      temperature=0
   )

   response_openai = llm_openai.invoke(
      "Say 'setup complete!' in one word"
   )

   print(f"Response OpenAI: {response_openai}")

   # Test Anthropic
   llm_anthropic = ChatAnthropic(
      model="claude-sonnet-4-5-20250929",
      temperature=0
   )

   response_anthropic = llm_anthropic.invoke(
      "Say 'setup complete!' in one word"
   )

   print(f"Response Anthropic: {response_anthropic}")

   print("Setup complete!")


if __name__ == "__main__":
    main()