def isValidSudoku(b):
    for i in range(0,9):
        t=[]
        c=[] 
        for j in range(0,9):
            if(b[i][j]!='.'): 
                if b[i][j] not in t:#row checking
                    t.append(b[i][j]) 
                else:
                    return 0
            if(b[j][i]!='.'): #column checking 
                if b[j][i] not in c:
                    c.append(b[j][i])
                else:
                    return 0    
    s=0
    er=0  
    for k in range(1,10):#diagonal checking
        rt=[] 
        for i in range(er,er+3):
            for j in range(s,s+3):
                if(b[i][j]!="."):
                    rt.append(b[i][j])
        if(len(rt)>=1 and len(rt)!=len(list(set(rt)))):
            return 0  
        s=s+3 
        if(k!=0 and k%3==0):
            er=er+3 
            s=0    
    return 1  