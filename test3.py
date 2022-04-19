import time
import requests
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import plost
import pandas as pd
import webbrowser


df = pd.read_csv('survey_form.csv')
df1 = df.groupby('age').count()
url = 'https://traffic-flow-counter.herokuapp.com/' #transfer to test6.py

st.title('Road Traffic Analysis')
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets6.lottiefiles.com/packages/lf20_eljprd4m.json"
lottie_hello = load_lottieurl(lottie_url_hello)
lottie_url_age = "https://assets8.lottiefiles.com/packages/lf20_r1dpwan1.json"
lottie_age = load_lottieurl(lottie_url_age)
lottie_url_vehicle = "https://assets7.lottiefiles.com/private_files/lf30_7kuqvbif.json"
lottie_vehicle = load_lottieurl(lottie_url_vehicle)
lottie_url_traffic = "https://assets8.lottiefiles.com/packages/lf20_useqtj8t.json"
lottie_traffic = load_lottieurl(lottie_url_traffic)
lottie_url_ts = "https://assets5.lottiefiles.com/packages/lf20_lo53sxhu.json"
lottie_ts = load_lottieurl(lottie_url_ts)
lottie_url_locv = "https://assets4.lottiefiles.com/packages/lf20_ampohobu.json"
lottie_locv = load_lottieurl(lottie_url_locv)
lottie_url_st = "https://assets9.lottiefiles.com/packages/lf20_HqofMq.json"
lottie_st = load_lottieurl(lottie_url_st)
lottie_url_mktg = "https://assets7.lottiefiles.com/packages/lf20_zy3citkh.json"
lottie_url_pd = "https://assets10.lottiefiles.com/packages/lf20_qmfs6c3i.json"
lottie_mktg = load_lottieurl(lottie_url_mktg)
lottie_pd = load_lottieurl(lottie_url_pd)




st_lottie(lottie_hello, key="hello")



if st.button("clickme for Visualizations"):
    
    st.balloons()
    st.header('Visualizations')
    st.dataframe(df)

    st.write("Ever stuck in traffic?")
    st_lottie(lottie_st)
    time.sleep(2)
    st.image('st.png')
    time.sleep(3)


    st.write('1. Age Frequency Analysis')
    st_lottie(lottie_age, key="age")
    time.sleep(5)
    st.image('age-freq.png')
    st.caption("Age frequency analysis based on real data")
    time.sleep(5)
    
    st.subheader("2 Vehicle type analysis")
    st_lottie(lottie_vehicle, key="vehicle")
    time.sleep(4)
    st.image('vehicle.png')
    time.sleep(3)

    st.write("3. Frequency of travelling and meeting traffic")
    st_lottie(lottie_traffic, key="traffic")
    time.sleep(4)
    st.image('travel-freq.png')
    time.sleep(3)

    st.markdown("4. Average time spent in traffic ( in seconds)")
    st_lottie(lottie_ts)
    time.sleep(2)
    ypoints = np.array([200,120,80,30,4,150,60,300,200,100,300,30,45,20,60,60,60,120,120,600,60,80,60,1,900,10,360,160,120,50,10,10,30,60,70,60,10,120,10,5,40,500,0,10,240,15,120,120,30,120,20,20,45,25,120,60,10,600,90,180,15,48,20,30,30,720,60,90,150,600,50,90,120,30,60,120,1200,600,900,10,200,35,80,600,120,10,60,40,45,30,130,30,900,60,400,60,20,143,90,60,90,120,30,120,60,200,120,80,30,4,150,60,300,200,100,300,30,45,20,60,60,60,120,120,600,60,80,60,1,900,10,360,160,120,50,10,10,30,60,70,60,10,120,10,5,40,500,0,10,240,15,120,120,30,120,20,20,45,25,1200,60,10,600,90,180,15,48,20,30,30,720,60,90,150,600,50,90,120,30,60,120,120,600,900,10,200,35,80,600,120,10,60,40,45,30,130,30,900,60,400,60,20,143,90,60,90,120,30,120,60,47, 121, 126, 245, 208, 9, 195, 80, 137, 36, 243, 150, 167, 40, 182, 205, 115, 266, 193, 241, 182, 123, 193, 254, 236, 52, 130, 29, 23, 119, 125, 162, 291, 251, 228, 145, 111, 116, 123, 93, 254, 128, 100, 152, 111, 179, 137, 109, 265, 240, 105, 277, 28, 56, 19, 119, 296, 188, 277, 219, 183, 98, 112, 76, 281, 177, 21, 288, 191, 169, 290, 242, 298, 108, 62, 93, 189, 241, 62, 138, 296, 272, 5, 158, 245, 270, 214, 257, 291, 19, 282, 206, 101, 233, 40, 196, 265, 228, 33, 140, 185, 2, 97, 44, 53, 91, 47, 87, 148, 74, 56, 146, 250, 39, 283, 238, 286, 299, 198, 67, 212, 281, 180, 67, 231, 227, 136, 230, 135, 112, 67, 4, 6, 221, 207, 161, 6, 246, 248, 60, 219, 138, 63, 247, 28, 140, 87, 135, 13, 254, 177, 124, 290, 118, 158, 258, 178, 207, 63, 102, 136, 215, 93, 296, 48, 159, 74, 163, 197, 174, 268, 264, 107, 244, 223, 109, 28, 42, 207, 109, 133, 7, 34, 277, 91, 56, 120, 274, 68, 75, 33, 136, 152, 141, 152, 242, 162, 246, 165, 61, 92, 29, 6, 272, 10, 133, 78, 281, 11, 30, 25, 151, 167, 102, 92, 229, 138, 166, 259, 184, 237, 87, 136, 167, 222, 229, 97, 198, 92, 249, 61, 236, 54, 207, 144, 113, 15, 57, 99, 287, 292, 103, 87, 300, 138, 164, 237, 223, 233, 201, 99, 11, 216, 216, 158, 194, 231, 207, 276, 178, 51, 118, 285, 105, 257, 69, 187, 72, 123, 98, 239, 211, 245, 134, 299, 239, 14, 134, 125, 165, 47, 60, 35, 131, 195, 223, 107, 193, 276, 143, 196, 142, 231, 31, 53, 206, 159, 267, 99, 50, 37, 24, 230, 155, 78, 285, 61, 60, 188, 24, 286, 176, 32, 284, 213, 40, 46, 32, 192, 254, 178, 81, 67, 78, 152, 284, 259, 255, 136, 243, 121, 151, 219, 160, 180, 242, 52, 146, 85, 51, 127, 99, 211, 166, 193, 227, 240, 191, 39, 100
])
    st.line_chart(ypoints)

    st.subheader("5. Location service analysis")
    st_lottie(lottie_locv)
    time.sleep(2)
    st.image('locv.png')
    time.sleep(4)

    st.markdown("Do you encounter any sort of marketing board??")
    st_lottie(lottie_mktg)
    time.sleep(3)
    st.imag('enc.png')
    time.sleep(3)

    st.write("What most people do")
    st_lottie(lottie_pd)
    time.sleep(8)
    st.image('wyd.png')
    time.sleep(3)



    


 

if st.button('Open browser'):
    webbrowser.open_new_tab(url)







