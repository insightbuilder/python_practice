#!/usr/bin/env python

import pandas as pd
import streamlit as st
import plotly.express as px

#with open('style.css') as f:
    #st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#Sending a hello world to the dashboard
st.write("### Split Screen on your laptop")
print("Hi there")
my_name = st.text_input("Name:")

st.write(f"My name is {my_name}")

st.write("Give me two numbers in the below text boxes")

a = st.text_input('A = ')

b = st.text_input('B = ')

st.write(f"A + B = {int(a) + int(b)}")

click = st.button('click for answer')
st.write(click)

if click:
    st.write(f"A + B = { 586 * int(a) + 25 * int(b)}")

dict_for_df = {'col1':[1,2,3,4,5],
               'col2':['a','y','aeo','the','err']}

st.write(dict_for_df)

df = pd.DataFrame(dict_for_df)

st.write(df)
#this is plotly chart function
fig = px.bar(df,x='col2',y='col1')
st.plotly_chart(fig,use_entire_width=True)
#st.bar_chart(data=df,x='col2',y='col1')

c1, c2 = st.columns(2)
c1.write("### Col1: ")
c2.write("##### Col2")
