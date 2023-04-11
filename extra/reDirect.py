import streamlit as st
import webbrowser

# Define your Streamlit app as usual
def main():
    button_pressed = st.button("Click me!")

    if button_pressed:
        st.markdown("""<a href="http://localhost:8501/mainLogin" target="_self">click me once again</a>""", unsafe_allow_html=True)

def newTab():
    if st.button('Open Link'):
        webbrowser.open_new_tab('https://www.google.com')

def sameTab():
    st.markdown("[Open Link](https://www.google.com)")


if __name__ == '__main__':
    sameTab()



