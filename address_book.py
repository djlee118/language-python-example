# create data type

addresses = [
    {'id': 1, 'name': 'hong kildong', 'email': 'hong@mail.com', 'hp_num': '010-222-3333'},
    {'id': 2, 'name': 'lee soonsin', 'email': 'lee@mail.com', 'hp_num': '010-222-3333'},
    {'id': 3, 'name': 'jang youngsil', 'email': 'jan@mail.com', 'hp_num': '010-222-3333'},
    {'id': 4, 'name': 'king sejong', 'email': 'king@mail.com', 'hp_num': '010-222-3333'}
]

addresses_new = {
    '1': {'name': 'hong kildong', 'email': 'hong@mail.com', 'hp_num': '010-222-3333'},
    '2': {'name': 'lee soonsin', 'email': 'lee@mail.com', 'hp_num': '010-222-3333'},
    '3': {'name': 'jang youngsil', 'email': 'jan@mail.com', 'hp_num': '010-222-3333'},
    '4': {'name': 'king sejong', 'email': 'king@mail.com', 'hp_num': '010-222-3333'}
}

print(addresses)
print(addresses_new)