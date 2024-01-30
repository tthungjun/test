val1 = [1, 3, ["헬", "로"], 3]
val1. remove(3)
print(val1)
val1. remove(3)
print(val1) 

student = ['a', 'b', 'c', 'c']
student[0] = "e"
student[1] = "f"
student[3] = [1,2]
people = student[:] #student.copy()
people[0] = "A"
print(people[0], student[0])
people[3][1] = 3 #이렇게 쓰면 people 리스트에만 [1,3]으로 바뀌는 것이 아닌가?
print(people, student)
people[3][1] += 5
print(people[3], student[3])