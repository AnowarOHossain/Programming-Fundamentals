#Slicing 

numbers=[5,10,15,20,25,30,35]

print(numbers[2:5])
print(numbers[:4])
print(numbers[-3:])
print(numbers[1:6:2])
print(numbers[ : :-1])

#List,Tuple,Slicing Example by code

info  = ['Alice', 25 , 'Engineer', 'Dhaka', 'Bangladesh']

a,_,b,_,_=info
print("\n")
print("a:",a)
print ("b:", b )

_,a,*b,=info 
print("\n")
print("a:",a)
print ("b:", b)

a,*_,b,=info
print("\n")
print("a:",a)
print ("b:", b)
