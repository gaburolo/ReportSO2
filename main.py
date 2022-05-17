from tkinter import *
from switchs import *
from matriz import *

#Temporary lists
lineList=[]
processList=[]
numBlocks=[]

# The class Table is a constructor that creates a table with the given dimensions and colors the cells
# based on the values in the employee_list
class Table:
    
    def __init__(self, gui):
        """
        This function creates a grid of Entry widgets, each of which is populated with a value from the
        employee_list
        
        :param gui: the name of the window
        """
        color=""
        
        for i in range(total_rows):
            for j in range(total_columns):
                #print(i)
                if j ==0:
                    self.entry = Entry(gui, width=10, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 10, 'bold'))
                elif employee_list[i][j]== 0:
                    self.entry = Entry(gui, width=10, bg='White',fg='White',
                                       font=('Arial', 10, 'bold'))
                else:
                    color=switchColors(employee_list[i][j])
                    self.entry = Entry(gui, width=10, bg=color,fg=color,
                                       font=('Arial', 10, 'bold'))

                self.entry.grid(row=i, column=j)
                self.entry.insert(END, employee_list[i][j])
        
                
#Variables for the scheduling matrix
lineList = check(lineList)
process(numBlocks,processList,lineList)
processList = duplicados(processList,0)
numBlocks = duplicados(numBlocks,0)
total_columns = len(lineList)
employee_list=processList
employee_list.append(lineList)
total_rows = len(employee_list)

#Main Window
root = Tk()
root.geometry("1100x600") 
root.title("Reporte de calendarización")

#Main Frame
gui = Frame(root, bg="#EBEBEB")
gui.grid()


#Main Canva
pantalla= Canvas(gui,width=1100, height=600, bg="#EBEBEB")
pantalla.grid(row=0, column=0, sticky="nsew")
tableCanvas = Frame(gui, bg="#EBEBEB")
pantalla.create_window(0, 0, window=tableCanvas, anchor='nw')

#Create the table visually on the screen
table = Table(tableCanvas)


#Definition of scrollbar for the screen
scrollbar = Scrollbar(gui, orient=HORIZONTAL) 
scrollbar.config(command=pantalla.xview)
pantalla.config(xscrollcommand=scrollbar.set)
scrollbar.grid(row=0,column=0,sticky=E+W+S)

#Process Capability Text Label
Label(gui, text=numBlocks, bg='#EBEBEB').grid(row=0, column=0, sticky=S)

root.mainloop()