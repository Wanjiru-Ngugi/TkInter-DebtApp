# --------------------
# @author: Wanjiru
# 2019
# --------------------
from tkinter import *
from tkinter import ttk

class Debts:
    def __init__(self, root):
        root.title('YOU OWE ME!!!')
        root.geometry("400x250")
        root.resizable(0,0)
        count = 0
        
        self.listOfItems = ["Spa Date", "Birthday Getaway", "Visit Shags", "Phone","Samsung Gear Watch"]
        self.tempVars = ["temp" + str(count) for count in range(0, 5)]
        self.label = ttk.Label(root, text='!!!YOU OWE ME!!!\n No more dodging your debts!')
        self.label.grid(row=0, column=2, columnspan=4)
        self.label.config(justify= 'center', font=('consolas', 17, 'bold'), foreground= 'red')

        while count < 5:
            self.tempVars[count] = ttk.Label(root, text= '', justify= 'left')
            count += 1
            
        self.addBtn = ttk.Button(root, text='Click Me!', command=self.addItem)
        self.style = ttk.Style()
        self.style.configure('TButton', background='blue', foreground= 'blue')
        self.addBtn.grid(row=9,column=2, columnspan=4)
        
    def addItem(self):        
        count = 0    
        while count < 5:            
            self.addBtn["text"] = 'NOW PAY UP!!'
            self.tempVars[count].config(text= str(count+1) + ": " + self.listOfItems[count], justify= 'left')
            self.tempVars[count].config(font=('consolas', 11))
            self.tempVars[count].grid(row=3+count, column=2, columnspan=4)
            count += 1

    
def main():
    root = Tk()
    myApp = Debts(root)
    root.mainloop()

if __name__ == "__main__": main()