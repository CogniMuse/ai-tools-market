import pandas as pd
import streamlit as st

# Data loading and preprocessing

df = pd.read_csv("Futurepedia_Ai_Tools_Dataset.csv",encoding='cp1252')
df['Categories'] = df['Categories'].fillna('')
df['Categories'] = df['Categories'].map(lambda x: x.split('\n'))
df['Site url'] = df['Site url'].map(lambda x: x.split('?')[0])
df['Categories'] = df['Categories'].fillna('')

# Exploding data
exploded = df.explode('Categories')


st.set_page_config(layout='wide')

st.write("# AI Tools Market 💹")
st.write("Understand the AI tools market")

if 'category' not in st.session_state:
    st.session_state.category = '#fitness'


def click(label):
    st.session_state.category = label
    
with st.sidebar:
    btn = [st.button(label=x,on_click=click,args=[x]) for x in exploded['Categories'].value_counts().keys().values]


st.dataframe(exploded[exploded['Categories']==st.session_state.category],
             use_container_width=True,
             column_config= {"Site url":st.column_config.LinkColumn()},
             hide_index=True)

st.bar_chart(x=list(exploded['Categories'].value_counts().keys()),y=list(exploded['Categories'].value_counts()))

