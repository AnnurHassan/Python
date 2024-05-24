last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = []
for i in range(len(subjects)):
   gradebook.append([subjects[i], grades[i]])

gradebook.append(["compurter science", 100])
gradebook.append(["visual arts", 93])
gradebook[-1][-1] += 5

for i in gradebook:
    if i[0] == "poetry":
        i.remove(i[1])
        i.append("Pass")

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)

