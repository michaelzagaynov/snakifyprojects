a = int(input())
print(a%10)


a=input()
b = (int(a)//10%10)
print(b)




a = input()
one = (int(a)//100)
seven = (int(a)//10%10)
nine=(int(a)%10)
print(one+seven+nine)



from math import floor
a = float(input())
b = floor(a)
print(a-b)



from math import floor
a=input()
L=floor(a)
D = (float(a)-L)
answer = (D*100)//10
print(answer)




from math import ceil
a=input()
b=input()
D=(int(b)/int(a))
d=float(D)
answer=ceil(d)
print(answer)





a=input()
d=(int(a))//60
mihn=(int(a)%60)
print(d, mihn)



d=input()
c=input()
n=input()
td=(int(d)+(int(c)/100))
dollars=(td*int(n)*10//10)
cents = (td*int(n)*10%10)*10
print(dollars, cents)



h = int(input())
m = int(input())
s = int(input()) 
print(h * 30 + m * 30 / 60 + s * 30 / 3600)






alpha = float(input())
print(alpha % 30 * 12)






