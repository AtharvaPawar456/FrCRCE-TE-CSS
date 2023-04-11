import streamlit as st

def hill_cipher(key, message): 

    key_matrix = [[ord(i) - 97 for i in key[:2]], 
                  [ord(i) - 97 for i in key[2:]]] 
  
    inverse_key_matrix = inverse_matrix(key_matrix) 
  
    encrypted_message = "" 
    for i in range(0, len(message), 2): 
        column_matrix = [[ord(message[i]) - 97], [ord(message[i + 1]) - 97]] 
        cipher_matrix = matrix_multiply(key_matrix, column_matrix) 
        cipher_vector = [i[0] for i in cipher_matrix] 
        for num in cipher_vector: 
            encrypted_message += chr((num % 26) + 97) 
  
    return encrypted_message 
  
def matrix_multiply(A, B): 
    result = [[0, 0],[0, 0]] 
    for i in range(len(A)): 
        for j in range(len(B[0])): 
            for k in range(len(B)): 
                result[i][j] += A[i][k] * B[k][j] 
  
    return result 
  
def inverse_matrix(key): 
    determinant = (key[0][0] * key[1][1]- key[0][1] * key[1][0]) % 26
    determinant_inverse = 0
    for i in range(1, 26): 
        if (determinant * i) % 26 == 1: 
            determinant_inverse = i 
            break
    # Calculate the inverse key matrix 
    inverse_key = [[0, 0], [0, 0]] 
    inverse_key[0][0] = (determinant_inverse * key[1][1]) % 26
    inverse_key[0][1] = (-determinant_inverse * key[0][1]) % 26
    inverse_key[1][0] = (-determinant_inverse * key[1][0]) % 26
    inverse_key[1][1] = (determinant_inverse * key[0][0]) % 26
    return inverse_key 

def SignleColumnarwithoutKey(data,):
    # get input from user
    # data = input("Enter a string of data: ")

    # convert data to lowercase and split into words
    words = data.lower().split()

    # create nested list
    test_list = []
    for word in words:
        if len(test_list) == 0 or len(test_list[-1]) == 3:
            test_list.append([word])
        else:
            test_list[-1].append(word)

    # print the original list
    # print("The original list is: " + str(test_list))
    # st.write(f"The original list is: {str(test_list)}")

    # flatten the list
    res = [ele for sub in test_list for ele in sub]

    # print the flattened list
    # print("Single columnar without key: " + str(res))

    return str(test_list), str(res)

  
if __name__ == "__main__": 
    # key = "gybnqkurp"
    # message = "CSSPractical"
    # encrypted_message = hill_cipher(key, message) 
    # print(f'Key : {key}')
    # print(f'Raw Message : {message}')
    # print("Encrypted Message: {}".format(encrypted_message))


    st.header("CSS : Practical - 1 ")
    st.markdown('''<h3 style="color: aquamarine;">Hill Cipher</h3>''', unsafe_allow_html=True)

    # set the default passphrase
    default_passphrase = "demo_secret_key"  
    placeholderPass = f'example : {default_passphrase}'
    PassPhrase  = st.text_input("Enter the key", value=default_passphrase, placeholder=placeholderPass)

    # set the default message
    default_message = "deom_CSS Practical-1"  
    placeholderMsg = f'example : {default_message}'
    message     = st.text_input("Enter the Message", value=default_message, placeholder=placeholderMsg)
    if st.button('Encrypt'):
        encrypted_message = hill_cipher(PassPhrase, message) 
        st.info(f'Key     ==> "{PassPhrase}"')
        st.info(f'Message ==> "{message}"')
        st.warning(f'Cipher Text :  {encrypted_message}')

    st.markdown("<hr>", unsafe_allow_html=True)
# ----------------------------------------------------------------------------------------------------------

    st.header("")
    st.markdown('''<h3 style="color: aquamarine;">Single Columnar without key</h3>''', unsafe_allow_html=True)

    default_msg = "This is my demo default message"
    msg  = st.text_input("Enter a Message", value=default_msg, placeholder=f'example : {default_msg}')
    tas2Value = SignleColumnarwithoutKey(msg)
    if st.button('Encrypt', key="123"):
        # st.info(f"The original list is: {str(tas2Value[0])}")
        st.warning(f"Single columnar without key: {str(tas2Value[1])}")

