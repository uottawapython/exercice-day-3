#Question 1
"""
I ask a student to create a variable that contains his Twitter handle.
The problem is that he didn't add an "@" symbol before his Twitter handle.

Could take the same variable and add an '@' to his handle 
so that the print result  should be "@guinslym"
""" 
my_twitter_handle = "guinslym"

#do something with this variable my_twitter_handle

print(my_twitter_handle)
#result =>   @guinslym

#==============================================
#==============================================
#==============================================
#==============================================
#==============================================

#Question 2
"""	
A student create two variables. One contains his firstname and the other
one contains his lastname. I want you to print both names with a space between

i.e:

firstname = "Susan"
lastname = "Mowers"

print(firstname + add something + lastname)

#result => Susan Mowers
""" 
firstname = "Susan"
lastname = "Mowers"

#print(firstname + add something + lastname)
#result => Susan Mowers

#==============================================
#==============================================
#==============================================
#==============================================
#==============================================

#Question 3 --- Built-in functions (diapo 12)
"""
I have a variable that contains many students. 
I want to know what type of Data Objects that variable is.
What function can I use to know that information?

tips: look at the list of built-in functions.
""" 

#==============================================
#==============================================
#==============================================
#==============================================
#==============================================

#Question 4 --- usage of dir()
"""
I have a list of students.
What function(s) do you think I can use to add one more student
in that list

students = ['Ange', 'Dan', 'Julie']

#I want my list to look like this 
['Ange', 'Dan', 'Julie', 'Miro']
But I don't know what function can I use to add 'Miro' into my list
""" 

#==============================================
#==============================================
#==============================================
#==============================================
#==============================================


#Question 5 dict --- usage of  dict.get('') or dict['']
"""
I have this dictionnary

student = {'id': 3456, 'name':'Judy June', 'courses': ['COM4566', 'ADM9873', 'ISI4560']}

#This is the same variable writting in a different way to be more readable to you

student = {
		'id':      3456, 
		'name':    'Judy June', 
		'courses': ['COM4566', 'ADM9873', 'ISI4560']
}

#I want to know how many courses this students have.

#answer
i.e: size_of_courses = get_size(get_list_of_courses_for_this_student)
""" 

#==============================================
#==============================================
#==============================================
#==============================================
#==============================================

#Questions 6 
""" 
I have this variables list I want to know how many students are part-time
students. 

students = [
{
		'id':      4566, 
		'name':    'Taiwo June', 
		'courses': ['COM4566', 'ADM9873', 'ISI4560', 'HME4520', 'MNG093', 'HMX0283'],
		'grades':  ['A', 'B+', 'C+', 'A-', 'abandon']
},
{
		'id':      9586, 
		'name':    'Julie Tremblay', 
		'courses': ['COM4566', 'ADM9873', 'ISI4560', 'HMX0283', 'BIO2394'],
		'grades':  ['A+', 'A+', 'A', 'A+', 'A-']
},
{
		'id':      2839, 
		'name':    'Judy June', 
		'courses': ['COM4566'],
		'grades':  ['A+']
},
{
		'id':      4950, 
		'name':    'Judy June', 
		'courses': ['COM4566', 'ADM9873', 'ISI4560'],
		'grades':  ['A', 'C+', 'A+']
}
]

#6-a What type of Objects the 'students' variable is. Is it a Dict or a list?
#6-b Is this variable an iterable?
#6-c Write a script that will determine how many students are part-time students 
#To be part-time the students needs to have less than 4 courses.
""" 

#Question 8 --- for Yaozong and Syam

""" 
The manager at Shopify wants to know how many items where sold today with the USD
currency and what was the total purchases of the day for prices in EUR. 
The following file contains all the transactions.

with open('file_name') as f:
    content = f.readlines()

tips: pseudo-code
"""
#please uncomment this following lines
"""
try:
    amount = []
    with open('shopify.txt') as f:
        #read lines by lines
        content = f.readlines()
        #do something with this line to retrieve only the numbers
        #add each price into the list amount by converting them to Int or float
except:
    print('the file "Shopify.txt" needs to be in the current directory')
"""