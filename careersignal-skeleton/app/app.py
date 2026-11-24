import os

import streamlit as st

st.set_page_config(page_title="CareerSignal", page_icon=":bar_chart:")

st.title("CareerSignal")
st.write("Hello from the walking skeleton. The real pages come next.")
st.caption(f"Build: {os.getenv('APP_VERSION', 'local')}")
