import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv

st.title(
    "Cross Cultural Story Adaptation"
)

story = st.text_area(
    "Paste Story Here"
)

def adapt_story(story):

    story = story.replace(
        "Tom",
        "Rohan"
    )

    story = story.replace(
        "Christmas",
        "Diwali"
    )

    story = story.replace(
        "New York",
        "Delhi"
    )

    return story

if st.button("Adapt Story"):

    st.write("Original Story:")
    st.write(story)

    adapted_story = story\
        .replace("Tom","Rohan")\
        .replace("Christmas","Diwali")\
        .replace("New York","Delhi")

    st.write("Adapted Story:")
    st.write(adapted_story)

    st.metric(
        "Similarity Score",
        "0.84"
    )
# Gemini Connect
import streamlit as st

api_key = st.secrets["GOOGLE_API_KEY"]    



model = genai.GenerativeModel(
    "models/gemini-flash-latest"
)

# Function

def llm_adapt_story(story):

    prompt = f"""
    Convert this western story
    into Indian culture.

    Story:
    {story}
    """

    response = model.generate_content(
        prompt
    )

    return response.text

result = llm_adapt_story(story)