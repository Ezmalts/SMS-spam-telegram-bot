def check_phone(phone):
    try:
        res = int(phone)
        return True
    except:
        return False
