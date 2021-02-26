from tkinter import *
import random
root=Tk()
root.geometry("900x500")

Label_hospital=Label(root)
Label_hospital.place(relx=0.11,rely=0.35,anchor=CENTER)

Label_IT=Label(root)
Label_IT.place(relx=0.14,rely=0.65,anchor=CENTER)

Label_chemical=Label(root)
Label_chemical.place(relx=0.11,rely=0.95,anchor=CENTER)

class Parent():
    def __init__(self):
        print("Find Job")
    def doctor(user):
        hospital_list=["Galaxy","Asian","Fortis","Apollo","AIIMS","Artemis"]
        hospital_selected=hospital_list[random.randint(0, 5)]
        Label_hospital["text"]=user+" has been alloted to "+hospital_selected
    def IT(it):
        it_list=["Tata Consultancy S","Infosys","HCL Technologies","Wipro Limited","Larsen Infotech","Tech Mahindra"]
        it_selected=it_list[random.randint(0, 5)]
        Label_IT["text"]=it+" has been alloted to "+it_selected
    def chemical(chemi):
        chemical_list=["BASF","Ineos","Reliance","DuPont"]
        chemical_selected=chemical_list[random.randint(0, 3)]
        Label_chemical["text"]=chemi+" has been alloted to "+chemical_selected
class doctor(Parent):
    def __init__(self,name):
        self.user=name
    def getDoctor(self):
        Parent.doctor(self.user)
class IT(Parent):
    def __init__(self,member):
        self.it=member
    def getmember(self):
        Parent.IT(self.it)
class Chemical(Parent):
    def __init__(self,members):
        self.chemi=members
    def getmembers(self):
        Parent.chemical(self.chemi)
hospital=doctor("Micheal")
It=IT("Jessica")
chemic=Chemical("Peter")
btn_hospital=Button(root,text="Show the hospital alloted",command=hospital.getDoctor())
btn_hospital.place(relx=0.09,rely=0.2,anchor=CENTER)

btn_IT=Button(root,text="Show the IT company alloted",command=It.getmember())
btn_IT.place(relx=0.1,rely=0.5,anchor=CENTER)

btn_chemical=Button(root,text="Show the chemical company alloted",command=chemic.getmembers())
btn_chemical.place(relx=0.12,rely=0.8,anchor=CENTER)
root.mainloop()
