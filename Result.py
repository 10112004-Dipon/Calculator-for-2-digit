no = {
    "UP101":94,
    "WB102":90,
    "WB103":94,
    "WB104":99,
    "WB105":84,
    "WB106":85,
    "WB107":49,
    "WB108":65,
    "WB109":78,
    "TR110":85,
    "TR111":57,
    "TR112":92,
    "AS113":90,
    "AS114":69,
    "AS116":89,
    "BH117":69,
    "BH118":49,
    "JK119":75,
    "JK120":78,
}
a= (input("enter your id:"))
if a in no.keys():
        print (no[a])
       
else:
        print("Invalid id!!")
if no[a]>=60:
        print ("Congratulations, you have passed.")
else:
        print("unfortunately you failed !!!!  Better Luck next time")
