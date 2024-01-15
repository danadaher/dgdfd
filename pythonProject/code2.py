from tkinter import *
from tkintermapview import TkinterMapView
myframe = Tk()
myframe.geometry('880x450')
myframe.title('My Application')
myframe.configure(background='white')
def FirstPharmacy():
    map = TkinterMapView(myframe,width=500, height=400, corner_radius=0 )
    map.place(x=410, y=35)
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_position(31.889324949634826, 35.886668781868046)
    map.set_zoom(15)
    marker = map.set_marker(31.889324949634826, 35.886668781868046)
    marker.set_text('صيدلية شمس عمان')

def SecondPharmacy():
    map = TkinterMapView(myframe,width=500, height=400, corner_radius=0 )
    map.place(x=410, y=35)
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_position(31.893894754751102, 35.8761894)
    map.set_zoom(15)
    marker = map.set_marker(31.893894754751102, 35.8761894)
    marker.set_text('صيدلية اللؤلؤ')

def ThirdPharmacy():
    map = TkinterMapView(myframe,width=500, height=400, corner_radius=0 )
    map.place(x=410, y=35)
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_position(31.90045667138789, 35.895156003545694)
    map.set_zoom(15)
    marker = map.set_marker(31.90045667138789, 35.895156003545694)
    marker.set_text('pharmacy 1')

def FourthPharmacy():
    map = TkinterMapView(myframe,width=500, height=400, corner_radius=0 )
    map.place(x=410, y=35)
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_position(31.922280208697117, 35.8590543595332)
    map.set_zoom(15)
    marker = map.set_marker(31.922280208697117, 35.8590543595332)
    marker.set_text('صيدلية ليف')

def FifthPharmacy():
    map = TkinterMapView(myframe,width=500, height=400, corner_radius=0 )
    map.place(x=410, y=35)
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_position(31.903829642251775, 35.859455344790824)
    map.set_zoom(15)
    marker = map.set_marker(31.903829642251775, 35.859455344790824)
    marker.set_text('صيدلية جوي')

def SixthPharmacy():
    map = TkinterMapView(myframe,width=500, height=400, corner_radius=0 )
    map.place(x=410, y=35)
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_position(31.93779655244697, 35.869672991503315)
    map.set_zoom(15)
    marker = map.set_marker(31.93779655244697, 35.869672991503315)
    marker.set_text('صيدلية كن بصحة')

def SeventhPharmacy():
    map = TkinterMapView(myframe,width=500, height=400, corner_radius=0 )
    map.place(x=410, y=35)
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_position(31.908002807750318, 35.852734828836276)
    map.set_zoom(15)
    marker = map.set_marker(31.908002807750318, 35.852734828836276)
    marker.set_text('صيدلية ناصيف')

def EighthPharmacy():
    map = TkinterMapView(myframe,width=500, height=400, corner_radius=0 )
    map.place(x=410, y=35)
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_position(31.893961045329277, 35.878875799999996)
    map.set_zoom(15)
    marker = map.set_marker(31.893961045329277, 35.878875799999996)
    marker.set_text('صيدلية بوابة البتراء')

def NinthPharmacy():
    map = TkinterMapView(myframe,width=500, height=400, corner_radius=0 )
    map.place(x=410, y=35)
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_position(31.91693536916252, 35.86217291540209)
    map.set_zoom(15)
    marker = map.set_marker(31.91693536916252, 35.86217291540209)
    marker.set_text('صيدلية كاميليا')

def country():
    country = Entry1.get()
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom= 22)
    map.set_address(country, marker=True)
# ------- Title ----------
title1 = Label(myframe, text='pharmacy location الصيدليات المناوبة', fg='white', bg='grey', font='Tajawal 18')
title1.pack(fill = X)
# --------picture ----------
pic = PhotoImage(file='4.png')
lab_pic = Label(myframe, image=pic, bd=0, bg='white', width=400, height=210)
lab_pic.place(x=5, y =35)
# ------ Lable + Entry + button --------
label1 = Label(myframe, text='country:', font='Tajawal 14', fg='black', bg='white')
label1.place(x=50, y= 260)

Entry1 = Entry(myframe, font='Tajawal 14', width=10, bd = 2 , relief=GROOVE)
Entry1.place(x = 140, y = 260)

button1 = Button(myframe, text='Get country', bg='black', fg='white', bd=1, relief=SOLID, width=10, cursor='hand2', command=country)
button1.place(x= 260, y = 260)
# -------- pharmacy buttons ----------
b1 = Button(myframe, text='صيدلية شمس عمان', cursor='hand2', bg= 'white', fg= 'black', bd= 1, relief=SOLID, font='Tajawal 12', width=13, command= FirstPharmacy )
b1.place(x= 10, y=300)

b2 = Button(myframe, text='صيدلية اللؤلؤ', cursor='hand2', bg= 'white', fg= 'black', bd= 1, relief=SOLID, font='Tajawal 12', width=13, command=SecondPharmacy)
b2.place(x= 140, y=300)

b3 = Button(myframe, text='صيدلية 1', cursor='hand2', bg= 'white', fg= 'black', bd= 1, relief=SOLID, font='Tajawal 12', width=13, command= ThirdPharmacy)
b3.place(x= 270, y=300)

b4 = Button(myframe, text='صيدلية ليف', cursor='hand2', bg= 'white', fg= 'black', bd= 1, relief=SOLID, font='Tajawal 12', width=13, command= FourthPharmacy)
b4.place(x= 10, y=340)

b5 = Button(myframe, text='صيدلية جوي', cursor='hand2', bg= 'white', fg= 'black', bd= 1, relief=SOLID, font='Tajawal 12', width=13, command=FifthPharmacy)
b5.place(x= 140, y=340)

b6 = Button(myframe, text='صيدلية كن بصحة', cursor='hand2', bg= 'white', fg= 'black', bd= 1, relief=SOLID, font='Tajawal 12', width=13, command=SixthPharmacy)
b6.place(x= 270, y=340)

b7 = Button(myframe, text='صيدلية ناصيف', cursor='hand2', bg= 'white', fg= 'black', bd= 1, relief=SOLID, font='Tajawal 12', width=13, command=SeventhPharmacy)
b7.place(x= 10, y=380)

b8 = Button(myframe, text='صيدلية بوابة البتراء', cursor='hand2', bg= 'white', fg= 'black', bd= 1, relief=SOLID, font='Tajawal 12', width=13, command=EighthPharmacy )
b8.place(x= 140, y=380)

b9 = Button(myframe, text='صيدلية كاميليا', cursor='hand2', bg= 'white', fg= 'black', bd= 1, relief=SOLID, font='Tajawal 12', width=13, command=NinthPharmacy)
b9.place(x= 270, y=380)
# ------ maps---------
map = TkinterMapView(myframe,width=500, height=400, corner_radius=0 )
map.place(x = 410, y= 35)

myframe.mainloop()