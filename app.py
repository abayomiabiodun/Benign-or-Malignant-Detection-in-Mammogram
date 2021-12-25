import streamlit as st
from PIL import Image 
import pickle

model = pickle.load(open('./model.pickle', 'rb'))

def run():
    img1 = Image.open("mammogram.jpg")
    img1 = img1.resize((156, 145))
    st.image(img1, use_column_width=False)
    st.title("Mammographic mass Prediction Using Machine Learning")


    ## Full Name
    fn = st.text_input("Full Name")

    ## Hospital  ID
    Hospital_id = st.text_input("Hospital ID")

    ## For BI-RADS Assessment
    bi_display = ("One", "Two", "Three", "Four", "Five")
    bi_option = list(range(len(bi_display)))
    Bi = st.selectbox("BI-RADS Assessment", bi_option, format_func=lambda x: bi_display[x])

    ## Patient's Age
    ag_display = ("18-23", "24-29", "30-35","36-41", "42-47", "48-53", "54-59", "60-65", "66-71", "72-77", "78-83", "84-89", "90-95", "96-101")
    ag_option = list(range(len(ag_display)))
    Age = st.selectbox("Patient's Age", ag_option, format_func=lambda x: ag_display[x])

    ## Mass Shape
    sh_display = ("round", "oval", "lobular", "irregular")
    sh_option = list(range(len(sh_display)))
    shape = st.selectbox("Mass Shape", sh_option, format_func=lambda x: sh_display[x])

    ## Mass Margin
    marg_display = ("Circumscribed", "Microlobulated", "Obscured", "Spiculated")
    marg_option = list(range(len(marg_display)))
    margin = st.selectbox("Mass Margin", marg_option, format_func=lambda x: marg_display[x])

    ## Mass Density
    den_display = ("high", "iso", "low", "fat-containing")
    den_option = list(range(len(den_display)))
    density = st.selectbox("Mass density", den_option, format_func=lambda x: den_display[x])


    if st.button("Submit"):
        features = [[Bi, Age, shape, margin, density]]
        print(features)
        prediction = model.predict(features)
        lc =[str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 1:
            st.error(
                "Hello: " + fn + " || "
                "Hospital ID: " + Hospital_id + " || "
                "According to our calculation based on your test result, you have Malignant" + "||"
                "Try to see doctor for further consultation"
            )
        else:
            st.warning(
                "Hello: " + fn + " || "
                "Hospital ID: " + Hospital_id + " || "
                "You have Benign" + "||"
                "Try to see doctor for further consultation"
            )

run()
