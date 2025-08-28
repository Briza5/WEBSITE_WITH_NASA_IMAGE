import streamlit as st
import requests as req
import os


api_key = os.getenv("API_KEY_NASA")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = req.get(url)
content = response.json()
image_url = content["url"]

st.title(content["title"])
st.image(image_url)
st.write(content["explanation"])






#st.title("Galaxy by the Lake")