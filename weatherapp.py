import requests
from tkinter import *

def weather():
	city=citylistbox.get()
	link = "https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(city)
	result = requests.get(link)
	op=result.json()
	weatherstat=op['weather'][0]['description']
	temp=op['main']['temp']
	hume=op['main']['humidity']
	windspeed=op['wind']['speed']

	weatherstatlab.configure(text="weather status : "+weatherstat)
	templab.configure(text="Temprature : "+str(temp))
	humelab.configure(text="Humidity : "+str(hume))
	speedlab.configure(text="wind speed : "+str(windspeed))

window = Tk()
window.geometry("350x200")

cityname = ["Pune","Mumbai","Delhi","Jintur"]
citylistbox = StringVar(window)
citylistbox.set("Select the city")
option = OptionMenu(window,citylistbox,*cityname)
option.grid(row=2,column=2,padx=95,pady=15)

btn=Button(window,text="Get Weather Information",width=20,command=weather,bg='black',fg='yellow')
btn.grid(row=3,column=2,padx=95)

weatherstatlab=Label(window,font=('italic',12),fg='red')
weatherstatlab.grid(row=4,column=2)

templab=Label(window,font=('italic',12),fg='red')
templab.grid(row=5,column=2)

humelab=Label(window,font=('italic',12),fg='red')
humelab.grid(row=6,column=2)

speedlab=Label(window,font=('italic',12),fg='red')
speedlab.grid(row=7,column=2)

window.mainloop()
