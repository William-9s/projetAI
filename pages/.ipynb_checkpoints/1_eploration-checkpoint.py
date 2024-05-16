import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import learning_curve
from sklearn.metrics import accuracy_score,f1_score

st.header("ANALYSE EXPLORATOIRE DES DONNEES")
def main():

    #charger la dataset
    file=st.file_uploader("telecharger votre dataset",type=["csv"])

    if file is not None:
        data=pd.read_csv(file)
        st.dataframe(data)
        
        fig=px.bar(data_frame=pd.DataFrame(data),x="age",y="sex",title="mamam")
        st.plotly_chart(fig)
        #diagramme a barre
        # bar_data=pd.dataframe(data)
        #st.barchart(bar_data)


        #nuage des points   
        cars==pd.read_csv("patient_data_edited.cvs")
        st.data_frame(cars)
        numeric_cols=cars.select_types(exclude="object").conlums.to_list()
        var_x=st.selectbox("choisir la valeur dabscice",numeric_cols)
        var_y=st.selectbox("choisir la valeur dordonne",numeric_cols)
        
        fig2=px.scatter(data_frame=cars,x=var_x,y=var_y,title=str(var_y)+"vs"+str(var_x))
        st.plotly_chart(fig2)
if __name__=="__main__":
     main()