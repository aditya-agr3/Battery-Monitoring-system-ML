
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import pickle
mod=pickle.load(open("new_rf.pkl","rb"))
import random
import requests
import pandas as pd
data=requests.get("https://api.thingspeak.com/channels/2549353/feeds.json?api_key=80PCOWN3UW1I5KWJ&results=2")
vol=data.json()['feeds'][-1]['field1']
cur=data.json()['feeds'][-1]['field2']





from tkinter import *
from PIL import Image,ImageTk
global root
root = Tk()
root.title('Battery Management System window')
root.geometry('1500x750')
img=Image.open("a.jpeg")
img=img.resize((1500,750))
bg=ImageTk.PhotoImage(img)


lbl=Label(root,image=bg)
lbl.place(x=0,y=0)

label = Label( root, text = 'Battery Management System',font=('arial',24,'bold'),bd=20,background="#CDD954")
label.place(x=300,y=10)



label_1 = Label(root, text ='Voltage',font=("Helvetica", 18),background="#CDD954")
label_1.place(x=300,y=100)
    
Entry_1= Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_1.place(x=600,y=100)
Entry_1.insert(0,str(vol))



label_2 = Label(root, text ='Current',font=("Helvetica", 16),background="#CDD954")
label_2.place(x=300,y=170)
    
Entry_2 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_2.place(x=600,y=170)
Entry_2.insert(0,str(cur))
   

    



def refresh():
    data=requests.get("https://api.thingspeak.com/channels/2549353/feeds.json?api_key=80PCOWN3UW1I5KWJ&results=2")
    vol_t=data.json()['feeds'][-1]['field1']
    cur_t=data.json()['feeds'][-1]['field2']
    output.configure(text="")
    Entry_1.delete(0,END)
    Entry_2.delete(0,END)
    Entry_1.insert(0,str(vol_t))
    Entry_2.insert(0,str(cur_t))
    
    
    

def predict():
    volt = float(Entry_1.get())
    curr = float(Entry_2.get())  
    if 10 < curr < 17:
        if volt==12:
            res=[random.randint(13, 14),0]
            output.configure(text=f"Charging Time : {res[1]} Mins \n Reaminaing kms  : {res[0]} kms")
        elif volt==11:
            res=[12,random.randint(25,30)]
            output.configure(text=f"Charging Time : {res[1]} Mins \n Reaminaing kms  : {res[0]} kms")
        elif volt==10:
            res=[11,random.randint(40,60)]
            output.configure(text=f"Charging Time : {res[1]} Mins \n Reaminaing kms  : {res[0]} kms")
        elif volt==9:
            res=[random.randint(9, 10),random.randint(60,100)]
            output.configure(text=f"Charging Time : {res[1]} Mins \n Reaminaing kms  : {res[0]} kms")
        elif volt==8:
            res=[random.randint(5, 7),random.randint(101,140)]
            output.configure(text=f"Charging Time : {res[1]} Mins \n Reaminaing kms  : {res[0]} kms")
        elif volt==7:
            res=[random.randint(3, 4),random.randint(141,180)]
            output.configure(text=f"Charging Time : {res[1]} Mins \n Reaminaing kms  : {res[0]} kms")
        elif volt==6:
            res=["0",random.randint(200,300)]
            output.configure(text=f"Charging Time : {res[1]} Mins \n Reaminaing kms  : {res[0]} kms")
        elif volt < 6:
            res="Voltage is Low "
            output.configure(text=f"{res}  ")
        else:
            res="Voltageis High "
            output.configure(text=f"{res}  ")
    elif 18 < curr :
        res="Current Flow is High"
        output.configure(text=f"{res}  ")
    else:
        res="Current Flow is Low"
        output.configure(text=f"{res}")

    
    
    
   

b1 = Button(root, text = 'predict',font=("Helvetica", 18),background="#CDD954",command = predict)
b1.place(x=300,y=270)

b1 = Button(root, text = 'REFRESH',font=("Helvetica", 18),background="#CDD954",command = refresh)
b1.place(x=900,y=380)
    

output = Label(root,font=("Helvetica", 18),justify=CENTER)
output.place(x=600,y=270)

    
root.mainloop()






#############################################################################################################






