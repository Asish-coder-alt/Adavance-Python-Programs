from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Marvel's Plaza")

root.geometry('500x500+0+0')
root.configure(background='sky blue')

def confirm_login():
    email = email_entry.get()
    password = password_entry.get()

    if email == 'giet@gmail.com' and password == 'giet123':
        messagebox.showinfo("Greetings","Login successful")
    else:
        messagebox.showerror("Login failed", "Invalid email or password")

# image
img = Image.open("marvel.png")
resize_img = img.resize((100,70))
img = ImageTk.PhotoImage(resize_img)
img_label = Label(root,image = img)
img_label.pack(pady=10,padx=20)

# text label
text_label = Label(root,text="Marvel's Plaza",font=('Arial', 18,'bold'),bg="#3BD478",fg='white')
text_label.pack(pady=10,padx=20)

email_label = Label(root,text="Email",font=('Arial', 18,'bold'),bg="#45A836",fg='white')
email_label.pack(pady=(20,5))

email_entry = Entry(root,font=('Arial', 18,'bold'),fg='white',bg='grey')
email_entry.pack(pady=(5,10))

password_label = Label(root,text="Password",font=('Arial', 18,'bold'),bg="#00A323",fg='white')
password_label.pack(pady=(20,5))

password_entry = Entry(root,font=('Arial', 18,'bold'),fg='white',bg='grey')
password_entry.pack(pady=(5,10))

login_btn = Button(root,text="Login",font=('Arial', 18,'bold'),bg="#21B400",fg='white',command=confirm_login)
login_btn.pack(pady=(5,10))

root.mainloop()