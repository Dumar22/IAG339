import nltk

try:
	nltk.download('punkt')
	print("NLTK 'punkt' tokenizer downloaded successfully.")
except Exception as e:
	print("An error occurred while downloading 'punkt':", e)