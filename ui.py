
import streamlit as st
from youtube_Analyzer import build_youtube_agent

st.set_page_config(
    page_title="YouTube Video Analyzer",
    page_icon="🎥",
    layout="centered",
)

st.title("🎥 AI YouTube Video Analyzer")
st.caption("Turn YouTube videos into summaries and study notes.")

@st.cache_resource
def get_agent():
    return build_youtube_agent()


@st.cache_data(ttl=3600, show_spinner=False)
def analyze_video(video_url):
    agent = get_agent()
    response = agent.run(
        f"Analyze this YouTube video: {video_url}"
    )
    return response.content


video_url = st.text_input(
    "Enter YouTube Video Link",
    placeholder="https://www.youtube.com/watch?v=..."
)

if st.button("Analyze Video", type="primary"):
    if not video_url.strip():
        st.warning("Please enter a YouTube video link.")
    elif "youtube.com/" not in video_url and "youtu.be/" not in video_url:
        st.warning("Please enter a valid YouTube URL.")
    else:
        try:
            with st.spinner(
                "Fetching the video transcript and generating your report..."
            ):
                report = analyze_video(video_url.strip())

            st.success("Analysis completed!")
            st.markdown("## 📚 Analysis Report")
            st.markdown(report)

        except Exception as e:
            st.error(
                "Analysis failed. Please try again or check whether "
                "the video has accessible captions."
            )
            st.caption(f"Error details: {e}")
