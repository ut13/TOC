s=input()
f=0
if '(' or ')' or '{' or '}' or '[' or ']' or '\"' or '\'' or '<' or '>' in s :
    if '(' in s :
        if s.count('(')==s.count(')') :
            f=1
        else :
            f=0
            print("No")
            exit()
    if '{' in s :
        if s.count('{')==s.count('}') :
            f=1
        else :
            f=0
            print("No")
            exit()
    if '[' in s :
        if s.count('[')==s.count(']') :
            f=1
        else :
            f=0
            print("No")
            exit()
    if '<' in s :
        if s.count('<')==s.count('>') :
            f=1
        else :
            f=0
            print("No")
            exit()
    if '\'' in s :
        if s.count('\'')%2==0 :
            f=1
        else :
            f=0
            print("No")
            exit()
    if '\"' in s :
        if s.count('\"')%2==0 :
            f=1
        else :
            f=0
            print("No")
            exit()
else :
    f=1
    print("Yes")
