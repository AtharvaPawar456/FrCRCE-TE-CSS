import streamlit as st
from streamlit_ace import st_ace


st.title("Code Editor on Streamlit")

first,second = st.columns(2)

with first:
    st.markdown("## Input")
    code = st_ace(language = 'python',
    theme='xcode')

with second:
    note = "Hello Friends this is a Note for u"
    st.markdown("## Output")
    #st.markdown("``` python\n"+code+"```")
    st_ace(value = note,
    language = 'python',
    # theme = 'pastel_on_dark',
    theme = 'chrome',
    readonly  = True)