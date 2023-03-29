import streamlit as st

st.title('Noleggia auto')

if 'False' not in st.session_state:
    st.session_state.disabled = True
    
age_select=st.number_input('Inserisci la tua età', 0, 120,)
st.checkbox("Disable radio widget",key="disabled")
#age=st.slider('Seleziona la tua età', 0, 100, 18)
patente=st.radio(
            'Hai la patente?',
            ['SI','NO'], 
            key="False",
            disabled=st.session_state.disabled,
        )


# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False
#     st.session_state.horizontal = False

# col1, col2 = st.columns(2)

# with col1:
#     st.checkbox("Disable radio widget", key="disabled")
#     st.checkbox("Orient radio options horizontally", key="horizontal")

# with col2:
#     st.radio(
#         "Set label visibility 👇",
#         ["visible", "hidden", "collapsed"],
#         key="visibility",
#         label_visibility=st.session_state.visibility,
#         disabled=st.session_state.disabled,
#         horizontal=st.session_state.horizontal,
#     )


# def go_nogo (age_select,patente):
#     if (age_select < 0):
#         go_nogo='come fai ad avere meno di zero anni?'

#     else: 
#         if (age_select >=18 and patente=='SI'):
#             go_nogo='daje!'
#         elif (age_select >=18 and patente=='NO'):
#             go_nogo='devi prima prendere la patente'
#         else : 
#             go_nogo='sei un bimbo, cresci e ripassa'
#     return(go_nogo)


# if st.button('Verifica'):
    
#     while (go_nogo(age_select,patente) != 'daje'):
#         st.snow()
#     else:
#         st.balloons()

#     st.write(go_nogo(age_select,patente))



