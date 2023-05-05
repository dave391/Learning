import streamlit as st
import requests



def main ():
    st.title ("ARASAAC")
    
    

    i = st.number_input('Inserisci id')

    url = f'https://api.arasaac.org/api/pictograms/{i}?download=false'
    
    response = requests.get(url)

    st.write(response)     
    
    st.image(url)         



if __name__=="__main__":
    main()  