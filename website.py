import streamlit as st
import toxicity

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    st.image('safechatlogo.jpg', width=400)

with col3:
    st.write(' ')

st.title('SAFECHAT')
st.subheader('A toxicity detection bot')
st.write(
    '''    
    SAFECHAT is a NLP-based discord bot built to stop toxicity using machine learning.
  
    Using Cohere's NLP Platform, we were able to build a discord bot which could detect toxic messages and delete
    them soon after they are sent. We used Cohere's "cohere-toxicity" model to test our initial development, and
    later decided to train Cohere's model using data from other sources, namely a variety of tweets which
    were labelled as either "toxic" or "non-toxic".
    '''
)

st.video('demovid.mp4')

with st.form("form", clear_on_submit=True):
    entry = st.text_input('Test it for yourself!')
    submit = st.form_submit_button("Submit")
    if submit:
        toxic = toxicity.isToxic(entry)
        if toxic:
            st.write('That message is toxic!')
        else:
            st.write('That message is not toxic!')