import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

MODEL_DIR="models"
MODEL_PATH=os.path.join(MODEL_DIR,"model.pkl")
VECTORIZER_PATH=os.path.join(MODEL_DIR,"vectorizer.pkl")
ANSWERS_PATH=os.path.join(MODEL_DIR,"answers.pkl")

def build_and_train_model(train_pairs):
	questions = [q for q, _ in train_pairs]
	answers = [a for _, a in train_pairs]
	vectorizer = CountVectorizer()
	x=vectorizer.fit_transform(questions)

	unique_answers = sorted(set(answers))
	answer_to_label = {a:i for i,a in enumerate(unique_answers)}
	y = [answer_to_label[a] for a in answers]
	model = MultinomialNB()
	model.fit(x,y)
	# crear el directorio para el modelo si no existe
	os.makedirs(MODEL_DIR, exist_ok=True)
	# guardar el modelo entrenado
	with open(MODEL_PATH, "wb") as f:
		pickle.dump(model, f)
	# guardar el vectorizador
	with open(VECTORIZER_PATH, "wb") as f:
		pickle.dump(vectorizer, f)
	# guardar las respuestas únicas
	with open(ANSWERS_PATH, "wb") as f:
		pickle.dump(unique_answers, f)
	print("Modelo entrenado y guardado en", MODEL_DIR)

	return model, vectorizer, unique_answers

def load_model():
	if (
		not os.path.exists(MODEL_PATH)
		and os.path.exists(VECTORIZER_PATH)
		and os.path.exists(ANSWERS_PATH)
	):
		with open(MODEL_PATH, "rb") as f:
			model = pickle.load(f)
		with open(VECTORIZER_PATH, "rb") as f:
			vectorizer = pickle.load(f)
		with open(ANSWERS_PATH, "rb") as f:
			unique_answers = pickle.load(f)
		print("Modelo cargado desde", MODEL_DIR)
		return model, vectorizer, unique_answers	
	else:
		print("Modelo no encontrado. Entrena el modelo primero.")
		return None, None, None
	
def predict_answer(model, vectorizer, unique_answers, user_text):
	x = vectorizer.transform([user_text])
	predicted_label = model.predict(x)[0]
	return unique_answers[predicted_label]