import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Inisialisasi
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Fungsi pembersihan teks (sesuai dengan di notebook)
def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    
    # lowercase
    text = text.lower()
    
    # hapus url, username, hashtag
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"@\w+|#\w+", "", text)
    
    # hapus emoji dan karakter non-ascii
    text = text.encode("ascii", "ignore").decode()
    
    # hapus tanda baca dan angka
    text = re.sub(r"[^a-z\s]", " ", text)
    
    # tokenisasi
    words = nltk.word_tokenize(text)
    
    # hapus stopwords dan kata pendek (< 3 huruf)
    words = [w for w in words if w not in stop_words and len(w) > 2]
    
    # stemming
    words = [stemmer.stem(w) for w in words]
    
    return " ".join(words)
