# Allows us to work with a list of values and perform operations on them.

courses = ['History', 'Maths', 'Physics', 'ÇompSci']

print(courses)

#If you want to get how many values you have in the list then we add len.
print(len(courses))

#To access the members in a list, Indexing begin from zero.
print(courses[0])

#We can also use negative indexing. eg -1 gives the last list member.
print(courses[-1])


#Modifying lists
#Append adds a new member to the list
courses.append('Árt')
print(courses)

#Insert add a member to a specific location.
courses.insert(2, 'Biology')
print(courses)