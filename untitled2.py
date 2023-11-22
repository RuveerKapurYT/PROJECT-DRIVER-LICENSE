from tkinter import*
root= Tk()

root.title("Driver's License")
root.geometry("600x800")

root.configure(bg="white")
canvas=Canvas(root,width=300,height=400)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0,0,300,55,fill="#1463B0")
canvas.create_rectangle(0,345,300,400,fill="#1463B0")

label_heading = canvas.create_text(150,90, font=('Times', '24', 'bold italic') ,text="Driver's License")
label_name_tag = canvas.create_text(40,165, font=('Times', '16', 'bold') ,text="Name : ")
label_grade_tag = canvas.create_text(40,205, font=('Times', '16', 'bold') ,text="Date of Birth : ")
label_subjects_tag = canvas.create_text(50,250, font=('Times', '16', 'bold') ,text="ID NO. : ")

label_name = Label(root)
label_grade = Label(root)
label_subjects = Label(root)

def myCardDetails():
    name = "Ruveer Kapur"
    print(type(name))
    DOB = 18/12/2010
    print(type(DOB))
  
    
button1 = Button(root, text = "Show my ID Card", command=myCardDetails)
 
button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_grade_window = canvas.create_window(90, 205, anchor=CENTER, window=label_grade)
label_subjects_window = canvas.create_window(155, 252, anchor=CENTER, window=label_subjects)
canvas.pack()    

root.mainloop()



