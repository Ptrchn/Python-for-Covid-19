import requests
import tkinter as tk

url = '	https://covid19.ddc.moph.go.th/api/Cases/today-cases-by-provinces'

r = requests.get(url)
result = r.json()
count = 0 

def bangkok():
    count = 0
    Cv19 = ''
    for t  in result:
        
        count += 1
        if count == 1:
            Cv19 = str(t['update_date']) + '\n'
    for k in result[1:2]:
        Cv19 += '\n' 'จังหวัด : ' + str(k['province']) + '\n'
        Cv19 += 'จำนวนผู้ติดเชื้อรายใหม่ : ' + str(k['new_case']) + '\n'
        Cv19 += 'จำนวนผู้ติดเชื้อทั้งหมด : ' + str(k['total_case']) + '\n'
        Cv19 += 'จำนวนผู้เสียชีวิตรายใหม่ : ' + str(k['new_death']) + '\n'
        Cv19 += 'จำนวนผู้เสียชีวิตทั้งหมด : '  + str(k['total_death']) + '\n'
    for p in result[16:17]:
        Cv19 += '\n' 'จังหวัด : ' + str(p['province']) + '\n'
        Cv19 += 'จำนวนผู้ติดเชื้อรายใหม่ : ' + str(p['new_case']) + '\n'
        Cv19 += 'จำนวนผู้ติดเชื้อทั้งหมด : ' + str(p['total_case']) + '\n'
        Cv19 += 'จำนวนผู้เสียชีวิตรายใหม่ : ' + str(p['new_death']) + '\n'
        Cv19 += 'จำนวนผู้เสียชีวิตทั้งหมด : '  + str(p['total_death'])

    L3.configure(text=Cv19)
    

###############  UI  ######################


UI = tk.Tk()
UI.geometry('600x500')
UI.title('Covid-19 App')

FONT1 = ('Angsana New' , 25)
FONT2 = ('Angsana New' , 35)

L1 = tk.Label(text = 'สถานการณ์ผู้ติดเชื้อ COVID-19 อัพเดทรายวัน',font = FONT2)
L1.pack()

B1 = tk.Button(UI,text='run',command= bangkok)
B1.pack(ipadx=20,ipady=10)


v1_result = tk.StringVar
L2 = tk.Label(textvariable =v1_result,font=FONT1)
L2.pack()

L3 = tk.Label(master=UI)
L3.pack()

UI.mainloop()


