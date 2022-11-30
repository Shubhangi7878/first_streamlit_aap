import streamlit
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & bluberry Oatmeal')
streamlit.text('🥗 Kale, snipach @ rocket smothie')
streamlit.text('🦃 Hard-boild free-range egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected =streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),[1,2])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
my_fruit_list = my_fruit_list.set_index('Fruit')
