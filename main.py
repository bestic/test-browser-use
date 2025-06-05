import asyncio
import base64
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from browser_use import Agent
from browser_use.browser import BrowserSession
from browser_use.agent.views import AgentSettings

load_dotenv()

async def main():
    session = BrowserSession()
    await session.navigate("https://example.com")
    page = await session.get_current_page()
    await page.wait_for_load_state()

    screenshots = Path("screenshot")
    screenshots.mkdir(exist_ok=True)
    screenshot_path = screenshots / "content.png"
    await page.locator("div#content").screenshot(path=str(screenshot_path))

    with open(screenshot_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    agent = Agent(
        task="Is there a smile icon in the provided screenshot?",
        llm=ChatOpenAI(model="gpt-4o"),
        browser_session=session,
        settings=AgentSettings(use_vision=True),
    )

    # send screenshot to the agent as initial message
    agent.message_manager._add_message_with_tokens(
        HumanMessage(
            content=[
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{img_b64}"},
                }
            ]
        )
    )

    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
