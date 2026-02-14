#datatype
var=["python","An","Hello"]
print(var)
print(var[1])
print(var[2])
print(var[0][1])
#length calculate
print(len(var))
#append
var.append(2)
print(var)
var.append("sanika")
print(var)
#insert
var.insert(1,'smbst')
print(var)
#insert multiple elements using 'extend'
var.extend([10,"good","morning"])
print(var)
#reverse element
var.reverse()
print(var)
#remove only one element
var.remove(2)
print(var)
#pop operation deletes the last element from list 
var.pop()
print(var)

#tuple datatype
tuple=(5,'python','good',10)
print(tuple)
t1=(45)
t2=(6)
t3=t1+t2
print(t3)
#dictionary datatype
d={1:'python',2:'good',3:'morning'}
print(d)
#set datatype
set={56,7,8,9}
print(set)
#boolean data types

a=True
print(type(a))

b=False
print(type(b))
