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

st.header("What to.. Where to .. What type of ... ? ")

insight = 'https://share.streamlit.io/pgstorm148/tac-traffic-v1/main/tac_app.py'
poc = 'https://github.com/pgstorm148/eda-traffic/tree/main/eda-traffic'

if st.button('Insights'):
    webbrowser.open_new_tab(insight)

if st.button('EDA - traffic'):
    webbrowser.open_new_tab(poc)



#at end of tac traffic transfer to https://traffic-flow-counter.herokuapp.com


