import numpy as np

def sudoku_solver(sudoku):
    changes = True
    while changes:
        changes = False
        for i in range(9):
            for j in range(9):
                if sudoku[i,j]==0:
                    cand = np.arange(1,10,dtype='int').tolist() 
                    for k in range(0,9):
                        if sudoku[k,j]==0: continue
                        try:
                            cand.remove(sudoku[k,j])
                        except ValueError:
                            continue
                    for k in range(0,9):
                        if sudoku[i,k]==0: continue
                        try:
                            cand.remove(sudoku[i,k])
                        except ValueError:
                            continue
                    i3 = 3*int(i/3)
                    j3 = 3*int(j/3)
                    print(i3,j3)
                    for k in range(i3,i3+3):
                        for l in range(j3,j3+3):
                            if sudoku[k,l]==0: continue
                            try:
                                cand.remove(sudoku[k,l])
                            except ValueError:
                                continue
                    if len(cand)==1: 
                        sudoku[i,j] = cand[0]
                        changes = True
    return sudoku
