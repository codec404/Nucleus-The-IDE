from tkinter import *
from tkinter.filedialog import asksaveasfilename , askopenfilename
import subprocess
from PIL import ImageTk, Image

compiler = Tk()
compiler.title('Nucleus')
filePath = ''
saveImage = Image.open('220-2201567_png-file-save-icon-vector-png-transparent-png.png')
resize_image = saveImage.resize((13, 13))
img = ImageTk.PhotoImage(resize_image)

openImage = Image.open('png-clipart-file-manager-computer-icons-file-explorer-android-android-blue-rectangle-thumbnail.png')
getImgResized = openImage.resize((13, 13))
img1 = ImageTk.PhotoImage(getImgResized)

def setFilePath(path):
    global filePath
    filePath = path

def OpenFile():
    try:
        path = askopenfilename(filetypes=[('Python Files(*.py)','*.py')])
        with open(path , 'r') as file:
            code = file.read()
            editor.delete('1.0' , END)
            editor.insert('1.0' , code)
            setFilePath(path)
    except Exception as e:
        pass

def saveAs():
    try:
        if filePath == '':
            path = asksaveasfilename(filetypes=[('Python Files(*.py)' , '*.py')])
        else:
            path = filePath
        with open(path , 'w') as file:
            code = editor.get('1.0' , END)
            file.write(code)
            setFilePath(path)
    except Exception as e:
        pass

def run():
    try:
        if filePath == '':
            prompt = Toplevel()
            text = Label(prompt , text = 'Please Save Your Code')
            text.pack()
            return
        command = f'python {filePath}'
        process = subprocess.Popen(command , stdout = subprocess.PIPE ,stderr=subprocess.PIPE, shell = True)
        out , error = process.communicate()
        output.delete('1.0',END)
        output.insert('1.0' , out)
        output.insert('1.0', error)
    except Exception as e:
        pass

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0 , font=('MV Boli',11),background="#26242f")
file_menu.add_command(label='Open' ,foreground= 'white', command=OpenFile , image=img1,compound='left')
file_menu.add_command(label='Save', foreground='white' , command=saveAs , image = img , compound='left')
file_menu.add_command(label='Save As', foreground='white' , command= saveAs)
file_menu.add_separator()
file_menu.add_command(label='Exit', foreground='white' , command=exit)
menu_bar.add_cascade(label='File',menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0 , font=('MV Boli',11) , background="#26242f")
run_bar.add_command(label='Run',foreground='white' , command=run)
menu_bar.add_cascade(label='Run',menu=run_bar)

compiler.config(menu = menu_bar)
editor = Text(height = 20,width=176,foreground = '#00FF00',background="#26242f" , font=("Calibri",15))
editor.configure(insertbackground="#00ab41")
editor.pack()

output = Text(height = 15,width=176,foreground = '#00FF00',background="#26242f",font=("Calibri",15))
output.configure(insertbackground="#00ab41")
output.pack()
compiler.mainloop()
