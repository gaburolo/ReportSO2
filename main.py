from tkinter import *


lineList=[]
processList=[]
numBlocks=[]

def check():
    contador=0
    lineList.append('FCFS')
    with open('calend.txt') as f:
        datafile = f.readlines()
    found = False  # This isn't really necessary
    for line in datafile:
        cont=0
        for char in line:
            if "i"==char:
                number=line[cont+6:cont+8:1].rstrip()
                lineList.append(int(number))
                cont=0
                break
            else:
                cont=cont+1
        
        
    return False  # Because you finished the search without finding
def process():
   
    with open('calend.txt') as f:
        datafile = f.readlines()
    numLine=1
    name=""
    for line in datafile:
        cont=0
        for char in line:
            if "c"==char:
                while numLine<=20:
                    if ("id:   "+str(numLine) in line)  :
                        name=switchName(numLine)
                        createProcess(numLine,int(line[cont+4:cont+6:1]),str(name))
                        cont=0
                        numLine=0
                        break
                    else:
                        numLine=numLine+1

            else:
                cont=cont+1

def duplicados(lst, i):
    if i==len(lst):
        return lst
    else:
    
        for j in range(len(lst)):
            
            if lst[i] == lst[j] and i!=j:
                del lst[j]
                return duplicados(lst,i)
        return duplicados(lst,i+1)

    

def switchName(argument):
    switcher = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P",
        17: "Q",
        18: "R",
        19: "S",
        20: "T"
    }
    return switcher.get(argument, "Invalid month")

def switchColors(argument):
    switcher = {
        1: "#FFFF33",#Amarillo
        2: "#FF0000",#Rojo
        3: "#0000FF",#Azul
        4: "#00FF00",#Verde
        5: "#FF9933",#Naranja
        6: "#4C9900",#Verde Ogre
        7: "#00FFFF",#Celeste
        8: "#FFCCCC",#Rosa
        9: "#A0A0A0",#Gris
        10: "#B266FF",#Violeta
        11: "#CCCC00",#Amarillo Verdoso
        12: "#660000",#Marron
        13: "#66B2FF",#Azul Oceano
        14: "#99FF99",#Verde Claro
        15: "#000000",#Negro
        16: "#009999",#Cian
        17: "#FF007F",#Magenta
        18: "#330066",#Morado Noche
        19: "#FF9999",#Piel
        20: "#36E1BF"#Verde Azulado
    }
    return switcher.get(argument, "Invalid month")  

def createProcess(num,length,name):
    tempList=[]
    tempList.append(name)
    for i in range(len(lineList)):
        if i<=length-1:
            tempList.append(num)
        else:
            tempList.append(0)
    numBlocks.append(name+":"+ str(length))
    
    processList.append(tempList)
    




# Table class
class Table:
    # Initialize a constructor
    def __init__(self, gui):
        color=""
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
                else:
                    color=switchColors(employee_list[i][j])
                    self.entry = Entry(gui, width=10, bg=color,fg=color,
                                       font=('Arial', 10, 'bold'))

                self.entry.grid(row=i, column=j)
                self.entry.insert(END, employee_list[i][j])
        
                

check()


# take the data
#employee_list=[]
#
process()
final=[]
final = duplicados(processList,0)
numBlocks =duplicados(numBlocks,0)



total_columns = len(lineList)

employee_list=final
employee_list.append(lineList)
total_rows = len(employee_list)
#print(numBlocks)
#print(final)
# create root window
root = Tk()
root.geometry("1100x600") 
root.title("Reporte de calendarización")

gui = Frame(root, bg="#EBEBEB")
#gui.configure(bg='White')
gui.grid()



pantalla= Canvas(gui,width=1100, height=600, bg="#EBEBEB")
pantalla.grid(row=0, column=0, sticky="nsew")
tableCanvas = Frame(gui, bg="#EBEBEB")
pantalla.create_window(0, 0, window=tableCanvas, anchor='nw')

table = Table(tableCanvas)



scrollbar = Scrollbar(gui, orient=HORIZONTAL) 
scrollbar.config(command=pantalla.xview)
pantalla.config(xscrollcommand=scrollbar.set)
scrollbar.grid(row=0,column=0,sticky=E+W+S)


Label(gui, text=numBlocks, bg='#EBEBEB').grid(row=0, column=0, sticky=S)

root.mainloop()