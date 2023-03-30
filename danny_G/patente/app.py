import streamlit as st
import datetime
from datetime import timedelta
import time

st.title('Noleggia auto')

disabled_patente = True
disabled_age_input = True
disabled_slider = True
disabled_data = True

option = st.radio (
    'Come vuoi inserire la tua età?',
    ('Input', 'Slider','Data'), horizontal=True)

if option == 'Input':
   disabled_age_input = False 
elif option == 'Slider':
   disabled_slider = False 
else :
   disabled_data = False 
   

age_input=st.number_input('Inserisci la tua età', 0, 120, disabled = disabled_age_input)
age_slider=st.slider('Seleziona la tua età', 0, 100, 0, disabled= disabled_slider)  
age_data= st.date_input( "Inserisci la tua data di nascita",
                            min_value = datetime.date(1900, 1, 1),
                            max_value = datetime.datetime.today().date(), 
                            disabled= disabled_data)



if age_input>0 or age_slider>0 or age_data != datetime.datetime.today().date() :
    patente=st.radio(
                'Hai la patente?',
                ['SI','NO'], 
                
            )


maggiorenne = datetime.datetime.today().date()-timedelta(days=6570)
    
if age_data < maggiorenne:
    data_go = '1'
else :
    data_go = '0'


def go_nogo (age_input,age_slider,data_go,patente):

    if (((age_input >=18) or (age_slider>=18) or (data_go=='1') ) and (patente=='SI')):
        go_nogo='daje!'
    elif (((age_input >=18) or (age_slider>=18) or (data_go=='1')) and  (patente=='NO')):
        go_nogo='devi prima prendere la patente'
    else : 
        go_nogo='sei un bimbo, cresci e ripassa'
    return(go_nogo)


if st.button('Verifica'):
    
    with st.spinner('Stiamo controllando'):
        time.sleep(3)

    if (go_nogo(age_input,age_slider,data_go,patente) == 'daje!'):
        st.balloons()
        st.success(go_nogo(age_input,age_slider,data_go,patente))
    else:
        st.error(go_nogo(age_input,age_slider,data_go,patente))
    


