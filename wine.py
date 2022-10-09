import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.io as pio


# READ CSV
df=pd.read_csv("winequality-red.csv")
df.columns = df.columns.str.replace(' ', '_')
st.dataframe(df)

st.write(df.isnull().sum())

#Corr matrix heat map

st.plotly_chart(px.imshow(df.corr(), text_auto=True).update_layout(width=800,height=800))

st.plotly_chart(px.scatter(df,y="density", x='fixed_acidity', color_discrete_sequence=['#87CEEB'], template="plotly_dark").update_layout(width=800,height=800))

st.plotly_chart(px.histogram(df,x="density", color_discrete_sequence=['#87CEEB'], template="plotly_dark").update_layout(width=800,height=800))
st.plotly_chart(px.histogram(df,x="alcohol", color_discrete_sequence=['#87CEEB'], template="plotly_dark").update_layout(width=800,height=800))
st.plotly_chart(px.histogram(df,x="pH", color_discrete_sequence=['#87CEEB'], template="plotly_dark").update_layout(width=800,height=800))
st.plotly_chart(px.histogram(df,x="quality", color_discrete_sequence=['#87CEEB'], template="plotly_dark").update_layout(width=800,height=800))
