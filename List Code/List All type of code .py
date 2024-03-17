my_list= ["Apple" , "Mango" ,"Jackfruit"]
print(my_list)


my_list.append("Orange")
print(my_list)

my_list.insert(0,"Balckberry")
print(my_list)


################# Two List Marge ###################
list1=[1,2,3,4,5]
list2=[6,7,8,9,0]

list1.extend(list2)
print(list1)

################# Touple And List aldo Marge in one List ################
thislist = ["apple", "banana", "cherry"]
thistuple = ("Bananna", "orange")
thislist.extend(thistuple)
print(thislist)



##################### Upper Case List ##############
list_uppercase =["sajjad" , "hossain" , "jim"]
newList= [ x.upper() for x in list_uppercase ]
print(newList)
list_lower=["JIM" ,"SAJJAD"]
newList1 =[x.lower() for x in list_lower]
print(newList1)


####################### Sort List Item ####################
list_sort =[2,6,1,9,3,8]
list_sort.sort()
print(list_sort)

####################### Reverse The List Item ##################
list_reverse = [12,45,2,78,45,48]
list_reverse.sort(reverse= True)
print(list_reverse)


###################  case-insensitive sort of the list:
case_sort=["apple", "orange" ,"Cherry" ,"Pineapple"]
case_sort.sort(key=str.upper)   #case_sort.sort(key=str.lower)
print(case_sort)



# reverse The List Item
reverse_list=[100,99,91,88,50,45,30]
reverse_list.reverse()
print(reverse_list)


############################## Copy Nad List List item ################
copy_list = [1,2,3,4,5,6,7]
new_copy =copy_list.copy()
print(new_copy)


list_list =[11,22,33,44,55,66]
list_list1 =list(list_list)
print(list_list1)




############### Join two List
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Second Model
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)

print(list1)











