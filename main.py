import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.browser import BrowserSession

load_dotenv()

async def main():
    agent = Agent(
        task="Open example.com and print the page title",
        llm=ChatOpenAI(model="gpt-4o"),
        browser_session=BrowserSession()
    )
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
