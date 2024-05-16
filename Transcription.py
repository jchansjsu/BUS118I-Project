import streamlit as st
from openai import OpenAI
from pathlib import Path


client = OpenAI(api_key="your_api_key_here")


# Set the page configuration
st.set_page_config(
   page_title="Audio Transcription and Analysis",
   page_icon=":microphone:",
   layout="wide",
   initial_sidebar_state="expanded"
)


audio_file_path = Path(__file__).parent / 'speech.mp3'
print("Audio File Path: ", audio_file_path)
audio_file = open(audio_file_path, 'rb')
audio_bytes = audio_file.read()
# st.write("Transcribing and Summarizing Audio file... Please wait for the results...")


def speech_to_text(audio_file_path):
   # Load the audio file
   audio_file = open(audio_file_path, 'rb')
   audio_bytes = audio_file.read()


   # Display the audio file
   st.audio(audio_bytes, format='audio/mp3')


   # Convert the audio file to text
   # Call the OpenAI API to convert speech to text
   # Replace the API key with your
   response = client.audio.transcriptions.create(
       model="whisper-1",
       file=audio_file_path
   )
   return response.text


def summarize_text(text):
   response = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages = [
           {"role": "system", "content": "System message: Summarize the text."},
           {"role": "user", "content": text}
       ]
   )
   return response.choices[0].message.content


def sentiment_analysis(text):
   response = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages = [
           {"role": "system", "content": "System message: Give me Sentiment Analysis on this text."},
           {"role": "user", "content": text}
       ]
   )
   return response.choices[0].message.content


def action_items(text):
   response = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages = [
           {"role": "system", "content": "System message: Give me action items of this text."},
           {"role": "user", "content": text}
       ]
   )
   return response.choices[0].message.content


# Function to load and apply CSS styles
def load_css():
   st.markdown("""
   <style>
   body {
       color: #555;
       background-color: #f4f4f8;
       font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
   }
   .stMarkdown, .stButton, .stTextInput {
       border-radius: 8px;
       box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
   }
   .sidebar .sidebar-content {
       background-color: #f0f0f5;
       padding: 10px;
   }
   h1 {
       text-align: center;
       font-size: 2em;
       text-shadow: 0 0 10px rgba(0,0,0,0.2);
       color: #4ABDAC; /* relaxing teal color */
   }
   h2, h3 {
       color: #3e4b5b;
       text-align: center;
   }
   .css-1aumxhk {
       background-color: #f0f0f5;
       border-color: #666;
   }
   .stButton>button {
       color: #fff;
       background-color: #4a69bd;
       border-color: #4a69bd;
       font-size: 1em;
       padding: 8px 24px;
       width: 100%;
       margin: 5px 0;
   }
   .stMarkdown {
       text-align: center;
   }
   </style>
   """, unsafe_allow_html=True)


# Load the CSS styles
load_css()


# Main application logic here
st.header('Audio File Transcription and Analysis')
st.sidebar.header('Settings and Options')


# Example of how to use the custom radio buttons in sidebar with your custom settings
option = st.sidebar.radio(
   "Choose Analysis Type:",
   ["Summary", "Sentiment Analysis", "Action Items"]
)


# Display based on chosen option
if option == "Summary":
   st.subheader("Meeting Summary")
   # Assuming you have a function to get the summary
   responseText = speech_to_text(audio_file_path)
   summaryText = summarize_text(responseText)
   st.write(summaryText)
elif option == "Sentiment Analysis":
   st.subheader("Sentiment Analysis")
   responseText = speech_to_text(audio_file_path)
   sentimentText = sentiment_analysis(responseText)
   st.write(sentimentText)
elif option == "Action Items":
   st.subheader("Action Items")
   responseText = speech_to_text(audio_file_path)
   actionItemsText = action_items(responseText)
   st.write(actionItemsText)


# Include more interactive widgets as needed
