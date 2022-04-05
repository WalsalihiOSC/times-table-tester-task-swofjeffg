from tkinter import *
from random import *

class App:
    def __init__(self, parent):
        self.parent = parent
        self.given_answer = IntVar()
        self.widgets()
        self.next()
        
    def widgets(self):
        paddings = {'padx': 5, 'pady': 5}
        
        super_frame = Frame(self.parent)
        super_frame.place(relx=.5, rely=.5, anchor=CENTER)
        
        self.question = Label(super_frame, **paddings, text="Click next")
        self.answer = Entry(super_frame, textvariable=self.given_answer)
        self.check_button = Button(super_frame, **paddings, text="Check answer", command=self.check)
        self.next_button = Button(super_frame, **paddings, text="Next", command=self.next)
        
        self.question.grid(row=0, column=0)
        self.answer.grid(row=0, column=1)
        self.check_button.grid(row=1, column=0)
        self.next_button.grid(row=1, column=1)
    
    def next(self):
        self.q = Generator()
        self.question['text'] = self.q.equation()
        self.answer.delete(0, END)
        self.next_button['state'] = DISABLED
        self.check_button['state'] = NORMAL
    
    def check(self):
        try:
            if self.given_answer.get() == (self.q.x * self.q.y):
                self.question['text'] = f'Correct!'
            else:
                self.question['text'] = f'Incorrect, answer was\n{self.q.x*self.q.y}'
            self.next_button['state'] = NORMAL
            self.check_button['state'] = DISABLED
        except:
            self.question['text'] = self.q.equation()
        
class Generator:
    def __init__(self):
        self.x, self.y = randint(-1, 12), randint(-1, 12)
    
    def equation(self):
        return f'{self.x} * {self.y} = ?'
        

if __name__ == '__main__':
    root = Tk()
    root.title("Times Table Tester")
    root.geometry("250x150")
    App(root)
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()