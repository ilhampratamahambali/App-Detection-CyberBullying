from flask import Blueprint, request, render_template
import joblib
from utils.preprocessing import preprocess_text

# Buat blueprint
prediction_bp = Blueprint('prediction_bp', __name__)

# Load model dan tools
model = joblib.load('models/model_lr.pkl')
tfidf = joblib.load('models/tfidf_vectorizer.pkl')
label_encoder = joblib.load('models/label_encoder.pkl')

@prediction_bp.route('/predict', methods=['POST'])
def predict():
    tweet = request.form['tweet_text']

    # Preprocessing
    clean_tweet = preprocess_text(tweet)

    # TF-IDF dan prediksi
    tweet_tfidf = tfidf.transform([clean_tweet])
    prediction = model.predict(tweet_tfidf)
    label = label_encoder.inverse_transform(prediction)[0]

    return render_template('index.html', prediction_text=f'Hasil Prediksi: {label}')
