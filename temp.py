from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city= city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=1e8984348f46033da1959c65743ee33b").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Weather APP")
win.config(bg= "lavender")
win.geometry("500x570")

name_label = Label(win, text = "Weather App⛅", font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name= ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Hyderabad","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Khammam","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Daman and Diu","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text = "Weather App", values=list_name, font=("Times New Roman", 20, "bold"), textvariable= city_name)
com.place(x=50, y=120, height=50, width=400)

#Labels
w_label = Label(win, text = "Weather Climate", font=("Times New Roman", 15))
w_label.place(x=90, y=260, height=50, width=150)

w_label1 = Label(win, text = "", font=("Times New Roman", 15))
w_label1.place(x=260, y=260, height=50, width=150)

wb_label = Label(win, text = "Weather Description", font=("Times New Roman", 13))
wb_label.place(x=90, y=330, height=50, width=150)

wb_label1 = Label(win, text = "", font=("Times New Roman", 13))
wb_label1.place(x=260, y=330, height=50, width=150)

temp_label = Label(win, text = "Temperature", font=("Times New Roman", 15))
temp_label.place(x=90, y=400, height=50, width=150)

temp_label1 = Label(win, text = "", font=("Times New Roman", 15))
temp_label1.place(x=260, y=400, height=50, width=150)

per_label = Label(win, text = "Pressure", font=("Times New Roman", 15))
per_label.place(x=90, y=470, height=50, width=150)

per_label1 = Label(win, text = "", font=("Times New Roman", 15))
per_label1.place(x=260, y=470, height=50, width=150)


#done button
done_button = Button(win, text = "Done", font=("Times New Roman", 20, "bold"),command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()