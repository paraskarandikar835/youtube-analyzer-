
import os
from textwrap import dedent

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.youtube import YouTubeTools

# Load API keys from .env
load_dotenv()

if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY is missing from your .env file")


def build_youtube_agent():
    return Agent(
        name="YouTube Agent",
        model=Gemini(
            id="gemini-3.8-flash",
            api_key=os.getenv("GEMINI_API_KEY"),
        ),
        tools=[YouTubeTools()],
       
instructions=dedent("""
    You are an expert YouTube content analyst.

    Analyze the video and return one concise report containing:

    1. Video Overview
       - Main topic, purpose, and video type.

    2. Timestamped Summary
       - Main sections with accurate timestamps when available.

    3. Key Takeaways
       - Important concepts and practical examples.

    4. Study Notes
       - Essential definitions and three revision questions.

    Guidelines:
    - Use clear headings, bullets, and relevant emojis.
    - Explain technical concepts simply.
    - Avoid repetition and unnecessary detail.
    - Never invent video content or timestamps.
    - State clearly if captions are unavailable.
"""),

        markdown=True,
    )


if __name__ == "__main__":
    youtube_agent = build_youtube_agent()

    youtube_agent.print_response(
        "Analyze this YouTube video: "
        "https://www.youtube.com/watch?v=MdPEFO3oVm0",
        stream=True,
    )
