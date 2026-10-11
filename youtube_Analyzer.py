
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

            1. Video Overview
               - Identify the main topic and purpose.
               - Identify the video type.

            2. Timestamped Summary
               - Divide the video into logical sections.
               - Summarize key points with accurate timestamps.

            3. Key Takeaways
               - List important concepts and practical examples.
               - Explain difficult concepts simply.

            4. Study Notes
               - Include definitions and revision questions.

            5. Analysis Style
               - Use clear, descriptive section titles.
               - Use relevant emojis:
                 📚 Educational
                 💻 Technical
                 🎮 Gaming
                 📱 Tech Review
                 🎨 Creative
               - Highlight key learning points and demonstrations.

            6. Quality Guidelines
               - Avoid unnecessary repetition.
               - Distinguish facts from opinions.
               - Never invent video content or timestamps.
               - Explain if captions are unavailable.
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
