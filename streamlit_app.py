import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

#Crear un codigo repetible llamado funcion
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#New section to display fruity vice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('De que fruta te interesa información? ')
  if not fruit_choice:
    streamlit.error("Elija una fruta para obtener información")
  else:  
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except UrlError as e:
  streamlit.error()

streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur
  my_cur.execute("SELECT * FROM fruit_load_list")
  return my_cur.fetchall()

#Add a button to load the fruit
if streamlit.button('Get fruit load list'):  
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

#dont run anything ---troubleshooting section
streamlit.stop()
  
# Allow the enduser to add a fruit to the list
add_my_fruit = streamlit.text_input('Que fruta quieres añadir? ')
streamlit.write('Gracias por añadir --->   ', add_my_fruit) 

#codigo temporal
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
