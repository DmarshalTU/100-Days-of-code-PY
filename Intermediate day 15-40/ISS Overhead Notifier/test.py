# http://open-notify.org/Open-Notify-API/ISS-Location-Now/


# API test
# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
# iss_position = (latitude, longitude)
# print(iss_position)

# response code:
"""
תגובות מידע (100–199),
תגובות הצלחה(200–299),
הפניות (300–399),
שגיאות לקוח (400–499),
שגיאות שרת (500–599).
"""

# https://api.kanye.rest

# Kanye Says...
# from tkinter import *
# import requests


# def get_quote():
#     response = requests.get("https://api.kanye.rest")
#     response.raise_for_status()
#     data = response.json()
#     quote = data['quote']
#     canvas.itemconfig(quote_text, text=quote)
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=300)
# background_img = PhotoImage(file='kanye.png')
# canvas.create_image(150, 150, image=background_img)
# quote_text = canvas.create_text(150, 150, text="Kanye Qoute", width=200, font=("Ariel", 24, "bold"), fill='white')
# canvas.grid(row=0, column=0)
#
# button = Button(text='click', command=get_quote)
# button.grid(row=1, column=0)
#
# window.mainloop()



import requests
from datetime import datetime

params = {
    "lat": 31.690782,
    "lng": 35.250694,
    "formatted": 0,

}

response = requests.get(" https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()

data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(f"sunrise: {sunrise}\nsunset: {sunset}")

time_now = datetime.now()
print(f"hour now: {time_now.hour}")


















