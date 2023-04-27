import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def main ():
    st.title ("es Machine")
    numero_punti = st.slider('punti da calcolare', 0, 100, 50)
    random = np.random.RandomState ()
    x = 10 * random.rand(numero_punti)
    noise = random.randn(numero_punti)
    coef = st.slider('coefficiente', 0, 10, 3)
    y = coef*x + noise


    fig = plt.figure(figsize=(10,8))
    plt.scatter (x,y);

    st.pyplot(fig)


    if st.button('Regressione lineare'):
    
        X = x.reshape(-1, 1)
        y = y

        model = LinearRegression(fit_intercept=True)
        model.fit(X, y)

        y_pred = model.predict(X)
        fig2 = plt.figure(figsize = (10, 8))
        plt.scatter(x, y);
        plt.plot(x, y_pred,'-r');
        plt.title('Simple Linear Regression')
        st.pyplot(fig2)

        st.text(f"Il modello è : {round(model.coef_[0],2)} *x + {round(model.intercept_,2)}")






if __name__=="__main__":
    main()  