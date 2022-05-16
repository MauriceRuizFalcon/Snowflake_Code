import streamlit
import pandas
streamlit.title('Restaurante Mayimba')
streamlit.header('MENÚ DESAYUNO')
streamlit.text('Cafe de olla')
streamlit.text('Huevos rancheros')
streamlit.text('🍞 Pan')
streamlit.text('Pan de dulce')
streamlit.header('MENÚ COMIDA')
streamlit.text('Arroz blanco')
streamlit.text('🥣 Caldo de verduras')
streamlit.text('🐔 Pollo en papas')
streamlit.text('🥑 Ensalada')
streamlit.header('🍌🥭 Crea tus batidos de frutas 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Se coloca una seleccion de la lista de frutas
fruits_selected = streamlit.multiselect("Selecciona tus frutas favoritas :", list(my_fruit_list.index),['Avocado','Strawberries','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# despliega la tabla en la pagina
streamlit.dataframe(fruits_to_show)

#New section to display fruity vice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('De que fruta te interesa información? ' + 'Kiwi')
streamlit.write('El usuario escogio', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#take the json version of the response and normaliz it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table
streamlit.dataframe(fruityvice_normalized)
