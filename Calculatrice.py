from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.configure(background="#101419")
    root.title("Calculatrice By Finoana Randri")
    root.geometry("385x485")
    root.minsize(385,485)
    #root.maxsize(385,485)
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
        b.bind("<Button-1>",print)
    
        b.grid(row=ligne,column=colonne)
        
        colonne += 1
        if colonne ==4:
            colonne=0
            ligne +=1
        b= Label(root,text="Effacer",bg="red",fg="#fff",height=5,width=12)
        b.bind("<Button-1>",print)
        b.grid(columnspan=4)
    root.mainloop()