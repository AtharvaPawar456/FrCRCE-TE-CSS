# pip install pycryptodome, crypto, cryptography

import streamlit as st
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


def AESalgo():
	st.header("")
	st.markdown('''<h3 style="color: aquamarine;">AES : Advanced Encryption Standard</h3>''', unsafe_allow_html=True)

	message = st.text_input("Enter Message: ",value="Atharva")
	password = st.text_input("Enter Password: ",value="456@Atharva")
	
	if st.button("Encrypt",key="enc"):

		# Set up password and salt
		# password = "mysecretpassword" # Replace with user input
		salt = get_random_bytes(16)

		# Generate key from password and salt
		key = PBKDF2(password, salt, dkLen=16)

		# Set up cipher
		cipher = AES.new(key, AES.MODE_ECB)

		# Encrypt and decrypt message (same as previous examples)
		# message = "Hello, world!" # Replace with user input
		message_bytes = message.encode()
		padded_message = pad(message_bytes, AES.block_size)
		ciphertext = cipher.encrypt(padded_message)

		# Print encrypted message
		st.warning(f'Cipher text: {ciphertext}')
		st.warning(f'Key: {key}')

		# Decrypt message
		decrypted_message = cipher.decrypt(ciphertext)
		unpadded_message = unpad(decrypted_message, AES.block_size)
		plaintext = unpadded_message.decode()

		# Print decrypted message
		if not plaintext:
			st.info('Message is corrupted')
		else:
			st.info(f'Decrypted PlainText  : " {plaintext} "')


def DESalgo():
	st.header("")
	st.markdown('''<h3 style="color: aquamarine;">DES : Data encryption standard</h3>''', unsafe_allow_html=True)

	message = st.text_input("Enter Message: ",value="Atharva")
	password = st.text_input("Enter Password: ",value="456@Atharva")

	if st.button("Encrypt",key="enc"):
		# Set up password
		# password = "mysecretpassword" # Replace with user input

		# Generate 8-byte key from password
		key = password.encode('utf-8')[:8]

		# Set up cipher
		cipher = DES.new(key, DES.MODE_ECB)

		# Encrypt message
		# message = "Hello, world!" # Replace with user input
		message_bytes = message.encode()
		padded_message = pad(message_bytes, DES.block_size)

		ciphertext = cipher.encrypt(padded_message)

		# Decrypt message
		decrypted_message = cipher.decrypt(ciphertext)
		unpadded_message = unpad(decrypted_message, DES.block_size)
		plaintext = unpadded_message.decode()

		# Print encrypted message
		st.warning(f'Cipher text: {ciphertext}')
		st.warning(f'Key: {key}')

		# Print decrypted message
		if not plaintext:
			st.info('Message is corrupted')
		else:
			st.info(f'Decrypted PlainText  : " {plaintext} "')




if __name__ == "__main__":
	st.header("CSS Project : AES & DES")
	st.write('''<h5 style="color: #008CBA;   border: 1px solid gray;padding: 8px; ">
      		Team Members: Atharva Pawar, Aditya Vyas, Deon Gracias</h5>''', unsafe_allow_html=True)
	st.header("")

	options = ['AES','DES' ]
	selected_option = st.selectbox(' ', options)

	# st.write('You selected:', selected_option)

	if selected_option == "AES":
		AESalgo()

	if selected_option == "DES":
		DESalgo()







	st.markdown("<hr>", unsafe_allow_html=True)
