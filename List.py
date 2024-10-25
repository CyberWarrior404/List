list = [10,12,"Hello",True,5.0,"be","and","of","a","in","to","have"]
print(list)

#add element to list
list.append("World")
list.append(99)
print(list)

#Add particularty in a place
list.insert(2,False)
print(list)

#remove a element
list.pop()
print(list)

list.remove(12)
print(list)

#reverse list
list.reverse()
print(list)

for item in list:
    print(item)

if 87 in list:
    print("Item present")
else:
    print("Item not present")

numbers= [1,2,3,4,5,6,7,8,9,10,11,12]
print(max(numbers))
print(min(numbers))
print(len(numbers))
print(sum(numbers))

numbers.sort(reverse=True)
print(numbers)
numbers.sort()
print(numbers)

#Slicing(3=start index  12= stop index  2 = optional(skipby number/2))

print(numbers[3:12:2])
print(numbers[1:11:-3])
