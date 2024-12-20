import streamlit as st 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("pondering-tutorial-d3903-82f2333c645d.json")

#firebase_admin.initialize_app(cred)

def app():

    st.title("Welcome to :violet[Pondering]")

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    def f():

        try:
            user = auth.get_user_by_email(email)
            st.success("Login Successfull!")

            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            # print(user.uid)

            st.session_state.signedout = True
            st.session_state.useremail = True

        except:
            st.warning("Login Failed, please enter correct email-ID")

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False 
        st.session_state.username = ''

    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False
    
    if not st.session_state['signedout']:
        choice = st.selectbox('Login/Signup', ['Login','Sign Up'])

        if choice == "Login":

            email = st.text_input("Email Address")
            password = st.text_input("Password", type = 'password')

            st.button("Login", on_click=f)

        else:

            email = st.text_input("Email Address")
            password = st.text_input("Password", type = 'password')
            username = st.text_input("Enter unique username")

            if st.button("Create my account"):

                user = auth.create_user(email = email, password = password, uid = username)

                st.success("Account created successfully!")
                st.markdown("Please login using your email and password.")
                st.balloons()

    if st.session_state.signout:

        st.text("Name "+st.session_state.useremail)
        st.text("Email id: "+st.session_state.useremail)
        st.button("Sign out",onclick = t)


