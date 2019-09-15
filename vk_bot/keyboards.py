from vk_api.utils import get_random_id
import json



def compile_kboard(keyboard):

    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))

    return keyboard

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

keyboard_start = {
    "one_time": True,
    "buttons": [

    [get_button(label="Начать", color="default")]]
} 

keyboard_start = compile_kboard(keyboard_start)

keyboard_reg = {
    "one_time": True,
    "buttons": [

    [get_button(label="Подтвердить информацию о себе", color="positive")],
    [get_button(label="Изменить данные", color="primary")]]
} 

keyboard_reg = compile_kboard(keyboard_reg)

keyboard_change = {
    "one_time": True,
    "buttons": [

    [get_button(label="Изменить", color="default")]]
} 

keyboard_change = compile_kboard(keyboard_change)

keyboard_name = {
    "one_time": True,
    "buttons": [

    [get_button(label="Взять из VK", color="positive")],
    [get_button(label="Ввести ФИО", color="primary")]]
} 

keyboard_name = compile_kboard(keyboard_name)



keyboard_admin = {
    "one_time": True,
    "buttons": [

    [get_button(label="Подтвердить", color="positive")],
    [get_button(label="Отклонить", color="negative")]]
} 

keyboard_admin = compile_kboard(keyboard_admin)
