import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from keyboards import keyboard, keyboard_reg, keyboard_change, keyboard_name
import pickle
import os
import json
import bot_func as bf
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

while True:
    user_id, message_text = get_event()
    if message_text == "Начать":
        profile_name = bf.uid_to_name(user_id)
        text = f"Взять имя из профиля - {profile_name} ?"
        send_message(user_id, text, keyboard_name)

    user_id, message_text = get_event()

    if message_text == "Взять из VK":
        USER_FIO = profile_name

    elif message_text == "Ввести ФИО":
        text = "Введите свое ФИО"
        send_message(user_id, text, keyboard_reg, add_keyboard=False)

        user_id, message_text = get_event()
        USER_FIO = message_text

        
        text = "Вы подтверждает ввод данных?"
        send_message(user_id, text, keyboard_reg)
        user_id, message_text = get_event()

        while message_text != "Подтвердить информацию о себе":
            text = "Введите свое ФИО"
            send_message(user_id, text, keyboard_reg, add_keyboard=False)
            user_id, message_text = get_event()
            USER_FIO = message_text

            text = "Вы подтверждает ввод данных?"
            send_message(user_id, text, keyboard_reg)
            user_id, message_text = get_event()
            

    user_metadata['FIO'] = USER_FIO
    user_metadata['vk_link'] = f"https://vk.com/id{user_id}"

    text = "Информация сохранена"
    send_message(user_id,text, keyboard_reg, add_keyboard=False)

    # О себе
    text = "Пожалуйста, напишите развернуто о себе."
    send_message(user_id, text, keyboard_reg, add_keyboard=False)
    user_id, message_text = get_event()
    ABOUT_USER = message_text

    text = "Вы подтверждает ввод данных?"
    send_message(user_id,text, keyboard_reg)

    user_id, message_text = get_event()

    while message_text != "Подтвердить информацию о себе":
        text = "Пожалуйста, расскажите о себе"
        send_message(user_id, text, keyboard_reg, add_keyboard=False)
        user_id, message_text = get_event()
        ABOUT_USER = message_text

        text = "Вы подтверждает ввод данных?"
        send_message(user_id, text, keyboard_reg)
        user_id, message_text = get_event()

    user_metadata['about_user'] = ABOUT_USER

    text = "Информация сохранена"
    send_message(user_id,text, keyboard_reg, add_keyboard=False)




    # Номер телефона
    text = "Введите номер телефона"
    send_message(user_id,text, keyboard_reg, add_keyboard=False)


    user_id, message_text = get_event()
    USER_NUMBER = message_text

    while not bf.val_number(message_text):
        text = "Введите верный номер телефона"
        send_message(user_id, text, keyboard_reg, add_keyboard=False)

        user_id, message_text = get_event()
        USER_NUMBER = message_text


    user_metadata["phone_number"] = USER_NUMBER

    text = "Информация сохранена"
    send_message(user_id,text, keyboard_reg, add_keyboard=False)



    # Дата рождения
    text = "Введите дату своего рождения в формате: 01.01.1970"
    send_message(user_id,text, keyboard_reg, add_keyboard=False)

    user_id, message_text = get_event()
    USER_BIRTH = message_text

    while not bf.check_date(message_text):
        text = "Введите дату рождения в соответствии с форматом"
        send_message(user_id, text, keyboard, add_keyboard=False)

        user_id, message_text = get_event()
        USER_BIRTH = message_text

    user_metadata["birthday"] = USER_BIRTH

    text = "Информация сохранена"
    send_message(user_id,text, keyboard, add_keyboard=False)



    name = user_metadata['FIO']
    user_info = user_metadata['about_user']
    phone = user_metadata["phone_number"]
    birthday = user_metadata['birthday']
    vk_link = user_metadata['vk_link']


    last_text = f"""
    ФИО: {name}
    О себе: {user_info}
    Номер телефона: {phone}
    Дата рождения: {birthday}
    Профиль vk: {vk_link} 

    Ожидайте подтверждения администратора
    """
    send_message(user_id,last_text, keyboard)

    path = "{}.json".format(user_id)

    if not os.path.exists(path):
        with open(path, "w") as write_file:
            json.dump(user_metadata, write_file)

