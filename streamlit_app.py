import streamlit
import pandas
streamlit.title('Restaurante Mayimba')
streamlit.header('MENÚ DESAYUNO')
streamlit.text('Café de olla')
streamlit.text('Huevos rancheros')
streamlit.text('🍞 Pan')
streamlit.text('Pan de dulce')
streamlit.header('MENÚ COMIDA')
streamlit.text('Arroz blanco')
streamlit.text('🥣 Caldo de verduras')
streamlit.text('🐔 Pollo en papas')
streamlit.text('🥑 Ensalada')
streamlit.header('🍌🥭 Batidos de frutas 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
