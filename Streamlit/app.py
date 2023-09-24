import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import chart_studio.plotly as py
import matplotlib.pyplot as plt

# THIS IS THE CSV FILE TO READ
df = pd.read_csv('Mental health Depression disorder Data.csv')

#The first thing I am going to do is create a container to make sections in a horizontal mannerinst
header = st.container()
data_used_lebanon = st.container()
data_used_world = st.container()

#The first part is going to be the header section
with header:
    st.title('Mental Health Depression Disorder Data')
    st.text('This project will focus on looking at Mental Health Depression Disorder Data collected from countries around the world')

with data_used_world:   
   
   st.header("Alcohol use around the world")
   st.subheader("Below you can choose what country you'd like to see data from")
   
   # This is to create the buttons in order to select a country.
   select_a_country = st.selectbox("Select a Country", df['Entity'].unique())
   divide_countries = df[df['Entity'] == select_a_country]

   # This is so that I can adjust the graph to show the years on the X axis, not just the country.
   years = list(range(1990, 2018))

    # This is the graph I created on plotly for Alcohol use disorders for all countries over the world.
    # The code in this is edited to fit the "divide_countries" variable I created.
    # The code adjusts the years, and includes a new title for each year chosen from the list.

fig_bar = px.bar(
    divide_countries,
    x='Year', 
    y='Alcohol use disorders (%)',
    title=f'Alcohol use Disorder in {select_a_country}',
    labels={'Alcohol use disorders (%)': 'Percentage'},
    category_orders={'Year': years} 
)

st.plotly_chart(fig_bar)

st.write("In plotly, I had created a bar graph which combined all countries around the world and their relation to Alcohol use Disorders. With streamlit, I found it interesting to apply this method by being able to manually choose whichever country I am interested in, and receive a seperate bar chart for this data (as demonstrated aboe)")

with data_used_lebanon:
 
# This is basically to denote the start of the app
 def start():
    st.title('Health Disorders in Lebanon (1990-2017)')

    # I will start by creating labels for the disorders from the CSV file imported
    disorders = [
        "Schizophrenia (%)",
        "Eating disorders (%)",
        "Anxiety disorders (%)",
        "Drug use disorders (%)",
        "Depression (%)",
        "Alcohol use disorders (%)"
    ]

    # I did research to see how I can adjust the size of the pie chart in accordance to the slider, and I got that I should create 2 columns by using the function "st.columns"
    col1, col2 = st.columns([5, 1])  # Adjust the column widths as needed

    # SLIDER COMMAND (placed in column 1)
    select_a_year = col1.slider('Select a Year', min_value=1990, max_value=2017, step=1)

    # Extracting the exact data from the CSV file. Second line makes sure that it extracts the values and stores them in that list. 
    year_data = df[(df['Entity'] == 'Lebanon') & (df['Year'] == select_a_year)]
    values = [year_data[disorder].values[0] for disorder in disorders]
    
    # Without this part, I had the labels as percentages, so I had to adjust them to make the chart look better visually.
    # disorder.split(' ')[0]: To extract only the name from the "disorders" list without the percentage.
    # Second line used to remove the ":" and the percentage value after it.
    labels = [f"{disorder.split(' ')[0]}:\n{values[i]:.2f}%" for i, disorder in enumerate(disorders)]
    labels = [label.split(':')[0] for label in labels]

    # Create the figure itself. Used functions such as explode, label distance, and label rotation to design/fix the way the pie chart looks.
    fig, ax = plt.subplots()
    explode = (0, 0.2, 0.1, 0.1, 0.1, 0.1)
    labeldistance = 1.2
    label_rotation = 50 
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, explode=explode, labeldistance=labeldistance, textprops={'rotation': label_rotation})
    ax.axis('equal')

    # This part is to place a header/title depending on the year selected on the slider.
    col1.header(f'Health Disorders in Lebanon for {select_a_year}')
    col1.pyplot(fig)
    
if __name__ == '__main__':
    start()

    st.write("")
    st.write("")
    st.subheader("Why I chose to visualize this?")
    st.write("When I was looking for a dataset from Kaggle, I found this one to be interesting since I could play around with the data and relate to events that have occured in different countries. In the case of Lebanon, the civil war ended in 1990. For that reason, I thought it would be interesting to see if there was any real change in health disorders since then.")
