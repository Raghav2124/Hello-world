theList=["apple","banana","orange"]#can contain items of more than one data type    
print(theList)
print(len(theList))#find the length of list 
thisList = list(("apple","banana","orange",1,2,3))
print (thisList)
print (thisList[1])
thisList.insert(2, "watermelon")#insert new item in the list we have to pass the index as well as the value 
if "apple" in thisList:
      print("Yes, 'apple' is in the fruits list")
print (thisList)
thisList.append("orange")#adds at the end of the list 
tropical = ["mango", "pineapple", "papaya"]
thisList.extend(tropical)#to append two list can also be used to append other data types
tropical.clear()
print(tropical)