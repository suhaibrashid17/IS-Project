from flask import Flask, request, jsonify
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import re

app = Flask(__name__)

device = "cuda" if torch.cuda.is_available() else "cpu"
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("suhaibrashid17/SQL-Injection-Detection")
model.config.max_length = 512
model.to(device)
model.eval()

@app.route('/detect_sql_injection', methods=['POST'])
def detect_sql_injection():
    try:
        data = request.get_json()
        sql_query = data.get('sql_query', '')

        if not sql_query:
            return jsonify({"error": "No SQL query provided"}), 400

        sql_query = sql_query.lower()
        sql_query = re.sub(r'\d+', '0', sql_query)
        sql_query = re.sub(r'([<>!=])', r' \1 ', sql_query)

        with torch.no_grad():
            temp = tokenizer(sql_query, return_tensors="pt", max_length=512, padding="max_length", truncation=True)
            input_ids = temp.input_ids.to(device)
            attention_mask = temp.attention_mask.to(device)
            output = model(input_ids=input_ids, attention_mask=attention_mask)
        
        logits = output.logits
        probabilities = torch.nn.functional.softmax(logits, dim=1)
        class_index = torch.argmax(probabilities, dim=1).item()

        if class_index == 0:
            return jsonify({"result": "Not SQL Injection"})
        elif class_index == 1:
            return jsonify({"result": "SQL Injection"})
        else:
            return jsonify({"result": "Unknown Classification"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
