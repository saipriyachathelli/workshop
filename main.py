import streamlit as st
st.title('hello')
st.write('this is simple streamlit app')
st.chat_input('enter your name')
if st.button('hello'):
    st.write('hello')
st.text_input('name please')    
    
