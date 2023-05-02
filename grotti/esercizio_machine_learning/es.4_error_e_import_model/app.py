import streamlit as st
import pandas as pd
import mlem

def main ():
    st.title ("es linear regression con import modello")
    
    #uploaded_file= st.file_uploader('carica file')

    R_D_Spend= st.number_input('Inserisci le spese di Ricerca e Sviluppo',0,10000,5000)
    Administration = st.number_input('Inserisci le spese di amministrazione',0,10000,5000)
    Marketing_Spend	= st.number_input('Inserisci le spese di marketing',0)


    new_model = mlem.api.load('model_.mlem')
    
    if Marketing_Spend != 0:

        pred= new_model.predict([[R_D_Spend,Administration,Marketing_Spend]])
        st.write(pred[0])
    
if __name__=="__main__":
    main()  