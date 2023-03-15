#p is a seq of page nos.
p=[2,3,4,1,7,4,2,5,7,1]

#f_size is the size of frame.
f_size=3
q=[]
r=[]

#firstly extracting no. of pages equal to frame size .
for i in range(f_size):
        q.append(p[0])
        r.append(p[0])
        print(q,end='\n')
        print('Miss')
        p.remove(p[0])
        
#replacing pages on basis of seq and it's availability in frame.
#printing Miss , if next page in seq is not present in frame
#printing Hit , if next page in seq is already present in frame
        
while(len(p)>0):
    if(p[0] in q):
        print(q,end='\n')
        r.append(p[0])
        p.remove(p[0])
        print('Hit')        
    else:
        r.append(p[0])
        q.insert(q.index(r[0]),p[0])
        q.remove(r[0])
        r.remove(r[0])
        p.remove(p[0])
        print(q,end='\n')
        print('Miss')
        