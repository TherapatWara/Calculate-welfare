from tkinter import *
import csv


filepath = 'welfare.csv'

def ReadCSV():
    lst_main =[]
    with open(filepath,'r',encoding ='utf-8') as outfile:        
        reader = csv.reader(outfile)
        lst_main = list(reader)        
        outfile.close()        
    return lst_main

def Register ():    
    def reginput():
        try:                
            def calyear(year):
                old = 2021-year
                if old >= 80 :
                    moneyget = 1000
                else:
                    if old >= 70 :
                        moneyget = 800
                    else:
                        if old >= 60 :
                            moneyget = 600
                        else:
                            moneyget = 0
                            
                return moneyget
            
            lst_main = ReadCSV()

            lst_add = []
            inputID = str(ent_1.get())
            inputname = str(ent_2.get())
            inputday = int(ent_3.get())
            inputcountry = str(ent_5.get())
            money_welfare = calyear(inputday)
            lst_add.append(str(inputID))
            lst_add.append(str(inputname))
            lst_add.append(int(inputday))
            lst_add.append(str(inputcountry))
            lst_add.append(int(money_welfare))

            lst_main.append(lst_add)            

            print(lst_main)
            
            with open(filepath,'w',encoding ='utf-8',newline="") as outfile:
                writer = csv.writer(outfile)
                writer.writerows(lst_main)
                print("Write Success.")
            
            mywin1.destroy()
        except Exception as e:
            print(e)
            mywin1.destroy()
              
    mywin1 = Tk()
    mywin1.title('Welfare for elderly')
    mywin1.minsize(295,190)
    lb1 = Label(mywin1,text='Sign Up',font = 'Helvetica 18 bold ').grid(pady=10,columnspan=12)

    lb_name = Label(mywin1,text='ID Card :',font ='10').grid(row=1,padx=40)
    ent_1 = Entry(mywin1,width=20)
    ent_1.grid(row=1,column=1,pady=5)

    lb_date = Label(mywin1,text='Name :',font ='10').grid(row=2)
    ent_2 = Entry(mywin1,width=20)
    ent_2.grid(row=2,column=1,pady=5)

    lb_ID = Label(mywin1,text='Birth Year :',font ='10').grid(row=3)
    ent_3 = Entry(mywin1,width=20)
    ent_3.grid(row=3,column=1,pady=5)

    lb_country = Label(mywin1,text='County :',font ='10').grid(row=4)
    ent_5 = Entry(mywin1,width=20)
    ent_5.grid(row=4,column=1,pady=5)

    btOK = Button(mywin1,text='Close',command=mywin1.destroy,width=10)
    btOK.grid(row=6,pady=30,column=1)
    
    btoff = Button(mywin1,text='Sign Up',command=reginput,width=10).grid(row=6,column=0)    
    mywin1.mainloop()

def Login(idCard,loginLabelStr):    
    loginSuccess=False    
    lst_main = ReadCSV()
    loginLabelStr.set("")

    selectData =[]
    for data in lst_main:
        if data[0]==idCard:
            selectData =data
            loginSuccess=True
            break

    if loginSuccess :
        print("Login Success")
        ViewData(selectData)
    else:
        print("Login Failed")
        loginLabelStr.set("Login Failed")

def ViewData(selectData):
    print(selectData)

    mywin1 = Tk()
    mywin1.title('Welfare for elderly')
    mywin1.minsize(295,190)
    lb1 = Label(mywin1,text='Information',font = 'Helvetica 18 bold ').grid(pady=10,columnspan=12)

    idCard = StringVar()
    memberName = StringVar()
    memberDate = StringVar()
    memberCountry = StringVar()
    memberWelfare = StringVar()

    lb_name = Label(mywin1,text='ID Card :',font ='10').grid(row=1,padx=40)
    ent_1 = Entry(mywin1,textvariable=idCard ,width=20)
    ent_1.insert(0,selectData[0])
    ent_1.grid(row=1,column=1,pady=5)

    lb_date = Label(mywin1,text='Name :',font ='10').grid(row=2)
    ent_2 = Entry(mywin1,textvariable=memberName,width=20)
    ent_2.insert(0,selectData[1])
    ent_2.grid(row=2,column=1,pady=5)

    lb_ID = Label(mywin1,text='Birth Year :',font ='10').grid(row=3)
    ent_3 = Entry(mywin1,textvariable=memberDate,width=20)
    ent_3.insert(0,selectData[2])
    ent_3.grid(row=3,column=1,pady=5)

    lb_country = Label(mywin1,text='County :',font ='10').grid(row=4)
    ent_5 = Entry(mywin1,textvariable=memberCountry,width=20)
    ent_5.insert(0,selectData[3])
    ent_5.grid(row=4,column=1,pady=5)

    lb_welfare = Label(mywin1,text='Welfare :',font ='10').grid(row=5)
    ent_6 = Entry(mywin1,textvariable=memberWelfare,width=20)
    ent_6.insert(0,selectData[4])
    ent_6.grid(row=5,column=1,pady=5)

    btOK = Button(mywin1,text='Close',command= mywin1.destroy,width=10)
    btOK.grid(row=7,pady=30,column=1)

    mywin1.mainloop()
        
if __name__== '__main__':

    ReadCSV()

    mywin = Tk()
    mywin.title('Welfare for elderly')
    mywin.minsize(275,250)
            
    myinput= StringVar()
    loginLabelStr = StringVar()
            
    lb1 = Label(mywin,text='Login',font = 'Helvetica 18 bold ').grid(pady=10,columnspan=12)
    lb2 = Label(mywin,text='  ID Card  :',font ='10',width=12).grid(row=1,padx=10)
    
    inp1 = Entry(mywin,textvariable=myinput).grid(row=1,column=1,pady=5)
    lbLogin = Label(mywin,textvariable=loginLabelStr,font ='10',fg='red',anchor=CENTER).grid(row=2,padx=10,columnspan=12)

    btOK = Button(mywin,text='Login', font='Tahoma', bg='#FFFF00',fg='blue',command= lambda: Login(myinput.get(),loginLabelStr),width=10).grid(row=20,pady=30,column=1)
    btoff = Button(mywin,text='Sign Up',font='Tahoma', bg='#00B2EE',fg='black',command=Register,width=10).grid(row=20,column=0) 
    mywin.mainloop()
