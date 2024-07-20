from PIL import Image
import streamlit as st
import requests as rs
from streamlit_lottie import st_lottie

st.set_page_config(page_title="WebPage",page_icon=":tada:",layout="wide")

def load(url):
    r = rs.get(url)
    if r.status_code != 200:
        return None 
    return r.json()

#---Load Css
def load_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style/style.css")


#---Load Image---
image = load("https://lottie.host/188ace8b-b296-4cd2-950e-26b7cdd8b2f4/VTXkYaMVTP.json")
load_image = Image.open("Img/Screenshot (8).png")
#------Header Section-----
with st.container():
    st.subheader("Hi, my name is David Adeniyi :wave:")
    st.title("I'm an Aspiring Developer")
    st.write("I am Passionate about Programming and the idea of creating functional and efficient Programs that showcase my level of skill.")


with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            I enjoy Creating WebPages and Programs about things i am passionate about. Those things include:
            - Mangas. 
            - Anime.
            - Programming.
            - Novels(Light and Web novels).
            In my free time, i write code in Python and sometimes Javascript.
            I am also very entusiastic about learning, especially when it come to learning about new and existing programming languages i haven't tried before.
            My goal is to become a developer that specialises in a diverse range of languages and make money off of my  skills.
            """
        )

    with right_column:
        st_lottie(image,height=500,key="programming",)
   

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    img_column, text_column = st.columns((1,2))
    with img_column:
        st.image(load_image)

    with text_column:
        st.subheader("A Form Page using PyQt5 and sqlite3 database")
        st.write(
            """
            I built a Form Page that stores the entered data of the user into a database.
            The Forum page was built using PyQt5 Library of python, and the database use sqlite3 as well as Qtdesigner for designing the page.
            DBbrowser was used to view the contents of the database.
            Qtdesigner was used to create the layout for the gui, while the funtionality was coded using python.

            """
        )


#-----Contact----
with st.container():
    st.write("---")
    st.header("You can get in touch with me Today!")
    st.write("##")

    contact = """
    <form action="https://formsubmit.co/dadeniyi136@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
     <textarea name = "message" placeholder = "Your message" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact,unsafe_allow_html=True)
    with right_column:
        st.empty()

