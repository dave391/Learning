import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import seaborn as sns


def main ():

    st.title ("es 2")
    path_startup = "https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Startup.csv"
    path_company = "https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Company.csv"

    df_startup = pd.read_csv('https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Startup.csv')
    df_company = pd.read_csv('https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Company.csv')


    scaler = MinMaxScaler()
    arr_scaled_startup = scaler.fit_transform(df_startup)
    df_scaled_startup = pd.DataFrame(arr_scaled_startup, columns= [["R&D_Spend","Administration","Marketing_Spend","Profit"]])
    arr_scaled_company = scaler.fit_transform(df_company)
    df_scaled_company = pd.DataFrame(arr_scaled_company, columns= [["TV","Radio","Newspaper","Sales"]])



    if st.button('Heatmap correlazione Startup'):
        fig =  plt.figure(figsize = (10, 8))
        sns.heatmap(data=df_scaled_startup.corr(),annot=True,cmap="crest")
        st.pyplot(fig)

    if st.button('Heatmap correlazione Company'):
        fig =  plt.figure(figsize = (10, 8))
        sns.heatmap(data=df_scaled_company.corr(),annot=True)
        st.pyplot(fig)


    


    if st.button('Calcola il modello'):
    
        y = df_startup["Profit"]
        X = df_startup.drop("Profit",axis=1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size = 0.2, 
                                                    random_state = 667
                                                    )
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        res_profit_df = pd.DataFrame(data=y_pred,columns=['profit_predicted'])
        res_profit_df

        res_df = pd.DataFrame(data=list(zip(y_pred, y_test)),columns=['profit_predicted', 'real'])
        res_df['error'] = res_df['real'] - res_df['profit_predicted']
        res_df

        st.text(f"profitto medio predetto: {round(res_profit_df['profit_predicted'].mean(),2)}")

        st.text(f"profitto medio reale: {round(y_test.mean())}")

        error=res_profit_df['profit_predicted'].sum()- y_test.sum()
        percent = (error/y_test.sum())*100

        st.text(f"l'errore totale è della prediction è : {error} pari al {round(percent,2)}% ")


        st.text(f"Il modello è : {round(model.intercept_,2)} + {round(model.coef_[0],2)} *x + {round(model.coef_[1],2)} *x1 + {round(model.coef_[2],2)} *x2")


    #if st.button('Predici risultati'):
        
    r_d=st.number_input('Inserisci costi di R&D')
    administration=st.number_input('Inserisci costi di amministrazione')
    marketing = st.number_input('Inserisci costi di marketing')
    time = st.number_input('Inserisci numero mesi di riferimento',min_value=1,max_value=12)
        

    
    r_d_annualized = (r_d/time) * 12
    administration_annualized = (administration/time) * 12
    marketing_annualized = (marketing/time)*12
    profit_predicted =  46722.41 + 0.82 *r_d_annualized+ -0.03 *administration_annualized + 0.03 *marketing_annualized
    st.text(f"I profitti previsti per l'anno sono : {profit_predicted}")








if __name__=="__main__":
    main()  