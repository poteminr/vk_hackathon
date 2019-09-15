from keyboards import keyboard_start, keyboard_reg, keyboard_change, keyboard_name, keyboard_admin
from bot_functions import *
import os
import glob
import time
import json

user_metadata = {}
ADMIN_ID = 312281474
counter = 1

while True:
    try:
        path = glob.glob("*.json")[0]
        
        with open(path, "r") as read_file:
            user_data = json.load(read_file)
        
        user_id = path.split(".json")[0]

        name = user_data['FIO']
        user_info = user_data['about_user']
        phone = user_data["phone_number"]
        birthday = user_data['birthday']
        vk_link = user_data['vk_link']


        text = f"""
        ФИО: {name}
        О себе: {user_info}
        Номер телефона: {phone}
        Дата рождения: {birthday}
        Профиль vk: {vk_link} 
        """
        if counter == 1 :
            send_message(ADMIN_ID, text, keyboard_admin)
            counter = 0
        
        mes_id, message_text = get_event()

        user_id = int(user_id)
        if mes_id == ADMIN_ID:
            if message_text == "Подтвердить":
                text = "Заявка подтверждена"
                send_message(ADMIN_ID, text, keyboard_change, add_keyboard=False)
                text = "Вашу заявку приняли, ожидайте."
                send_message(user_id, text, keyboard_change, add_keyboard=False)

            elif message_text == "Отклонить":
                text = "Заявка отклонена"
                send_message(ADMIN_ID, text, keyboard_change, add_keyboard=False)
                text = "Вашу заявку отклонили."
                send_message(user_id, text, keyboard_change, add_keyboard=False)
            os.remove(path)

            counter = 1
    except IndexError:
        time.sleep(5)