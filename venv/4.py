a = int(input('podaj 1 liczbe: '))
b = int(input('podaj 2 liczbe :'))
if b<a:
    a,b=b,a
while  a<=b:
    if a%2 == 1:
        a = a + 1
        continue
    print(a,end='')
    a=a+1