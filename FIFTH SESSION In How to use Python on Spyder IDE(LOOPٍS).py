'''بسم الله الرحمن الرحيم'''               
#اولا البايثون هي أحدث اللغات المستخدمة للبرمجة
#In this training program
#you will learn how to collect
#analyze and visualize any size of data
#Learn ٍsome-NOT ALL- Python basics.
#Learn simplest way in OOP (Object-Oriented Programming) and data structures in python
#Be able to implement some algorithms or program using python
#Learn the most needed data science algorithms

                       #FIFTH SESSION In How to use Python on Spyder IDE(LOOPٍS)
#For & While LOOPS
#أنواع المتغيرات:
#Global Variable:
#وهو المتغير اللى بعرفة مرة واحدة فى البرنامج وبيكون متعرف على البرنامج كلة
#Local Variable:
#ودة بيتعرف من داخل الblock of code بتاعها بس مش بيكون متعرف برة البرنامج
#for loop is counting on (i) conditition which is local variable
listx=[1,2,3,4,5]
for i in listx:
#where (i) means the number of elements in the listx
#معاناها طالما الi فى الlistx اى بمعنى ان الi هيلف جوة الlistx بعدد مرات الelement داخل الlistx
#means that "i" will loop inside the for condition by the number of loops inside the "listx"     
    print(i)
#طيب لو عايز يطبع رقم او كلمة فى كل مرة بيعمل loop 
    print("next")
#to add number on list
    i+=i
    print(i)
#to print numbers in range
for t in range(1000):
    print(t)
#range function:
#هي function بتجيبلك الرانج مابين الارقام اللى انت محددهالة بين الاقواس
for u in range(2,10):
    print(u)
#طيب هوة اضاف فى الrange رقم واحد فى الفرق مابين الارقام
#لو عايز يزود الفرق مابين الارقام
for u in range(2,10,2):
    print(u) 