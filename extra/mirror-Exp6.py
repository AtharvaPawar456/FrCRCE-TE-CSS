import secrets
import streamlit as st


def genSalt():
    rand_bytes = secrets.token_bytes(14)

    # convert bytes to a binary string
    rand_bits = ''.join(f'{byte:08b}' for byte in rand_bytes)

    # add 2 more random bits to make 114 bits
    rand_bits += secrets.choice(['0', '1'])
    rand_bits += secrets.choice(['0', '1'])

    # convert the binary string to hex
    rand_hex = hex(int(rand_bits, 2))

    # remove the '0x' prefix from the hex string and pad with zeros if necessary
    rand_str = rand_hex[2:].zfill(29)
    return rand_str


def genPepper():
    rand_bits = ''.join(secrets.choice(['0', '1']) for i in range(2)) # generate a random 2-bit string
    return rand_bits


def main():
    st.markdown('''<h2 style="color: aquamarine;">Hashing with Salt and Pepper</h2>''', unsafe_allow_html=True)

    userName = st.text_input("Enter your username",value="Atharva")
    userPassword = st.text_input("Enter your password",value="45612387123676@Atharva")
    st.write(f'userName = {userName},  userPassword = {userPassword}')

    # enteredpassword = 'GeeksforGeeks3254612'

    # print("The string simple hash value is : " + simpleHash)

    st.markdown("""<br><hr>""",unsafe_allow_html=True)

    colm1, colm2,colm3,colm4,colm5,colm6 = st.columns(6) 
    with colm1:
        SignUpBtn = st.button("SignUp")
    with colm2:
        loginBtn = st.button("Login")




    if SignUpBtn:
        st.subheader("Simple Hashing:")

        # normal hash
        simpleHash = str(hash(userPassword))
        st.write(simpleHash)
        # -----------------------------------------------------------------------------------------
        # Hash + Salt
        hashSalt = str(userPassword) + str(genSalt())
        saltHashing = str(hash(hashSalt))
        # print("The string hash + salt value is : " + saltHashing)
        st.subheader("Salted Hashing:")
        st.write(saltHashing)
        # -----------------------------------------------------------------------------------------
        # pepper generator (Hash + salt + pepper)
        hashPeperval = str(userPassword) + str(genSalt()) + str(genPepper())
        pepperHashing = str(hash(hashPeperval))
        print("The string hash Pepper is : " + pepperHashing)
        st.subheader("Pepper Hashing:")
        st.write(pepperHashing)

                    # userName = "Atharva"
                    # simplehash = "simplehashAedtfb23"
                    # saltHash = "simpsaltHashshAedtfb23"
                    # pepperHash = "simpepperHashfb23"




if __name__ == "__main__":
    # main()