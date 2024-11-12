i=1
for i in range(1,51):
    if i%15==0:
        print("fizzbuzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")
    else :
        print(i)
    end=""
for i in range(1,101):
    output = ""
    if i%3==0:
        output = output + 'Fizz'
    if i%5==0:
        output = output + 'Buzz'
    print(output or i)