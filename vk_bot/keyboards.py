from vk_api.utils import get_random_id
import json
def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

keyboard = {
    "one_time": True,
    "buttons": [

    [get_button(label="Начать", color="default")]]
} 

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))


keyboard_reg = {
    "one_time": True,
    "buttons": [

    [get_button(label="Подтвердить информацию о себе", color="positive")],
    [get_button(label="Изменить данные", color="primary")]]
} 

keyboard_reg = json.dumps(keyboard_reg, ensure_ascii=False).encode('utf-8')
keyboard_reg = str(keyboard_reg.decode('utf-8'))


keyboard_change = {
    "one_time": True,
    "buttons": [

    [get_button(label="Изменить", color="default")]]
} 

keyboard_change = json.dumps(keyboard_change, ensure_ascii=False).encode('utf-8')
keyboard_change = str(keyboard_change.decode('utf-8'))


keyboard_name = {
    "one_time": True,
    "buttons": [

    [get_button(label="Взять из VK", color="positive")],
    [get_button(label="Ввести ФИО", color="primary")]]
} 

keyboard_name = json.dumps(keyboard_name, ensure_ascii=False).encode('utf-8')
keyboard_name = str(keyboard_name.decode('utf-8'))



keyboard_admin = {
    "one_time": True,
    "buttons": [

    [get_button(label="Подтвердить", color="positive")],
    [get_button(label="Отклонить", color="negative")]]
} 

keyboard_admin = json.dumps(keyboard_admin, ensure_ascii=False).encode('utf-8')
keyboard_admin = str(keyboard_admin.decode('utf-8'))