import googletrans as gt
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

win=Tk()

Label=Label(win,text="Hello World")
Label.pack()

text1=Text(win,height=10,width=90)
text1.place(x=300,y=100)
text2=Text(win,height=10,width=90)
text2.place(x=300,y=400)

#googleTrans.....


def trans():
        button.set("loding...")
        text2.delete(1.0,"end-1c")
        inp = text1.get(1.0, "end-1c")
        Trans=gt.Translator()
        if(g_var.get()=='text'):
            try:
                ans=Trans.translate(inp,src=str(lang_1.get()),dest=str(lang_2.get()))
                text2.insert(tk.END,ans.text)
                button.set("transulate")
            except:
                messagebox.showwarning("warning","Warning....please cheak your internet connection...!")
        if(g_var.get()=='pronunciation'):
            try:
                ans=Trans.translate(inp,src=str(lang_1.get()),dest=str(lang_2.get()))
                text2.insert(tk.END,ans.pronunciation)
                button.set("transulate")
            except:
                messagebox.showwarning("warning","Warning")

lang_1=tk.StringVar()
lang_2=tk.StringVar()
button=tk.StringVar()
g_var=tk.StringVar()
button=tk.StringVar()

#combo boxes........
g_combo=ttk.Combobox(win,height=6,width=12,state='readonly',textvariable=g_var)
g_combo['value']=('text','pronunciation')
g_combo.current(0)
g_combo.place(x=600,y=50)
combo=ttk.Combobox(win,height=6,width=12,state='readonly',textvariable=lang_1)
combo['value']=('English','Tamil')
combo.current(0)
combo.place(x=100,y=175)
combo_1=ttk.Combobox(win,height=6,width=12,state='readonly',textvariable=lang_2)
combo_1['value']=('English','Tamil')
combo_1.current(1)
combo_1.place(x=100,y=475)

btn=Button(win,height=3,width=20,textvariable=button,command=trans)
button.set("Translate")
btn.place(x=600,y=600)

mainloop()

