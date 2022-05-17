from tkinter import *


# Table class
class Table:
    # Initialize a constructor
    def __init__(self, gui):

        # An approach for creating the table
        for i in range(total_rows):
            for j in range(total_columns):
                #print(i)
                if j ==0:
                    self.entry = Entry(gui, width=10, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 10, 'bold'))
                elif employee_list[i][j]== 0:
                    self.entry = Entry(gui, width=10, bg='White',fg='White',
                                       font=('Arial', 10, 'bold'))
                elif employee_list[i][j]== 1:
                    self.entry = Entry(gui, width=10, bg='Yellow',fg='Yellow',
                                       font=('Arial', 10, 'bold'))
                elif employee_list[i][j]== 2:
                    self.entry = Entry(gui, width=10, bg='blue',fg='blue',
                               font=('Arial', 10, 'bold'))
                elif employee_list[i][j]== 3:
                    self.entry = Entry(gui, width=10, bg='green',fg='green',
                                       font=('Arial', 10, 'bold'))
                elif employee_list[i][j]== 4:
                    self.entry = Entry(gui, width=10, bg='red',fg='red',
                                       font=('Arial', 10, 'bold'))
                elif employee_list[i][j]== 5:
                    self.entry = Entry(gui, width=10, bg='gray',fg='gray',
                                       font=('Arial', 10, 'bold'))
                elif employee_list[i][j]== 6:
                    self.entry = Entry(gui, width=10, bg='pink',fg='pink',
                                       font=('Arial', 10, 'bold'))
                else:
                    self.entry = Entry(gui, width=10, bg='black',fg='black',
                                       font=('Arial', 10, 'bold'))

                self.entry.grid(row=i, column=j)
                self.entry.insert(END, employee_list[i][j])
        
                


# take the data
employee_list = [('A',1,1,0,0,0,1,1,0,0,0,0),
                ('B',2,2,2,0,0,0,0,2,2,2,0),
                ('C',3,0,0,0,0,0,0,0,3,0,0),
                ('RM',1,1,2,2,2,3,1,1,2,2,2)]


# find total number of rows and
# columns in list
total_rows = len(employee_list)
total_columns = len(employee_list[0])

# create root window
root = Tk()
root.geometry("600x300") 
root.title("Reporte de calendarización")

gui = Frame(root, bg="#EBEBEB")
#gui.configure(bg='White')
gui.grid()



pantalla= Canvas(gui,width=600, height=300, bg="#EBEBEB")
pantalla.grid(row=0, column=0, sticky="nsew")
tableCanvas = Frame(gui, bg="#EBEBEB")
pantalla.create_window(0, 0, window=tableCanvas, anchor='nw')

table = Table(tableCanvas)
#Label(tableCanvas, text="Reporte de calendarización", bg='#EBEBEB').grid(row=0, column=0)


scrollbar = Scrollbar(gui, orient=HORIZONTAL) 
scrollbar.config(command=pantalla.xview)
pantalla.config(xscrollcommand=scrollbar.set)
scrollbar.grid(row=0,column=0,sticky=E+W+S)

button1 = Button(gui, text='Informacion Extra', fg='black')
button1.grid(row=0,column=0)
root.mainloop()