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
        
        #fig=st.bar_chart(data_frame=pd.DataFrame(data),x="age",y="sex",title="mamam")
        #st.plotly_chart(fig)
        
        if st.button("donnee lineaire"):
            st.line_chart(data)
            

        if st.button("histogramme"):
            
            fig1,ax1=plt.subplots(figzise(20,20)) 
            ax1=plt.hist(data,bins=5)
            
            st.pyplot(fig1)   
        
        if st.button("diagramme a bar"):
            bar=pd.DataFrame(data)
            st.bar_chart(bar)
        # Affichage du nuage de points
        if st.button("nuage des points"):
            plt.scatter(data)
            st.pyplot()

        # Calcul de la matrice de corelation






if __name__=="__main__":
     main()