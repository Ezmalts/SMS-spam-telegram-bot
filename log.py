def log_user(user_id):
    with open('users.txt', 'r+') as file:
        users = file.read()
        users += (user_id + '\n')
        file.write(users)


def log_phone(phone):
    with open('phones.txt', 'r+') as file:
        phones = file.read()
        phones += (phone + '\n')
        file.write(phones)
