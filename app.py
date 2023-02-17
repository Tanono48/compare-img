import cv2
import streamlit as st
from PIL import Image
import numpy as np

with open('style.css') as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

# Explain How Code 
with st.sidebar: 
    st.header('👋👋 **_How does this code work?_**')
    st.markdown('_:red[First 1] Upload image files (Limit 200MB per file • JPG, JPEG, PNG)_')
    st.markdown('_:red[Step 2] After receiving the file , the fuction :orange[cvIMG] will be converted to :blue[array] in 8 bit format._')
    st.markdown('_:red[Step 3] Next function :orange[imdecode] to decode array into an image._') 
    st.text('This flag is set to 1, which means the image should be read as a color image with 3 channels (i.e., a BGR image)._')
    st.markdown('_:red[Step 4] this function takes two images, converts them to :green[grayscale] , compares them using OpenCV :orange[matchTemplate] function._') 
    st.markdown('_:red[Finally 5] calculates the percentage difference between them. It returns the percentage difference as the result._') 

st.header("Compare the faces of each person to see how many percent are different ( ❛ ω ❛ )")
st.markdown(" 👉 Let's try to compare the pictures to see how different these two pictures are.")
st.caption("The purpose of this webb app is to compare human faces to see how much they are different.")
st.markdown('----------------------------------------------------------------')

img1_up = st.file_uploader("Upload Picture1",type=["jpg","jpeg",'png'])
img2_up = st.file_uploader("Upload Picture2",type=["jpg","jpeg",'png'])

def cvIMG(path):
    temp = np.asarray(bytearray(path.read()), dtype=np.uint8)
    temp = cv2.imdecode(temp,1)
    return temp

def process_diff(param1,param2):
    gray1 = cv2.cvtColor(param1, cv2.COLOR_BGR2GRAY )
    gray2 = cv2.cvtColor(param2, cv2.COLOR_BGR2GRAY)
    #face_cascade = cv2.CascadeClassifier("E:\modul1-venv\haarcascade_frontalface_default.xml")
    #faces1 = face_cascade.detectMultiScale(gray1 ,1.3,5)
    #faces2 = face_cascade.detectMultiScale(gray2 ,1.3,5)
    result = cv2.matchTemplate(gray1, gray2 , cv2.TM_CCOEFF_NORMED)
    percent_diff = 100-(result[0][0]*100)
    return percent_diff
            
if st.button('RUN ! !'):
    if img1_up is None or img2_up is None:
        st.write("Error ☠️☠️ / Pls Upload Picture ( ͡❛ ⏥ ͡❛)")
    else:  
        img1 = cvIMG(img1_up)
        img2 = cvIMG(img2_up)
        print(img1_up)
        if img1 is not None or img2 is not None:  
            st.write(f"The percentage difference between the two images is : {process_diff(img1, img2):.2f}" )
            st.image(img1_up, use_column_width=True)
            st.image(img2_up, use_column_width=True)
        else:
            st.write("Error ( ͡❛ ⏥ ͡❛)")

