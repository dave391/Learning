import streamlit as st
import json
import requests

def main():



    st.title('My first API app')

    num1=st.number_input('Inserisci il primo numero')
    num2=st.number_input('Inserisci il secondo numero')
    num3=st.number_input('Inserisci il terzo numero')

    operation= st.selectbox("Che cosa vuoi fare?", ('sum', 'mult'))
    
    if st.button ("Esegui GET"):
        res = requests.get(url=f"http://127.0.0.1:8000/{operation}?num1={num1}&num2={num2}&num3={num3}")
        res= res.json()
        st.markdown(f"Risultato GET : {res['result']}")

    if st.button ("Esegui PUT"):
        url = f"http://localhost:8000/{operation}"


        data = {
                "operation" : operation,
                "numero1": num1,
                "numero2": num2,
                "numero3": num3,
                }

        data_keys = data.keys()
        response =requests.post(url,
                                headers={"Content-Type": "application/json"},
                                data = json.dumps({"num1":data['numero1'],
                                                "num2":data['numero2'],
                                                "num3":data['numero3']})
                                )
        response =response.json()
        st.markdown(f"Risultato PUT : {response['result']}")


if __name__ == '__main__':
	main()