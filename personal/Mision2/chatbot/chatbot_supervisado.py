from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

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
	return model, vectorizer, unique_answers

def predict_answer(model, vectorizer, unique_answers, user_text):
	x = vectorizer.transform([user_text])
	predicted_label = model.predict(x)[0]
	return unique_answers[predicted_label]
if __name__ == "__main__":
	training_data = [
		("buenos días", "!Buenos días¡"),
		("Hola", "Hola!, en que puedo ayudarte?"),
		("Como estas?", "Soy solo un bot, pero estoy aquí para ayudar!"),
		("adiós", "!HAsta luego¡"),
		("tu nombre", "Soy un chatbot de ejmplo"),
		("que puedes hacer", "Puedo responder preguntas simples")
	]
	model, vectorizer, unique_answers = build_and_train_model(training_data)

	print("Chatbot supervisado listo, Escribe salir pra terminar")

	while True:
		user_input = input("Tú: ").strip()
		if user_input.lower() in {"salir","exit","quit"}:
			print("Bot: !hasta luego¡")
			break
		response = predict_answer(model, vectorizer, unique_answers, user_input)
		print("Bot: ", response)

			