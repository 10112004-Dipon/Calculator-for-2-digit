a= (input("Name:"))
b=(input("Roll.No.:"))
c=(input("write Ready if you are ready for the exam:"))
count=0
if c=="Ready":
    print("Best of luck")
else :
    print("Are you not ready:")
print("Who is our president?")
print("1.You")
print("2.Donald Trump")
print("3.Narendra Modi")
print("4.Meloni")
A=input("enter your answer:")
if A=="3":
    count+=1
else:
    count-=0.25
if A=="3":
    print("you are correct")
else:
    print("wrong Answer go to nxt qwuestion")
print("Who was the first President of India?")
print("1.Dr. Rajendra Prasad")
print("2.Mahatma Gandhi")
print("3.Jawaharlal Nehru")
print("4.Mamata Banerjee")
B=input("enter your answer:")
if B=="1":
    count+=1
else:
    count-=0.25
if B=="1":
    print("you are correct")
else:
    print("wrong Answer go to nxt qwuestion")
print("In which year did India gain independence?")
print("1.1945")
print("2.1948")
print("3.1947")
print("4.1950")
C=input("enter your answer:")
if C=="3":
    count+=1
else:
    count-=0.25
if C=="3":
    print("you are correct")
else:
    print("wrong Answer go to nxt qwuestion")  
print("Who is known as the Father of the Nation in India?")
print("1.Me")
print("2.Mahatma Gandhi")
print("3.SUbash Chandra Bose")
print("4.Lal bahadur Sastri")
D=input("enter your answer:")
if D=="2":
    count+=1
else:
    count-=0.25
if D=="2":
    print("you are correct")
else:
    print("wrong Answer go to nxt qwuestion")
print("Which ancient civilisation was located in the Indus Valley?")
print("1.Mohenjodaro Civilisation")
print("2.Egyptian Civilisation")
print("3.English Civilisation")
print("4.Harappan Civilisation")
E=input("enter your answer:")
if E=="4":
    count+=1
else:
    count-=0.25
if E=="4":
    print("you are correct")
else:
    print("wrong Answer go to nxt qwuestion")
print("Who led the Salt March in 1930?")
print("1.You")
print("2.Me")
print("3.Netaji Subash chandra Bose")
print("4. Mahatma Gandhi")
F=input("enter your answer:")
if F=="4":
    count+=1
else:
    count-=0.25
if F=="4":
    print("you are correct")
else:
    print("wrong Answer go to nxt qwuestion")
print(" Which Mughal Emperor built the Taj Mahal?")
print("1.Aurangjeb")
print("2.Babar")
print("3.Akbar")
print("4.Saha Jahan")
G=input("enter your answer:")
if G=="4":
    count+=1
else:
    count-=0.25
if G=="4":
    print("you are correct")
else:
    print("wrong Answer go to nxt qwuestion")
d=(input("do you want to know your result(Y/N)?:"))
if d=="Y":
    print(count)
