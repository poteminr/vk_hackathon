import re
import vk
TOKEN = "bbfbcbefbbfbcbefbbfbcbef3ebb971c09bbbfbbbfbcbefe680eafe0e533f85630e7c61"
session = vk.Session(access_token=TOKEN)
vk_api = vk.API(session)

def val_number(phone_nuber):
    pattern = re.compile("^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", re.IGNORECASE)
    return pattern.match(phone_nuber) is not None

def check_date(date:str):
    if len(date) == 10:
        if date[2] == "." and date[5] == ".":
            return True

    return False


def uid_to_name(user_id):
    user_name = vk_api.users.get(user_id=user_id, v=5.84)[0]
    first_name = user_name['first_name']
    last_name = user_name['last_name']

    name = f'{first_name} {last_name}'.strip()
    return name