import streamlit as st
import random
import sys

titles = ["Hello", "Hi", "Howdy"]
icons = [":shark:", ":cat:", ":hamburger:", ":bomb:"]

st.beta_set_page_config(
    page_title=random.choice(titles),
    page_icon=random.choice(icons),
)


"""
# Hello world!!!
"""

x = st.slider("Foo", 0, 100)
st.write("Selected:", x)

print("Selected:", x)
sys.stdout.flush()
