import streamlit as st
import info
import requests
import json
import shutil
from info import AddImage
from PIL import Image

#Mainpage
def mainpage():
    st.title("Lifeline") #1st NEW streamlit method
    st.image(info.mainpageImg)
    name = st.text_input("What is your name?") #2nd NEW streamlit method
    st.subheader(f'Hello {name}')
    st.write(info.mainpageTxt)
    st.write("---")
mainpage()

#Navigation Sidebar
st.sidebar.title("How Are You Feeling?")
feeling_choice = st.sidebar.radio("", ["", "Depressed", "Burnt Out", "Stressed", "Philosophical"])

#Indvidual Sections
def feeling_section(feeling, data):
    st.header(f"For those that are feeling {feeling}: ")
    #API Call
    img = st.button("Generate Image")  #Button implementation #3rd NEW streamlit method
    if img:
        AddImage(feeling)
        image = Image.open('img.jpg')
        st.image(image)
    expander = st.expander('Inspirational Quotes: ')
    for quote, author in data.items():
        expander.write(f"**{quote}**")
        expander.write(f"-- {author}")
    st.write("---")


#Display for Each page
if feeling_choice == "Depressed":
    feeling_section("Depressed", info.depData)
elif feeling_choice == "Burnt Out":
    feeling_section("Burnt Out", info.burntData)
elif feeling_choice == "Stressed":
    feeling_section("Stressed", info.stressData)
elif feeling_choice == "Philosophical":
    feeling_section("Philosophical", info.philData)  

#Features function
def features(featuresData):
    st.header("Features")
    for bullet in featuresData:
        st.write(bullet)
    st.write("---")
features(info.featuresData)






