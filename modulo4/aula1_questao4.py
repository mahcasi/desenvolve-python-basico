n = int(input())

maior = 0

while n > 0:
    x = int(input())
    if x > maior:
        maior = x
        n = n -1
    else: 
        n = n -1

else:
    print(f"{maior}")