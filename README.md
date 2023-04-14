# Steam Game Recommendation System
## Introduction
This project is a content-based recommender system designed to recommend games based on user input. The model is built using Scikit Learn's cosine similarity function and is deployed on a website using Streamlit. The dataset used is steam.csv.

## File Structure
The repository is split into several files:

- **app.py:** This file contains the main code for the Streamlit app.
- **predict_page.py:** This file contains the actual model for the game recommender system.
- **steam.csv:** This file is the dataset used to train and test the model.

## Usage
To use the game recommender system, visit https://juliusthecreator-steam-game-recommender-app-uherl8.streamlit.app/. 

The website may take some time to load, especially if there has been inactivity. Once loaded, the user can enter a game title in the search bar and the recommender system will suggest 5 similar games based on user input.
