import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from keyboards import keyboard, keyboard_reg, keyboard_change, keyboard_name, keyboard_admin
import os.path 
import glob
import bot_func as bf
import pickle
import time
import json
user_metadata = {}

TOKEN = "KEY"
GROUP_ID = 186480144

vk_session = vk_api.VkApi(token=TOKEN)

longpoll = VkBotLongPoll(vk_session, GROUP_ID)

send = "messages.send"



def send_message(user_id, text, keyboard_type, add_keyboard=True):
    if add_keyboard:
        vk_session.method(send, {"peer_id": user_id, "message": text,
        'keyboard': keyboard_type, "random_id": get_random_id()})
    else:
        vk_session.method(send, {"peer_id": user_id, "message": text,
         "random_id": get_random_id()})


def get_event():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            user_id = event.obj.from_id
            message_text = event.obj.text
            return user_id, message_text

def event_proccesing(text, keyboard_type):
    user_id, message_text = get_event()
    send_message(user_id, text, keyboard_type)
    return user_id, message_text


admin_ids = [312281474]
counter = 1
while True:
    try:
        path = glob.glob("*.json")[0]
        print(path)
        
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
            send_message(312281474, text, keyboard_admin)
            counter = 0
        
        mes_id, message_text = get_event()

        user_id = int(user_id)
        if mes_id == 312281474:

            if message_text == "Подтвердить":
                text = "Заявка подтверждена"
                send_message(admin_ids[0], text, keyboard_change, add_keyboard=False)
                text = "Вашу заявку приняли, ожидайте."
                send_message(user_id, text, keyboard_change, add_keyboard=False)

            
            elif message_text == "Отклонить":
                text = "Заявка отклонена"
                send_message(admin_ids[0], text, keyboard_change, add_keyboard=False)
                text = "Вашу заявку отклонили."
                send_message(user_id, text, keyboard_change, add_keyboard=False)
            os.remove(path)
            counter = 1
    except IndexError:
        time.sleep(5)