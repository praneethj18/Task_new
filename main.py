from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class TextInput(BaseModel):
    text:str
def get_words(text):
    return text.split()
def get_sentence_count(text):
    return sum(text.count(x) for x in ".!?")
def get_average_word_length(words):
    if not words:
        return 0
    total=sum(len(word.strip(".,!?")) for word in words)
    return round(total/len(words),2)
@app.post("/analyze")
def analyze(data:TextInput):
    text=data.text.strip()
    if not text:
        return {"error":"Text cannot be empty"}
    words=get_words(text)
    clean_words=[word.strip(".,!?").lower() for word in words]
    return {
        "word_count":len(words),
        "character_count":len(text),
        "unique_word_count":len(set(clean_words)),
        "sentence_count":get_sentence_count(text),
        "average_word_length":get_average_word_length(words),
        "uppercase_text":text.upper(),
        "lowercase_text":text.lower()
    }