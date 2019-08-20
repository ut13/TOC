str=input()
j=0
for i in str:
    if(i=='a'):
        j+=1
    else:
        break

for i in str[j:]:
    if(i=='a'):
        break
if(j%2==0 and i=='b'):
    print("Accepted")
else:
    print("Not Accepted")
            
        
