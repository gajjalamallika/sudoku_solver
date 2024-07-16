from flask import * 
from solver import *
from valid import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sudoku.html') 
@app.route('/returns')

def returns():
    return redirect(url_for('home')) 

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
    app.run(debug=False,host='0.0.0.0')                   
