
import tkinter as tk
from about import AboutMe
from about import TestWindow
import sys as sys


WHITE = "#F8F8F8" # black/white
TAN = "#F1EABC" # black/tan
GREEN = "#00AA00" # green
BACK='#272533'
CALL_TEXT="✆"
RECENT_TEXT='⏱'
ABOUT_TEXT='❓'


class InCall(tk.Toplevel):

    def __init__(self, master, number):
        super().__init__()
        self.transient(master)
        self.resizable(False, False)
        self.wm_attributes('-topmost', 'true')
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title('PhoneDialer')
        self.config(bg=BACK)
        self.master = master
        self.lbl = tk.Label(self, text=number, anchor='e', bg=BACK, fg='white', font=('Franklin Gothic Book', 48, 'bold'))
        self.lbl.grid(row=0, sticky='ew', padx=4, pady=2, )
        self.end_call_btn = self.std_btn(CALL_TEXT, 'red', 10, 1)
        
        #tests

    def about_me(self):
        """Application and license info"""
        AboutMe(self)

    def close(self):
        """Close window"""
        self.master.incall = None
        #self.master.focus_set()
        self.destroy()

    def std_btn(self, text, bg, row, col, width=7, height=2, font=('Franklin Gothic Book', 24)):
        btn = tk.Button(self, text=text, bg=bg, width=width, height=height, font=font, command=lambda: self.event_click(text))
        return btn.grid(row=row, column=col, padx=4, pady=4)

    def event_click(self, event):
        if event == CALL_TEXT:
            self.end_call()


    # click events
    def end_call(self):
        #todo    
        self.close()

if __name__ == '__main__':
    s = TestWindow()
    InCall(s, '')
    s.mainloop()        