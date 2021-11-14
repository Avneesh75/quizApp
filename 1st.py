from tkinter import *
from PIL import Image,ImageTk
from tkinter .ttk import Combobox,Treeview,Style,Scrollbar
from tkinter import messagebox
from tkinter import filedialog
import sqlite3 as sql
import random
from datetime import datetime
from tkinter import ttk


#datbase start
try:
    con=sql.connect(database="quiz.sqlite")
    cur=con.cursor()
    cur.execute("create table user_test(username text,marks text,day date)")
    cur.execute("create table users(username text primary key,password text,confirm password text)")
    cur.execute("create table question(ques_id int auto_increment primary key ,ques_title text,option1 text,option2 text,option3 text,option4 text,answer text)")
    con.commit()
    con.close()
    print("table created")
except:
    pass
#database End

#Main window start
win=Tk()
win.state("zoomed")
win.resizable(width=False,height=False)
img=Image.open("images/2nd.jpg")
img=img.resize((1550,850))
tk_img=ImageTk.PhotoImage(img)

l=Label(win,image=tk_img)
l.place(x=0,y=0)

lbl_title=Label(win,text="Python Quiz Application",font=('Arial',50,'bold','underline'))
lbl_title.pack()

# main window End


#login window start

login_img=Image.open(("images/login.png")).resize((150,70))
login_imgtk=ImageTk.PhotoImage(login_img)

reset_img=Image.open(("images/reset.png")).resize((150,70))
reset_imgtk=ImageTk.PhotoImage(reset_img)

back_img=Image.open(("images/back.png")).resize((80,40))
back_imgtk=ImageTk.PhotoImage(back_img)

logout_img=Image.open(("images/logout.png")).resize((170,80))
logout_imgtk=ImageTk.PhotoImage(logout_img)


def login_frame():

    frm=Frame(win,highlightbackground='gray',highlightthickness=3)
    frm.configure(bg="powder blue")
    frm.place(relx=.28,rely=.2,width=700,height=500) # frame destroy krne ke liye login frame m likenge

    def reset(event):
        entry_user.delete(0,"end")
        entry_pass.delete(0,"end")
        type_cb.current(0)
        entry_user.focus()

    def newuser():
        frm.destroy()
        newuser_frame()   

    def login(event):
        u=entry_user.get()
        p=entry_pass.get()
        if(len(u)==0 or len(p)==0):
            messagebox.showerror("Error","Please fill both details")
        else:
            t=type_cb.get()
            if(t=="user"):
                con=sql.connect(database="quiz.sqlite")
                cur=con.cursor()
                cur.execute("select * from users where username=? and password=? ",(u,p))
                global user
                user=cur.fetchone()
                if(user==None):
                    messagebox.showerror("error","Invalid Username & Password")
                else:
                    frm.destroy()
                    welcome_userframe()

            else:

                if(u=='Avneesh' and p=='yadav12345'):
                    messagebox.showinfo("","Valid Admin")
                    frm.destroy()
                    Welcome_adminframe()
                else:
                    messagebox.showerror("Error","Invalid Admin")

    lbl_user=Label(frm,text="Username : ",fg='blue',font=('Arial',20),bg="powder blue")
    lbl_user.place(relx=.1,rely=.1)

    lbl_pass=Label(frm,text="Password : ",fg='blue',font=('Arial',20),bg="powder blue")
    lbl_pass.place(relx=.1,rely=.25)

    lbl_type=Label(frm,text="Type : ",fg='blue',font=('Arial',20),bg="powder blue")
    lbl_type.place(relx=.1,rely=.4)

    entry_user=Entry(frm,font=('Arial',20),bd=5)
    entry_user.place(relx=.45,rely=.1)
    entry_user.focus()

    entry_pass=Entry(frm,font=('Arial',20),bd=5,show="*")
    entry_pass.place(relx=.45,rely=.25)

    type_cb=Combobox(frm,font=('Arial',20),values=['user','admin'])
    type_cb.current(0)
    type_cb.place(relx=.45, rely=.4)


    login_btn=Label(frm,image=login_imgtk,bg='powder blue')
    login_btn.place(relx=.2,rely=.55)
    login_btn.bind("<Button>",login)
    
    reset_btn=Label(frm,image=reset_imgtk,bg='powder blue')
    reset_btn.place(relx=.6,rely=.55)
    reset_btn.bind("<Button>",reset)

    reg_btn=Button(frm,text="New User",font=('Arial',20),bd=5,width=12,command=newuser)
    reg_btn.place(relx=.38,rely=.75)

#new user frame start
def newuser_frame():
    frm=Frame(win,highlightbackground='gray',highlightthickness=3)
    frm.configure(bg='powder blue')
    frm.place(relx=.28,rely=.2,width=700,height=400)

    def back(event):
        frm.destroy()
        login_frame()

    def register():
        u=entry_user.get()
        p=entry_pass.get()
        cp=entry_passconfrm.get()
        if(p==cp):
           pass

        else:
            messagebox.showerror("error","Password and confirm Password Not same")
            return
        try:
            con=sql.connect(database="quiz.sqlite")
            cur=con.cursor()
            cur.execute("insert into users values(?,?,?)",(u,p,cp))
            con.commit()
            messagebox.showinfo("Sucess","Account Created")
            frm.destroy()
            login_frame()
        
        except:
            messagebox.showerror("Error","User name already exixts")
        con.close()


    lbl_user=Label(frm,text="Username : ",fg='blue',font=('Arial',20),bg='powder blue')
    lbl_user.place(relx=.1,rely=.1)

    lbl_pass=Label(frm,text="Password : ",fg='blue',font=('Arial',20),bg='powder blue')
    lbl_pass.place(relx=.1,rely=.25)

    lbl_passconfrm=Label(frm,text="Confirm Password : ",fg='blue',font=('Arial',20),bg='powder blue')
    lbl_passconfrm.place(relx=.1,rely=.4)

    
    entry_user=Entry(frm,font=('Arial',20),bd=5)
    entry_user.place(relx=.45,rely=.1)
    entry_user.focus()

    entry_pass=Entry(frm,font=('Arial',20),bd=5,show="*")
    entry_pass.place(relx=.45,rely=.25)

    entry_passconfrm=Entry(frm,font=('Arial',20),bd=5,show="*")
    entry_passconfrm.place(relx=.45,rely=.4)


    reg_btn=Button(frm,text="Register",font=('Arial',20),bd=5,width=12,command=register)
    reg_btn.place(relx=.36,rely=.65)

    back_btn=Label(frm,image=back_imgtk,bg='powder blue')
    back_btn.place(relx=0,rely=0)
    back_btn.bind("<Button>",back)


#new user frame End

#Welcome Admin frame Start
def Welcome_adminframe():
    frm=Frame(win,highlightbackground='gray',highlightthickness=3)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.1,relwidth=1,relheight=1) 

    def logout(event):
        frm.destroy()
        login_frame()

    def set_question():
        frm.destroy()
        set_question_frame()

    def view_ques():
        frm.destroy()
        view_ques_frame()

    def view_users():
        frm.destroy()
        view_users_frame()

    def set_question_file():
        file=open(filedialog.askopenfilename(),"r",encoding="utf8")
        print(file)
        text=file.read()
       
        lines=text.split("\n")
        
        for i in range (0,len(lines),7):
            QUES=lines[i:i+6]
            con1=sql.connect(database="quiz.sqlite")
            cur1=con1.cursor()
            cur1.execute("Select max(ques_id) from question")
            qid=cur1.fetchone()[0]
            qid+=1
            con1.close()
            con=sql.connect(database="quiz.sqlite")
            cur=con.cursor()
            
            cur.execute("insert into question values(?,?,?,?,?,?,?)",(qid,QUES[0],QUES[1],QUES[2],QUES[3],QUES[4],QUES[5]))
            con.commit()
            con.close()
        messagebox.showinfo("Sucess","Question Inserted")

    wel_label=Label(frm,font=('Arial',20),text="WELCOME-ADMIN",bg='powder blue')
    wel_label.place(relx=0,rely=0)

    logout_btn=Label(frm,image=logout_imgtk,bg='powder blue')
    logout_btn.place(relx=.89,rely=0)
    logout_btn.bind("<Button>",logout)

    ques_btn=Button(frm,text="Set Question",font=('Arial',20),bd=5,width=18,command=set_question)
    ques_btn.place(relx=.4,rely=.1)

    ques_btn2=Button(frm,text="Upload Questions File",font=('Arial',20),bd=5,width=18,command=set_question_file)
    ques_btn2.place(relx=.4,rely=.25)

    view_btn=Button(frm,text="View User",font=('Arial',20),bd=5,width=18,command=view_users)
    view_btn.place(relx=.4,rely=.4)

    view_ques_btn=Button(frm,text="View Questions",font=('Arial',20),bd=5,width=18,command=view_ques)
    view_ques_btn.place(relx=.4,rely=.55)


#new Admin frame End

def set_question_frame():
    frm=Frame(win,highlightbackground='gray',highlightthickness=3)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.1,relwidth=1,relheight=1) 

    def logout(event):
        frm.destroy()
        login_frame()

    def back(event):
        frm.destroy()
        Welcome_adminframe()

    def setques_db():
        ques=entry_ques.get()
        op1=entry_op1.get()
        op2=entry_op1.get()
        op3=entry_op1.get()
        op4=entry_op1.get()
        ans=entry_op1.get()

        con=sql.connect(database="quiz.sqlite")
        cur=con.cursor()
        cur.execute("Select max(ques_id) from question")
        qid=cur.fetchone()[0]
        qid+=1
        con.close()

        con=sql.connect(database="quiz.sqlite")
        cur=con.cursor()
        cur.execute("insert into question values(?,?,?,?,?,?,?)",(qid,ques,op1,op2,op3,op4,ans))
        con.commit()
        con.close()
        messagebox.showinfo("Succesful","Question Inserted")
        entry_ques.delete(0,"end")
        entry_op1.delete(0,"end")
        entry_op2.delete(0,"end")
        entry_op3.delete(0,"end")
        entry_op4.delete(0,"end")
        entry_ans.delete(0,"end")


    wel_label=Label(frm,font=('Arial',20),text="WELCOME-ADMIN",bg='powder blue')
    wel_label.place(relx=0,rely=0)

    logout_btn=Label(frm,image=logout_imgtk,bg='powder blue')
    logout_btn.place(relx=.89,rely=0)
    logout_btn.bind("<Button>",logout)

    back_btn=Label(frm,image=back_imgtk,bg='powder blue')
    back_btn.place(relx=0,rely=.1)
    back_btn.bind("<Button>",back)

    lbl_ques=Label(frm,text="Question : ",fg='blue',font=('Arial',20),bg="powder blue")
    lbl_ques.place(relx=.3,rely=.1)

    lbl_op1=Label(frm,text="Option-1 : ",fg='blue',font=('Arial',20),bg="powder blue")
    lbl_op1.place(relx=.3,rely=.2)

    lbl_op2=Label(frm,text="Option-2 : ",fg='blue',font=('Arial',20),bg="powder blue")
    lbl_op2.place(relx=.3,rely=.3)

    lbl_op3=Label(frm,text="Option-3 : ",fg='blue',font=('Arial',20),bg="powder blue")
    lbl_op3.place(relx=.3,rely=.4)

    lbl_op4=Label(frm,text="Option-4 : ",fg='blue',font=('Arial',20),bg="powder blue")
    lbl_op4.place(relx=.3,rely=.5)

    lbl_ans=Label(frm,text="Answer : ",fg='blue',font=('Arial',20),bg="powder blue")
    lbl_ans.place(relx=.3,rely=.6)

    entry_ques=Entry(frm,font=('Arial',20),bd=5)
    entry_ques.place(relx=.45,rely=.1)
    
    entry_op1=Entry(frm,font=('Arial',20),bd=5)
    entry_op1.place(relx=.45,rely=.2)

    entry_op2=Entry(frm,font=('Arial',20),bd=5)
    entry_op2.place(relx=.45,rely=.3)

    entry_op3=Entry(frm,font=('Arial',20),bd=5)
    entry_op3.place(relx=.45,rely=.4)

    entry_op4=Entry(frm,font=('Arial',20),bd=5)
    entry_op4.place(relx=.45,rely=.5)

    entry_ans=Entry(frm,font=('Arial',20),bd=5)
    entry_ans.place(relx=.45,rely=.6)

    sub_btn=Button(frm,text="Submit",font=('Arial',20),bd=5,width=12,command=setques_db)
    sub_btn.place(relx=.45,rely=.7)


def view_ques_frame():
    frm=Frame(win,highlightbackground='gray',highlightthickness=3)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.1,relwidth=1,relheight=1) 

    def logout(event):
        frm.destroy()
        login_frame()

    def back(event):
        frm.destroy()
        Welcome_adminframe()

    def delete_ques():
        rowid=tv.focus()
        row=tv.item(rowid,'values')
        if(len(row)==0):
            messagebox.showerror("Delete","Please select a Question")
        else:
            con=sql.connect(database="quiz.sqlite")
            cur=con.cursor()
            cur.execute("delete from question where ques_id=?",(row[0]))
            con.commit()
            con.close()
            messagebox.showinfo("Delete","Question Delete")
            frm.destroy()
            view_ques_frame()

    wel_label=Label(frm,font=('Arial',20),text="WELCOME-ADMIN",bg='powder blue')
    wel_label.place(relx=0,rely=0)

    logout_btn=Label(frm,image=logout_imgtk,bg='powder blue')
    logout_btn.place(relx=.89,rely=0)
    logout_btn.bind("<Button>",logout)

    back_btn=Label(frm,image=back_imgtk,bg='powder blue')
    back_btn.place(relx=0,rely=.1)
    back_btn.bind("<Button>",back)

    tv=Treeview(frm)
    tv.place(relx=.1,rely=.2,relwidth=.8,height=200)

    st=Style()
    st.configure("Treeview.Heading",font=('Arial',15,'bold'),foreground='black')

    sb=Scrollbar(frm,orient="vertical",command=tv.yview)
    sb.place(relx=.9,rely=.2,height=200)
    tv.configure(yscrollcommand=sb.set)

    tv['columns']=['1','2','3','4','5','6','7']
    tv['show']='headings'

    tv.column('1',anchor='c',stretch='no',width=50)
    tv.column('2',anchor='c',stretch='no',width=150)
    tv.column('3',anchor='c',stretch='no',width=100)
    tv.column('4',anchor='c',stretch='no',width=100)
    tv.column('5',anchor='c',stretch='no',width=100)
    tv.column('6',anchor='c',stretch='no',width=100)
    tv.column('7',anchor='c',stretch='no',width=100)

    tv.heading('1',text="Quesid")
    tv.heading('2',text="Question")
    tv.heading('3',text="Option-1")
    tv.heading('4',text="Option-2")
    tv.heading('5',text="Option-3")
    tv.heading('6',text="Option-4")
    tv.heading('7',text="Answer")

    con=sql.connect(database='quiz.sqlite')
    cur=con.cursor()
    cur.execute("select * from question")
    qcount=0
    for row in cur:
        qcount+=1
        tv.insert("","end",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

    qcount_lbl=Label(frm,text=f"Total Question:{qcount}",font=('Arial',30,'bold'),fg='blue',bg='powder blue')
    qcount_lbl.place(relx=.3,rely=.1)
    con.close()

    del_btn=Button(frm,text="Delete",font=('Arial',20,'bold'),bd=5,width=12,fg='red',command=delete_ques)
    del_btn.place(relx=.42,rely=.5)


def view_users_frame():
    frm=Frame(win,highlightbackground='gray',highlightthickness=3)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.1,relwidth=1,relheight=1)

    def logout(event):
        frm.destroy()
        login_frame()
        
    def back(event):
        frm.destroy()
        Welcome_adminframe()
    
    def delete_user():
        rowid=tv.focus()
        row=tv.item(rowid,'values')
        if(len(row)==0):
            messagebox.showerror("Delete","please select user")
        else:
            con=sql.connect(database='quiz.sqlite')
            cur=con.cursor()
            cur.execute("delete from users where username=?",(row[0],))
            con.commit()
            con.close()
            messagebox.showinfo("Delete","Selected user delete")
            frm.destroy()
            view_users_frame()
    
    wel_label=Label(frm,font=('Arial',20),text="Welcome,Admin",bg='powder blue')
    wel_label.place(relx=0,rely=0)
    

    logout_btn=Label(frm,image=logout_imgtk,bg='powder blue')
    logout_btn.place(relx=.89,rely=0)
    logout_btn.bind("<Button>",logout)
    
    back_btn=Label(frm,image=back_imgtk,bg='powder blue')
    back_btn.place(relx=0,rely=.1)
    back_btn.bind("<Button>",back)
    
    tv=Treeview(frm)
    tv.place(relx=.3,rely=.25,width=400,height=100)
    
    sb=ttk.Scrollbar(frm,orient="vertical",command=tv.yview)
    sb.place(relx=.55,rely=.25,height=100)
    tv.configure(yscrollcommand=sb.set)
    
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Arial',10,'bold'),foreground='black')
    
    tv['columns']=['1','2']
    tv['show']='headings'
    
    tv.column('1',anchor='c',width=150)
    tv.column('2',anchor='c',width=150)
   
    
    tv.heading('1',text="Username")
    tv.heading('2',text="Password")

    
    con=sql.connect(database='quiz.sqlite')
    cur=con.cursor()
    cur.execute("select * from users")
    ucount=0
    for row in cur:
        ucount+=1
        tv.insert("","end",values=(row[0],row[1]))

    total_label=Label(frm,font=('Arial',40,'bold'),text=f"Total Users:{ucount}",bg='powder blue',fg='blue')
    total_label.place(relx=.3,rely=.1)
    con.close()
    
    del_btn=Button(frm,text="Delete User",font=('Arial',20),bd=5,width=18,command=delete_user)
    del_btn.place(relx=.32,rely=.45)


def view_result_frame():
    frm=Frame(win,highlightbackground='gray',highlightthickness=3)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.1,relwidth=1,relheight=1)
    
    def back(event):
        frm.destroy()
        welcome_userframe()
    
    def logout(event):
        frm.destroy()
        login_frame()
        
     
    wel_label=Label(frm,font=('Arial',20),text=f"Welcome,{user[0]}",bg='powder blue')
    wel_label.place(relx=0,rely=0)

    logout_btn=Label(frm,image=logout_imgtk,bg='powder blue')
    logout_btn.place(relx=.89,rely=0)
    logout_btn.bind("<Button>",logout)
    
    back_btn=Label(frm,image=back_imgtk,bg='powder blue')
    back_btn.place(relx=0,rely=.1)
    back_btn.bind("<Button>",back)

    tv=Treeview(frm)
    tv.place(relx=.3,rely=.25,width=400,height=100)
    
    sb=ttk.Scrollbar(frm,orient="vertical",command=tv.yview)
    sb.place(relx=.55,rely=.25,height=100)
    tv.configure(yscrollcommand=sb.set)
    
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Arial',10,'bold'),foreground='black')
    
    tv['columns']=['1','2']
    tv['show']='headings'
    
    tv.column('1',anchor='c',width=250)
    tv.column('2',anchor='c',width=150)
   
    
    tv.heading('1',text="Date")
    tv.heading('2',text="Marks")

    
    con=sql.connect(database='quiz.sqlite')
    cur=con.cursor()
    cur.execute("select * from user_test")
    tcount=0
    for row in cur:
        tcount+=1
        tv.insert("","end",values=(row[2],row[1]))

    total_label=Label(frm,font=('Arial',40,'bold'),text=f"Total Test Taken:{tcount}",bg='powder blue',fg='blue')
    total_label.place(relx=.3,rely=.1)
    con.close()
    


def welcome_userframe():
    frm=Frame(win,highlightbackground='gray',highlightthickness=3)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.1,relwidth=1,relheight=1) 

    def logout(event):
        frm.destroy()
        login_frame()

    def change_pass():
        frm.destroy()
        change_pass_frame()

    def start_test():
        frm.destroy()
        start_test_frame()

    def view_result():
        frm.destroy()
        view_result_frame()

    wel_label=Label(frm,font=('Arial',20),text=f"WELCOME-{user[0]}",bg='powder blue')
    wel_label.place(relx=0,rely=0)

    logout_btn=Label(frm,image=logout_imgtk,bg='powder blue')
    logout_btn.place(relx=.89,rely=0)
    logout_btn.bind("<Button>",logout)

    test_btn=Button(frm,text="Start Test",font=('Arial',20),bd=5,width=18,command=start_test)
    test_btn.place(relx=.4,rely=.1)

    result_btn2=Button(frm,text="Previous Result",font=('Arial',20),bd=5,width=18,command=view_result)
    result_btn2.place(relx=.4,rely=.25)

    cp_btn=Button(frm,text="Change Password",font=('Arial',20),bd=5,width=18,command=change_pass)
    cp_btn.place(relx=.4,rely=.4)


def change_pass_frame():
    frm=Frame(win,highlightbackground='blue',highlightthickness=3)
    frm.configure(bg='powder blue')
    frm.place(relx=.2,rely=.17,width=900,height=500)

    def back(event):
        frm.destroy()
        welcome_userframe()
    
    def logout(event):
        frm.destroy()
        login_frame()

    def update():
        p=entry_ps.get()
        cp=entry_cps.get()
        if(len(p)==0 or len(cp)==0):
            messagebox.showerror("Error","please fill password and confirm password")

        else:
            if(p==cp):
                con=sql.connect(database="quiz.sqlite")
                cur=con.cursor()
                cur.execute("update users set password=? where username=?",(p,user[0]))
                con.commit()
                con.close()
                messagebox.showinfo("Update","Password Update")
                frm.destroy()
                login_frame()
            else:
                messagebox.showerror("error","Password and Confirm Password not same")

    wel_label=Label(frm,font=('Arial',20),text=f"WELCOME-{user[0]}",bg='powder blue')
    wel_label.place(relx=0,rely=0)

    logout_btn=Label(frm,image=logout_imgtk,bg='powder blue')
    logout_btn.place(relx=.8,rely=0)
    logout_btn.bind("<Button>",logout)

        
    lbl_ps=Label(frm,text="Password : ",fg='blue',font=('Arial',20),bg='powder blue')
    lbl_ps.place(relx=.1,rely=.25)

    lbl_cps=Label(frm,text="Confirm Password : ",fg='blue',font=('Arial',20),bg='powder blue')
    lbl_cps.place(relx=.1,rely=.4)

    entry_ps=Entry(frm,font=('Arial',20),bd=5,show="*")
    entry_ps.place(relx=.45,rely=.25)
    entry_ps.focus()

    entry_cps=Entry(frm,font=('Arial',20),bd=5,show="*")
    entry_cps.place(relx=.45,rely=.4)


    reg_btn=Button(frm,text="Update",font=('Arial',20,'bold'),fg='green',bd=5,width=12,command=update)
    reg_btn.place(relx=.36,rely=.65)

    back_btn=Label(frm,image=back_imgtk)
    back_btn.place(relx=0,rely=.1)
    back_btn.bind("<Button>",back)


def start_test_frame():
    frm=Frame(win,highlightbackground='gray',highlightthickness=3)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.1,relwidth=1,relheight=1)

    timer_lbl=Label(frm,font=('Arial',20,'bold'),bg='powder blue',fg='red')
    timer_lbl.place(relx=.6,rely=.1)


    def back(event):
        frm.destroy()
        welcome_userframe()

    def logout(event):
        frm.destroy()
        login_frame()

    wel_label=Label(frm,font=('Arial',20),text=f"WELCOME-{user[0]}",bg='powder blue')
    wel_label.place(relx=0,rely=.1)

    logout_btn=Label(frm,image=logout_imgtk,bg='powder blue')
    logout_btn.place(relx=.89,rely=0)
    logout_btn.bind("<Button>",logout)

    con=sql.connect(database="quiz.sqlite")
    cur=con.cursor()
    cur.execute("select * from question")
    ques_list=cur.fetchall()
  
    var=StringVar(value="yes")

    l=Label(frm,bg='powder blue',font=('Arial',20,'bold'))
    l.place(relx=.3,rely=.2)

    rb1=Radiobutton(frm,bg='powder blue',font=('Arial',15,'bold'))
    rb1.place(relx=.3,rely=.3)

    rb2=Radiobutton(frm,bg='powder blue',font=('Arial',15,'bold'))
    rb2.place(relx=.3,rely=.4)

    rb3=Radiobutton(frm,bg='powder blue',font=('Arial',15,'bold'))
    rb3.place(relx=.3,rely=.5)

    rb4=Radiobutton(frm,bg='powder blue',font=('Arial',15,'bold'))
    rb4.place(relx=.3,rely=.6)
        
    ques_sample=random.sample(ques_list,5)
    print(ques_list)
    qcount=0
    marks=0
    flag=0 #kuch bhi le lo as your wish
    def get_quest():
        nonlocal qcount,flag
        flag+=1
        question=ques_sample[qcount]
        print(question)
        qcount+=1
        ans=var.get()

        if(flag==1):
            from threading import Thread
            import time
            def timer():
                for i in range(300,-1,-1):
                    timer_lbl.configure(text=f"Remaining Time :{i//60}:{i%60}")
                    time.sleep(1)
                    if(i==0):
                        messagebox.showwarning("Timeout","Time completed")
                        submit()

            t=Thread(target=timer)
            try:
                t.start()
            except:
                pass

        def sel():
            nonlocal marks
            user_ans=var.get()
            if(question[6]==user_ans):
                marks+=1

        def submit():
            messagebox.showinfo("Test",f"Test Completed and your score:{marks}")
            con=sql.connect(database="quiz.sqlite")
            cur=con.cursor()
            day=datetime.now()
            cur.execute("insert into user_test values(?,?,?)",(user[0],marks,str(day)))
            con.commit()
            con.close()

            frm.destroy()
            welcome_userframe()
    
        l.configure(text=f"Ques:{qcount} {question[1]}")
        rb1.configure(text=question[2],variable=var,value=question[2],command=sel)
        rb2.configure(text=question[3],variable=var,value=question[3],command=sel)
        rb3.configure(text=question[4],variable=var,value=question[4],command=sel)
        rb4.configure(text=question[5],variable=var,value=question[5],command=sel)

        if(qcount<5):
            reg_btn=Button(frm,text="Next",font=('Arial',20),bd=5,width=12,command=get_quest)
            reg_btn.place(relx=.4,rely=.7)
        else:
            sub_btn=Button(frm,text="Submit",font=('Arial',20),bd=5,width=12,command=submit)
            sub_btn.place(relx=.4,rely=.7)

    get_quest()#phle call krne hogi
    back_btn=Label(frm,image=back_imgtk)
    back_btn.place(relx=0,rely=0)
    back_btn.bind("<Button>",back)

login_frame()
#login window end
win.mainloop()



