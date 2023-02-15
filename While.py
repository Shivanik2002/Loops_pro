# while- else loop

i = 0
while i < 4:
    i += 1
    print(i)

else:              # Executed because no break in for
    print("No Break\n")    

i = 0
while i < 4 :
    i += 1
    print(i)
    break
else:         # Not executed as there is a break
    print("No Break")   


print("**********************************************")

i = 0
a = "hellopython"

while i < len(a):
    if a[i] == "o" or a[i] == "l":
        i += 1
        continue

    print("current Letter :",a[i])
    i += 1    
