import modules.database as m_data
import modules.main_window as m_window
import customtkinter as Ctk
from PIL import Image
import os
import datetime
import tkinter

def start_widget():
    def close():
        pass 

    PATH = os.path.abspath(__file__+"/../../images")
    m_data.cursor.execute("SELECT * FROM users")
    data = m_data.cursor.fetchall()
    if len(data) == 0:
        pass
    else:
        m_data.cursor.execute("SELECT city FROM users")
        db_city = m_data.cursor.fetchone()[0]
        
    global widget
    widget = Ctk.CTk()
    widget.geometry("350x350")
    widget.configure(fg_color="#163C5F")
    widget.resizable(False, False)
    widget.iconbitmap(os.path.join(PATH, "icon.ico"))
    widget.protocol("WM_DELETE_WINDOW", close)
    temp, weather, maxtemp, mintemp, timezone, main_wezer, main_id, response = m_data.get_weather(f"{db_city}")

    def weather_update():
        m_data.cursor.execute("SELECT * FROM users")
        data_ = m_data.cursor.fetchall()
        if len(data_) == 0:
            pass
        else:
            m_data.cursor.execute("SELECT city FROM users")
            db_city_ = m_data.cursor.fetchone()[0]

            temperature_, weather_, maxtemp_, mintemp_, time_zone, main_wezer, main_id, response = m_data.get_weather(f"{db_city_}")
            time_date_data1, time, date, week_day1 = find_date(time_zone)
    
            user_city.configure(text = f'{db_city_}')
            weather_labeli.configure(text = f"{weather_}")
            user_temp.configure(text = f'{temperature_}°')
            min_maxi.configure(text=f"↓{mintemp_}° ↑{maxtemp_}°")
            print(f'{db_city_}')

            hour_ = time_date_data1.strftime("%H")

            if hour_ in ["04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]:
                if main_wezer=="Atmosphere":#
                    desc_label.configure(image = haze_image)
                #
                elif main_wezer=="Clear":#
                    desc_label.configure(image = sun_image)# 
                #
                elif main_wezer=="Thunderstorm":
                    desc_label.configure(image = storm_image)
                #
                elif main_wezer=="Rain": #
                    desc_label.configure(image = rain_image)  
                #
                elif main_wezer=="Clouds":
                    if main_id == 804:
                        desc_label.configure(image = cloudy_image)  
                    elif main_id in [801,802,803]:
                        desc_label.configure(image = small_cloudy_image)  

                #
                elif main_wezer=="Drizzle":#
                    if main_id in [300, 310, 311]:
                        desc_label.configure(image = drizzle_sun_image)
                    elif main_id in [301, 302, 312, 313, 314, 321]:
                        desc_label.configure(image = drizzle_image)    
                #   
                elif main_wezer=="Snow":#
                    if main_id in [600, 601, 620, 612, 615, 616]:
                        desc_label.configure(image = small_snowy_image)
                    elif main_id in [602, 611, 613, 621, 622]:
                        desc_label.configure(image = snowy_image)    
                #   
                else:
                    desc_label.configure(image = vapros)
                    
            elif hour_ in ["18", "19", "20", "21", "22", "23", "00", "01", "02", "03"]:
                if main_wezer=="Atmosphere":#
                    desc_label.configure(image = haze_image)
                #
                elif main_wezer=="Clear":#
                    desc_label.configure(image = night_image)# 
                #
                elif main_wezer=="Thunderstorm":
                    desc_label.configure(image = storm_image)
                #
                elif main_wezer=="Rain": #
                    desc_label.configure(image = night_rain_image)
                #
                elif main_wezer=="Clouds":
                    if main_id == 804:
                        desc_label.configure(image = night_cloudy_image)  
                    elif main_id in [801,802,803]:
                        desc_label.configure(image = cloudy_night)  

                #
                elif main_wezer=="Drizzle":#
                    if main_id in [300, 310, 311]:
                        desc_label.configure(image = drizzle_sun_image)
                    elif main_id in [301, 302, 312, 313, 314, 321]:
                        desc_label.configure(image = drizzle_image)    
                #   
                elif main_wezer=="Snow":#
                    if main_id in [600, 601, 620, 612, 615, 616]:
                        desc_label.configure(image = snowy_night_image)
                    elif main_id in [602, 611, 613, 621, 622]:
                        desc_label.configure(image = snowy_night_image)    
                #   
                else:
                    desc_label.configure(image = vapros)
            widget.after(600000, weather_update)


        
        # print('update')
        
    global weather_labeli, min_maxi, user_city, desc_label
    weather_labeli = Ctk.CTkLabel(widget, width=200, height=53,text=f"{weather}", font=("Roboto Slab", 25), text_color="#FFFFFF", fg_color="#163C5F", anchor = tkinter.W)
    weather_labeli.place(x =30, y =200) 

    min_maxi = Ctk.CTkLabel(widget, width=150, height=30, text=f"↓{mintemp}° ↑{maxtemp}°", font=("Roboto Slab", 20), text_color="#FFFFFF", fg_color="#163C5F", anchor = tkinter.W)
    min_maxi.place(x = 30, y =245)
    
    user_city = Ctk.CTkLabel(widget, width=310, height=52, text=f"{db_city}", font=("Roboto Slab", 40), text_color="#FFFFFF", fg_color="#163C5F", compound="left", anchor = tkinter.E)
    user_city.place(x = 30.5, y=274)
    
     
    #
    user_temp = Ctk.CTkLabel(widget, width=70, height=70, text=f"{temp}°", font=("Roboto Slab", 58), text_color="#FFFFFF", fg_color="#163C5F",anchor = tkinter.E)
    user_temp.place(x = 270, y = 200)
    
    # widget.bind("<Double-1>", m_window.main_window_start)

    # description_image = Ctk.CTkImage(light_image=Image.open(os.path.join(PATH, "cloudy.png")), size=(172, 152))
        
    # Загружаем и сохраняем картинки погоды
    # os.path.join(PATH, "название_картинки.png")
    cloudy_image = Ctk.CTkImage(Image.open(os.path.join(PATH, "cloudy.png")), size=(171, 159))
    drizzle_sun_image = Ctk.CTkImage(Image.open(os.path.join(PATH,"drizzle_sun.png")), size=(171, 159))
    drizzle_image = Ctk.CTkImage(Image.open(os.path.join(PATH,"drizzle.png")), size=(171, 159))
    freezing_image = Ctk.CTkImage(Image.open(os.path.join(PATH,"freezing.png")), size=(171, 159))
    night_cloudy_image = Ctk.CTkImage(Image.open(os.path.join(PATH,"night_cloudy.png")), size=(171, 159))
    night_rain_image = Ctk.CTkImage(Image.open(os.path.join(PATH,"night_rain.png")), size=(171, 159))
    #rain_image = ImageTk.PhotoImage(Image.open("images/rain.png"))
    small_cloudy_image = Ctk.CTkImage(Image.open(os.path.join(PATH,"small_cloudy.png")), size=(171, 159))
    rain_image = Ctk.CTkImage(Image.open(os.path.join(PATH,"small_rain.png")), size=(171, 159))
    snowy_image = Ctk.CTkImage(Image.open(os.path.join(PATH,"snowy.png")), size=(171, 159))
    small_snowy_image = Ctk.CTkImage(Image.open(os.path.join(PATH,"small_snowy.png")), size=(171, 159))
    storm_image = Ctk.CTkImage(Image.open(os.path.join(PATH,"storm.png")), size=(171, 159))
    sun_image = Ctk.CTkImage(Image.open(os.path.join(PATH,"sun.png")), size=(171, 159))
    snowy_night_image = Ctk.CTkImage(Image.open(os.path.join(PATH,"snowy_night.png")), size=(171, 159))
    vapros = Ctk.CTkImage(Image.open(os.path.join(PATH, "vapros.png")), size=(171, 159))
    haze_image = Ctk.CTkImage(Image.open(os.path.join(PATH, "dym.png")), size=(171, 159))
    night_image = Ctk.CTkImage(Image.open(os.path.join(PATH,"night_clean.png")), size=(171, 159))
    cloudy_night = Ctk.CTkImage(Image.open(os.path.join(PATH,"night_cloudy.png")), size=(171, 159))

    
    def find_date(timezone):
        time_hour = timezone // 3600
        #print(time_hour)
        if time_hour == 2:
            time_date_data = datetime.datetime.now()
        else:
            time_date_data = datetime.datetime.now() + datetime.timedelta(hours=time_hour) - datetime.timedelta(hours=2)

        time = time_date_data.strftime("%H:%M")
        date = time_date_data.strftime("%d-%m-%Y")

        week_day1 = time_date_data.isoweekday() 
        if week_day1 == 1:
            week_day1 = "Понеділок"
        if week_day1 == 2:
            week_day1 = "Вівторок"
        if week_day1 == 3:
            week_day1 = "Середа"
        if week_day1 == 4:
            week_day1 = "Четвер"
        if week_day1 == 5:
            week_day1 = "П'ятниця"
        if week_day1 == 6:
            week_day1 = "Субота"
        if week_day1 == 7:
            week_day1 = "Неділя"
        return time_date_data, time, date, week_day1


    time_date_data, time, date, week_day1 = find_date(timezone)
    

    hour = time_date_data.strftime("%H")
    print(hour)

    desc_label = Ctk.CTkLabel(widget, width=171, height=159, text="", bg_color="#163C5F")
    desc_label.pack()
    desc_label.place(x = 10, y = 20)

    if hour in ["04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]:
        if main_wezer=="Atmosphere":#
            desc_label.configure(image = haze_image)
        #
        elif main_wezer=="Clear":#
            desc_label.configure(image = sun_image)# 
        #
        elif main_wezer=="Thunderstorm":
            desc_label.configure(image = storm_image)
        #
        elif main_wezer=="Rain": #
            desc_label.configure(image = rain_image)  
        #
        elif main_wezer=="Clouds":
            if main_id == 804:
                desc_label.configure(image = cloudy_image)  
            elif main_id in [801,802,803]:
                desc_label.configure(image = small_cloudy_image)  

        #
        elif main_wezer=="Drizzle":#
            if main_id in [300, 310, 311]:
                desc_label.configure(image = drizzle_sun_image)
            elif main_id in [301, 302, 312, 313, 314, 321]:
                desc_label.configure(image = drizzle_image)    
        #   
        elif main_wezer=="Snow":#
            if main_id in [600, 601, 620, 612, 615, 616]:
                desc_label.configure(image = small_snowy_image)
            elif main_id in [602, 611, 613, 621, 622]:
                desc_label.configure(image = snowy_image)    
        #   
        else:
            desc_label.configure(image = vapros)
            
    elif hour in ["18", "19", "20", "21", "22", "23", "00", "01", "02", "03"]:
        if main_wezer=="Atmosphere":#
            desc_label.configure(image = haze_image)
        #
        elif main_wezer=="Clear":#
            desc_label.configure(image = night_image)# 
        #
        elif main_wezer=="Thunderstorm":
            desc_label.configure(image = storm_image)
        #
        elif main_wezer=="Rain": #
            desc_label.configure(image = night_rain_image)
        #
        elif main_wezer=="Clouds":
            if main_id == 804:
                desc_label.configure(image = night_cloudy_image)  
            elif main_id in [801,802,803]:
                desc_label.configure(image = cloudy_night)  

        #
        elif main_wezer=="Drizzle":#
            if main_id in [300, 310, 311]:
                desc_label.configure(image = drizzle_sun_image)
            elif main_id in [301, 302, 312, 313, 314, 321]:
                desc_label.configure(image = drizzle_image)    
        #   
        elif main_wezer=="Snow":#
            if main_id in [600, 601, 620, 612, 615, 616]:
                desc_label.configure(image = snowy_night_image)
            elif main_id in [602, 611, 613, 621, 622]:
                desc_label.configure(image = snowy_night_image)    
        #   
        else:
            desc_label.configure(image = vapros)







    upd_image = Ctk.CTkImage(light_image=Image.open(os.path.join(PATH, "update.png")), size=(25, 25))
    upd_baton4ik = Ctk.CTkButton(widget,width=25,height=25, text="", image=upd_image, fg_color="#163C5F", command=weather_update)
    upd_baton4ik.place(x = 302, y = 11)
#   
    def open_main_window(event):
        m_window.main_window_start()
    widget.after(1000, weather_update)
    widget.bind("<Double-Button-1>", open_main_window)
    widget.mainloop()
    


    
# start_widget()