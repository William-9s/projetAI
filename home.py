import streamlit as st

from PIL import Image

def main():
    st.header("APPLICATION DE DETECTION DU PALUDISME")
    st.write("")
    st.write("")
    st.write("")
    image2 = '/home/william/projet/image2.jpeg' 
    st.image(image2, caption='', use_column_width=True)

    st.write("")
    st.write("")
    st.write("")
    st.subheader("ANALYSE ET BILAN ACTUEL DU PALUDISME EN AFRIQUE")
    st.write("")
    st.write("")
    st.write("""Le paludisme, egalement connu sous le nom de malaria, est une maladie parasitaire transmise 
      a l'homme principalement par la piqure de certains moustiques.Le paludisme est particulierement repandu en AFRIQUE,
     ou il represente un fardeau significatif pour la sante publique.En effet, 95%  des deces dus au paludisme surviennent en AFRIQUE
     ce qui en fait la region la plus touchee par cette maladie.En 2024, le paludisme continue de representer un lourd fardeau pour les pays d' ARIQUE,
      subsharienne, avec un nombre important de cas enregistres dans plusieurs pays de la region.La lutte contre le moustique porteur de la maladie reste une priorite pour l'OMS.""")
    st.write("")
    st.write("")

    st.subheader("OBJECTIF DU PROJET")
    st.write("""L'objectif de notre projet est d'utiliser l'intelligence artificielle afin de detecter si un individu est atteint du paludisme ou pas a partir des symptomes que presente cet individu. """)

if __name__=="__main__":
    main() 