#to find the common word in 2 lists and to print non-common words in the list
def common_name(list1, list2):#function for finding the common elements
    output = []
    for element in list1:#loop for finding the common elements
        if element in list2:
            output.append(element)
    return output

def noncommon_name(full, x):#function for finding the non-common elements
    output = []
    for element in full:#loop for finding the non common elements
        if element not in x:
            output.append(element)
    return output

input1 = input("Enter the students in Python class: ")#input for the 1st list from customer
list1 = input1.split()#splitting up the words
input2 = input("Enter the students in Web Application class: ")#input for the 2nd list from customer
list2 = input2.split()#splitting up the words
print('\nThe students common to both the classes are: ')
x = common_name(list1,list2)
print(x)#calling the function
full = list1 + list2
print ('\nStudents not common in both classes:',noncommon_name(full,x))