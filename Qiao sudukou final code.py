import math
import copy

originalSudokulist=[[0,0,0,0,8,0,0,0,2],        # The input is a list, which is called originalSoduko
                [5,6,7,2,3,9,8,1,0],        # empty cells are cells with value "0" 
                [1,2,8,7,4,5,3,6,9],
                [0,7,3,9,1,8,4,2,5],
                [8,9,4,3,5,2,6,7,0],
                [2,1,5,4,6,7,9,3,8],
                [0,5,2,0,9,3,0,4,6],
                [4,8,1,5,7,6,2,9,3],
                [9,3,6,1,2,4,0,8,0]]

######################################################                       
class sudoku:     # define the sudoku class
    sudoku=[]     # sudoku is a list
    def sudokuSize(self):             
        sudokuSize=len(sudoku)            # if sudoku is a 9*9 list, then the sudokuSize is 9
    def allOptions(self):                        # all options of each cell, without considering the limitation from its position
        self.allOptions=range(1,len(sudoku)+1)   # if sudoku is a 9*9 list, then allOptions is a list [1,2,3,4,5,6,7,8,9]
    def unitmatrixSize(self,sudokuSize):  
        return math.sqrt(sudokuSize)           #if sudoku is a 9*9 list, then unitmatrixSize is sqrt(9)=3
    def unfilledCells(self):                   #to get which cells are unfilled. This list changes when empty cells are filled.
        unfilledCells=[]
        for cell in dynamicCells:
                if cell(rowIndex,columnIndex).value==0:
                    unfilledCells.append((rowIndex,columnIndex))
        return unfilledCells

#####################################################
def dynamicCells(originalSudokulist):   # in the original sudoku list, to find out all the empty cells.        
    dynamicCells=[]                 # In the complex method, the cells will be sorted later. The index of each cell might change. So I call this list the dynamic cell list
    originalSudokulist=sudoku()         # give attributes to the originalSudoku
    for rowIndex in range (0,originalSudoku.sudokusize):
        for columnIndex in range(0,originalSudoku.sudokusize):
            if cell(rowIndex,columnIndex).value==0:    # if the value of a cell=0, put the positions of empty cells in a list.  
               dynamicCells.append((rowIndex,columnIndex))
        return dynamicCells
#######################################################    
class cell:                         # define the all the attribute of a cell
    
    def __init__(self,sudoku,rowIndex,columnIndex):     
        cell=(rowIndex,columnIndex)    # define the position of a cell. I hope this is a correct way, since I can not find a better way to define the rowIndex and columnIndex.

    def value(self):
        self.value=sudoku[rowIndex][columnIndex]   #define the value of a cell

    def rowFilled(self):   # Row filled= a list of used digits in this row
        rowFilled=[]        
        for columnIndex in range(0,sudokusize+1):
            rowFilled.append(cell.value)   
            return rowFilled        
    def rowOptions(self):   # Row options=a list of unused digits in this row
        return [x for x in allOptions if x not in rowFilled]

    def columnFilled(self):  #Column filled= a list of used digits in this column
        columnFilled=[]
        for rowIndex in range(0,sudokusize+1):
            columnFilled.append(cell.value)
            return columnFilled        
    def columnOptions(self):  #Column options= a list of unused digits in this column
        return [x for x in allOptions if x not in columnFilled]            
    
    def unitmatrixIndex(self,rowIndex,columnIndex):        #find out in which unit matrix a cell is
        rowQuotient,rowRem=divmod(rowIndex,unitmatrixSize) # if the sudoku is a 9*9 list, then the index is: |0 1 2|3 4 5| 6 7 8|  
        rowStart=rowQuotient*unitmatrixSize   
        return rowStart                             
        columnQuotient,columnRem=divmod(columnIndex,unitmatrixSize)  
        columnStart=columnQuotient*unitmatrixSize
        return columnStart 

    def unitmatrixFilled(self):  # Unit matrix filled= a list of used digits in this unit matrix
        unitmatrixFilled=[]            
        for rowIndex in rowIndexrange(rowStart, rowStart+unitmatrixSize):         
            for columnIndex in columnIndexrange(columnStart, columnStart+unitmatrixSize)
                if cell.value!=0:
                    unitmatrixFilled.append(cell.value)
                    return unitmatrixFilled
    def unitmatrixOptions(self):     #Unitmatrix options= a list of unused digits in this unitmatrix         
        return [x for x in allOptions if x not in unitmatrixFilled]            
        
    def optionList(self):  #OptionList=a list of digits that can be filled in a cell, considering the row, column, and unimatrix environment of the cell
        rowcolumnOptions=list(set(rowOptions).intersection(columnOptions))
        optionList=list(set(rowcolumnOptions).intersection(unitmatrixOptions))
        return optionList
    
    def possibilityAmount(self):   # get how many digits can be filled in to a cell
        return len(optionList)
    
  
#######################################################     
def possibilityAmountList(cell):   #Possibility amount list=a list that contains the possibility amount of each unfilled cell
    possibilityAmountList=[]
    for cell in unfilledCells:       ##?? syntax correct?
        possibilityAmountList.append(cell.possibilityAmount)
        return possibilityAmountList

def minPossibility(possibilityAmountList):  # Get minimum of the possibility amount of the unfilled cells
    return min(possibilityAmountList)
    

#######################################################
# the function solve_sudoku is written in two different ways. 
#the first way is called a simple method. The dynamicCells is only sorted for one time. It does not change later.
#The second way is called a complex method. The dynamicCells is sorted every time after a cell is filled. The positions of cells in the dynamicCells keep changing. 

#a simple method. Please see flow chart 2.####################  
def fill_value_in_cell(n):          #define a function on how to fill a value to a cell
    if dynamicCells[n].value!=0:    # if the value of a cell is not 0, then fill in the next untried value from the optionList
        optionIndex=dynamicCells[n].optionList.index(dynamicCells[n].value)    # get the index the current value in the optionList of this cell
    else:                           # if the value of a cell is 0, then fill in the first value from the optionList
        optionIndex=-1              # give optionIndex -1. 

    i=dynamicCells[n][0]            # get the rowIndex of this cell
    j=dynamicCells[n][1]            # get the columnIndex of this cell    
    newSudokulist[i][j]=dynamicCell[n].optionList[optionIndex+1]   # Find an untried value from the option list. Fill this value to the cell[i][j]
    return newSudokulist


def solve_sudoku(originalSudokulist):
    newSudokulist = copy.copy(originalSudokulist)     # copy the originalSudokulist to newSudokulist. All the update later on will be executed to the newSudokulist.
    newSudokulist = sudoku()                  # let the input sudokulist belongs to the sudoku class
    return dynamicCells.sort(key=lambda x: x.possibilityAmount, reverse=True)    # Sort the dynamic cells based on their possibility amount, from the smallest to the biggest possibility amount
    for n in range (0,len(dynamicCells)):     # n is the index of a cell in the dynamicCells list.
        if dynamicCells[n].possibilityAmount!=0:  # if the possibility amount of the nth cell >= 0, then fill in a value. 
            fill_value_in_cell(n)
            n=n+1                                 # Go to the next unfilled cell, which is the (n+1)th cell.
            while n > len(dynamicCells):          # if all the cells are filled, print out the sudoku
                print('the result is',newSudokulist)
            
        else: # if dynamicCells[n].possibilityAmount=0 This means if the possibility amount of the nth cell=0, then go to the previous filled cell. change its value.                        
            n=n-1
            if optionIndex<len(dynamicCells[n].optionList)-1 #If its value is not the last element of the option list, then fill in the an untried value. 
               fill_value_in_cell(n)
               n=n+1
            else:           ##If its value is the last element of the option list, then let erase its value. Go to its previous filled cell. 
                dynamicCell[n]=0
                n=n-1
    
solve_sudoku(originalSudokulist)  # this is the main function
    
    
    
    
#a complex method. Please see the flow chart 3.####################   
def solve_sudoku():
    if minPossibility!=0:        
        for cell in sudoku.unfilledCells: 
            if cell.possibilityAmount==minPossibility:           
                focusCell=cell                # call the cell that we want to fill in a value the "focusCell"             
                n=dynamicCells.index(focusCell)
                fill_value_in_cell(n)                 
                x=dynamicCells.pop(n)                
                dynamicCells.insert(m+1,x) 
                m=dynamicCells.index(focusCell)
                unfilledCells.remove(focusCell)                
                if len(sudoku.unfilledCells)!=0: #The list of unfilled cells is not empty
                    return min(possibilityAmountList)
                else: #The list of unfilled cells is empty
                    print(sudoku)
    else: #if minPossibility==0:
        for n in range (,): #???         
             focusCell=dynamicCells(n-1)   # goto the previous cell in the dynamic cell list.
             if focusCell.value==focusCell.optionList[-1]: #value of x is the last element in the option list
                n=n-1
            else: #value of x is not the last element in the option list
                focusCell.value=focusCell.optionList[optionIndex+1]
                # put the cell x in the correct place of the dynamic cell list
                # Get minimum of the possibility amount of the remaining unfilled cells
                dynamicCells.insert(m+1,x)
                m=dynamicCells.index(focusCell)

solve_sudoku(sudoku)  # this is the main function
#################################







