student={'name': 'jhone', 'age': 21, 'course': 'python'}
print(student, '\n', type(student))

print(student['name'])
print(student['age'])
print(student['course'])

print(student.get('name'))
print(student.get('age'))
print(student.get('course'))

student['age']=23
print(student)

student.update({'age': 25, 'course': 'java'})
print(student)

       # setdefaults
student.setdefault('gender', 'male')
student.setdefault('marks', 100)
student.setdefault('name', 'doe') #duplicate key will not be added
print(student)


