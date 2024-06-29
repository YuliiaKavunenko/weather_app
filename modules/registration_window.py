import os
import customtkinter
# import main_window as m_window
import modules.personal_window as personal_w
import modules.database as user_data
import requests

def start_registration():
    
#   
    root = customtkinter.CTk()
    # root = customtkinter.CTkToplevel(root)
    # root.attributes("-topmost", True)
    PATH = os.path.abspath(__file__+"/../../images")

    root.geometry("460x645")
    root.title("Реєстрація користувача")
    root.resizable(width=False, height=False)
    root.iconbitmap(os.path.join(PATH, "icon.ico"))
    root.configure(fg_color="#163C5F")
    our_font = customtkinter.CTkFont(family ="Roboto Slab",size=22)
    # main
    main_label = customtkinter.CTkLabel(master=root, text="Реєстрація користувача", font=("Roboto Slab",28), text_color="#FFFFFF")
    main_label.place(relx=0.155, rely=0.05)
    # country
    country_label = customtkinter.CTkLabel(master=root, text="Країна:", font=our_font, text_color="#FFFFFF")
    country_label.place(relx=0.1 , rely=0.145)
    country_entry = customtkinter.CTkEntry(master=root, width=218, height=46, corner_radius=20)
    country_entry.place(relx=0.1 ,rely=0.2)
    country_entry.configure(fg_color="#0D2841", border_color="#FFFFFF")
    # city
    city_label = customtkinter.CTkLabel(master=root, text="Місто:", font=our_font, text_color="#FFFFFF")
    city_label.place(relx=0.1 , rely=0.290)
    city_entry = customtkinter.CTkEntry(master=root, width=218, height=46, corner_radius=20)
    city_entry.place(relx=0.1 ,rely=0.355)
    city_entry.configure(fg_color="#0D2841", border_color="#FFFFFF")
    # name
    name_label = customtkinter.CTkLabel(master=root, text="Ім'я:", font=our_font, text_color="#FFFFFF")
    name_label.place(relx=0.1 , rely=0.445)
    name_entry = customtkinter.CTkEntry(master=root, width=218, height=46,corner_radius=20)
    name_entry.place(relx=0.1 ,rely=0.510)
    name_entry.configure(fg_color="#0D2841", border_color="#FFFFFF")
    # surname
    surname_label = customtkinter.CTkLabel(master=root, text="Прізвище:", font=our_font, text_color="#FFFFFF")
    surname_label.place(relx=0.1 , rely=0.6)
    surname_entry = customtkinter.CTkEntry(master=root, width=218, height=46,corner_radius=20)
    surname_entry.place(relx=0.1 ,rely=0.665)
    surname_entry.configure(fg_color="#0D2841", border_color="#FFFFFF")
    #error
    global error_label1
    error_label1 = customtkinter.CTkLabel(root, width=300, height=30, text='', text_color="#FFF0F0", font=("Roboto Slab", 15),anchor = 'center')
    error_label1.place(x = 74, y = 581)
    
    
    #registration
    def register():

        country = country_entry.get()
        city = city_entry.get()
        name = name_entry.get()
        surname = surname_entry.get()
        if city != "" and country != "" and name != "" and surname != "":
            weather_data = user_data.get_weather(city)
            if weather_data is not None:
                temperature, weather, maxtemp, mintemp, time_zone, main_wezer, main_id, response = weather_data
                # temperature, weather, maxtemp, mintemp, time_zone, main_wezer, main_id, response = user_data.get_weather(city)
                # if response.status_code == 200:
                user_data.cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?)",(country, city, name, surname))
                user_data.data_base.commit()
                #user_data.data_base.close()
                root.destroy()
                personal_w.personal_window_start()
            else:
                error_label1.configure(text = 'Не правильна назва міста')


        else:
            error_label1.configure(text = 'Не введені дані')
    #submit button
    submit_button = customtkinter.CTkButton(master = root, width = 218, height = 46, text = "Зберегти", text_color = "white", font = our_font,corner_radius=20, command=register, border_width= 2)
    submit_button.place(relx = 0.250, rely = 0.825)
    submit_button.configure(fg_color="#0D2841", border_color="#FFFFFF")
    root.mainloop()







































































































#помогите    -. -__. .. .--.--.-----..--