from keyboards import keyboard_start, keyboard_reg, keyboard_change, keyboard_name
import val_func as vf
from bot_functions import * 


user_metadata = {}

while True:
    user_id, message_text = get_event()
    if message_text == "Начать":
        profile_name = vf.uid_to_name(user_id)
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

        q_text = "Введите свое ФИО"
        USER_FIO = confirm_action(user_id, q_text, keyboard_reg, USER_FIO)
            

    user_metadata['FIO'] = USER_FIO
    user_metadata['vk_link'] = f"https://vk.com/id{user_id}"

    message_saved(user_id)

    # О себе
    text = "Пожалуйста, напишите развернуто о себе."
    send_message(user_id, text, keyboard_reg, add_keyboard=False)
    user_id, message_text = get_event()
    ABOUT_USER = message_text

    q_text = "Пожалуйста, расскажите о себе"
    ABOUT_USER = confirm_action(user_id, q_text, keyboard_reg, ABOUT_USER)

    user_metadata['about_user'] = ABOUT_USER

    message_saved(user_id)

    # Номер телефона
    text = "Введите номер телефона"
    send_message(user_id,text, keyboard_reg, add_keyboard=False)


    user_id, message_text = get_event()
    USER_NUMBER = message_text

    while not vf.val_number(message_text):
        text = "Введите верный номер телефона"
        send_message(user_id, text, keyboard_reg, add_keyboard=False)

        user_id, message_text = get_event()
        USER_NUMBER = message_text


    user_metadata["phone_number"] = USER_NUMBER

    message_saved(user_id)

    # Дата рождения
    text = "Введите дату своего рождения в формате: 01.01.1970"
    send_message(user_id,text, keyboard_reg, add_keyboard=False)

    user_id, message_text = get_event()
    USER_BIRTH = message_text

    while not vf.check_date(message_text):
        text = "Введите дату рождения в соответствии с форматом"
        send_message(user_id, text, keyboard_start, add_keyboard=False)

        user_id, message_text = get_event()
        USER_BIRTH = message_text

    user_metadata["birthday"] = USER_BIRTH

    message_saved(user_id)

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

    send_message(user_id,last_text, keyboard_start)

    save_userdata(user_id, user_metadata)