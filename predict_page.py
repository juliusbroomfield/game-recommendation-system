import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import streamlit as st


def extract_year(year):
    year = year[:4]
    return year

def to_lower(element:str):
    return element.lower()

# Import Data
df = pd.read_csv("steam.csv")

df = df[['appid','name','release_date','genres','steamspy_tags','positive_ratings','negative_ratings','owners']]


# Create New Column for Percent of Positive Reception
df['reception'] = df['positive_ratings'] / (df['negative_ratings'] + df['positive_ratings'])
df['reception'] = df['reception'].apply(lambda x: round(x * 100, 2))


df['steamspy_tags'] = df['steamspy_tags'].str.replace(' ', '-')
df['genres'] = df['steamspy_tags'].str.replace(';', ' ')

df['year'] = df['release_date'].apply(extract_year)

df.drop(['positive_ratings', 'negative_ratings', 'steamspy_tags', 'release_date'], axis = 1, inplace = True)
df = df.astype({'year': 'string', 'reception': 'string'})
df['target_features'] = df['year'] + " " + df['genres'] + " " + df['reception'] + " "

cv = CountVectorizer(stop_words = 'english')
cm = cv.fit_transform(df['target_features'])

cosine_sim = cosine_similarity(cm, cm)


def get_rec(nam: str):
    index = df[df['name'] == nam].index.to_list()[0]
    score = list(enumerate(cosine_sim[index]))
    score = sorted(score, key=lambda x: x[1], reverse=True)
    score = score[1:11]
    # Highest 10 Scores / Closest 10 Games
    best = [i[0] for i in score]
    best = df['name'].iloc[best]
    best.reset_index()
    return best

# ----------------------------------------------------------------------------------------------------------------


def show_predict_page():
    st.title("Steam Game Recommendation")
    st.write("Created by JuliustheCreator")
    user_game = st.text_input("Input Your Game Here:")
    button_pressed = st.button("Find Games")
    if button_pressed:
        scores = get_rec(user_game.title())
        st.write(scores)




