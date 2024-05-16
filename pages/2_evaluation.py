import streamlit as st
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

st.header("PRECISION")

dataset=pd.read_csv("patient_data_edited.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

import joblib
model1= joblib.load(filename="modeleD.joblib")

import joblib
model2= joblib.load(filename="modelek.joblib")

st.write("precision des madeles:")
import streamlit as st

st.title("ARBRE DE DECISION")

if st.button("evaluer le resultat de prediction de larbre de decision"):

    image1 = '/home/william/projet/apprentissage.png'
    st.image(image1, caption="courbe d'apprentissage", use_column_width=True)


    image2 = '/home/william/projet/confusion.png' 
    st.image(image2, caption='matrice de confusion', use_column_width=True)
if st.button("pourcentage de prediction:"):
    st.write("le score de l'abre de decision est: ",model1.score(X_train,y_train))
    


st.title("K-PLUS PROCHES VOISIN")

if st.button("evaluer le resultat de prediction du k-plus proche voisin"):

    image1 = '/home/william/projet/image2.png'
    st.image(image1, caption="courbe d'apprentissage", use_column_width=True)

    image2 = '/home/william/projet/image1.png' 
    st.image(image2, caption='matrice de confusion', use_column_width=True)
   
if st.button("pourcentage de prediction"):
    st.write("le score du k-plus proche voisin  est: ",model2.score(X_train,y_train))
