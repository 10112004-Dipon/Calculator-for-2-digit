list=[2,4,6,8,10,11]
for i in list :
    if i%2==0:
        print ("Even")
    else:
        print(i, "odd!!")
    end=""
  
d = {
    "name1":"Dipon Mitra", 
   "name2" :"Subhajit Shaw",
   "name3" :"Sayan Kumar Barai"
   }
d  ['name4']= "Arghya Roy Chowdhury"
print (d)
for i in d.values():
    if i=="Dipon Mitra":
        print("ok")
    elif  i=="Shubajit Shaw":
        print ("ok")
       
    else:
        print("no")