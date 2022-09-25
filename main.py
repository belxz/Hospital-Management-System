from logging import root
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox  as mb
from tkinter import ttk
import mysql.connector as ms
import time

def login ():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        mb.showerror('Error', 'Fields cannot be empty')

    elif usernameEntry.get() == 'patient' and passwordEntry.get() == 'password':
        mb.showinfo('Success', 'Welcome')
        clock()
    
    else:
        mb.showerror('Error', 'Please enter the correct credentials')
        

window = Tk()



window.geometry('1280x700+0+0')






window.resizable(False,False)
backgroundImage=ImageTk.PhotoImage(Image.open('C:\\Users\\belz1\\Projects\\HealthcareProject\\pexels-scott-webb-311458_1.jpg'))
bgLabel=Label(window, image=backgroundImage)
bgLabel.place(x=210, y=50)

loginFrame=Frame(window, bg='white')
loginFrame.place(x=400, y=150)
#logoImage=ImageTk.PhotoImage(Image.open("C:\\Users\\belz1\\OneDrive\\Pictures\\bg.jpg"))
logoLabel=Label(loginFrame)
logoLabel.grid(row=0,column=0, columnspan=2, pady=10)



usernameLabel=Label(loginFrame,text='Username',compound=LEFT,   font=('times new roman', 20, 'bold'), bg='white')
usernameLabel.grid(row=1, column=0)

usernameEntry=Entry(loginFrame,
            font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
usernameEntry.grid(row=1,column=1)

#passwordImage=ImageTk.PhotoImage(Image.open("C:\\Users\\belz1\\OneDrive\\Pictures\\bg.jpg"))
passwordLabel=Label(loginFrame, text='Password', compound=LEFT, font=('times new roman', 20, 'bold'), bg='white')
passwordLabel.grid(row=3, column=0)

passwordEntry=Entry(loginFrame,font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
passwordEntry.grid(row=3,column=1)

loginButton=Button(loginFrame, text='Login', font=('times new roman', 14, 'bold'), width=15, fg='white',bg='green', activebackground='green', activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=5, column=0)

exitButton=Button(loginFrame, text='Exit', command=window.destroy, font=('times new roman', 14, 'bold'), width=15, fg='white',bg='green', activebackground='green', activeforeground='white', cursor='hand2')
exitButton.grid(row=5, column=1)


welcomeLabel=Label(loginFrame, text='Welcome',compound=LEFT,font=('times new roman', 30, 'bold'),bg='white', width=20).grid(row=0, column=1)

#Window 2 Parts

def clock():
    root=Toplevel(window)
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    print(date, currenttime)



#GUI Part
#root=Toplevel(window)
    root.geometry('1174x680+50+20')
    root.resizable(0,0)
    root.title('Health Portal System')

    datetimeLabel=Label(root, font=('times new roman', 18, 'bold'))
    datetimeLabel.place(x=5,y=5)
    


    global addWindow
    addWindow=Toplevel(root)
    
    imageLabel=Label(root, text="Great Hospitals Do", font=('lucida handwriting' ,30),fg='magenta2', width =40 ).place(x=150, y=150)
    imageLabel=Label(root, text="Two Things.", font=('lucida handwriting' ,30),fg='royalblue1', width =40 ).place(x=150, y=250)
    imageLabel=Label(root, text="They Look After", font=('lucida handwriting' ,30),fg='forest green', width =40 ).place(x=150, y=350)
    imageLabel=Label(root, text="Patients, And They Teach", font=('lucida handwriting' ,30),fg='goldenrod', width =40 ).place(x=150, y=450)
    imageLabel=Label(root, text="Young Doctors", font=('lucida handwriting' ,30),fg='orange red', width =40 ).place(x=150, y=550)
    addButton=Button(root, text='ADD', font=('times new roman', 20, 'bold'), width=15, fg='black',bg='lightskyblue', activebackground='black', activeforeground='white',pady=30, command=addFunction)
    addButton.grid(row=1, column=0)
    

    deleteButton=Button(root, text='DELETE',font=('times new roman', 20, 'bold'),width=15, fg='black',bg='palegreen2', activebackground='black', activeforeground='white',pady=30, command=Del)
    deleteButton.grid(row=3, column=0)


    updateButton=Button(root, text='UPDATE',font=('times new roman', 20, 'bold'), pady=30, width=15, fg='black',bg='cornflowerblue', activebackground='black', command=Update)
    updateButton.grid(row=5, column=0)


    searchButton=Button(root, text='SEARCH',font=('times new roman', 20, 'bold'), width=15, fg='black',bg='lavenderblush',command=choose, activebackground='black', pady=30)
    searchButton.grid(row=7, column=0)
   
    graphButton=Button(root, text='GRAPH',font=('times new roman', 20, 'bold'), width=15, fg='black',bg='palegoldenrod', activebackground='black',command=graph, pady=30)
    graphButton.grid(row=9, column=0)


    
    exitButton=Button(root, text='EXIT', command=window.destroy, font=('times new roman', 20, 'bold'),width=15, fg='green',bg='plum2', activebackground='black', pady=30, )
    exitButton.grid(row=11, column=0)
    




   # scrollbarX=Scrollbar(rightFrame, orient=HORIZONTAL)
   # scrollbarY=Scrollbar(rightFrame, orient=VERTICAL)
   # scrollbarX.pack(side=BOTTOM, fill=X)
   # scrollbarY.pack(side=RIGHT, fill=Y)

    #patientTable=ttk.Treeview(rightFrame, columns=('Name', 'ID', 'Gender', 'Height', 'Weight')),

def addFunction():
    global patient_name
    global patient_ID
    global patient_gender
    global height
    global weight

    patient_name= StringVar()
    patient_ID = IntVar()
    patient_gender= StringVar()
    height= IntVar()
    weight= IntVar()

    global window2
    window2=Toplevel(addWindow)
    window2.geometry('1174x680+50+20')
    addNameLabel=Label(window2, text='Add Name', font=('times new roman', 20, 'bold'))
    addNameLabel.grid(row=1, column=0)
    addNameEntry=Entry(window2,font=('times new roman', 20, 'bold'), text=patient_name)
    addNameEntry.grid(row=1,column=1)

    addIDLabel=Label(window2, text='Add ID', font=('times new roman', 20, 'bold'))
    addIDLabel.grid(row=2, column=0)
    addIDEntry=Entry(window2, font=('times new roman', 20, 'bold'),text=patient_ID)
    addIDEntry.grid(row=2,column=1)

    addGenderLabel=Label(window2, text='Add Gender', font=('times new roman', 20, 'bold'))
    addGenderLabel.grid(row=3, column=0)
    addGenderEntry=Entry(window2, font=('times new roman', 20, 'bold'), text=patient_gender)
    addGenderEntry.grid(row=3,column=1)

    addHeightLabel=Label(window2, text='Add Height', font=('times new roman', 20, 'bold'),)
    addHeightLabel.grid(row=4, column=0)
    addHeightEntry=Entry(window2, font=('times new roman', 20, 'bold'),text=height)
    addHeightEntry.grid(row=4,column=1)

    addWeightLabel=Label(window2, text='Add Weight', font=('times new roman', 20, 'bold'))
    addWeightLabel.grid(row=5, column=0)
    addWeightEntry=Entry(window2, font=('times new roman', 20, 'bold'), text= weight)
    addWeightEntry.grid(row=5,column=1)

    addSubmitButton=Button(window2, text='Submit', font=('times new roman', 20, 'bold'),width=15, fg='black',bg='palegreen', activebackground='black', pady=30, command=addAlgorithm,)
    addSubmitButton.grid(row=6, column=0)

    addExitButton=Button(window2, text='Exit', font=('times new roman', 20, 'bold'), width=15, fg='black',bg='salmon', activebackground='black', pady=30, command=window2.destroy)
    addExitButton.grid(row=6, column=1)

def graph2():
    import pandas as pd
    import mysql.connector as ms
    import matplotlib.pyplot as plt
    criteria=n.get()
    mydb=ms.connect(host="localhost", user= "root", passwd = "!@#$Belz4ane", database = "patient")
    cur=mydb.cursor()
    x=[0,1,2,3,4]
    y=[0,1,2,3,4]
    heightlist=[1,20,21,40,41,60,61,80,81,100]
    weightlist=[1,20,21,40,41,60,61,80,81,100]
    heightcount=[]
    weightcount=[]
    heightgap=['1-20','21-40','41-60','61-80','81-100']
    weightgap=['1-20','21-40','41-60','61-80','81-100']
    if criteria=="On the basis of Height":
        for i in range(0,len(heightlist),2):
            cur.execute("select count(height)from patient_data where height>=%s and height<=%s",(heightlist[i],heightlist[i+1]))
            myrecords=cur.fetchone()
            heightcount.append(myrecords[0])
        plt.bar(y,heightcount,color='red')
        plt.xlabel("Height")
        plt.ylabel("Number of patients")
        plt.title("Number of Patients VS Height")
        plt.xticks(y,heightgap) 
        plt.show()
    if criteria=="On the basis of weight":
        for j in range(0,len(weightlist),2):
            cur.execute("select count(weight)from patient_data where weight>=%s and weight<=%s",(weightlist[j],weightlist[j+1]))
            myrecords=cur.fetchone()
            weightcount.append(myrecords[0])
        plt.bar(x,weightcount,color='green')
        plt.xlabel("Weight")
        plt.ylabel("Number of patients")
        plt.title("Number of Patients VS Weight")
        plt.xticks(x,weightgap)
        plt.show()
                      
                      
def graph():
    global window7
    window7 = Toplevel(addWindow)
    global n
    n  = StringVar()
    Label(window7, text = "Select the category: ",width=15, font =("arial", 20, "bold")). grid(row = 1, column = 0)
    choice = ttk.Combobox(window7,width= 28, height = 100, textvariable = n)
    choice['value'] = ("On the basis of Height", "On the basis of weight")
    choice.grid(row=2,column=0)
    choice.current(0)
   
                                                                                                                                                                              
    Button(window7,text="Show Graph",command=graph2,bg='light green',fg='purple',width=15,font=('arial',19,'bold')).grid(row=3,column=0)
    Button(window7,text="Back",command=window7.destroy,bg='red',fg='white',width=15,font=('arial',19,'bold')).grid(row=3,column=1)


def addAlgorithm():
  import mysql.connector as ms
  name_info = patient_name.get()
  patientID_info = patient_ID.get()
  patientGender_info = patient_gender.get()
  patientheight_info = height.get()
  patientweight_info = weight.get()
  if (name_info=="" or patientID_info =="" or patientGender_info=="" or patientheight_info==""):
    mb.showerror("Insert Status", "Everything is required", parent = window2)
  else:
    mydb = ms.connect(host="localhost", user= "root", passwd = "!@#$Belz4ane", database = "patient")
    cur = mydb.cursor()
    sql1 = ("insert into patient_data values(%s,%s, %s,%s, %s)")
    val1 = (name_info, patientID_info, patientGender_info, patientheight_info, patientweight_info)
    cur.execute(sql1, val1)
    mydb.commit()
    mb.showinfo("Insert Status", "Details added", parent= window2)

def Delete():
    print('3')
    import mysql.connector as ms
    patientID_info = patient_ID.get()
    mydb = ms.connect(host="localhost", user= "root", passwd = "!@#$Belz4ane", database = "patient")
    cur = mydb.cursor()
    sql2 = ("delete from patient_data where patient_ID=%s")
    val2 = (patientID_info,)
    cur.execute(sql2, val2)
    mydb.commit()
    mb.showinfo("Details successfully Deleted", parent=window3)
     
    
def Del():
    global window3
    window3=Toplevel(addWindow)
    global patient_ID
    patient_ID=StringVar()
    deleteIDLabel=Label(window3, text='Delete ID', font= 
    ('times new roman', 20, 'bold'))
    deleteIDLabel.grid(row=2, column=0)
    deleteIDEntry=Entry(window3, font=('times new roman', 20, 'bold'),text=patient_ID)
    deleteIDEntry.grid(row=2,column=1)
    print('1')
    DeleteButton=Button(window3, text='Delete', font=('times new roman', 20, 'bold'),width=15, fg='black',bg='salmon', activebackground='black', pady=30, command=Delete).grid(row=4, column=0)
    print('2')
    ExitButton=Button(window3, text='Exit', font=('times new roman',20,'bold'),width=15, fg='black',bg='palegreen1', activebackground='black', pady=30, command=window3.destroy).grid(row=4, column=1)

def updateNameAlgorithm():
    import mysql.connector as ms
    patientIDinfo = patient_ID.get()
    nameInfo = name1.get()
    if (name1 == ""):
        mb.showerror('Insert Status', 'Data is required!')
    else:
        mydb = ms.connect(host="localhost", user= "root", passwd = "!@#$Belz4ane", database = "patient") 
        cur = mydb.cursor()
        sql3 = "update patient_data set patient_name = %s where patient_ID = %s"
        val3 = (nameInfo, patientIDinfo)
        cur.execute(sql3, val3)
        mydb.commit()
        mb.showinfo("Insert Status", 'Data is updated!', parent=window5)

def updateName():
    global window5
    window5=Toplevel(window4)
    global name1
    name1 = StringVar()
    updateNameLabel=Label(window5, text='Enter the new name: ', font=('times new roman', 20, 'bold')).grid(row=1, column=0)
    updateNameEntry=Entry(window5, textvariable = name1, font=('times new roman', 20, 'bold')).grid(row=1, column=2)
    updateNameButton=Button(window5, text='Update', font=('times new roman', 20, 'bold'),width=15, fg='black',bg='palegreen2', activebackground='black', activeforeground='white',pady=30, command=updateNameAlgorithm).grid(row=4, column=0)
    ExitButton=Button(window5, text='Exit', font=('times new roman',20,'bold'), command=window5.destroy).grid(row=4, column=1)

def updateGenderAlgorithm():
    import mysql.connector as ms
    patientIDinfo = patient_ID.get()
    genderInfo = gender1.get()
    if (gender1 == ""):
        mb.showerror('Insert Status', 'Data is required!')
    else:
        mydb = ms.connect(host="localhost", user= "root", passwd = "!@#$Belz4ane", database = "patient") 
        cur = mydb.cursor()
        sql3 = "update patient_data set patient_gender = %s where patient_ID = %s"
        val3 = (genderInfo, patientIDinfo)
        cur.execute(sql3, val3)
        mydb.commit()
        mb.showinfo("Insert Status", 'Data is updated!', parent=window5)


def updateGender():
    global window5
    window5=Toplevel(window4)
    import mysql.connector as ms
    patientIDinfo = patient_ID.get()
    global gender1
       
    gender1 = StringVar()
    genderInfo = gender1.get()
    updateGenderLabel=Label(window5, text='Enter the new gender', font=('times new roman', 20, 'bold')).grid(row=1, column=0)
    updateGenderEntry=Entry(window5, textvariable = gender1, font=('times new roman', 20, 'bold')).grid(row=1, column=1)
    updateGenderButton=Button(window5, text='Update', font=('times new roman', 20, 'bold'),width=15, fg='black',bg='palegreen2', activebackground='black', activeforeground='white',pady=30, command=updateGenderAlgorithm).grid(row=2, column=0)
    ExitButton=Button(window5, text='Exit', font=('times new roman',20,'bold'), command=window5.destroy).grid(row=2, column=1).grid(row=2, column=1)
   
    
def updateWeightAlgorithm():
    import mysql.connector as ms
    patientIDinfo = patient_ID.get()
    weightInfo = weight1.get()
    if (weight1 == ""):
        mb.showerror('Insert Status', 'Data is required!')
    else:
        mydb = ms.connect(host="localhost", user= "root", passwd = "!@#$Belz4ane", database = "patient") 
        cur = mydb.cursor()
        sql3 = "update patient_data set weight = %s where patient_ID = %s"
        val3 = (weightInfo, patientIDinfo)
        cur.execute(sql3, val3)
        mydb.commit()
        mb.showinfo("Insert Status", 'Data is updated!', parent=window5)

def updateWeight():
    global window5
    window5=Toplevel(window4)
    import mysql.connector as ms
    patientIDinfo = patient_ID.get()
    global weight1
       
    weight1 = StringVar()
    weightInfo = weight1.get()
    updateWeightLabel=Label(window5, text='Enter the new weight', font=('times new roman', 20, 'bold')).grid(row=1, column=0)
    updateWeightEntry=Entry(window5, textvariable = weight1, font=('times new roman', 20, 'bold')).grid(row=1, column=1)
    updateWeightButton=Button(window5, text='Update', font=('times new roman', 20, 'bold'), width=15, fg='black',bg='palegreen2', activebackground='black', activeforeground='white',pady=30, command=updateWeightAlgorithm).grid(row=2, column=0)
    ExitButton=Button(window5, text='Exit', font=('times new roman',20,'bold'), command=window5.destroy).grid(row=2, column=1)

def updateHeightAlgorithm():
    import mysql.connector as ms
    patientIDinfo = patient_ID.get()
    heightInfo = height1.get()
    if (height1 == ""):
        mb.showerror('Insert Status', 'Data is required!')
    else:
        mydb = ms.connect(host="localhost", user= "root", passwd = "!@#$Belz4ane", database = "patient") 
        cur = mydb.cursor()
        sql3 = "update patient_data set height = %s where patient_ID = %s"
        val3 = (heightInfo, patientIDinfo)
        cur.execute(sql3, val3)
        mydb.commit()
        mb.showinfo("Insert Status", 'Data is updated!', parent=window5)

def updateHeight():
    global window5
    window5=Toplevel(window4)
    import mysql.connector as ms
    patientIDinfo = patient_ID.get()
    global height1
       
    height1 = StringVar()
    heightInfo = height1.get()
    updateHeightLabel=Label(window5, text='Enter the new height', font=('times new roman', 20, 'bold')).grid(row=1, column=0)
    updateHeightEntry=Entry(window5, textvariable = height1, font=('times new roman', 20, 'bold')).grid(row=1, column=1)
    updateheightButton=Button(window5, text='Update', font=('times new roman', 20, 'bold'),width=15, fg='black',bg='palegreen2', activebackground='black', activeforeground='white',pady=30, command=updateHeightAlgorithm).grid(row=2, column=0)
    ExitButton=Button(window5, text='Exit', font=('times new roman',20,'bold'),width=15, fg='black',bg='salmon', activebackground='black', pady=30, command=window5.destroy).grid(row=2, column=1)

def Update():
    global window4
    window4=Toplevel(addWindow)
    global patient_ID
    patient_ID=StringVar()
    updateIDLabel=Label(window4, text='Enter ID', font=('times new roman', 20, 'bold'))
    updateIDLabel.grid(row=2, column=0)
    updateIDEntry=Entry(window4, font=('times new roman', 20, 'bold'),text=patient_ID)
    updateIDEntry.grid(row=2,column=1)
    QuestionLabel=Label(window4, text='What would you like to update?', font=('times new roman', 20, 'bold')).grid(row=4,column=0)
    UpdateButton1=Button(window4, text='Patient Name', font=('times new roman', 20, 'bold'),width=15, fg='black',bg='lightskyblue', activebackground='black', activeforeground='white',pady=30, command=updateName).grid(row=5, column=0)
    UpdateButton2=Button(window4, text='Patient Gender', font=('times new roman', 20, 'bold'),width=15, fg='black',bg='royalblue', activebackground='black', pady=30, command=updateGender).grid(row=5, column=1)
    UpdateButton3=Button(window4, text='Patient Height', font=('times new roman', 20, 'bold'),width=15, fg='black',bg='lavenderblush', activebackground='black', pady=30, command=updateHeight).grid(row=6, column=0)
    UpdateButton4=Button(window4, text='Patient Weight', font=('times new roman', 20, 'bold'),width=15, fg='black',bg='honeydew3', activebackground='black', pady=30, command=updateWeight).grid(row=6, column=1)
    UpdateButton5=Button(window4, text='Exit', font=('times new roman', 20, 'bold'), command=window4.destroy).grid(row=7, column=0)

def showd():
    import mysql.connector as ms
    from tkinter import messagebox as mb
    global patient_name
    global patient_ID
    global patient_gender
    global height
    global weight
    ID_info=patient_ID.get()
    if ID_info=="":
        mb.showerror("Insert status","ID is required",parent=window8)
    else:
        mydb=ms.connect(host="localhost",user="root",passwd="!@#$Belz4ane",database="patient")
        cur=mydb.cursor()
        cur.execute("select* from patient_data where patient_ID=%s",(ID_info,))
        res=cur.fetchall()
        count=cur.rowcount
        if count==0:
            mb.showerror("Error","No such Id Is Present",parent=window8)
        else:
            for x in res:
                patient_name=x[0]
                patient_ID=x[1]
                patient_gender=x[2]
                height=x[3]
                weight=x[4]
        
            
            Label(window8,text="Name",font=('arial',19,'bold'),fg='white',bg='blue').place(x=100,y=250)
            Label(window8,text=patient_name,font=("arial",19,'bold'),bg='white',fg='red').place(x=200,y=250)
            Label(window8,text='ID',font=('arial',19,'bold'),fg='white',bg='blue').place(x=100,y=300)
            Label(window8,text=patient_ID,font=('arial',19,'bold'),fg='red',bg='white').place(x=200,y=300)
            Label(window8,text="Gender",font=('arial',19,'bold'),fg='white',bg='blue').place(x=100,y=350)
            Label(window8,text=patient_gender,font=("arial",19,'bold'),bg='white',fg='red').place(x=200,y=350)
            Label(window8,text="Height",font=('arial',19,'bold'),fg='white',bg='blue').place(x=100,y=400)
            Label(window8,text=height,font=("arial",19,'bold'),bg='white',fg='red').place(x=200,y=400)
            Label(window8,text="Weight",font=('arial',19,'bold'),fg='white',bg='blue').place(x=100,y=450)
            Label(window8,text=weight,font=("arial",19,'bold'),bg='white',fg='red').place(x=200,y=450)
            Button(window8,text="Back",font=("arial",19,"bold"),command=window8.destroy,bg='purple',fg='orange').place(x=250,y=150)
              
    

def showID():
    global window8
    
    window8=Toplevel(addWindow)
    window8.configure(background="sky blue") 
    window8.geometry("700x650")
    global patient_ID
    patient_ID=StringVar()
    Label(window8,text="Enter your ID ",font=("arial",19,"bold"),bg="green",fg="yellow").place(x=30,y=50)
    Entry(window8,textvariable=patient_ID,font=("arial",19,"bold")).place(x=250,y=50)
    Button(window8,text="SHOW",command=showd,fg="purple",bg="orange",font=("arial",19,"bold")).place(x=100,y=150)


def choose():
    global window7
    window7=Toplevel(addWindow)
    Label(window7,text='Choose the option',font=("arial",19,"bold"),width=15,bg='blue',fg='white').grid(row=1,column=1)
    Button(window7,text='All the data',font=("arial",19,"bold"),width=15,command=showInTable,fg='yellow',bg='sky blue').grid(row=10,column=1)
    Button(window7,text='On the basis of ID',command=showID,font=("arial",19,'bold'),width=15, fg='yellow',bg='sky blue').grid(row=11,column=1)
    Button(window7,text="Back",command=window7.destroy,bg='red',fg='white',width=15,font=('arial',19,'bold')).grid(row=3,column=1)



def showInTable():
    import mysql.connector as ms
    from tkinter import messagebox as mb
    from tkinter import ttk        
    mydb=ms.connect(host='localhost',user='root',passwd='!@#$Belz4ane',database='patient')
    cur=mydb.cursor()
    print('1')
    cur.execute("select * from patient_data",())
    print('2')
    res2=cur.fetchall()
    count=cur.rowcount
    if count==0:
        mb.showerror("Error","No data to Present",parent=window7)
    else:
        frame=Frame(window7)
        frame.grid(row=40,column=2)
        tv1=ttk.Treeview(frame,columns=(1,2,3,4,5),show='headings',height='5')
        tv1.pack()
        tv1.column(1,width=100)
        tv1.heading(1,text='Name')
        tv1.heading(2,text='ID')
        tv1.heading(3,text='Gender')
        tv1.heading(4,text='Height')
        tv1.heading(5,text='Weight')
        for i in res2:
            tv1.insert('','end',values=i)

    
window.mainloop()