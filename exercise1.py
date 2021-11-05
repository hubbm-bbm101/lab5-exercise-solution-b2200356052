N= int(input("Write a number!"))

numbers= range(N+1)

sumofodds=0
for i in numbers:
    if i%2==1:
        sumofodds= sumofodds + i
print("sum of odds:", sumofodds)




if N%2==1:
    y= (N-1)/2
else:              #How many evens
    y= N/2
x = N*(N+1)/2

avarageofevens = (x - sumofodds)/ y

print("avarage of evens", avarageofevens)
