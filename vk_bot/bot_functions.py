import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from keyboards import keyboard_start, keyboard_reg, keyboard_change, keyboard_name
import os
import json

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

def confirm_action(user_id, question_text, keyboard_type, USER_INFO):
    text = "Вы подтверждает ввод данных?"
    send_message(user_id, text, keyboard_reg)
    user_id, message_text = get_event()

    while message_text != "Подтвердить информацию о себе":
        send_message(user_id, question_text, keyboard_type, add_keyboard=False)
        user_id, message_text = get_event()
        USER_INFO = message_text

        send_message(user_id, text, keyboard_type)
        user_id, message_text = get_event() 

    return USER_INFO

def message_saved(user_id):
    text = "Информация сохранена"
    send_message(user_id, text, keyboard_reg, add_keyboard=False)

def save_userdata(user_id, user_metadata):
    path = "{}.json".format(user_id)

    if not os.path.exists(path):
        with open(path, "w") as write_file:
            json.dump(user_metadata, write_file)
