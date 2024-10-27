
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import pickle
mod=pickle.load(open("new_rf.pkl","rb"))
import random
import requests
import pandas as pd
data=requests.get("https://api.thingspeak.com/channels/2710609/feeds.json?api_key=BODVDT1ULNJAW9LD&results=2")
vol=data.json()['feeds'][-1]['field1']
cur=data.json()['feeds'][-1]['field2']
temp=float(data.json()['feeds'][-1]['field3'])

def temp_check(temp):
    if 16 < temp < 20:
        res="Moderate heat"
    elif temp > 20:
        res="High  Heat Chance of Fire"
    else:
        res="Battery is in correct temperature"
    return res



from tkinter import *
from PIL import Image,ImageTk
global root
root = Tk()
root.title('Battery Management System')
root.geometry('1500x750')
img=Image.open("a.jpeg")
img=img.resize((1500,750))
bg=ImageTk.PhotoImage(img)


lbl=Label(root,image=bg)
lbl.place(x=0,y=0)

label = Label( root, text = 'Battery Management System',font=('arial',24,'bold'),bd=20,background="#CDD954")
label.place(x=200,y=10)



label_1 = Label(root, text ='Cycle_Index',font=("Helvetica", 18),background="#CDD954")
label_1.place(x=200,y=100)
    
Entry_1= Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_1.place(x=500,y=100)
Entry_1.insert(0,str(random.randint(8, 9)))



label_2 = Label(root, text ='Discharge Time (min)',font=("Helvetica", 16),background="#CDD954")
label_2.place(x=200,y=170)
    
Entry_2 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_2.place(x=500,y=170)
Entry_2.insert(0,str(random.randint(7, 1000)))
   

    
label_3 = Label(root, text ='Decrement 3.6-3.4V (s)',font=("Helvetica", 18),background="#CDD954")
label_3.place(x=200,y=240)
    
Entry_3 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_3.place(x=500,y=240)
Entry_3.insert(0,str(random.randint(8, 1000)))



label_4 = Label(root, text =' Voltage Dischar. (V)',font=("Helvetica", 18),background="#CDD954")
label_4.place(x=200,y=310)
    
Entry_4= Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_4.place(x=500,y=310)
Entry_4.insert(0,str(vol))



label_5 = Label(root, text ='Current (A)',font=("Helvetica", 18),background="#CDD954")
label_5.place(x=200,y=380)
    
Entry_5 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_5.place(x=500,y=380)
Entry_5.insert(0,str(cur))


label_6 = Label(root, text ='Time at 4.15V (min)',font=("Helvetica", 18),background="#CDD954")
label_6.place(x=200,y=450)
    
Entry_6 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_6.place(x=500,y=450)
Entry_6.insert(0,str(random.randint(8, 1000)))



label_7 = Label(root, text ='Time constant current (s)',font=("Helvetica", 18),background="#CDD954")
label_7.place(x=200,y=520)
    
Entry_7 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_7.place(x=500,y=520)
Entry_7.insert(0,str(random.randint(1, 1000)))


def refresh():
    data=requests.get("https://api.thingspeak.com/channels/2710609/feeds.json?api_key=BODVDT1ULNJAW9LD&results=2")
    vol_t=data.json()['feeds'][-1]['field1']
    cur_t=data.json()['feeds'][-1]['field2']
    temp_t=float(data.json()['feeds'][-1]['field3'])
    output.configure(text="")
    tempp.configure(text="")
    Entry_1.delete(0,END)
    Entry_2.delete(0,END)
    Entry_3.delete(0,END)
    Entry_4.delete(0,END)
    Entry_5.delete(0,END)
    Entry_6.delete(0,END)
    Entry_7.delete(0,END)
    Entry_1.insert(0,str(random.randint(8, 9)))
    Entry_2.insert(0,str(random.randint(7, 1000)))
    Entry_3.insert(0,str(random.randint(8, 1000)))
    Entry_4.insert(0,str(vol_t))
    Entry_5.insert(0,str(cur_t))
    Entry_6.insert(0,str(random.randint(8, 1000)))
    Entry_7.insert(0,str(random.randint(1,1000 )))
    
    
    

def predict():
    v1 = Entry_1.get()
    v2 = Entry_2.get()
    v3 = Entry_3.get()
    v4 =Entry_4.get()
    v5 =Entry_5.get()
    v6 =Entry_6.get()  
    v7 = Entry_7.get()  
    result=temp_check(temp)
    tempp.config(text=f"Temperature : {temp} \n Status : {result}") 
    
    data = np.array([[v1, v2, v3, v4, v5, v6, v7]])
        
    res = mod.predict(data)[0]
    charge_time=res[0]//60
    rull=res[1]//60
    output.configure(text=f"Charging Time : {charge_time} Mins \n Reaminaing Time  : {rull} kms")

    
    
    
   

b1 = Button(root, text = 'predict',font=("Helvetica", 18),background="#CDD954",command = predict)
b1.place(x=200,y=590)

b1 = Button(root, text = 'REFRESH',font=("Helvetica", 18),background="#CDD954",command = refresh)
b1.place(x=900,y=350)

tempp = Label(root,font=("Helvetica", 18),justify=CENTER)
tempp.place(x=800,y=200)   

output = Label(root,font=("Helvetica", 18),justify=CENTER)
output.place(x=500,y=590)

    
root.mainloop()






#############################################################################################################






