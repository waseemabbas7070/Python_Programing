import requests
import streamlit as st

st.title("API Response Viewer")

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    st.subheader("API Response:")
    st.json(data)
else:
    st.error(f"Failed to fetch data. Status code: {response.status_code}")
