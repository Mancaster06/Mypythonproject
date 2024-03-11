input_string1 = input("Enter the elements separated by spaces")
set1 =  set(map(int,input_string1.split()))

input_string2 = input("Enter the elements separated by spaces")
set2 =  set(map(int,input_string2.split()))

common_elements = set1.intersection(set2)
print(common_elements)