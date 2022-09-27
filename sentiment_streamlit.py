# %%
import pickle
import streamlit as st
from sentiment import Sentiment_Analysis

# %%
# st.title('讀你的情緒')
st.markdown("<h1 style='text-align: center; color: #844200;'>讀你的情緒</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center'>我能夠分析你的情緒！請於下方輸入語句，讓我看看你現在的心情如何？</h6>", unsafe_allow_html=True)
# %%
inputSTR = st.text_input('輸入任何你想說的話：', '')
if inputSTR:
    st.write('你所輸入的句子為：', inputSTR)

# %%
sentiment_pickle = open('sentiment.pickle', 'rb') 
sentiment = pickle.load(sentiment_pickle) 
sentiment_pickle.close() 

# %%
if inputSTR:
    st.write('情緒指數：{}'.format(Sentiment_Analysis(inputSTR)))
    st.write('情緒程度：')
    st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-image: linear-gradient(to right, #FF9D6F , #FF95CA);
        }
    </style>""",
    unsafe_allow_html=True,
    )
    st.progress(Sentiment_Analysis(inputSTR))
    if Sentiment_Analysis(inputSTR) <= 0.19:
        st.write('你現在心情似乎很差，有需要幫助的時候不要不好意思開口喔！')
        st.image('./emotion_pic/01.png', width=200)
    elif Sentiment_Analysis(inputSTR) > 0.19 and Sentiment_Analysis(inputSTR) <= 0.4:
        st.write('你的心情好像不太好，聽首歌或許會有幫助喔！')
        st.image('./emotion_pic/02.png', width=200)
    elif Sentiment_Analysis(inputSTR) > 0.4 and Sentiment_Analysis(inputSTR) <= 0.5:
        st.write('你目前的心情好像很平靜呢。')
        st.image('./emotion_pic/03.png', width=200)
    elif Sentiment_Analysis(inputSTR) > 0.5 and Sentiment_Analysis(inputSTR) <= 0.7:
        st.write('你的心情好像滿不錯的呢！')
        st.image('./emotion_pic/04.png', width=200)
    else:
        st.write('你感覺很開心唷！有什麼好事可以跟我分享嗎？')
        st.image('./emotion_pic/05.png', width=200) 


