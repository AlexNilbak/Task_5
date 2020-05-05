try:
    file = open("data.txt", "r")
except:
    raise Exception("Cannot open file\n")


def Read_int(filename):
    f=0
    z=0
    x='0'
    while (x!=' ') and (x!=''):
        x=filename.read(1)
        if (x==' ' or x=='') and (f!=0):
            return z
        if (x=='') and (f==0):
            return 'end'        
        elif (x!=' '):
            try:
                x=int(x)
                z=z*10+x
                if (f==0):
                    f+=1            
            except:
                if (x!=' ') and (x!=''):
                    raise Exception("Wrong data\n")
 

e1=None
while (e1==None):        
    e1=Read_int(file)
    if (e1=='end'):
        raise Exception("Empty file\n")

e2=None
while (e2==None):        
    e2=Read_int(file)
    if (e2=='end'):
        raise Exception("There is only one element\n")
    
e3=None
while (e3==None):        
    e3=Read_int(file)
    if (e3=='end'):
        raise Exception("There are only two elements\n") 
     
f=0

if ((e1+e3)/2==e2):
    f+=1
e1=e2
e2=e3
e3=None

while(e3!='end'):
    while (e3==None):        
        e3=Read_int(file)
        if (e3!=None) and (e3!='end'):
            if ((e1+e3)/2==e2):
                f+=1
            e1=e2
            e2=e3            
        if (e3!='end'):
            e3=None
             
print("Number of averages equals {}".format(f))   

file.close()