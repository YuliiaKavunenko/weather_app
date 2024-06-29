import modules.database as data_b
import customtkinter
import modules.search_path as m_path
import modules.main_window as main_w
import modules.database as user_data
import os
from PIL import Image


def personal_window_start():
    PATH = os.path.abspath(__file__+"/../../images")
    import modules.file_widget as wg
    

    personal_area = customtkinter.CTk()
    
    personal_area.geometry("460x645")
    personal_area.title("Особистий кабінет")
    personal_area.resizable(width = False, height=False)
    personal_area.iconbitmap(os.path.join(PATH, "icon.ico"))
    personal_area.configure(fg_color="#163C5F")

    font1 = customtkinter.CTkFont("Roboto Slab", 28, underline=True)
#
    main_info_label = customtkinter.CTkLabel(master=personal_area, text="Особистий кабінет", font=("Roboto Slab", 28), text_color="#FFFFFF")
    main_info_label.place(relx=0.235, rely=0.05)

    user_data.cursor.execute("SELECT country FROM users")
    db_country = user_data.cursor.fetchone()[0]

    user_data.cursor.execute("SELECT city FROM users")
    db_city = user_data.cursor.fetchone()[0]

    user_data.cursor.execute("SELECT name FROM users")
    db_name = user_data.cursor.fetchone()[0]

    user_data.cursor.execute("SELECT surname FROM users")
    db_surname = user_data.cursor.fetchone()[0]

#
    country_info_label = customtkinter.CTkLabel(master=personal_area, text=f"Країна:", font=("Roboto Slab", 22), text_color="#FFFFFF")
    country_info_label.place(relx=0.1 , rely=0.145)

    country_info_text = customtkinter.CTkLabel(master=personal_area,text=f"{db_country}", font=font1, text_color="#FFFFFF")
    country_info_text.place(relx=0.3, rely=0.2)
#

    city_info_label = customtkinter.CTkLabel(master=personal_area, text=f"Місто:", font=("Roboto Slab", 22), text_color="#FFFFFF")
    city_info_label.place(relx=0.1 , rely=0.290)

    city_info_text = customtkinter.CTkLabel(master=personal_area, text=f"{db_city}", font=font1, text_color="#FFFFFF")
    city_info_text.place(relx=0.3, rely = 0.345)
#

    name_info_label = customtkinter.CTkLabel(master=personal_area, text=f"Ім'я:", font=("Roboto Slab", 22), text_color="#FFFFFF")
    name_info_label.place(relx=0.1 , rely=0.445)

    name_info_text = customtkinter.CTkLabel(master=personal_area, text=f"{db_name}", font=font1, text_color="#FFFFFF")
    name_info_text.place(relx = 0.3, rely = 0.5)
#

    surname_info_label = customtkinter.CTkLabel(master=personal_area, text=f"Прізвище:", font =("Roboto Slab", 22), text_color="#FFFFFF")
    surname_info_label.place(relx=0.1 , rely=0.6)

    surname_info_text = customtkinter.CTkLabel(master=personal_area, text=f"{db_surname}", font =font1, text_color="#FFFFFF")
    surname_info_text.place(relx=0.3 , rely=0.655)

    def next_window():
        personal_area.destroy()
        main_w.main_window_start()
    
    button_m = customtkinter.CTkButton(master = personal_area, width = 218, height = 46, text = "Перейти до додатку", text_color = "white", font = ("Roboto Slab", 22),corner_radius=20, command=next_window,  border_width= 2, border_color="#FFFFFF")
    button_m.place(relx = 0.2, rely = 0.825)
    button_m.configure(fg_color="#0D2841")
    
    def delete_db():
        data_b.data_base.close()
        os.remove("data_base.db")
        personal_area.destroy()    
        wg.widget.destroy()  
    # customtkinter.CTkImage(Image.open(os.path.join(PATH,"rain.png")), size=(171, 159))
    # image_button = customtkinter.CTkImage(Image.open(os.path.join(PATH,"exit.png")), size=(28, 29))
    
    button_e = customtkinter.CTkButton(master=personal_area, width=28, height=29, text = "Вихід",  compound="right", font = ("Roboto Slab", 13), command=delete_db)
    button_e.place(relx=0.8, rely = 0.01)
    button_e.configure(fg_color="#163C5F")

    personal_area.mainloop()

#personal_window_start()













































































































































































    #😬🥳🕺👍😘👍👄🤗😜😬😱👊👍🤭😯🍌🏴‍☠️💃💃🎸💃🎸👊🧁🧼👍💃💃😏👋🦸‍♂️🤪😅🏖🧛‍♂️😎👊🙂😛🤔😎🤔😘🤪👹🙂😶😯😐🫥💃😡😭