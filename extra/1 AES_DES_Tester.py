import streamlit as st
import AESencrypt

def main():
    default_passphrase = "demo_secret_key"  # set the default passphrase
    PassPhrase  = st.text_input("Enter in the 16 character passphrase to encrypt your message", value=f'example : {default_passphrase}')
    default_message = "deom_Hello,Cryptgraphy World!"  # set the default message
    message     = st.text_input("Enter in the Message", value=f'example : {default_message}')
    if st.button('Encrypt'):
        st.write(f'Cipher Text :  {AESencrypt.AESFun(PassPhrase,message)}')

# if __name__ == "__main__":
st.header("CSS Project : AES & DES")
st.write('''<h5 style="color: #008CBA;   border: 1px solid gray;
  padding: 8px; ">Team Members: Atharva Pawar, Aditya Vyas, Deon Gracias</h5>''', unsafe_allow_html=True)

st.header("")
st.markdown('''<h3 style="color: aquamarine;">AES : Advanced Encryption Standard</h3>''', unsafe_allow_html=True)

main()

st.markdown("<hr>", unsafe_allow_html=True)

# st.markdown('''<h3 style="color: aquamarine;">DES : Data Encryption Standard</h3>''', unsafe_allow_html=True)


# streamlit run 1 CSS Project.py


# # create anchor tag
# st.markdown("<a name='my_anchor'></a>", unsafe_allow_html=True)

# # create link to anchor tag
# st.write("Click [here](#my_anchor) to go to my anchor tag.")
