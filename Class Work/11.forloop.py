lang=['python','java','c++','csharp','javascript','ruby','go','rust','php','swift','kotlin']      #list
for i in lang:
    print(i)

for i in enumerate(lang):
    print(i,i[0],i[1])

lang={1:'python',2:'java',3:'c++',4:'csharp'}       #dictionary
for i in lang:
    print(f'Key-{i} Value-{lang[i]}')
for i in enumerate(lang):
    print(f'Index-{i[0]} Key-{i[1]} Value-{lang[i[1]]}')


str='python programming'        #string
for i in str:
    print(f'{i}')

for i in enumerate(str):
    print(f'Index-{i[0]} val-{i[1]}')
  
num=int(input('Enter a number: '))     #syntax of range(start,stop+1,step) 
for i in range(1,21):
    print(f'{num} x {i} = {num*i}')

l=['laptop','mouse','keyboard','monitor']
for i in range(len(l)):
    print(i,l[i])
