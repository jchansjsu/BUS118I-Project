import streamlit as st
import openai
from openai import OpenAI


# Custom CSS to style the Streamlit app
def load_css():
   st.markdown("""
       <style>
           /* Reset some Streamlit default styles to make the design cleaner */
           .stAlert, .stButton, .stTextInput, .stSelectbox, .stTextarea {
               border: 1px solid #ddd;
               border-radius: 5px;
           }
           .st-bf, .st-bj, .st-cm {
               margin-bottom: 10px; /* Adjust spacing between widgets */
           }
           .st-bj {
               padding: 10px 0px; /* Adjust padding around radio buttons */
           }
          
           /* Main content styles */
           .block-container {
               padding: 2rem;
               max-width: 700px;
               margin: auto;
           }
           .stMarkdown h1 {
               text-align: center;
               margin-bottom: 2rem;
               font-weight: 700;
               color: #4a69bd;
           }
           .stMarkdown p {
               text-align: center;
               margin-bottom: 2rem;
               color: #555;
               font-size: 1rem;
           }
           .stTextInput label, .stSelectbox label, .stTextarea label {
               font-weight: 500;
           }
           .stTextArea > div > div > textarea {
               min-height: 150px; /* Increase text area size */
           }
           .stButton > button {
               width: 100%;
               border: none;
               background-color: #4a69bd;
               color: #fff;
               padding: 0.75rem 1.5rem;
               font-size: 1.1rem;
               border-radius: 5px;
               transition: background-color 0.3s ease;
           }
           .stButton > button:hover {
               background-color: #357ABD;
           }
           .css-1cpxqw2 {
               align-items: center;
           }
           .css-145kmo2 {
               flex-direction: column; /* Align sidebar items vertically */
           }
           .css-1d391kg {
               padding-top: 3.5rem; /* Extra padding at the top of sidebar */
           }
           .sidebar .sidebar-content {
               padding: 2rem;
           }


           /* Sidebar styles */
           .sidebar .stMarkdown h1 {
               font-size: 1.25rem; /* Smaller font size for sidebar title */
               margin-bottom: 1rem; /* Less margin bottom */
           }
       </style>
   """, unsafe_allow_html=True)


load_css()


# Initialize OpenAI client
client = OpenAI(api_key="your_api_key_here")


# Optional: Adjust this to your actual function to perform the translation
def translate(text, source_language, target_language):
   # Translation logic goes here
   # Example: return f"Translation placeholder from {source_language} to {target_language}"
   # Write code that uses openAI to translate the text
   response = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages = [
           {"role": "system", "content": f"System message: Translate from {source_language} to {target_language}. - {text}"},
       ]
   )
   return response.choices[0].message.content
st.markdown("# Translation Service")


st.sidebar.markdown("## Select Languages")


# Extended list of languages
languages = [
   'Arabic', 'Chinese', 'Dutch', 'English', 'French', 'German',
   'Hindi', 'Italian', 'Japanese', 'Korean', 'Portuguese',
   'Russian', 'Spanish', 'Turkish'
]


# Select source and target languages
source_language = st.sidebar.selectbox('Source Language:', languages, index=languages.index('English'))
target_language = st.sidebar.selectbox('Target Language:', languages, index=languages.index('Spanish'))


# Text input area
st.markdown("### Please Enter Text to Translate")
text_to_translate = st.text_area("", height=150)


# Translate button
if st.button('Translate'):
   if text_to_translate:
       # Translation logic
       result = translate(text_to_translate, source_language, target_language)


       # Display translation result
       st.markdown("### Translated Text")
       st.write(result)  # Replace with the actual translation result
   else:
       st.error('Please enter some text to translate.')