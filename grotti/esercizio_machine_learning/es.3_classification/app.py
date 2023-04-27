import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import seaborn as sns


def main ():

    st.title ("IRIS CLASSIFICATION")
    df_iris= pd.read_csv('iris.data',names=["sepal length","sepal width","petal length","petal width","class"])


    y = df_iris["class"]
    X = df_iris.drop("class",axis=1)

    X.to_csv("sample_csv", index=False)


    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size = 0.20, 
                                                    random_state = 667
                                                    )

    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    res_df = pd.DataFrame(data=list(zip(y_pred, y_test)),columns=['predicted', 'real'])


    sepal_length=st.number_input('sepal_length')
    sepal_width=st.number_input('sepal_width')
    petal_length=st.number_input('petal_length')
    petal_width=st.number_input('petal_width')

    model.predict([[sepal_length,sepal_width,petal_length,petal_width]])[0]
    
    
    uploaded_file= st.file_uploader('carica file')
    if uploaded_file is not None:
#MIA SOLUZIONE FUNZIONANTE
        file = uploaded_file.name
        array = np.loadtxt(file,skiprows=1, delimiter=',')
        pred=model.predict(array)
      
        df_upload = pd.DataFrame(data=array)
        df_upload['prediction']=pred
        
        csv= df_upload.to_csv()
        #csv= df_upload.to_excel()

        st.download_button(label="Download ", data=csv, mime='text/csv')
            

        


#SOLUZIONE FUNZIONANTE DI GROTTI
        # df_up= pd.read_csv(uploaded_file)
        # st.dataframe(df_up)
        # pred=model.predict(df_up.to_numpy())
        # #download button 2 to download dataframe as xlsx
        # st.write(pred)
        # df_up['prediction']=pred
      
        # import io
        # buffer = io.BytesIO()
        # with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        #     # Write each dataframe to a different worksheet.
        #     df_up.to_excel(writer, sheet_name='Sheet1', index=False)
        #     # Close the Pandas Excel writer and output the Excel file to the buffer
        #     writer.save()

        #     download2 = st.download_button(
        #         label="Download Excel",
        #         data=buffer,
        #         file_name='risultati.xlsx',
        #         mime='application/vnd.ms-excel')
    




if __name__=="__main__":
    main()  