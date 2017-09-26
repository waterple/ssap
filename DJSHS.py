# -*- coding: utf-8 -*-

_list = ['01 : 독서실','08 : 정보검색실(인검실)-1','09 : 정보검색실(인검실)-2','10 : 도서관','11 : 일반물리실험(다산관302호)','12 : 물리실험실 및 강의실(물리과)','13 : 정보과 멀티미디어실(다산관 4층)','14 : 지구과학(다산관 710호)','15 : 지구과학(다산관 707호)','16 : 지구과학(다산관 708호)','17 : 모델생물실(다산관201호)','18 : 박테리아 배양실(다산관202호)','19 : 일반생물학실험실(다산관 203호)    ','20 : 현미경실험실(다산관 206호)','21 : 생화학실험실(다산관 207호)','22 : 전자현미경실(다산관 209호)','23 : 생명과학실험실(일신관 201호)','24 : 화학R&E실(101호)','25 : 일반화학실험실(다산관 103호)','26 : 무기화학실험실(다산관 104호)','27 : 유기화학실험실(다산관 107호)','28 : 화학기기분석실(다산관 108호)','29 : 화학실험실(다산관 607호)','30 : 화학동아리실(다산관 502호)','31 : R&E 연구 외출','32 : 부모외출','33 : 종교외출','34 : 병외출    ','35 : 병외박','36 : 기숙사 호실','37 : 다산관 (505호)','38 : 시청각실','39 : 국제화상회의실','40 : 체육관','41 : 다산관 대강당    ','42 : 다산관7층 무한상상실','43 : 세종학당','44 : 다산관 510호','45 : 수학교실 1','46 : 수학교실 2','47 : 수학교실 3','48 : 수학교실 4','49 : 수학교실 5','50 : 다산관 608호', '51 : 외박(금요일)']
from os import system

try:
    from tkinter import *
except ImportError:
    from Tkinter import *
'''
try:
    import selenium
except ImportError:
    system('pip install selenium')
'''

import sys, time
from main import work

window = Tk()
window.wm_title('대전과학고 자습신청 프로그램')
window.iconbitmap('./ico.ico')

'''자습 변수들'''

_1 = IntVar() ; _1.set(0)
_2 = IntVar() ; _2.set(0)
_3 = IntVar() ; _3.set(0)
_4 = IntVar() ; _4.set(0)

s1 = StringVar() ; s1.set('')
s2 = StringVar() ; s2.set('')
s3 = StringVar() ; s3.set('')
s4 = StringVar() ; s4.set('')

def onselect1(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    _1.set(1 if index == 0 else index + 7)
    value = w.get(index)
    s1.set(value)

def onselect2(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    _2.set(1 if index == 0 else index + 7)
    value = w.get(index)
    s2.set(value)

def onselect3(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    _3.set(1 if index == 0 else index + 7)
    value = w.get(index)
    s3.set(value)

def onselect4(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    _4.set(1 if index == 0 else index + 7)
    value = w.get(index)
    s4.set(value)

_info = ['','']
with open('info.txt', 'at') as _:
    pass
f = open('info.txt', 'r')
info = f.read().split()
if len(info)>=2:
    _info = info[:2]
f.close()

frame1 = Frame(window)
frame1.pack()

lb1 = Label(frame1, text='학번')
lb1.grid(row=0,column=0)
txt1 = Entry(frame1)
txt1.grid(row=1,column=0)
txt1.insert(END, _info[0])

lb2 = Label(frame1, text='비번')
lb2.grid(row=0,column=1)
txt2 = Entry(frame1, show='*')
txt2.grid(row=1,column=1)
txt2.insert(END, _info[1])

frame2 = Frame(window)
frame2.pack()

lb3 = Label(frame2, text='1자')
lb3.grid(row=0,column=0)
lst1 = Listbox(frame2, width=35, height=30)
lst1.grid(row=1,column=0)
lst1.bind('<<ListboxSelect>>', onselect1)

lb4 = Label(frame2, text='2자')
lb4.grid(row=0,column=1)
lst2 = Listbox(frame2, width=35, height=30)
lst2.grid(row=1,column=1)
lst2.bind('<<ListboxSelect>>', onselect2)

lb5 = Label(frame2, text='3자')
lb5.grid(row=0,column=2)
lst3 = Listbox(frame2, width=35, height=30)
lst3.grid(row=1,column=2)
lst3.bind('<<ListboxSelect>>', onselect3)

lb6 = Label(frame2, text='4자')
lb6.grid(row=0,column=3)
lst4 = Listbox(frame2, width=35, height=30)
lst4.grid(row=1,column=3)
lst4.bind('<<ListboxSelect>>', onselect4)

lb_1 = Label(frame2, textvariable=s1)
lb_1.grid(row=2,column=0)
lb_2 = Label(frame2, textvariable=s2)
lb_2.grid(row=2,column=1)
lb_3 = Label(frame2, textvariable=s3)
lb_3.grid(row=2,column=2)
lb_4 = Label(frame2, textvariable=s4)
lb_4.grid(row=2,column=3)

'''
btn1 = Button(frame2, text='1자 결정', width=30)
btn2 = Button(frame2, text='2자 결정', width=30)
btn3 = Button(frame2, text='3자 결정', width=30)
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
'''

for i in _list:
    lst1.insert(END, i)
    lst2.insert(END, i)
    lst3.insert(END, i)
    lst4.insert(END, i)

frame3 = Frame(window)
frame3.pack()

error = StringVar()
error.set('')

def end(evt):
    _1_ = _1.get()
    _2_ = _2.get()
    _3_ = _3.get()
    _4_ = _4.get()
    n1 = txt1.get()
    n2 = txt2.get()

    if (n1 == '') or (n2 == ''):
        error.set('정보가 부족합니다')
    else:
        with open('info.txt', 'wt') as f:
            f.write('{id} {pw}'.format(id=n1, pw=n2))
        error.set('Loading...')
        time.sleep(.5)
        work((None, '2017'+n1, n2, _1_, _2_, _3_, _4_))
        sys.exit()


lb_e = Label(frame3, textvariable=error)
lb_e.pack()

btn = Button(frame3, text='신청하기', width=90)
btn.bind("<Button-1>", end) 
btn.pack()

window.mainloop()