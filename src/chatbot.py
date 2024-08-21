# src/chatbot.py
from transformers import AutoModel, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")
model = AutoModel.from_pretrained("neuralmind/bert-base-portuguese-cased")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def responder_pergunta(pergunta, texto):
    inputs = tokenizer(pergunta, texto, return_tensors="pt", truncation=True, padding=True)
    inputs = {key: value.to(device) for key, value in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
    
    resposta = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return resposta
