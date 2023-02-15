arr = [23,567,890,3452,6789]

maximum = arr[0]
for i in range(len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
print(maximum)

minimum = arr[0]
for i in range(len(arr)):
    if arr[i]< minimum:
        minimum = arr[i]
print(minimum)



print("__________________________")
print("___________________________________")

a = []
m = int(input("Enter the m value: "))
for i in range(m):
    v = int(input("Enter the value: "))
    a.append(v)
print(a)

sum = 0
for i in range(m):
    sum = sum+a[i]

print(sum)    