from tkinter import *


expression =""


def appuyer(touche):
     if touche =="=":
         calculer()
         return
     global expression 
     expression += str(touche)
     equation.set(expression)
#ici je defini la fontion calculer ainsi que les try et exept pour que l appli ne plante pas face au calcule impossible
def calculer():
    try:
        global expression
        total = str(eval(expression))
        
        equation.set(total)
        expression=total
    except:
        equation.set("erreur")
        expression=""    

def effacer():
    global expression
    expression =""
    equation.set("")

if __name__ == "__main__":
    root = Tk()
    root.configure(background="#984447")
    root.title("Calculatrice By Finoana Randri")
    root.geometry("385x600")
    root.minsize(385,600)
    root.maxsize(385,600)
#ici c'est la variable pour stocker les contenus
    equation = StringVar()
#boite de resultat
    resultat = Label(root,bg="orange",fg="#fff",textvariable=equation,height="4",width="49")
    resultat.grid(columnspan=4)
#bouton
    boutons =[7,8,9,"*",1,2,3,"+",0,".","/","="]
    ligne =1
    colonne =0
    for bouton in boutons:
        b= Label(root,text=str(bouton),bg="#476C9B",fg="#fff",height=8,width=12)
    #Vision Xd Follow Finoana On Git Hub or Po**Hub xdxd
        b.bind("<Button-1>",lambda e,bouton=bouton: appuyer(bouton))
    
        b.grid(row=ligne,column=colonne)
        
        colonne += 1
        if colonne ==4:
            colonne=0
            ligne +=1
        b= Label(root,text="Effacer",bg="#984447",fg="#FFF",height=5,width=13)
        b.bind("<Button-1>",lambda e: effacer())
        b.grid(columnspan=4)
    
    
         #barre de menu

        menu_bar = Menu(root,bg="white")

        #preminer menu(i love python now but i am beginer  XD FinoanaRandria)
        file_menu = Menu(menu_bar ,tearoff=0)
        file_menu.add_command(label="Effacer",command= effacer)
        file_menu.add_command(label="Quit" ,command=root.quit)  
        menu_bar.add_cascade(label="Options",menu=file_menu)

        #insertion dans la fenetre
        root.config(menu=menu_bar)

    root.mainloop()