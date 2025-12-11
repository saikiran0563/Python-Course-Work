lwish= lambda name: f'welcome to python {name}!'
print(lwish('mohan'))
print(lwish('manoj'))


lsquare= lambda n:f'square of {n} is {n*n}'
print(lsquare(5))
print(lsquare(9))


ladd = lambda a,b:a+b
print(ladd(5,7))

EorO= lambda n: 'even' if n%2==0 else 'odd'
print(EorO(6))
print(EorO(7))

vowel= lambda ch: 'vowel' if ch in 'aeiouAEIOU' else 'consonant'
print(vowel('a'))
print(vowel('b'))
print(vowel('E'))



l=[1,2,3,4,5,6,7,8,9,10]
names=['sai','ram','mohan','manoj']
price=[1000,2500,3000,1500]

res=list(map(lambda i:f'{i}%',l))
res1=list(map(lambda i:i.title(),names))
res2=list(map(lambda i:f'${i+i*0.18}',price))

print(res)
print(res1)
print(res2)


l1=[1,2,3,4,5]
names1=['apple','banana','grapes','orange','kiwi']
price1=[50,20,80,30,60]
products={
    'laptop':50,
    'mouse':15,
    'keyboard':20,
    'monitor':10,
    'speakers':25,
    'webcam':30,
    'headphones':40
}

res3=list(filter(lambda i:i%2==0,l1))
res4=list(filter(lambda i:i[0]=='k',names1))
res5=list(filter(lambda i:i>40,price1))
res6=list(filter(lambda i:products[i]>30,products))

print(res3)
print(res4)
print(res5)
print(res6)


from functools import reduce

l2=[1,2,3,4,5]
lang=['python','java','c++','csharp','javascript','ruby','go','rust','php','swift','kotlin']

res7=reduce(lambda a,b:a*b,l2)
res8=reduce(lambda a,b:a+','+b,lang)

print(res7)
print(res8)

d={
    'Praveen':80,
    'Ram':90,
    'Rohan':75,
    'Moksha':88,
    'Anjali':95,
    'Sita':70
} 
print(dict(sorted(d.items(),key=lambda i:i[0])))
print(dict(sorted(d.items(),key=lambda i:i[0],reverse=True)))