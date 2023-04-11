import streamlit as st

# Create a file uploader component
uploaded_file = st.file_uploader("Choose a text file", type="txt")

# Check if a file was uploaded
if uploaded_file is not None:
    # Read the contents of the file
    file_contents = uploaded_file.read()

    # Decode the contents as UTF-8 text
    text = file_contents.decode("utf-8")

    # Display the text in the app
    st.write("File contents:")
    st.write(text)