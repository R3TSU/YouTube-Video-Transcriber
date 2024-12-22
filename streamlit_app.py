import streamlit as st
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    video = YouTube(url)
    return video.video_id

def get_transcript(video_id):
    """Get transcript for a given video ID"""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['id', 'en'])
        transcript = ' '.join([t['text'] for t in transcript_list])
        return transcript
    except Exception as e:
        return f"Error getting transcript: {str(e)}"

def main():
    st.title("YouTube Video Transcriber")
    
    # URL input
    url = st.text_input("Enter YouTube Video URL:")
    
    if url:
        try:
            video_id = get_video_id(url)
            video = YouTube(url)
            
            # Display video title
            st.subheader(video.title)
            
            # Get and display transcript
            transcript = get_transcript(video_id)
            st.text_area("Transcript", transcript, height=400)
            
            # Add download button
            st.download_button(
                label="Download Transcript",
                data=transcript,
                file_name="transcript.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()