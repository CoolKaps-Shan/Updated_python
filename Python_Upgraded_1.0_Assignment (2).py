#!/usr/bin/env python
# coding: utf-8

# In[ ]:


user_input = input("enter your name : ")
if ((user_input.isalnum()== False) and (user_input.isspace()==True) or (user_input.isdigit()==False)): 
    print("hi " +user_input)
else :
    print("pls enetr valid name")


# In[ ]:


#using time say hello gm or gn
import datetime

user_inputs = input ("enter your name : ")
time = datetime.datetime.now().time()
print(time)
hours = time.hour
#print(hours)
def show_time():
    for i in user_inputs :
        if ((user_inputs.isalpha()==True ) and (user_inputs.isspace() == False) and (user_inputs.isnumeric()==False)):
            if (hours < 12) :
                print("hi "+user_inputs,"good morning macha")
            elif (hours >= 12 and hours < 18 ):
                print("hi "+user_inputs,"good afternoon macha")
            else :
                print("hi"+user_inputs,"good evening macha")
        else:
            print(" bro !! enter valid name  ")
show_time()


# In[ ]:


#circumfr and area
def ALL():
    try :
        rad = float(input("enter radius :  "))
        if (rad >=0.001):
            circumference(rad)
            areas(rad)
        else :
            print("enter +ve nos")
    
    except ValueError:
        print("That's not an float/int")
        
def circumference(rad):
    circum = 2*3.14*rad
    print(circum)
    
def areas(rad):
    area = 3.14*rad**2
    print(area)

ALL()


# In[ ]:


#7.  Given the area of the circle, write a program to print the radius
import numpy as np
def Checks ():
    try :
        area_of_circle = float(input("enter area of circle :  "))
        if (area_of_circle >=0.0000000000000001):
            rad_circle(area_of_circle)
        else :
            print("enter +ve nos")
    
    except ValueError:
        print("enter +ve no not Special Char")
        
def rad_circle(area_of_circle):
    #radius = (area_of_circle / 3.14)**(.5)
    radius = (area_of_circle / 3.14)
    radius_only = np.sqrt(radius)
    print(radius_only)
    
Checks()


# In[ ]:





# In[ ]:


#next prime nos
def original():
    try :
        num = int(input("No: "))
        
        #print(n)
        if (num > 1):
            Check_Prime(num)
        
        else :
            print(num," enter the number above 1")
    except ValueError:
        print("enter valid nos ")


def Check_Prime(num):
    n= num//2;
    print("-----------------------------------------------------------------")
    for i in range(2,num):

        if (num % i == 0):
            print(num,"is not a prime number")
            
        else:
            print(num,"yesss...its prime")
            
original()


# In[ ]:


# Python program to display next prime
def check():
    try:
        initial_no = int(input("enter 1st nos   "))
        #range_upto = int(input("enter range  "))
       
        if (initial_no >1):
            next_prime(initial_no)
            
        else:
            print("invalid -ve no")
    except ValueError:
        print("valid nos")

def next_prime(initial_no):
    lists = []
    for num in range(initial_no,initial_no+10):

        if (num > 1):
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                lists.append(num)
                
    print(lists)
    print(lists[1])
#next_prime(initial_no,range_upto)
check()


# In[ ]:


def original():
    try :
        num = int(input("no "))
        n= num//2;
        #print(n)
        if (num > 1):
            for i in range(2, n):
                
                if (num % i == 0):
                    print(num,"is not a prime number")
                    break
            else:
                print("Prime number...yesssssssssss")
                   
                
                
        else:
            print(num," enter the number above 1")
    except ValueError:
        print("enter valid nos ")
original()



# In[ ]:


#Given few words, convert them to lowercase, UPPERCASEand CamelCase. Print them to the console

#string1 = "I LOVE MY I   
try:
    string2 = input("enter string ")
    if (string2.isalpha()==True) :
        choose()
    else:
        print("enter valid string")
        
except :
    print("please enter valid string")
        
def case():
    helo = string2.casefold()
    print(helo)
    


def lower():
    helo1 = string2.lower()
    print(helo1)

    
def upper():
    hello = string2.upper()
    print(hello)

def camel ():
    hellos = string2.title()
    print(hellos)
    
def choose():
    camel()
    case()
    lower()
    upper()
    


# In[ ]:


#len of str
def check_in():
    try:
        Input_Str=input("Enter a string ")
        if ((Input_Str.isalnum() == True) ):
            str_len(Input_Str)
        else:
            print("invalid string")
    except ValueError :
        print("no symbole")

def str_len(Input_Str):
    var_a = 0
    for num in Input_Str:
        var_a = var_a +1
    print(var_a)
check_in()


# In[ ]:


#len of str 2
#len of str
bhus = "India won by 10"
var_a = (map(lambda x:1, bhus))
print(sum(var_a))


# In[ ]:


def menu():
    print("***Menu_Card***")
    choice = input("""
A: Tea
B: Coffie
C: Maggie
D: total sale
Q: Quit/Log Out
Please enter your choice:""")
    for i in choice :
        if choice == "A" or choice =="a":
            Total_Tea()
        elif choice == "B" or choice =="b":
            Total_Coffie()
        elif choice == "C" or choice =="c":
            Total_Maggie()
        elif choice=="D" or choice=="d":
            Total_sale()
        elif choice=="Q" or choice=="q":
            sys.exit
        else:
            print("You must only select either A,B,C, or D.")
            print("Please try again")
            menu()
menu()

def Total_Tea(choice):
    tea = 0
    for num in (A.menu() or a.menu()):
        tea = tea +1
    print(tea)
Total_Tea(choice)


def Total_Coffie(choice):
    coffie = 0
    for num in Input_Str:
        coffie = coffie +1
    print(coffie)
Total_Coffie(choice)


def Total_Maggie(choice):
    maggie = 0
    for num in Input_Str:
        maggie = maggie +1
    print(maggie)
    
Total_Maggie(choice)

def Total_sale(choice):
    sale = 0
    for num in Input_Str:
        sale = sale +1
    print(sale)
Total_sale(choice)


# In[ ]:


#list append using odd and even sequence
List1 = [-1,-2,3,4,5,6,7,8,9,10,11,12,14,15,19,20,0,0]
#List1 = range(0,10)
#List1 = int(input("enter no"))
#List2 = List1+20
even_list = []
odd_list = []
final = []
def odd_even():
    for i in List1 :
    #for i in range(List1,List2):
        if (i % 2 == 0):
            even_list.append(i)
        else:
            odd_list.append(i)
    print(even_list)
    print(odd_list)
    final = [*even_list,*odd_list]
    print(final)
odd_even()


# In[ ]:


import functools
l2 = [5,4,3,2,1]
sum1 = functools.reduce(lambda x,y :x+y,l2)
print(sum1)


# In[ ]:


#sort list and 
List1 = [1,2,3,4,5,6,7,8,9,10,11,12]
even_list = []
odd_list = []
sum1 = 0
def odd_even():
   
    for i in List1 :
        if (i % 2 == 0):
            even_list.append(i)
        else:
            odd_list.append(i)
    print(even_list)
    print(odd_list)

def add():
    print(sum(even_list))
    print(sum(odd_list))


def main():
    odd_even()
    add()
main()


# In[ ]:


#largest numbers
List2 = [100,200,900,600,400,700,1000,5000]
#List2 = range (0,20)
#List2 = int(input("no"))
def maximum():
    max = List2[0]
    for a in List2:
        if a > max:
            max = a

    print(max)
maximum()


# In[ ]:


#largest num alc to nth
ID = [900,200,600,300,400,700,800,1000,2000,3000,4000,4000,200,600,800,200,100,8000,8000]

choice = int(input("enetr nos  "))
def Nth_Large():
    s = sorted(set(ID))
    #s = sorted(set(ID))
    print(s)
    ss = s[::-1]
    nth = ss[0:choice]
    ith = nth[::-1]
    print(ith[0])
Nth_Large()


# In[ ]:


#fact of num
def Try():
    try :
        a = int(input("enter no you want to fact"))
        if (a > 0):
            fact(a)
        else :
            print("enter +ve nos")
    except ValueError:
        print("That's not an float/int")

def fact(a):
    fact_list = []
    for i in range (1,a+1):
        if (a % i ==0):
            fact_list.append(i)
    print(fact_list)
    

def main():
    Try()
      
main()


# In[ ]:


#basic current days
import datetime
cool = datetime.datetime.now().date()
print(cool)
date_entry = input('Enter a date in YYYY-MM-DD format ')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
#recent = datetime.date(cool) - datetime.date(dates)
recent = cool - date1
recent.days


# In[ ]:


#note count Atm 
#count_notes = []

def cash_in():
    try:
        cash = int(input("enter a cash : "))
        if (cash > 0 ):
            initial(cash)
        else:
            print("enter + cash")
    except ValueError :
        print("no symbole")


def initial(cash):
    #global cash
    
    Notes = [2000,1000,500,200,100,50,20,10,5,2,1]
    counts = [0,0,0,0,0,0,0,0,0,0,0]
    Note_Count = zip(Notes,counts)
    for a,b in Note_Count :
        #print(a,b)
        if (cash >= a) :
            b = cash // a
            cash = cash - b * a
            print(a ,"cash having no of note count :",b)
def main():        
    cash_in()
    #initial(cash)
main()


# In[ ]:


import sys
import json
#contact list model
print ("contact list")
Names = ['kaps','kl'] 
Cell_no = ['9890100','12']            
Contact_Dict = dict(zip(Names,Cell_no))
#for i in range (0,1):
#    Name = input("Enter Name : ")  # insert name
#    Names.extend([Name])     
#    Cell = int(input("Enter No : ")) #insert no
#    Cell_no.extend([Cell])        # append to list
#    Contact_Dict = dict(zip(Names,Cell_no))     #combine both list and typecast to dict
print(Contact_Dict)
                       

#def AddContact (Contact_Dict):                #add new contact fun
#    New_Name = input("Enter new_Name : ")
#    New_Cell = input("enetr cell_number : ")
#    Contact_Dict[New_Name] = New_Cell        #merge to original
#    print(Contact_Dict)

def AddContact (Contact_Dict): #add new contact fun
    N_Name = []
    N_Cell = []
    New_Name = input("Enter new_Name : ")
    N_Name.extend([New_Name]) 
    New_Cell = input("enetr cell_number : ")
    N_Cell.extend([New_Cell])
    Con = dict(zip(N_Name,N_Cell))        #merge to original
    #print(Con)
    Contact_Dict.update(Con)
    #menu()                #fun call for add

def Delete (Contact_Dict) :
    Delete_no = input("enter a num you want to delete")
    if Delete_no in Contact_Dict :
        del Contact_Dict[Delete_no]
        print("Deleated contact from your list :"+str(Contact_Dict))
    else :
        print("not in contact")


def searching (Contact_Dict) :
    search = int(input("enter no you want to search : "))
    
    for search in Contact_Dict.items():     #.values()
    
        if (search == Contact_Dict.keys()) or (search == Contact_Dict.values()):
            print(search,Contact_Dict[Names])
        else :
            print("contact not found")
            break

""""def main():
    AddContact(Contact_Dict)
    Delete(Contact_Dict) 
    searching(Contact_Dict)
main()"""

def menu():
    print("***Contact_list***")
    choice = input("""
A: AddContact
B: Delete
C: Searching
Q: Quit/Log Out
Please enter your choice:""")
    for i in choice :
        if choice == "A" or choice =="a":
            AddContact(Contact_Dict)
        elif choice == "B" or choice =="b":
            Delete(Contact_Dict)
        elif choice == "C" or choice =="c":
            searching(Contact_Dict)
        elif choice=="Q" or choice=="q":
            sys.exit
        else:
            print("You must only select either A,B or D.")
            print("Please try again")
            menu()
menu()
def write():
    with open('/home/bhush/Desktop/contact.txt', 'w') as outfile:  
        json.dump(Contact_Dict, outfile)
        out = outfile.close()
write()


# In[ ]:





# In[5]:


#read a file and calculate no of words and chars

def file():
    try:
        read = open("/home/bhush/Desktop/bhush.txt")
        read = read.read()
        print(read)
        count_no(read)
    except:
        print("no file found")

def count_no(read):
    var_a = 0
    for num in read:
        var_a = var_a +1
    print("no of char in file is : ",+var_a)
    count_line(read)
#count_no(read)

def count_line(read):
    var_b = 0
    for i in read:
        if i.endswith('.'):
            var_b = var_b +1
    print("no of lines in file is : ",+var_b)
    count_words(read)
#count_line(read)

def count_words (read):
    var_c = 0
    for i in read:
        if (i.endswith('.') or i.endswith(" ")):
            var_c = var_c + 1
    print("no of words in file is : ",+var_c)
    
#count_words(read)

def main():
    file()
main()


# In[9]:


#read a webpage
import urllib
from bs4 import BeautifulSoup
web = ('http://www.google.com')
page = urllib.request.urlopen(web)
#pages = page.read()
#pages
if (page.status_code == 200): 
    print("web page is present") 
    soup=BeautifulSoup(page.text,'html.parser')       
    l=soup.find("ul",{"class":"searchNews"}) 
    for i in l.findAll("a"): 
        print(i.text) 
else: 
    print("Error") 


# In[29]:


import urllib.request
from urllib.error import URLError
from bs4 import BeautifulSoup
web = ('https://www.hackerearth.com/fr/practice/machine-learning/machine-learning-projects/python-project/tutorial/')
page = urllib.request.urlopen(web)


def dead_or_alive():
    try :
        link = urllib.request.urlopen(web).getcode()
        if (link == 200) :
            print("sucess for website : " + web )
            read_web(page)
        else :
            print("unsucess for website : " + web)
    except URLError as e:
        print("web is not Available : "+web,e.code,e.reason)
            


def read_web(page):
    #l = []
   # soup=BeautifulSoup(page,'html.parser')       
    #l=soup.find("ul",{"class":"machine-learning"}) 
    #for i in l.findAll("a"): 
        #print(i.text) 
    f = requests.get(link)
    print(f.text)    
dead_or_alive()


# In[24]:


import urllib.request

link = "https://www.hackerearth.com/fr/practice/machine-learning/machine-learning-projects/python-project/tutorial/"
f = urllib.request.urlopen(link)
myfile = f.read()
print(myfile)


# In[28]:


import requests

link = "https://www.hackerearth.com/fr/practice/machine-learning/machine-learning-projects/python-project/tutorial/"
f = requests.get(link)
print(f.text)


# In[30]:


import urllib.request

fp = urllib.request.urlopen("http://www.python.org")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)


# In[ ]:




