import json

def load_knowledge_base(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def get_answer(question, knowledge_base):
    return knowledge_base.get(question, "I don't know the answer to that.")