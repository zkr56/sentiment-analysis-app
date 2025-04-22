def clean_text(text):
    import re
    text = re.sub(r'@[\w]*', '', text)  # Suppression des mentions (@username)
    text = re.sub(r'#[\w]*', '', text)  # Suppression des hashtags
    text = re.sub(r'<.*?>', '', text)   # Suppression des balises HTML
    text = re.sub(r'http\S+|www\S+', '', text)  # Suppression des URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Suppression des caractères non alphabétiques
    text = re.sub(r'\s+', ' ', text).strip()  # Suppression des espaces multiples
    return text.lower()