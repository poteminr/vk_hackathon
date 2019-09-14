import re
def val_number(phone_nuber):
    pattern = re.compile("^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", re.IGNORECASE)
    return pattern.match(phone_nuber) is not None