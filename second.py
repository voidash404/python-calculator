"""A=int(input("A:"))
B=int(input("B:"))

if A>=B:
    print("true")
else:
    print("false")"""
    
    
"""Marks=input("Enter student marks:")

if Marks>=90:
    print("grade: A")
elif 90>Marks>=80:
    print("grade: B")
elif 80>Marks>=70:
    print("grade: C")
else:
    print("grade: D")"""


"""Age=int(input("Enter your age:"))

#nesting
if Age>=18:
    if Age>=80:
        print("cannot drive")
    else:
        print("can drive")
else:   
    print("cannot drive")"""
    
    
"""marks=[89,67,98,76,43,76]
print(marks[1:4])"""


"""movies=[]
    
movies.append(input("enter 1st movie:"))
movies.append(input("enter 2nd movie:"))
movies.append(input("enter 3rd movie:"))

print(movies)"""


"""student = {
    "name":"Asmita", #nested dictionary
    "age":20,
    "cgpa":8.5,
    "marks":{
            "maths":90,
            "science":80,
            "english":70,
            "french":60,
            }
}

print(student)"""


"""info = {
    "name":"Asmita",
    "age":20,
    "cgpa":8.5,
    "marks":{
            "maths":90,
            "science":80,
            "english":70,
            "french":60,
            }
}

print(type(info))"""


"""info = {
    "name":"Asmita",
    "subjects":["python", "C", "Java"],
    "topics":("dict","set"),
    "age" :35,
    "is adult":True,
    12.99 : 95.5
}

info["name"] = "khushi" #overwrite
info["surname"] = "Singh"
print(info)"""


"""student = {
    "name":"Asmita", #nested dictionary
    "age":20,
    "cgpa":8.5,
    "marks":{
            "maths":90,
            "science":80,
            "english":70,
            "french":60,
            }
}

new_dict = {"city": "prayagraj", "age":18, "name":"khushi"} #update dictionary
student.update(new_dict)
print(student)"""


"""collection = set()
collection.add(1)
collection.add(2) 
collection.add("apna college")
collection.add((1,2,3))

#collection.add([1,2,3]) #list is unhashable
collection.remove("apna college")
collection.clear()
print(len(collection))"""


"""collection = {
    "python", "C", "Java", "C++","coding", "javascript"
    }

print(collection.pop())
print(collection.pop())"""


"""set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))"""


"""dict={
    "cat":"a small animals that purr",
    "table":["a piece of furniture","list of facts and figures"],
}
print(dict)"""


"""subjects = {
    "python", "Java", "C++","python", "javascript", "Java","python","Java","C++","C"
    }

print(len(subjects))"""


"""marks={}#empty dictionary

X=int(input("Enter physics:"))
marks.update({"physics":X})
Y=int(input("Enter chemistry:"))
marks.update({"chemistry":Y})
Z=int(input("Enter maths:"))
marks.update({"maths":Z})

print(marks)"""


"""values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)"""


"""count = 1
while count<=10:
    print("hello, I am a bot")
    count+=1
    
print(count)"""


"""i=1
while i<=100:
    print(i,"hello, I am a bot")
    i+=1

print("end of loop")"""
    
    
"""i=100
while i>=1:
    print(i)
    i-=1"""
    
    
"""i=17
while i<=170:
    print(i)
    i+=17"""
    

"""n=int(input("Enter a number:"))
i=1
while i<=10:
    print(n*i)
    i+=1"""


"""nums=[1,4,9,16,25,36,49,64,81,100]

idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1"""
    
    
"""nums=(1,4,9,16,25,36,49,64,81,100,36)

x=36

i=0
while i<len(nums):
    if(nums[i]==x):
        print("found at indx",i)
    else:
        print("founding...")
    i+=1"""
    
    
"""nums=(1,4,9,16,25,36,49,64,81,100,36)

x=36
i=0
while i<len(nums):
    if(nums[i]==x):
        print("found at indx",i)
        break
    else:
        print("founding...")
    i+=1 """
    
    
