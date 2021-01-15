# 딕셔너리 + 반복문

character = {
    'id': '도끼살인자',
    'job': '기사',
    'level': 99,
    'hp': 1000,
    'mp': 100,
    'skill': ['썰기', '베기', '찌르기', '방패치기'],
    'items': ['검', '방패', '갑옷']

}
print(character)
# print('체력 : ', character['hp'])
char_itmes = character.items()
print(char_itmes)
# print(key, ':', value, type(value))
for key, value in char_itmes:
    if type(value) is list:
        # 리스트면~ 어떻게 출력할지
        for el in range(len(value)):
            print(key, ":", value[el])
    else:
        print(key, ':', value)
