import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
st.set_page_config(page_title="KH Instability",layout='wide',page_icon="👀")
st.title("Growth Factor Calculator")
a,b = st.columns(2)
def function(t,a,b):
    return a*np.exp(2*b*t)
with a:
    try:
        file = st.file_uploader("upload the file here:")
        df = np.genfromtxt (file)
    except Exception as e:
        file = 'kh0_5.dat'
        df = np.genfromtxt(file)
    t = df[:,0]
    Ey = df[:,2]
    s=st.slider(label="Starting Point",min_value=0, max_value=len(t), step=1, value=6)
    s=int(s)
    e=st.slider(label="Ending Point",min_value=0, max_value=len(t), step=1, value=12)
    e=int(e)
    k = st.text_input("Value of K:")
with b:
    fig, ax = plt.subplots()
    ax.scatter([t[s],t[e]],[Ey[s],Ey[e]], color='r')
    params, covt = curve_fit(function,t[s:e+1],Ey[s:e+1] )
    pred_Ey = function(t,params[0],params[1])
    ax.plot(t,Ey)
    ax.plot(t[s:e+1], pred_Ey[s:e+1],'r',label=f"B: {params[1]}")
    ax.set_xlabel('t')
    ax.set_ylabel('Ey (log scale)')
    ax.set_yscale('log')
    ax.legend()
    ax.set_title(f"Growth Factor for k={k}")
    st.pyplot(fig)
    st.write("# Value of b:",params[1])

content = '''
<a href='https://www.linkedin.com/in/prasad-posture-6a3a77215/' target='blank'><img align='center' src='https://img.shields.io/badge/-Prasad Posture-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/prasad-posture-6a3a77215/'  height='20' width='100' /></a>
<a href='https://github.com/prasadposture' target='blank'><img align='center' src='https://img.shields.io/badge/-prasadposture-black?style=flat-square&logo=GitHub&logoColor=white&link=https://github.com/prasadposture'  height='20' width='100' /></a>
<a href='https://www.kaggle.com/prasadposture121' target='blank'><img align='center' src='https://img.shields.io/badge/-prasadposture121-blue?style=flat-square&logo=Kaggle&logoColor=white&link=https://www.kaggle.com/prasadposture121' height='20' width='100' /></a>

'''
st.markdown(content, unsafe_allow_html=True)
