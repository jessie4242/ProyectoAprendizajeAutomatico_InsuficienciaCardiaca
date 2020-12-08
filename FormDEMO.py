from tkinter import *
from tkinter import messagebox
import numpy as np
import pickle


def send_data():
    model = pickle.load(open("modeloIC.sav", 'rb'))
    edad = entry_1.get()
    genero = varGenero.get()
    enzima = entry_2.get()
    ejectionFraction = entry_3.get()
    hipertension = varHip.get()
    plaqueta = entry_4.get()
    creatinaS = entry_5.get()
    dias = entry_6.get()
    print(edad,"\t",genero,"\t",enzima,"\t",ejectionFraction,"\t",hipertension,"\t",plaqueta,"\t",creatinaS,"\t",dias)
    data = np.array([[edad,genero,enzima,ejectionFraction,hipertension,plaqueta,creatinaS,dias]])
    result = model.predict(data)[0]
    print(result) 
    if result == 0:
        messagebox.showinfo("Respuesta: ","Sobrevive")
    else:
        messagebox.showinfo("Respuesta: ","No sobrevive")


root = Tk()
root.geometry('800x650')
root.title("Registration Form")
root.configure(background="#c56183") 

label_0 = Label(root,bg = "#c56183", text="Supervivencia ante la insuficiencia cardiaca",width=50,font=("bold", 20))
label_0.place(x=0,y=30)


label_1 = Label(root,bg = "#c56183", text="Edad: ",width=20,font=("bold", 13))
label_1.place(x=200,y=130)
entry_1 = Entry(root)
entry_1.place(x=400,y=130)

label_2 = Label(root,bg = "#c56183", text="Género: ",width=20,font=("bold", 13))
label_2.place(x=200,y=180)
varGenero = IntVar()
rbgenero1=Radiobutton(root, bg = "#c56183",text="Hombre",padx = 5, font=("bold", 13),variable=varGenero, value=1).place(x=400,y=180)
rbgenero2=Radiobutton(root, bg = "#c56183",text="Mujer",padx = 20, font=("bold", 13),variable=varGenero, value=0).place(x=500,y=180)

label_3 = Label(root,bg = "#c56183", text="Nivel de enzima",width=20,font=("bold", 13))
label_3.place(x=200,y=230)
entry_2 = Entry(root)
entry_2.place(x=400,y=230)

label_4 = Label(root,bg = "#c56183", text="Ejection Fraction",width=20,font=("bold", 13))
label_4.place(x=200,y=280)
entry_3 = Entry(root)
entry_3.place(x=400,y=280)

label_5 = Label(root,bg = "#c56183", text="Hipertensión",width=20,font=("bold", 13))
label_5.place(x=200,y=330)
varHip = IntVar()
rbhipertension1=Radiobutton(root, bg = "#c56183",text="Si",font=("bold", 13),padx = 5, variable=varHip, value=1).place(x=400,y=330)
rbhipertension2=Radiobutton(root, bg = "#c56183",text="No",font=("bold", 13),padx = 20, variable=varHip, value=0).place(x=500,y=330)

label_6 = Label(root, bg = "#c56183",text="Núm. plaquetas \n en la sangre",width=20,font=("bold", 13))
label_6.place(x=200,y=380)
entry_4 = Entry(root)
entry_4.place(x=400,y=390)

label_7 = Label(root, bg = "#c56183",text="Nivel de Creatina sérica \n en sangre (mg/dL)",width=20,font=("bold", 13))
label_7.place(x=200,y=450) 
entry_5 = Entry(root)
entry_5.place(x=400,y=460)

label_8 = Label(root, bg = "#c56183",text="Dias de Tratamiento",width=20,font=("bold", 13))
label_8.place(x=200,y=530) 
entry_6 = Entry(root)
entry_6.place(x=400,y=530)

submit_btn = Button(root, text='Enviar',command=send_data, width=20,bg='#d7385e',fg='white').place(x=350,y=600)

root.mainloop()

