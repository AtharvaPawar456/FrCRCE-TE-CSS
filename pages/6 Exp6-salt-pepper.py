import streamlit as st
import requests

# userName = "Atharva"
# simplehash = "simplehashAedtfb23"
# saltHash = "simpsaltHashshAedtfb23"
# pepperHash = "simpepperHashfb23"

def signUp():
    st.subheader("SignUp Page")

    userName = st.text_input("Enter your username",value="Atharva")
    userEmail = st.text_input("Enter your email",value="talktoatharva14@gmail.com")
    userPassword = st.text_input("Enter your password",value="456@MySecretPassword")

    st.write(f'userName = {userName}, userName = {userEmail}, userPassword = {userPassword}')

    signUpSubmitBtn = st.button("SignUp",use_container_width=4)
    # st.write(f"signUpSubmitBtn : {signUpSubmitBtn}")

    if signUpSubmitBtn:
        response = requests.get(f"http://localhost:8000/signup/{userName}/{userEmail}/{userPassword}")
        st.warning(response.json())



def login():
    st.subheader("Login Page")
    userName = st.text_input("Enter your username",value="Atharva")
    userPassword = st.text_input("Enter your password",value="456@MySecretPassword")
    st.write(f'userName = {userName},  userPassword = {userPassword}')
    loginSubmitBtn = st.button("Login",use_container_width=10)
    Status = False
    if loginSubmitBtn:
        response = requests.get(f"http://localhost:8000/login/{userName}/{userPassword}")
        st.warning(response.json())
        data = response.json()
        Status = data['login_status']
        st.write(Status)
        print(Status)
        if Status:
            st.write(f"Welcome {userName} !!! ")
            st.write(f"Login SuccessFull")






if __name__ == "__main__":
    st.markdown('''<h1 style="color: aquamarine;">Hashing with Salt and Pepper</h1>''', unsafe_allow_html=True)
    st.markdown("""<br>""",unsafe_allow_html=True)

    # st.markdown("""<h4>
    #                     <a href="http://localhost:8501/mainSignUp" target="_self">SIGNUP</a>
    #                     /
    #                     <a href="http://localhost:8501/mainLogin" target="_self">LOGIN</a>
    #                 </h4>""", unsafe_allow_html=True)


options = ['Login','SignUp' ]
selected_option = st.selectbox(' ', options)

# st.write('You selected:', selected_option)

if selected_option == "SignUp":
    signUp()

if selected_option == "Login":
    login()
