import json, os

DATA_FILE="students.json"
def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f: return json.load(f)
    return {}
def save_students(data):
    with open(DATA_FILE,'w') as f: json.dump(data,f,indent=2)
def add_student(data,name):
    if name not in data: data[name]=[]
def add_score(data,name,score):
    data[name].append(score)
def calculate_average(scores):
    return round(sum(scores)/len(scores),1) if scores else 0
def letter_grade(avg):
    return "A" if avg>=90 else "B" if avg>=80 else "C" if avg>=70 else "D" if avg>=60 else "F"
def class_average(data):
    avgs=[calculate_average(v) for v in data.values() if v]
    return calculate_average(avgs)
