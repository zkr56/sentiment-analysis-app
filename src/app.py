import streamlit as st
import pandas as pd
import pickle
from utils.text_processing import clean_text

# Chargement du modèle, du vectorizer et de l'encodeur de labels
with open('models/sentiment_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('models/vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

with open('models/label_encoder.pkl', 'rb') as label_encoder_file:
    label_encoder = pickle.load(label_encoder_file)

# Titre de l'application
st.title("Analyse des Sentiments des Commentaires")

# Zone de texte pour l'entrée de l'utilisateur
user_input = st.text_area("Entrez votre commentaire ici:")

# Bouton pour soumettre le commentaire
if st.button("Analyser"):
    if user_input:
        # Nettoyage du texte
        cleaned_text = clean_text(user_input)
        
        # Vectorisation du texte nettoyé
        text_features = vectorizer.transform([cleaned_text])
        
        # Prédiction du sentiment
        prediction = model.predict(text_features)
        decoded_prediction = label_encoder.inverse_transform(prediction)
        
        # Affichage du résultat
        st.success(f"Sentiment prédit: {decoded_prediction[0]}")
    else:
        st.warning("Veuillez entrer un commentaire avant de soumettre.")