def switchName(argument):
    """
    It takes an integer as an argument and returns the corresponding letter of the alphabet
    
    :param argument: The argument is the value which is to be passed to the function
    :return: The name of the month
    """
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
    """
    It takes an integer as an argument and returns a string with the hexadecimal code of the color
    
    :param argument: The argument is the number of the color you want to use
    :return: The color of the node
    """
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