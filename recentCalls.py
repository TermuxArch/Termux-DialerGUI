
import tkinter as tk
from about import AboutMe
from utils import TestWindow
import subprocess
import os
import utils as utils
from utils import MessageDialog
from json import JSONDecoder, JSONDecodeError


def RecentCallView(self, r, json={}, fg='black', bg='white', func=lambda text: print(text)):
    ''
    frm = tk.Frame(self, bg=bg)
    s = '⬇️'
    if str(json['type']) == 'OUTGOING':
        s = '⬆️'
    name = json['name']
    if name == 'UNKNOWN_CALLER' :
        name = json['phone_number']
    textvar1 = tk.StringVar(value = name+' '+json['duration']+' '+s)
    textvar2 = tk.StringVar(value = json['phone_number']+' '+json['date'])
    lbl1 = tk.Label(frm, textvariable= textvar1, anchor='e', bg=bg, fg=fg, font=('Franklin Gothic Book', 14),)
    lbl1.grid(row=0, sticky='e')
    lbl2 = tk.Label(frm,textvariable= textvar2, anchor='e', bg=bg, fg=fg, font=('Franklin Gothic Book', 10))
    lbl2.grid(row=1, sticky='e')
    frm.bind("<Button-1>", func=lambda text: func(json['phone_number']))
    lbl1.bind("<Button-1>", func=lambda text: func(json['phone_number']))
    lbl2.bind("<Button-1>", func=lambda text: func(json['phone_number']))
    return frm.grid(row=r, columnspan=4, sticky='e', padx=4, pady=2, ) 

def RecentListView(self, json='[]', row=0, fg='black', bg='white', func=lambda text: print(text) ):
    ''
    frm = tk.Frame(self, bg=bg)
    frm.grid(row=row, columnspan=4, sticky='e', padx=4, pady=2, )
    j = JSONDecoder().decode(json)
    total = len(j)
    for i in range(0, total):
        RecentCallView(frm, total-i, j[i], fg= fg, bg=bg, func= lambda text: func(text) )
    return frm

class RecentCallsPage(tk.Toplevel):

    wait = None
    offset=0

    def __init__(self, master):
        super().__init__()
        self.transient()
        self.resizable(False, False)
        self.master = master
        #self.wm_attributes('-toolwindow', 'true')
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title('Recent calls')
        self.config(bg=utils.BACK)

        self.lbl = tk.Label(self, text='Recent 10', anchor='e', bg=utils.BACK, fg=utils.FRONT, font=('Franklin Gothic Book', 14))
        self.lbl.grid(row=0, columnspan=4, sticky='ew', padx=4, pady=2, )

        self.lista = tk.Label(self, text='asdasd')

        tk.Button(self, text='Show 10 more', command=lambda: self.more10()).grid(row=2, column=1, padx=4, pady=2)


        self.fillRecent()

        #tests
    def more10(self):
        self.offset+=10
        self.lista.destroy()
        self.fillRecent()

    def close(self):
        """Close window"""
        self.master.wait = None
        self.destroy()

    def event_click(self, event):
        print()

    def favClic(self, text):
        print(text)

    def fillRecent(self):
        a = str(subprocess.check_output(['/bin/sh','/Volumes/Datos/_Projects/+python/PhoneDialer/termux-call-log']))#["termux-call-log", "-l", '10', '-o', str(self.offset)]))
        if a.__contains__('error'):
            self.wait = EOFError(a)
            utils.Utils.showError(self, a)
        else:
            a=a.replace('b\'', '').replace('\\n\'','').replace('\\n','').replace('\\','\\\\')
            self.lista = RecentListView(self, a, row=1, bg=utils.BACK, fg='white')
            


if __name__ == '__main__':
    s = TestWindow()
    RecentCallsPage(s)
    s.mainloop()           
    
