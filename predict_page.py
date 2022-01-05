import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image

def load_model():
    with open('model.sav', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()




def show_predict_page(): 
    def user_report():
        teams = (
        'Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets',
        'Charlotte Hornets', 'Chicago Bulls', 'Cleveland Cavaliers',
        'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons',
        'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers',
        'Los Angeles Clippers', 'Los Angeles Lakers', 'Memphis Grizzlies',
        'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves',
        'New Orleans Pelicans', 'New York Knicks', 'Oklahoma City Thunder',
        'Orlando Magic', 'Philadelphia 76ers', 'Phoenix Suns',
        'Portland Trailblazers', 'Sacramento Kings', 'San Antonio Spurs',
        'Toronto Raptors', 'Utah Jazz', 'Washington Wizards',
        'New Orleans Hornets', 'Charlotte Bobcats', 'New Jersey Nets',
        'Seattle SuperSonics', 'Vancouver Grizzlies', 'Washington Bullets'
        )
        seasons = (
        '2017-18', '2016-17', '2015-16', '2014-15', '2013-14', '2012-13',
        '2011-12', '2010-11', '2009-10', '2008-09', '2007-08', '2006-07',
        '2005-06', '2004-05', '2003-04', '2002-03', '2001-02', '2000-01',
        '1999-00', '1998-99', '1997-98', '1997-97', '1995-96', '1994-95',
        '1993-94', '1992-93', '1991-92', '1990-91'
        )
    
        team = st.selectbox("Teams", teams)
        team = teams.index(team)
        season = st.selectbox("Season", seasons)
        season = seasons.index(season)
        user_report_data = {
        'Team':team,
        'Season':season
        
        }
        report_data = pd.DataFrame(user_report_data, index=[0])
        return report_data


    #Title, selection and images
    st.title('NBA Player Salary Prediction')
    st.sidebar.header('Player Data')
    image = Image.open('nba.png')
    st.image(image, '')
    user_data = user_report()
    st.write(user_data)



    salary = data.predict(user_data)
    st.subheader('Player Salary Prediction:')
    st.subheader('$'+str(np.round(salary[0], 2)))