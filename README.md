# Application d'Analyse de Sentiment

Ce projet est une application web permettant d'analyser le sentiment des commentaires des utilisateurs à l'aide d'un modèle d'apprentissage automatique pré-entraîné. L'application est construite avec Streamlit, permettant aux utilisateurs de saisir des commentaires et de recevoir une analyse de sentiment en temps réel.

## Structure du Projet

```
sentiment-analysis-app
├── src
│   ├── app.py                # Point d'entrée principal de l'application Streamlit
│   ├── models
│   │   ├── sentiment_model.pkl  # Modèle de classification des sentiments entraîné
│   │   ├── vectorizer.pkl       # Instance de TfidfVectorizer pour la transformation des textes
│   │   └── label_encoder.pkl    # Instance de LabelEncoder pour l'encodage/décodage des labels
│   ├── utils
│   │   └── text_processing.py   # Fonctions utilitaires pour le prétraitement des textes
│   └── __init__.py              # Traite le répertoire src comme un package Python
├── requirements.txt              # Liste des dépendances du projet
├── .gitignore                    # Fichiers et répertoires à ignorer par Git
└── README.md                     # Documentation du projet
```

## Installation

1. Clonez le dépôt :
   ```
   git clone <url-du-dépôt>
   cd sentiment-analysis-app
   ```

2. Installez les packages requis :
   ```
   pip install -r requirements.txt
   ```

## Utilisation

Pour exécuter l'application, lancez la commande suivante dans votre terminal :
```
streamlit run src/app.py
```

Une fois l'application lancée, vous pouvez entrer un commentaire dans la zone de texte fournie et le soumettre pour voir les résultats de l'analyse de sentiment.

## Dépendances

Ce projet nécessite les packages Python suivants :
- Streamlit
- scikit-learn
- pandas
- imbalanced-learn

## Licence

Ce projet est sous licence MIT.