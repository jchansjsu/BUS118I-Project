import streamlit as st
from openai import OpenAI
from pathlib import Path


# Setup the OpenAI client
client = OpenAI(api_key="you_api_key_here")
speech_file_path = Path(__file__).parent / "speech.mp3"


# Define the function to get a completion from OpenAI
def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(model=model,
       messages=[
           {"role": "system", "content": "System message: Provide guidance."},
           {"role": "user", "content": prompt},
       ])
   return completion.choices[0].message.content


def text_to_speech(text, path):
   response = client.audio.speech.create(
       model="tts-1",
       voice="nova",
       input=text
   )
   response.stream_to_file(path)


# Load CSS to style the page
def load_css():
   st.markdown("""
   <style>
   body {
       color: #333;
       background-color: #f4f4f8;
       font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
   }
   .stButton>button {
       color: #fff;
       background-color: #4a69bd;
       border-color: #4a69bd;
       font-size: 16px;
       padding: 10px 20px;
       width: 100%;
       border-radius: 20px;
       transition: background-color 0.3s, border-color 0.3s;
   }
   .stButton>button:hover {
       background-color: #357ABD;
       border-color: #357ABD;
   }
   .stTextInput {
       padding: 10px;
   }
   .css-2trqyj {
       padding-bottom: 10px;
   }
   </style>
   """, unsafe_allow_html=True)


load_css()


# Create the Streamlit app interface
with st.form(key="chat"):
   st.markdown("## Support for Homeless Veterans")
   st.markdown("Enter your questions or prompts below:")
   prompt = st.text_input("", placeholder="How can I find nearby veteran support services?")
  
   # Example questions
   st.markdown("""
   **Example Questions You Might Ask:**
   - "Where can I find emergency housing for veterans?"
   - "What mental health resources are available for veterans?"
   - "How can I apply for veteran's health benefits?"
   - "Where to find job training programs for veterans?"
   """)
  
   submitted = st.form_submit_button("Submit")
   if submitted:
       response = get_completion(prompt)
       st.write(response)
       text_to_speech(response, speech_file_path)
       with open(speech_file_path, "rb") as audio_file:
           audio_bytes = audio_file.read()
       st.audio(audio_bytes, format='audio/mp3')