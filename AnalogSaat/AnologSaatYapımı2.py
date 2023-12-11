from tkinter import*
import time
import math

pencere = Tk()
pencere.geometry("600x600")
pencere.title("ANOLOG SAAT")

ekran = Canvas(pencere, width=600, height=600)  # highlightthickness = 5 pencere çerçeve çizgi kalınlığı
ekran.pack()                                    # highlightbackground = "red"  çerçeve çizgi rengi

x, y = 300, 300
x1, y1, x2, y2 = x, y, x, 25
r1, r2 = 300, 300
derece = 0
derece_s = int(time.strftime("%S")) * 6  # Saniye değerini alıyoruz. 1 saat arası 5 birim ve 6 derece yapar.
derece_d = int(time.strftime("%M")) * 6  # Dakika değerini alıyoruz
derece_h = int(time.strftime("%I")) * 30  # Saat değerini alıyoruz. 1 saat arası 30 derece eder
date_n = int(time.strftime("%d"))

if derece_h >= 360:  # Yukarıda bilgisayar saati olarak 24 alabiliriz. 24x30=720 bu yuzden 0 a döndürdük
    derece_h = 0

rs, ry, ra = 220, 240, 180  # akrep ve yelkovan için uzunluk belirtiyoruz
rl = 225
j = 0
radyan = 0
ekran.create_oval(0, 0, 600, 600, fill="#05acab")  # ekranımızda bir daire oluşturuyoruz
ekran.create_oval(295, 295, 305, 305, fill="black")  # merkezde bir daire oluşturuyoruz

number = ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

for i in range(60):
    radyan = math.radians(derece)
    if i % 5 == 0:
        oran = 0.8
        s1 = x+rl*math.sin(radyan)
        s2 = y-rl*math.cos(radyan)
        if derece % 90 == 0 :
            ekran.create_text(s1, s2, fill="white", text=number[j], font="Helveetica 22")
        else:
            ekran.create_text(s1, s2, fill="black", text=number[j], font="Helveetica 20")
        j += 1
        if j >= len(number):
            j = 0
    else:
        oran = 0.9

    x1 = x + oran * r2 * math.sin(radyan)
    y1 = y - oran * r2 * math.cos(radyan)
    x2 = x + r1 * math.sin(radyan)
    y2 = y - r1 * math.cos(radyan)
    if oran == 0.8:
        ekran.create_line(x1, y1, x2, y2, width=2, fill="red")
    else:
        ekran.create_line(x1, y1, x2, y2, width=1, fill="white")
    derece += 6


radyan_s = math.radians(derece_s)
x2 = x+rs*math.sin(radyan_s)
y2 = y-rs*math.cos(radyan_s)
saniye = ekran.create_line(x, y, x2, y-rl, fill="black", width=2, arrow="last")
def sec():
    global derece_s, saniye
    radyan_s = math.radians(derece_s)
    ekran.delete(saniye)
    x2 = x+rs*math.sin(radyan_s)
    y2 = y-rs*math.cos(radyan_s)
    saniye = ekran.create_line(x, y, x2, y2, fill="black", width=2, arrow="last")
    ekran.after(1000, sec)
    if derece_s >= 360:
        derece_s = 0
        min()
    derece_s += 6
    date = ekran.create_rectangle(330, 270, 350, 290, fill="white", width=2)
    date_no = ekran.create_text(340, 280, fill= "black", text=date_n, font="Helvetica 13")

radyan_d = math.radians(derece_d)
x2 = x+ry*math.sin(radyan_d)
y2 = y-ry*math.cos(radyan_d)
dakika = ekran.create_line(x, y, x2, y2, fill="black", width=4)
def min():
    global derece_d, dakika
    derece_d += 6
    radyan_d = math.radians(derece_d)
    ekran.delete(dakika)
    x2 = x+ry*math.sin(radyan_d)
    y2 = y-ry*math.cos(radyan_d)
    dakika = ekran.create_line(x, y, x2, y2, fill="black", width=4)
    if derece_d >= 360:
        derece_d = 0

    hour()

derece_h = derece_h + (derece_d * 0.0833)
radyan_h = math.radians(derece_h)
x2 = x+ra*math.sin(radyan_h)
y2 = y-ra*math.cos(radyan_h)
saat = ekran.create_line(x, y, x2, y2, fill="black", width=5)
def hour():
    global derece_h, saat
    derece_h += 0.5
    radyan_h = math.radians(derece_h)
    ekran.delete(saat)
    x2 = x+ra*math.sin(radyan_h)
    y2 = y-ra*math.cos(radyan_h)
    saat  = ekran.create_line(x, y, x2, y2, fill="black", width=5)
    if derece_h >= 360:
        derece_h = 0

sec()
mainloop()