from flask import * 
from solver import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sudoku.html') 
@app.route('/returns')

def returns():
    return redirect(url_for('home')) 

#valid sudoku    
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
  
@app.route('/solve', methods=['POST'])
def p():
    grid=request.form.getlist('grid') 
    pl=[['.' for i in range(0,10)] for j in range(0,10)] 
    k=0 
    for i in range(0,9):
        for j in range(0,9):
            if(grid[k]!=''): 
                pl[i][j]=grid[k]  
            k=k+1  
    if(isValidSudoku(pl)==1):  
        solveSudoku(pl)             
        return render_template('final.html',pl=pl)  
    else:
        pl[0][9]='0'
        return render_template('final.html',pl=pl)

if __name__ == '__main__':         
    app.run(debug=True)                   
