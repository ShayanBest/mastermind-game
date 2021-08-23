from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno  
from random import randint
from datetime import datetime
from DAL import *


class MainWindow():

    def __init__(self, mainWidget):
        self.main_frame = Frame(mainWidget, width=200, height=250)
        self.main_frame.grid(row=0, column=0)

        self.controler = 0

        self.main_gui()
    


    def creat_random_number(level):
        global random_num, date, len_num
        len_num = int(level)
        random_num = randint(10**(level-1) , ((10**level)-1))
        date = datetime.now()

    #region MainMenu

    def main_gui(self):
        root.title('Master Mind')

        def close_window():
            close = askyesno("Confirm","Are you sure?")
            if close:  
                root.destroy()

        self.main_label = Label(self.main_frame, text='Master Mind !',width=20, justify='center')
        self.main_label.grid(row= 0, column= 0, columnspan= 3, sticky= 'EW', ipady= 25 , ipadx= 0, padx= (20,20))

        self.level_button = Button(self.main_frame, text='Start Game', fg= 'black', bg= 'white', activeforeground= 'white', activebackground= 'black')
        self.level_button.grid(row=1, column= 0, columnspan= 3, sticky= 'EW', ipady= 10 , ipadx= 25, padx= (65,65))
        self.level_button.bind('<Button-1>', self.level_gui)
        
        self.btn_score = Button(self.main_frame, text='Score List', fg= 'black', bg= 'white', activeforeground= 'white', activebackground= 'black')
        self.btn_score.grid(row=2, column= 0, columnspan= 3, sticky= 'EW', ipady= 10 , ipadx= 25, padx= (65,65))
        self.btn_score.bind('<Button-1>', self.score_gui)

        self.btn_exit = Button(root, text= 'Exit', fg= 'black', bg= 'white', activeforeground= 'white', activebackground= 'black', command=close_window)
        self.btn_exit.grid(row= 3, column= 0, columnspan= 3, sticky= 'EW', ipady= 10 , ipadx= 25, padx= (65,65))

        self.controler = 1

        self.gui_elements = [self.main_label,
                             self.level_button,
                             self.btn_score,
                             self.btn_exit]
    #endregion

    #region levels

    def level_gui(self, event):
        self.gui_elements_remove(self.gui_elements)

        root.title('Choose Level')

        self.main_label = Label(self.main_frame, text='Choose Level :',width=20, justify='center')
        self.main_label.grid(row=0, column=0, sticky= 'EW', ipady= 25, padx= 5)

        self.digits = IntVar()
        self.scale = Scale(self.main_frame, variable = self.digits ,tickinterval=1, showvalue=0, from_=4 , to= 9 , sliderlength=20, orient = HORIZONTAL,width=20)
        self.scale.grid(row= 2, column= 0 , ipady= 10 , ipadx= 5, padx= (65,65))

        self.btn_letsgo = Button(self.main_frame, text='Let\'s Go !!!', fg= 'black', bg= 'white', activeforeground= 'white', activebackground= 'black')
        self.btn_letsgo.grid(row= 7, column= 0, columnspan= 3, sticky= 'EW', ipady= 10 , ipadx= 25, padx= (65,65))
        self.btn_letsgo.bind('<Button-1>', self.game_gui)
        

        self.btn_back = Button(self.main_frame, text='Back', fg= 'black', bg= 'white', activeforeground= 'white', activebackground= 'black')
        self.btn_back.grid(row= 8, column= 0, columnspan= 3, sticky= 'EW', ipady= 10 , ipadx= 25, padx= (65,65))
        self.btn_back.bind('<Button-1>', self.back_to_main)

        self.controler = 1

        self.gui_elements = [self.main_label,
                             self.scale,
                             self.btn_letsgo,
                             self.btn_back]

    #endregion


    #region game

    def game_gui(self, event):
        self.gui_elements_remove(self.gui_elements)
        MainWindow.creat_random_number(self.digits.get())
        
        self.game_frame = Frame(root, width=300, height=310)
        self.game_frame.grid(row=0, column=0)

        root.title('Game')

        self.main_label = Label(self.game_frame, text='Type Your Guess :', width=20 , justify='center')
        self.main_label.grid(row=0, column=0, columnspan= 3, sticky= 'EW', ipady= 10 , ipadx= 5, padx= (45,45))
        

        def check_guess():
            
            x = self.ent_guess_num.get()
            errormessage = []
             
            try:
                y = int(x)
            except:
                messagebox.showerror("Error",'Please Enter Number !!!')
                self.ent_guess_num.delete(0,END)  
                return

            if  len(x.strip())!= len_num :
                errormessage.append('Invalid number !\nEnter number with '+str(len_num)+' Digits')

            if len(errormessage)!=0:
                messagebox.showerror("Error", "\n".join(errormessage) )
                self.ent_guess_num.delete(0,END)  
                return
            x = int(x)
            
            self.answer_label = Label(self.game_frame)
            self.answer_label.grid(row=4, column=0, columnspan= 3, sticky= 'EW', ipady= 10 , ipadx= 5, padx= (65,65))

            if x > random_num :
                self.answer_label['text'] = self.ent_guess_num.get()+' > ? '
                self.ent_guess_num.delete(0,END)
            elif x < random_num :
                self.answer_label['text'] = self.ent_guess_num.get()+' < ? '
                self.ent_guess_num.delete(0,END)
            else :
                self.answer_label['text'] = self.ent_guess_num.get()+' is Correct'
                time = datetime.now() - date
                self.time_label = Label(self.game_frame, text = 'Time : '+str(time))
                self.time_label.grid(row=5, column=0, columnspan= 3, sticky= 'EW', ipady= 4, padx= 5)
                self.ent_guess_num.delete(0,END)
                self.ent_name_label = Label(self.game_frame, text = 'Enter Your Name :')
                self.ent_name_label.grid(row=6, column=0, columnspan= 3, sticky= 'EW', ipady= 10, padx= 5)
                self.ent_name = Entry(self.game_frame,justify=CENTER)
                self.ent_name.grid(row=7, column=0, columnspan= 3, sticky= 'EW', ipady= 5 , ipadx= 5, padx= (65,65))
                self.ent_guess_num.destroy()
                self.btn_check.destroy()
                self.btn_back.destroy()
                self.main_label = Label(self.game_frame, text='You Won !!!', width=20 , justify='center')
                self.main_label.grid(row=0, column=0, columnspan= 3, sticky= 'EW', ipady= 14, padx= 5)           
                self.btn_submit = Button(self.game_frame, text='Submit', fg= 'black', bg= 'white', activeforeground= 'white', activebackground= 'black' , command = lambda : self.submit(self.ent_name.get(),len_num,time) )
                self.btn_submit.grid(row=9, column=0, columnspan= 3, sticky= 'EW', ipady= 10 , ipadx= 25, padx= (65,65))


        self.ent_guess_num = Entry(self.game_frame,justify=CENTER)
        self.ent_guess_num.grid(row=1, column=0, columnspan= 3, sticky= 'EW', ipady= 5 , ipadx= 5, padx= (65,65))
        
        self.btn_check = Button(self.game_frame, text='Check Guess', fg= 'black', bg= 'white', activeforeground= 'white', activebackground= 'black', command = check_guess )
        self.btn_check.grid(row=2, column=0, columnspan= 3, sticky= 'EW', ipady= 10 , ipadx= 25, padx= (65,65))
        

        self.label_show = (self.digits.get())*' ?'
        self.label_show = Label(self.game_frame, text= self.label_show)
        self.label_show.grid(row=4, column=0, columnspan= 3, sticky= 'EW', ipady= 10 , ipadx= 5, padx= (55,55))

        self.btn_back = Button(self.game_frame, text='Exit Game', fg= 'black', bg= 'white', activeforeground= 'white', activebackground= 'black')
        self.btn_back.grid(row= 7, column= 0, columnspan= 3, sticky= 'EW', ipady= 10 , ipadx= 25, padx= (65,65))
        self.btn_back.bind('<Button-1>', self.back_to_main)

        self.controler = 2

        self.gui_elements = [self.main_label,
                             self.ent_guess_num,
                             self.btn_check,
                             self.label_show,
                             self.btn_back]

    #endregion
       
    #region scores

    def score_gui(self, event):
        self.gui_elements_remove(self.gui_elements)
        
        root.title('Scores List')

        self.main_label = Label(self.main_frame, text='Scores List :', width = 20, justify = 'center')
        self.main_label.grid(row=0, column=0, columnspan= 3, sticky= 'EW', ipady= 4, ipadx= 5)

        self.scroll_listbox = Scrollbar(self.main_frame)
        self.score_listbox = Listbox(self.main_frame , yscrollcommand = self.scroll_listbox.set)
        self.scroll_listbox.config( command = self.score_listbox.yview )  
        self.score_listbox.grid(row=1,column=0,columnspan = 3  , sticky= 'EW' , padx= (10,0) , pady = 4)
        self.scroll_listbox.grid(row=1,column=3  , sticky= 'NS' , padx = (0,10), pady = 4)

        if self.controler != 1:
            save_data_to_database(p_name,p_level,p_time,self.score_listbox)
        
        init(self.score_listbox)
             
        self.btn_again = Button(self.main_frame, text='Play Again !', fg= 'black', bg= 'white', activeforeground= 'white', activebackground= 'black')
        self.btn_again.grid(row=2 , column= 0, columnspan= 3, sticky= 'EW', ipady= 5 , ipadx= 20, padx= (60,60))   
        self.btn_again.bind('<Button-1>', self.level_gui)
        self.btn_back = Button(self.main_frame, text='Back to Main', fg= 'black', bg= 'white', activeforeground= 'white', activebackground= 'black')
        self.btn_back.grid(row=3 , column= 0, columnspan= 3, sticky= 'EW', ipady= 5 , ipadx= 20, padx= (60,60))
        self.btn_back.bind('<Button-1>', self.back_to_main)

        if self.controler == 1:
            self.btn_again.destroy()

        self.controler = 1

        self.gui_elements = [self.main_label,
                             self.score_listbox,
                             self.scroll_listbox,
                             self.btn_again,
                             self.btn_back
                             ]

    #endregion

    def back_to_main(self, event):
        if self.controler == 1:
            self.gui_elements_remove(self.gui_elements)
        elif self.controler == 2:
            self.gui_elements_remove(self.gui_elements)
            self.game_frame.destroy()
        else:
            pass

        self.main_gui()

    def gui_elements_remove(self, elements):
        for element in elements:
            element.destroy()



    def submit(self,name,level,time):
        
        if  len(name.strip())== 0 :
            messagebox.showerror("Error",'Please Enter Your Name !') 
            return
        global p_name, p_level, p_time
        p_name = name
        p_level = 'Level : '+str(level)
        p_time = str(time)
        self.game_frame.destroy()
        self.score_gui(True)
           

def main():
    global root

    root = Tk()
    root.geometry('260x290')
    window = MainWindow(root)

    root.mainloop()

if __name__ == '__main__':
    main()