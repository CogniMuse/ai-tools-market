import pandas as pd
import streamlit as st

# Data loading and preprocessing

#TODO preprocess and save file to improve performance
df = pd.read_csv("Futurepedia_Ai_Tools_Dataset.csv",encoding='cp1252')
df['Categories'] = df['Categories'].fillna('')
df['Categories'] = df['Categories'].map(lambda x: x.split('\n'))
df['Site url'] = df['Site url'].map(lambda x: x.split('?')[0])
df['Categories'] = df['Categories'].fillna('')


# Exploding data
exploded = df.explode('Categories')

#Constants
tools_total_count = df.shape[0]
categories_total = len(exploded['Categories'].unique())
subheading = '<p style="color:#ccff00">Hello!</p>'

st.set_page_config(layout='wide')

st.title(body="AI Tools Market 💹 by [Cognimuse.com](https://www.cognimuse.com/)")
st.write("### Explore over 3000 AI tools and understand the AI tools market")
st.write("""** ** """)
# st.markdown(subheading,unsafe_allow_html=True)

if 'category' not in st.session_state:
    st.session_state.category = '#fun tools'

if 'count' not in st.session_state:
    st.session_state.count = exploded[exploded['Categories']=='#fun tools'].shape[0]


def click(label):
    st.session_state.category = label
    st.session_state.count = exploded[exploded['Categories']==st.session_state.category].shape[0]

#Sidebar 
st.sidebar.title("Categories",)
st.sidebar.header("Total Categories: {0}".format(categories_total))
btn = [st.sidebar.button(label=x,on_click=click,args=[x]) for x in exploded['Categories'].value_counts().keys().values]

# Main area
st.write("#### Number of tools in ",":green["+st.session_state.category+']'," : ",
         st.session_state.count)

st.write("#### Percentage of  :green["+st.session_state.category+"] tools: ",
         round(st.session_state.count/tools_total_count*100,2),':green[%]' )

st.dataframe(exploded[exploded['Categories']==st.session_state.category][['Ai Tools Name','Types For Use','Pricing','Site url']],
             use_container_width=True,
             column_config= {"Site url":st.column_config.LinkColumn()},
             hide_index=True)

# Bar chart distribution of AI tools
st.write("""** ** """)

st.write('### Categorical distribution of AI tools')
st.bar_chart(exploded['Categories'].value_counts(),color="#ccff00",)

#st.bar_chart(exploded[exploded['Categories']=='#fun tools']['Pricing'].value_counts(),color="#ccff00")