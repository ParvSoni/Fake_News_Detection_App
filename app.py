import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
port_stem = PorterStemmer()
vectorization = TfidfVectorizer()

vector_form = pickle.load(open('vector.pkl', 'rb'))
load_model = pickle.load(open('model.pkl', 'rb'))

def stemming(content):
    con=re.sub('[^a-zA-Z]', ' ', content)
    con=con.lower()
    con=con.split()
    con=[port_stem.stem(word) for word in con if not word in stopwords.words('english')]
    con=' '.join(con)
    return con

def fake_news(news):
    news=stemming(news)
    input_data=[news]
    vector_form1=vector_form.transform(input_data)
    prediction = load_model.predict(vector_form1)
    return prediction



if __name__ == '__main__':
    st.title('Fake News Classification app ')
    st.subheader("Input the News Title below")
    sentence0 = st.text_area("Enter your news Title here", "Why the Truth Might Get You Fired",height=200)
    st.subheader("Input the News Author below")
    sentence1 = st.text_area("Enter your news Author here", "Consortiumnews.com",height=200)
    sentence = sentence1+sentence0
    predict_btt = st.button("predict")
    if predict_btt:
        prediction_class=fake_news(sentence)
        print(prediction_class)
        if prediction_class == [0]:
            st.subheader('Reliable')
        if prediction_class == [1]:
            st.subheader('Unreliable')
