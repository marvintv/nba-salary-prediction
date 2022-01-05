import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

def load_model():
    with open('saved_file.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

#define model from pickle file
regressor = data["model"]


def show_predict_page(): 
    #Title, selection and images
    st.title('NBA Player Salary Prediction')
    st.sidebar.header('Player Data')
    image = Image.open('nba.png')
    st.image(image, '')
    def user_report():
        teams = (
            'Los Angeles Lakers', 'Los Angeles Clippers', 'Milwaukee Bucks',
        'Brooklyn Nets', 'Houston Rockets', 'Golden State Warriors',
        'Portland Trail Blazers', 'Philadelphia 76ers', 'Denver Nuggets',
        'Minnesota Timberwolves', 'Miami Heat', 'Utah Jazz',
        'Detroit Pistons', 'Boston Celtics', 'Dallas Mavericks',
        'San Antonio Spurs', 'Washington Wizards', 'Indiana Pacers',
        'Toronto Raptors', 'Sacramento Kings', 'Phoenix Suns',
        'Cleveland Cavaliers', 'New Orleans Pelicans', 'Orlando Magic',
        'Atlanta Hawks', 'Chicago Bulls', 'Oklahoma City Thunder',
        'New York Knicks', 'Memphis Grizzlies', 'Charlotte Hornets'
        )
        countries = (
            'United States', 'Other Countries'
        )
        positions = (
            'F', 'F-G', 'G', 'F-C', 'C', 'G-F', 'C-F'
        )
        rating = st.slider("Rating", 50, 75, 100)

        team = st.selectbox("Teams", teams)
        team = teams.index(team)

        position = st.selectbox("Position", positions)
        position = positions.index(position)

        age = st.slider("Age", 20, 34, 45)

        country = st.selectbox("Countries", countries)
        country = countries.index(country)

        user_report_data = {
        'rating':rating,
        'team':team,
        'position':position,
        'age':age,
        'country':country
        }
        report_data = pd.DataFrame(user_report_data, index=[0])
        return report_data


    user_data = user_report()
   # st.write(user_data)


    ok = st.button("Calculate Salary")
    if ok:
        st.subheader('Estimated value of NBA Player:')
        salary = regressor.predict(user_data)
        salary = str(np.round(salary[0], 2))
        salary = '{:0,.2f}'.format(float(salary))
 
        st.subheader('$'+ salary)
        #option to display what options you chose from inputs
        #st.write(user_data) 
