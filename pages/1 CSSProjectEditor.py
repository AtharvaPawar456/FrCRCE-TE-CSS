
import streamlit as st
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES
from cryptography.fernet import Fernet


from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES

import io
import contextlib

st.set_page_config(
    # page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)


def main():
    # with st.write("streamlit-ace", st_ace, __file__):
    c1, c2 = st.columns([5, 2])

    c2.subheader("Parameters")
    Guid = "#Choose a programming language: \n#First, you need to choose a programming language in which you want to write your AES code. \n#Popular programming languages for writing AES code are C, C++, Python, and Java.\n\n\n\n#Find a suitable AES library: Next, you need to find a suitable AES library for your chosen programming language. \n#There are many open-source AES libraries available that you can use. \n#Some popular libraries are OpenSSL, Crypto++, and PyCrypto.\n\n\n\n#Install the AES library: Once you have chosen an AES library, you need to install it. \n#Most libraries have installation instructions available on their website or GitHub page.\n\n\n\n#Import the AES library: After installation, you need to import the AES library into your project.\n\n\n\n#Initialize the AES algorithm: Initialize the AES algorithm by specifying the key size \n#(128, 192, or 256 bits) and the encryption mode (ECB, CBC, CFB, or OFB). \n#This can be done using the functions provided by the AES library.\n\n\n\n#Provide the input data: Provide the input data that you want to encrypt or decrypt. \n#This can be a file or a string.\n\n\n\n#Encrypt or decrypt the data: Use the AES library functions to \n#encrypt or decrypt the input data using the initialized AES algorithm.\n\n\n\n#Save the output data: Save the encrypted or decrypted output data to a file or a string.\n\n\n\n#Test the code: Test your code with sample inputs to ensure that it is working correctly.\n\n\n\n#Optimize the code: Optimize your code by making any necessary \n#modifications to improve performance or reduce code size."

    DESCode = "# editor working\nfrom cryptography.fernet import Fernet\n# Generate a random key\nkey = Fernet.generate_key()\n# Create a Fernet instance with the key\nfernet = Fernet(key)\n# Encode a message using the Fernet instance\nmessage = 'This is a secret message.'.encode()\nencrypted = fernet.encrypt(message)\n# Print the encrypted message\nprint('Encrypted message: ', encrypted)\n# Decrypt the message using the same Fernet instance\ndecrypted = fernet.decrypt(encrypted)\n# Print the decrypted message\nprint('Decrypted message: ', decrypted.decode())"


    AESCode= '# editor working\n\n# Import the necessary modules\nfrom Crypto.Cipher import AES\nfrom Crypto.Random import get_random_bytes\n\n# Define the encryption and decryption functions\ndef encrypt(key, plaintext):\n\t# Generate a random 16-byte initialization vector\n\tiv = get_random_bytes(16)\n\t# Create an AES cipher object with the given key and IV\n\tcipher = AES.new(key, AES.MODE_CBC, iv)\n\t# Pad the plaintext to a multiple of 16 bytes\n\tplaintext_padded = plaintext + b"\0" * (16 - len(plaintext) % 16)\n\t# Encrypt the padded plaintext\n\tciphertext = cipher.encrypt(plaintext_padded)\n\t# Return the IV and ciphertext as bytes objects\n\treturn iv + ciphertext\n\ndef decrypt(key, ciphertext):\n\t# Extract the IV from the ciphertext\n\tiv = ciphertext[:16]\n\t# Create an AES cipher object with the given key and IV\n\tcipher = AES.new(key, AES.MODE_CBC, iv)\n\t# Decrypt the ciphertext\n\tplaintext_padded = cipher.decrypt(ciphertext[16:])\n\t# Remove the padding from the plaintext\n\tplaintext = plaintext_padded.rstrip(b"\0")\n\t# Return the plaintext as a bytes object\n\treturn plaintext\n\n# Define the key and plaintext\nkey = b"ThisIsASecretKey"\nplaintext = b"Hello, World!"\n# Encrypt the plaintext\nciphertext = encrypt(key, plaintext)\nprint("Ciphertext:", ciphertext.hex())\n\n# Decrypt the ciphertext\ndecrypted_plaintext = decrypt(key, ciphertext)\nprint("Decrypted plaintext:", decrypted_plaintext.decode())\n\n\n\n#Note: b"." replace with b"\0" on line 14 and on line 28'


    with c1:
        # note = "#Hello Friends this is a Note for u"

        content = st_ace(
            value = DESCode,
            placeholder=c2.text_input("Editor placeholder", value="Write your code here"),
            language=c2.selectbox("Language mode", options=LANGUAGES, index=121),
            theme=c2.selectbox("Theme", options=THEMES, index=35),
            keybinding=c2.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),
            font_size=c2.slider("Font size", 5, 24, 14),
            tab_size=c2.slider("Tab size", 1, 8, 4),
            show_gutter=c2.checkbox("Show gutter", value=True),
            show_print_margin=c2.checkbox("Show print margin", value=False),
            wrap=c2.checkbox("Wrap enabled", value=False),
            auto_update=c2.checkbox("Auto update", value=True),
            readonly=c2.checkbox("Read-only", value=False),
            min_lines=45,
            key="ace",
        )

    if c1.button('Run'):
        with st.spinner(text='Running the code...'):
            with contextlib.redirect_stdout(io.StringIO()) as new_stdout:
                exec(content)

            output = new_stdout.getvalue()

            st.subheader("Output")
            st.text(output)



if __name__ == "__main__":
    main()
