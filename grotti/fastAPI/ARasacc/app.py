import streamlit as st
import shutil
import requests
from PIL import Image

def main():
    st.header("Search for any image you want")
    locale ="it"
    search = st.text_input("What do you want to search for?")
    btn = st.button("search")
    if search:
        url = f"https://api.arasaac.org/api/pictograms/{locale}/search/{search}"
        result = requests.get(url.format(locale,search))
        json = result.json()
        id = json[0]["_id"]
        # download_url = f'https://api.arasaac.org/api/pictograms/{id}?download=false'
        # response = requests.get(result, stream=True)
        
    if btn:
        st.write(id)
        chiamata = f'https://api.arasaac.org/api/pictograms/{id}?download=false'
        # image = Image.open(result)
        st.image(chiamata)
    


if __name__ == "__main__":
    main()