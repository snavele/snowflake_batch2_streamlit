import streamlit
streamlit.title('My Parents new Healthy Diner')

streamlit.header('🥣 🥗 Breakfast Menu 🐔 🥑🍞')
streamlit.text('🐔 Boiled Eggs')
streamlit.text('🍞 Bread Omlet')
streamlit.text('Tea/Coffee')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🍞 🐔 Hard-Boiled Free-Range Egg')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
