# Allows us to work with a list of values and perform operations on them.

courses = ['History', 'Maths', 'Physics', 'ÇompSci']
nums = [1,4,2,6,7]

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

#Remove removes a value at a particular index.
courses.remove('Maths')
print(courses)

#Pop removes the last value of a list.
last_value = courses.pop()
print(last_value)
print(courses)

#Sortinf lists.
courses.sort()
nums.sort()
nums.sort(reverse=True)

print(nums)
print(courses)

print(min(nums))
print(max(nums))
print(sum(nums))

