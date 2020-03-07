n = int(input("Input Quantity:"))
chisla= [None] * n
results=[]
print(chisla)
for i in range(n):
    chisla[i] = float(input("Input Number {} :".format(i)))
    if(i>1):
        if(chisla[i-2] < chisla[i-1] and chisla[i] < chisla[i-1]):
            results.append(chisla[i-1])
print("Results:{}".format(results))