from datetime import date
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    return age 


@st.cache
def load_data():
    df = pd.read_csv("nba2k-full.csv")

    #remove undrafted players
    df = df[~df["draft_round"].isin(['Undrafted'])] 
    df = df[~df["draft_peak"].isin(['Undrafted'])]

    #remove '$' char from salary
    df['salary'] = df['salary'].map(lambda x: x.lstrip('$'))
    df['salary'] = df['salary'].astype(int)

    #selected columns to train 
    df = df[["rating", "team", "position", "b_day", "country", "salary"]]
    df = df[df["salary"].notnull()]
    df = df.dropna()

    #format birthdate and assign age to each row 
    df["b_day"] = pd.to_datetime(df["b_day"])
    df["b_day"] = df["b_day"].apply(calculateAge)
    df = df.rename({"b_day": "age"}, axis=1)



    return df

df = load_data()

def show_explore_page():
    st.title("Explore NBA Salaries")

    st.write(
        """
    ### Explore Kaggle NBA2k20 dataset
    """
    )

    data = df['age'].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Number of Player from different ages""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Average Salary Based on Player Rating
    """
    )

    data = df.groupby(['rating'])['salary'].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Average Salary Based on Team
    """
    )

    data = df.groupby(["team"])["salary"].mean().sort_values(ascending=True)
    st.line_chart(data)