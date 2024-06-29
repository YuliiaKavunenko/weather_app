import modules.database as data_b
import modules.main_window as m_window
import modules.personal_window as p_window
import modules.registration_window as r_window
import modules.search_path as s_path
import modules.file_widget as widget
import os
import sqlite3


#нет виджета - нет проблем
data_b.cursor.execute("SELECT * FROM users")
data = data_b.cursor.fetchall()
if len(data) == 0:
    r_window.start_registration()
    widget.start_widget()
else:
    widget.start_widget()
    # m_window.main_window_start()
