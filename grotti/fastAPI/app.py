import streamlit as st
import os
from dotenv import load_dotenv
import requests




def main ():
    st.title ("Previsioni del tempo")
    
    load_dotenv('.env')
    api_key : str = os.getenv('API_KEY')

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    
    city = st.text_input('Inserisci città')


    result = requests.get(url.format(city, api_key))     
    dato = result.json()
    tipo = st.radio('Cosa vuoi vedere?', ['coord', 'weather','visibility'])
    ricerca = dato[tipo]
    st.write(f'hai selezionato {tipo} e il risultato è : {ricerca}')
            



if __name__=="__main__":
    main()  