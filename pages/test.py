
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
st.header("      INFORMATION DU PATIENT ET SYMPTOMES")





def predire():

    #entrer de lutilisateur 

    #Nom = st.number_input("Entrer votre nom",value=0)
    caracteristique_1 = st.number_input("Entrer votre age",min_value=17)
    caracteristique_2 = st.number_input("Entrer votre sexe M(1) ou F(0): ",min_value=0,max_value=1,value=1)
    caracteristique_3 = st.number_input("Avez-vous la fievre? OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_4 = st.number_input("Avez-vous le rhume? OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_5 = st.number_input("Avez_vous les frissons? OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_6 = st.number_input("Etes-vous la fatigue? OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_7 = st.number_input("Avez-vous le mal user_features? OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_8 = st.number_input("votre langue est-il amere? OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_9 = st.number_input("Avez-vous les vomissements? OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_10 = st.number_input("Avez-vous la diarrhe OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_11= st.number_input("Faites-vous des convulsions? OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_12= st.number_input("Avez-vous de l'anemie OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_13= st.number_input("Avez-vous la jaunisse OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_14= st.number_input("vos urines sont-ils couleur coca-cola OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_15= st.number_input("Avez-vous l'hypoglycemie OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_16= st.number_input("Avez-vous la prostration OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)
    caracteristique_17= st.number_input("Avez-vous l'hyperpyrexies OUI(1) OU NON(0): ",min_value=0,max_value=1,value=0)

    #creation dun pouton predict
    import joblib
    model= joblib.load(filename="modeleD.joblib")


    #
    def inference(caracteristique_1, caracteristique_2, caracteristique_3, caracteristique_4, caracteristique_5, caracteristique_6, caracteristique_7, caracteristique_8, caracteristique_9, caracteristique_10, caracteristique_11, caracteristique_12, caracteristique_13, caracteristique_14, caracteristique_15, caracteristique_16, caracteristique_17):
        user_features =np.array( [caracteristique_1, caracteristique_2, caracteristique_3, caracteristique_4, caracteristique_5, caracteristique_6, caracteristique_7, caracteristique_8, caracteristique_9, caracteristique_10, caracteristique_11, caracteristique_12, caracteristique_13, caracteristique_14, caracteristique_15, caracteristique_16, caracteristique_17])
        modele1_predict = model.predict(user_features.reshape(1,17))
        return modele1_predict

    #boutton predict
    if  st.button("predict"):
        predition=inference(caracteristique_1, caracteristique_2, caracteristique_3, caracteristique_4, caracteristique_5, caracteristique_6, caracteristique_7, caracteristique_8, caracteristique_9, caracteristique_10, caracteristique_11, caracteristique_12, caracteristique_13, caracteristique_14, caracteristique_15, caracteristique_16, caracteristique_17)
        
        if predition[0]== 1:
            st.write("La personne est atteinte du paludisme.")
        else:
            st.write("La personne n'est pas atteinte du paludisme.")
#p=st.button("commencez votre test!!!!!!!!")
#if p: 
predire()

