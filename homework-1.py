#Eddie Neitenbach
#UWYO COSC 1010
#HW 01
#Lab Section: 11


students = [
{"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
{"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
{"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
{"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
]
average = {}
for student in students:
    name = student["name"]
    scores = student["scores"]
    mean = sum(scores.value())/len(scores)
    average[name] = mean
print("These are the students with an average score higher than 80:")
for name, avg in average.items():
    if avg > 80:
        print(name)

