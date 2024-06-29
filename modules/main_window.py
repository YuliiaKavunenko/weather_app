import datetime
import customtkinter
from PIL import Image, ImageTk
import modules.database as m_data
import sqlite3
import os
import time as tm
import requests

def main_window_start():
    import modules.personal_window as p_window
    import modules.file_widget as widget
    PATH = os.path.abspath(__file__+"/../../images")

    # main = customtkinter.CTk()
    main = customtkinter.CTkToplevel(widget.widget)
    main.title("Погода")
    main.geometry("1200x800")
    main.resizable(width = False, height=False)
    main.iconbitmap(os.path.join(PATH, "icon.ico"))
    main.configure(fg_color="#163C5F")

    #
    user_location = customtkinter.CTkLabel(main, width=314, height=61, text="Поточна позиція", font=("Roboto Slab", 35), text_color="#FFFFFF")
    user_location.place(x = 576, y = 101)
    

    m_data.cursor.execute("SELECT name FROM users")
    db_name = m_data.cursor.fetchone()[0]

    m_data.cursor.execute("SELECT surname FROM users")
    db_surname = m_data.cursor.fetchone()[0]

    m_data.cursor.execute("SELECT * FROM users")
    data = m_data.cursor.fetchall()
    if len(data) == 0:
        pass
    else:
        m_data.cursor.execute("SELECT city FROM users")
        db_city = m_data.cursor.fetchone()[0]
    

    #
    user_city = customtkinter.CTkLabel(main, width=314, height=31, text=f"{db_city}", font=("Roboto Slab", 22), text_color="#FFFFFF")
    user_city.place(x = 576, y=162)
    
    temp, weather, maxtemp, mintemp, time_zone, main_wezer, main_id, response  = m_data.get_weather(f"{db_city}")
    print(time_zone)

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
    
    time_date_data, time, date, week_day1 = find_date(time_zone)
    
    # кнопка поиска
    
    user_temp = customtkinter.CTkLabel(main, width=314, height=31, text=f"{temp} °", font=("Roboto Slab", 58), text_color="#FFFFFF")
    user_temp.place(x = 576, y=193)

    user_weather = customtkinter.CTkLabel(main, width=314, height=31, text=f"{weather}", font=("Roboto Slab", 26), text_color="#FFFFFF")
    user_weather.place(x = 576, y=260)

    min_temp_user = customtkinter.CTkLabel(main, width=314, height=31, text=f"↓{mintemp}°  ↑{maxtemp}°", font=("Roboto Slab", 35), text_color="#FFFFFF")
    min_temp_user.place(x = 576, y=300)
    ###########################
    week_day = customtkinter.CTkLabel(main, width=200, height=31, text=week_day1, font=("Roboto Slab", 18), text_color="#FFFFFF")
    week_day.place(x = 936, y=191)

    user_date = customtkinter.CTkLabel(main, width=200, height=47, text=date, font=("Roboto Slab", 35), text_color="#FFFFFF")
    user_date.place(x = 936, y=227)

    user_time = customtkinter.CTkLabel(main, width=200, height=47, text=time, font=("Roboto Slab", 22), text_color="#FFFFFF")
    user_time.place(x = 936, y=274)


    # Загружаем и сохраняем картинки погоды
    # os.path.join(PATH, "название_картинки.png")
    cloudy_image = customtkinter.CTkImage(Image.open(os.path.join(PATH, "cloudy.png")), size=(171, 159))
    drizzle_sun_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"drizzle_sun.png")), size=(171, 159))
    drizzle_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"drizzle.png")), size=(171, 159))
    freezing_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"freezing.png")), size=(171, 159))
    night_cloudy_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"night_cloudy.png")), size=(171, 159))
    night_rain_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"night_rain.png")), size=(171, 159))
    light_rain_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"rain.png")), size=(171, 159))
    small_cloudy_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"small_cloudy.png")), size=(171, 159))
    rain_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"small_rain.png")), size=(171, 159))
    snowy_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"snowy.png")), size=(171, 159))
    small_snowy_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"small_snowy.png")), size=(171, 159))
    storm_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"storm.png")), size=(171, 159))
    sun_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"sun.png")), size=(171, 159))
    snowy_night_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"snowy_night.png")), size=(171, 159))
    vapros = customtkinter.CTkImage(Image.open(os.path.join(PATH, "vapros.png")), size=(171, 159))
    haze_image = customtkinter.CTkImage(Image.open(os.path.join(PATH, "dym.png")), size=(171, 159))
    night_image = customtkinter.CTkImage(Image.open(os.path.join(PATH,"night_clean.png")), size=(171, 159))
    cloudy_night = customtkinter.CTkImage(Image.open(os.path.join(PATH,"cloudy.png")), size=(171, 159))
    storm_el = customtkinter.CTkImage(Image.open(os.path.join(PATH,"storm_el.png")), size=(171, 159))
    heavy_snow = customtkinter.CTkImage(Image.open(os.path.join(PATH,"heavy_snow.png")), size=(171, 159))
    snowy_rain = customtkinter.CTkImage(Image.open(os.path.join(PATH,"snowy_rain.png")), size=(171, 159))
    night_drizzle = customtkinter.CTkImage(Image.open(os.path.join(PATH,"night_drizzle.png")), size=(171, 159))

    desc_label = customtkinter.CTkLabel(main, width=171, height=159, text="", bg_color="#163C5F")
    desc_label.place(x = 380, y = 171)
    
    # проверка погоды find image 

    hour = time_date_data.strftime("%H")
    print(hour)

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
    # c = customtkinter.CTkImage(Image.open(os.path.join(PATH, "snowy_night_.png")), size=(171, 159))
    # desc_label.configure(image = c)
    def opening_personal_area():
        main.destroy()
        p_window.personal_window_start()
        

    personal_area_image = customtkinter.CTkImage(Image.open(os.path.join(PATH, "personal_area.png")), size=(49, 50))
    personal_area_button = customtkinter.CTkButton(master = main, width = 282, height = 50, text = f"{db_name} {db_surname}", text_color = "white", font = ("Roboto Slab", 14), image=personal_area_image, fg_color = "#163C5F", command=opening_personal_area)
    personal_area_button.place(y = 29, x = 318 )
    
    

    frame1 = customtkinter.CTkScrollableFrame(main, width=275, height=770, scrollbar_button_color="#FFFFFF")
    frame1.place(x = 0, y=133)
    frame1.configure(fg_color ="#0D2841", bg_color = '#0D2841', corner_radius=20)


    frame_2 = customtkinter.CTkFrame(master=main, width=275.5, height=163)
    frame_2.place(x =0,y=0)
    frame_2.configure(fg_color ="#0D2841", bg_color = '#0D2841')

    class Tekushya_pozicia(customtkinter.CTkFrame):
        def __init__(self, frame_2, temperature, town, weather, min, max):
            super().__init__(master = frame_2)######################
            self.configure(width=236,height=101, border_width=2, border_color="#D3D3D3", fg_color="#163C5F", corner_radius=20)
            self.pack(pady = 32, padx = 37.5) 
            self.locationuser = customtkinter.CTkLabel(self, width=1, height=0, font = ("Roboto Slab", 15), text="Поточна позиція", text_color="#FFFFFF").place(x = 16, y = 13)
            self.cityuser = customtkinter.CTkLabel(self, width=1, height=1, font = ("Roboto Slab", 14), text=f"{town}", text_color="#FFFFFF")
            self.cityuser.place(x = 16, y = 32)
            self.temperature = customtkinter.CTkLabel(self, width=1, height=1, font = ("Roboto Slab", 50), text=f"{temperature}°", text_color="#FFFFFF")
            self.temperature.place(x = 157, y = 3)
            self.userminmax = customtkinter.CTkLabel(self, width=1, height=1, font = ("Roboto Slab", 12), text=f"макс.: {max}° мін.: {min}°", text_color="#FFFFFF")
            self.userminmax.place(x = 115, y = 75)
            self.weather = customtkinter.CTkLabel(self, width=1, height=1, font = ("Roboto Slab", 12), text=f"{weather}", text_color="#FFFFFF")
            self.weather.place(x = 16, y = 75)
        def update_data(self, new_temp, new_city, new_min, new_max, new_weather):
            self.temperature.configure(text = f"{new_temp}°")
            self.cityuser.configure(text = f"{new_city}" )
            self.userminmax.configure(text = f"макс.: {new_min}° мін.: {new_max}°")
            self.weather.configure(text = f"{new_weather}")
    
    # city_squares
    locuser = Tekushya_pozicia(frame_2=frame_2, temperature=temp, town=db_city, weather=weather, min=mintemp, max=maxtemp)
            
    class City_frame_scroll(customtkinter.CTkFrame):
        def __init__(self, frame1, text, temp, weather, maxtemp, mintemp, time):
            super().__init__(master=frame1)

            self.configure(width=236, height=101, corner_radius=20, border_width=2, border_color="#D3D3D3", fg_color="#0D2841")
            self.pack(pady = 20, padx = 10)
            self.text0 = customtkinter.CTkLabel(self, width=1, height=1, font = ("Roboto Slab", 16), text=f"{text}", text_color="#FFFFFF").place(x = 16, y = 13)
            self.text2 = customtkinter.CTkLabel(self, width=1, height=1, font = ("Roboto Slab", 12), text=time, text_color="#FFFFFF")
            self.text2.place(x = 16, y = 32)
            self.update_time(time, time_zone1)
            self.text3 = customtkinter.CTkLabel(self, width=1, height=1, font = ("Roboto Slab", 12), text=f"{weather}", text_color="#D3D3D3").place(x = 16, y = 75)
            self.text4 = customtkinter.CTkLabel(self, width=1, height=1, font = ("Roboto Slab", 50), text=f"{temp}°", text_color="#FFFFFF").place(x = 150, y = 5)
            self.text5 = customtkinter.CTkLabel(self, width=1, height=1, font = ("Roboto Slab", 12), text=f"макс.: {maxtemp}° мін.: {mintemp}°", text_color="#D3D3D3").place(x = 115, y = 75)

        def update_time(self, new_time, new_time_zone):
            time_date_data3, time3, date3, week_day4 = find_date(new_time_zone)
            self.text2.configure(text = time3)
            self.after(10, self.update_time, new_time, new_time_zone) 

    for i in range(7):
        temp1, weather1, maxtemp1, mintemp1, time_zone1, main_wezer1, main_id1, response1 = m_data.get_weather(m_data.city_list[0+i])
        time_date_data1, time1, date1, week_day2 = find_date(time_zone1)
        frame = City_frame_scroll(frame1, text=m_data.city_list[0+ i], temp = temp1, weather=weather1, maxtemp=maxtemp1, mintemp=mintemp1, time =time1)
    
    # функция обновления города
    global error_label
    error_label = customtkinter.CTkLabel(main, width=100, height=100, text="", text_color="#FFF0F0", font=("Roboto Slab", 15))
    error_label.place(x = 930, y = 45)

    frame666 = customtkinter.CTkScrollableFrame(main, width=718, height=200, scrollbar_button_color="#FFFFFF", orientation="horizontal", border_color="#FFFFFF", border_width=5)
    frame666.place(x = 373, y=455)
    frame666.configure(fg_color ="#0D2841", corner_radius=20)

    class BarPragnoz(customtkinter.CTkFrame):
        def __init__(self, frame666, temp666, image666, time666):
            super().__init__(master = frame666)
            self.configure(width = 55, height = 149, fg_color = '#0D2841')
            self.pack(padx = 12, pady = 0)
            self.time = customtkinter.CTkLabel(self, width=51, height=31, font = ("Roboto Slab", 18), text=f"{time666}", text_color="#FFFFFF", fg_color = '#0D2841')
            self.time.place(x = 2, y = -5)
            self.image = customtkinter.CTkLabel(self, width=54, height=50,text="",image=image666, fg_color = '#0D2841')
            self.image.place(x = 0, y = 35)
            self.temp = customtkinter.CTkLabel(self, width=34, height=27, font = ("Roboto Slab", 28), text=f"{temp666}", text_color="#FFFFFF", fg_color = '#0D2841')
            self.temp.place(x = 6.5, y = 100)
        def change_image(self, new_image):
            self.image.configure(image=new_image)
                
            
    b = customtkinter.CTkImage(Image.open(os.path.join(PATH, "night_drizzle.png")), size=(54, 50))
    nimber = 0
    sunrise_1, sunset_1, response2 = m_data.hour_weather(f"{db_city}", i = nimber)
    # i = 0
    # for haver in hour_w2:
    #     # print(i)
    #     wrema, temp_c, hour_w, sunrise, sunset = m_data.hour_weather(f"{db_city}", i = i)
    #     kvadratik = BarPragnoz(frame666 = frame666, temp666 = f'{temp_c}°', image666 = b, time666 = wrema)
    #     kvadratik.pack(side = "left")
    #     i +=1


    def save_city():
        city_update = search.get()
        
        if city_update != "":
            wdata = m_data.get_weather(f"{city_update}")
            if wdata is not None:
                temp__, weather__, maxtemp__, mintemp__, time_zone__, main_wezer__, main_id__, response__  = m_data.get_weather(f"{city_update}")
                error_label.configure(text = "")

                if response__.status_code == 200:
                    i = 0
                    new_sunrise, new_sunset, res = m_data.hour_weather(f"{city_update}", i = i)
                    if res.status_code == 200:
                        global widget_data
                        widget_data = city_update
                        error_label.configure(text = "")

                        # new_sunrise, new_sunset = m_data.hour_weather(f"{city_update}", i = i)
                        temp_up, weather_up, maxtemp_up, mintemp_up, time_zone_up, main_wezer_up, main_id_up, response_up  = m_data.get_weather(f"{city_update}")
                        connect = sqlite3.connect("data_base.db")
                        cursor = connect.cursor()
                        #m_data.cursor.execute(f"UPDATE users SET city = '{city_update}'")
                        cursor.execute(f"UPDATE users SET city = '{city_update}'")
                        time_date_data_up, time_up, date_up, week_day1_up = find_date(time_zone_up)
                        user_city.configure(text = f"{city_update}")
                        user_temp.configure(text = f"{temp_up}°")
                        user_weather.configure(text = f"{weather_up}")
                        min_temp_user.configure(text = f"↓{mintemp_up}°  ↑{maxtemp_up}°")
                        user_date.configure(text = date_up)
                        user_time.configure(text = time_up)
                        week_day.configure(text = week_day1_up)
                        locuser.update_data(new_temp = temp_up, new_city=city_update, new_min=mintemp_up, new_max=maxtemp_up, new_weather=weather_up)
                        label_sans.configure(text=f"Захід Сонця о {new_sunset}. Світанок о {new_sunrise}")

                        update_hour(city_update)
                        #main.after(10, apdet_time_up, time_zone_up)

                        hour_up = time_date_data_up.strftime("%H")
                        print(f"{hour_up} hour")
                        if hour_up in ["04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]:
                            if main_wezer_up=="Atmosphere":#
                                desc_label.configure(image = haze_image)
                            #
                            elif main_wezer_up=="Clear":#
                                desc_label.configure(image = sun_image)# 
                            #
                            elif main_wezer_up=="Thunderstorm":
                                desc_label.configure(image = storm_image)
                            #
                            elif main_wezer_up=="Rain": #
                                desc_label.configure(image = rain_image)  
                            #
                            elif main_wezer_up=="Clouds":
                                if main_id_up == 804:
                                    desc_label.configure(image = cloudy_image)  
                                elif main_id_up in [801,802,803]:
                                    desc_label.configure(image = small_cloudy_image)  

                            #
                            elif main_wezer_up=="Drizzle":#
                                if main_id_up in [300, 310, 311]:
                                    desc_label.configure(image = drizzle_sun_image)
                                elif main_id_up in [301, 302, 312, 313, 314, 321]:
                                    desc_label.configure(image = drizzle_image)    
                            #   
                            elif main_wezer_up=="Snow":#
                                if main_id_up in [600, 601, 620, 612, 615, 616]:
                                    desc_label.configure(image = small_snowy_image)
                                elif main_id_up in [602, 611, 613, 621, 622]:
                                    desc_label.configure(image = snowy_image)    
                            #   
                            else:
                                desc_label.configure(image = vapros)
                        elif hour_up in ["18", "19", "20", "21", "22", "23", "00", "01", "02", "03"]:
                            if main_wezer_up=="Atmosphere":#
                                desc_label.configure(image = haze_image)
                            #
                            elif main_wezer_up =="Clear":#
                                desc_label.configure(image = night_image)# 
                            #
                            elif main_wezer_up=="Thunderstorm":
                                desc_label.configure(image = storm_image)
                            #
                            elif main_wezer_up=="Rain": #
                                desc_label.configure(image = night_rain_image)
                            #
                            elif main_wezer_up=="Clouds":
                                if main_id_up == 804:
                                    desc_label.configure(image = night_cloudy_image)  
                                elif main_id_up in [801,802,803]:
                                    desc_label.configure(image = cloudy_night)  

                            #
                            elif main_wezer_up=="Drizzle":#
                                if main_id_up in [300, 310, 311]:
                                    desc_label.configure(image = drizzle_sun_image)
                                elif main_id_up in [301, 302, 312, 313, 314, 321]:
                                    desc_label.configure(image = drizzle_image)    
                            #   
                            elif main_wezer_up=="Snow":#
                                if main_id_up in [600, 601, 620, 612, 615, 616]:
                                    desc_label.configure(image = snowy_night_image)
                                elif main_id_up in [602, 611, 613, 621, 622]:
                                    desc_label.configure(image = snowy_night_image)    
                            #   
                            else:
                                desc_label.configure(image = vapros)
                        connect.commit()
                    connect.close()

                # hour_weather(f"{city_update}")
                else:
                    error_label.configure(text = "Не правильна назва міста!")
            else:
                error_label.configure(text = "Не правильна назва міста!")
        else:
            error_label.configure(text = "Тут порожньо")
            print("б")
    def apdet_time(time_zone):
        time_date_data2, time2, date2, week_day2 = find_date(time_zone)

        user_time.configure(text=time2)
        main.after(10, apdet_time, time_zone)
    def apdet_time_up(time_zone_up):
        time_date_data2, time_up, date2, week_day2 = find_date(time_zone_up)

        user_time.configure(text=time_up)
        main.after(10, apdet_time_up, time_zone_up)

    # кнопка поиска
    image_search = customtkinter.CTkImage(light_image=Image.open(os.path.join(PATH, "search.png")), size=(27, 27))
    search_p = customtkinter.CTkButton(main, width=27, height=27, text="", image=image_search, bg_color="#5DA7B1", fg_color="#5DA7B1", command=save_city)
    search_p.place(x = 870, y = 35)
    search_p.configure(fg_color = "#163C5F", bg_color ="#163C5F")
    
    # поиск

    search = customtkinter.CTkEntry(main, width=218, height=46, corner_radius=20, placeholder_text="пошук", font=("Roboto Slab", 18))
    search.place(x = 918, y = 31)
    # search.children
    search.configure(fg_color="#0D2841", border_color="#FFFFFF", placeholder_text_color="#FFFFFF")

    #темпаретарнавсегдавсердце
    # темпарутар 🕯️🌹🫡f🥲😭
    # time_hour = time_zone // 3600

    # sunset = sunset + datetime.timedelta(hours=time_hour)
    # sunrise = sunrise + datetime.timedelta(hours=time_hour)

    label_sans = customtkinter.CTkLabel(master = main, text_color = "#FFFFFF", font = ("Roboto Slab", 14), text=f"Захід Сонця о {sunset_1}. Світанок о {sunrise_1}", width = 0, height = 0, fg_color = '#0D2841')
    # label_sans.pack() 
    label_sans.place(x = 407, y = 475)
    



    global hour_weather
    
    def hour_weather(city):
        api_key2 = "5c3c27af2a8a49bb923164323231512"
        url2 = f'http://api.weatherapi.com/v1/forecast.json?key={api_key2}&q={city}&days=1&aqi=no&alerts=yes'
        response2 = requests.get(url2)
        print(response2)
        line_image = customtkinter.CTkImage(Image.open(os.path.join(PATH, "line.png")), size=(1900, 2.5))
        line_label = customtkinter.CTkLabel(master = frame666,text = "", width = 1200, height = 10, image = line_image)
        line_label.pack(pady=15)
        if response2.status_code == 200:
            data2 = response2.json()
            #print(data2)
            forecast = data2["forecast"]["forecastday"][0]["hour"]#["temp_c"]
    
            # weather = forecast[5]["condition"]["text"]
            #print(time)
            # print(temp_c)
            # print(weather)
            i = 0
            
            # temp_c = round(forecast[i]["temp_c"])
            # time = forecast[i]["time"].split()[1]
            cloudy_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH, "cloudy.png")), size=(54, 50))
            drizzle_sun_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"drizzle_sun.png")), size=(54, 50))
            # drizzle_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"drizzle.png")), size=(54, 50))
            freezing_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"freezing.png")), size=(54, 50))
            night_rain_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"night_rain.png")), size=(54, 50))
            light_rain_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"rain.png")), size=(54, 50))
            small_cloudy_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"small_cloudy.png")), size=(54, 50))
            rain_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"small_rain.png")), size=(54, 50))
            snowy_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"snowy.png")), size=(54, 50))
            small_snowy_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"small_snowy.png")), size=(54, 50))
            storm_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"storm.png")), size=(54, 50))
            sun_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"sun.png")), size=(54, 50))
            snowy_night_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"snowy_night.png")), size=(54, 50))
            vapros_ = customtkinter.CTkImage(Image.open(os.path.join(PATH, "vapros.png")), size=(54, 50))
            haze_image_ = customtkinter.CTkImage(Image.open(os.path.join(PATH, "dym.png")), size=(54, 50))
            cloudy_night_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"night_cloudy.png")), size=(54, 50))
            storm_el_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"storm_el.png")), size=(54, 50))
            heavy_snow_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"heavy_snow.png")), size=(54, 50))
            snowy_rain_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"snowy_rain.png")), size=(54, 50))
            night_drizzle_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"night_drizzle.png")), size=(54, 50))
            night_clean_ = customtkinter.CTkImage(Image.open(os.path.join(PATH,"night_clean.png")), size=(54, 50))
                
            i = 0
            for haver in forecast:
                # print(i)
                code = forecast[i]["condition"]["code"]
                print(code)
                kvadratik = BarPragnoz(frame666 = frame666, temp666 = f'{round(forecast[i]["temp_c"])}°',image666=None, time666 = forecast[i]["time"].split()[1])
                kvadratik.pack(side = "left")
                if i in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
                    if code == 1000:#солнечно
                        kvadratik.change_image(sun_image_)
                    elif code == 1003:#немножко хмарно
                        kvadratik.change_image(small_cloudy_image_)# 
                    elif code in [1006,1009]:#хмарно
                        kvadratik.change_image(cloudy_image_)
                    elif code in [1030, 1135, 1147]:#туман
                        kvadratik.change_image(haze_image_)  
                    elif code in [1063, 1150,1153,1180,1184,1186,1189]:#дождь мини
                        kvadratik.change_image(rain_image_)    
                    elif code in [1066, 1069,1072,1210,1213,1216,1219,1237,1255]:#мини снег
                        kvadratik.change_image(small_snowy_image_) 
                    elif code == 1087:#гроза
                        kvadratik.change_image(snowy_image_) 
                    elif code in [1114,1117,1222,1225,1258]:#сильный снег
                        kvadratik.change_image(snowy_image_) 
                    elif code == 1168:#изморозь
                        kvadratik.change_image(freezing_image_) 
                    elif code == 1171:#сильный ледяной снег/дождь
                        kvadratik.change_image(heavy_snow_) 
                    elif code in [1192,1195,1243,1246]:#ливень
                        kvadratik.change_image(drizzle_sun_image_)
                    elif code in [1198,1201,1204,1207,1249,1252,1261,1264]:#ледяной дождь
                        kvadratik.change_image(snowy_rain_)    
                    elif code == 1240:#дождь моросит
                        kvadratik.change_image(light_rain_image_) 
                    elif code in [1273,1276,1279,1282]:#дождь и гроза
                        kvadratik.change_image(storm_image_) #
                    else:
                        kvadratik.change_image(vapros_)
                # НОЧЬ
                elif i in [18, 19, 20, 21, 22, 23, 0, 1, 2, 3]:
                    if code == 1000:#
                        kvadratik.change_image(night_clean_)
                    #
                    elif code == 1003:
                        kvadratik.change_image(cloudy_night_)# 
                    #
                    elif code in [1006,1009]:
                        kvadratik.change_image(cloudy_image_)
                    #

                    elif code in [1030, 1135, 1147]:#туман
                        kvadratik.change_image(haze_image_)  
                    #
                    elif code in [1063, 1150, 1153, 1180, 1184, 1186, 1189]:#дождь мини
                        kvadratik.change_image(night_rain_image_) 
                    #   
                    elif code in [1066, 1069,1072,1210,1213,1216,1219,1237,1255]:#мини снег
                        kvadratik.change_image(snowy_night_image_)  
                    #   
                    elif code == 1087:#гроза
                        kvadratik.change_image(storm_el_) 
                        
                    elif code in [1114,1117,1222,1225,1258]:#сильный снег
                        kvadratik.change_image(snowy_image_) 

                    elif code == 1168:#изморозь
                        kvadratik.change_image(freezing_image_) 
                        
                    elif code == 1171:#сильный ледяной снег/дождь
                        kvadratik.change_image(heavy_snow_) 

                    elif code in [1192,1195,1243,1246]:#ливень
                        kvadratik.change_image(night_drizzle_)

                    elif code in [1198,1201,1204,1207,1249,1252,1261,1264]:#ледяной дождь
                        kvadratik.change_image(snowy_image_)
                         
                    elif code == 1240:#дождь моросит
                        kvadratik.change_image(light_rain_image_) 
                    elif code in [1273,1276,1279,1282]:#дождь и гроза
                        kvadratik.change_image(storm_image_) 
                    else:
                        kvadratik.change_image(vapros_)
                i +=1

            # for haver in forecast:
            
            #     temp_c = round(forecast[i]["temp_c"])
            #     time = forecast[i]["time"].split()[1]
            #     print(time)
            #     i += 1    
            #     print(temp_c)
            
            #print(forecast)
        else:
            print("zagranpasport ")


    hour_weather(f"{db_city}")
    def update_hour(city):
        for widget in frame666.winfo_children():
            widget.destroy()
        hour_weather(city)


    #main.after(10, apdet_time, time_zone)
    # frame666.destroy()
    # print(f"{time_zone} после функции")
    # main.mainloop()


#main_window_start()

































#господи помилуй даст бог даст бог









# #.-- -.--  .- .... ..- . .-.. ..  --. .-. .- ...- -.. .- -. . 
 
 
#  -.. --- ...- -.. -..-  -. .-  ... -. . --.  .--. --- ---- . .-.. 
 
 
#  .-- -.--  ---. .  ... ..- -.- .-  --. --- .-.. --- .-.. . -..  .... --- - .. - . 
 
 
#  - .-  .-.-  -... .-.. .-.- - -..- 
 
 
#  --.- .- ...  .-- --- --.. -..- -- ..-  -.- --- .-. --- .-.. .-.- 
 
 
#  ..  - .- -.-  ...- .. .-- --- -  . --. ---  ... --- ...- -- ..-  ---. - ---  --. .-.. --- -... .- .-.. -..- -. --- .  .--. --- - . .--. .-.. . -. .. .  -. .- ---. -. . - ... .-.- 
 
 
#  ..  -. .. -.- .- -.- --- .---  --.. .. -- -.--  -... .-.. .-.- - -..- 
 
 
#  .-.. . - ---  .-.. . - ---  ..  .-.. . - ---  -... ..- -.. . - 
 
#  ..-. .. .-.. --- ... J ..-.  .-- --- --.- --.- .  ..- -... .. .-.. ..  -... . --.. ..- -- -. -.-- .---  .- .-. - .... .- ..- ... --..--  [ ..--- ---.. .-.-.- .---- .---- .-.-.- ..--- ----- ..--- ...--  ..--- ----- ---... .---- -.... ] 
#  ..  - -.--  --.. .- --. .- -.. --- ---. -. -.-- .---  -.- --- -. . ---. -. --- --..--  - .-- --- .. ....  .-. ..- -.-  -.. . .-.. ---  ..-.. - --- -  -.. --- ...- -.. -..-  -.. .-



#господи помилуй даст бог даст бог