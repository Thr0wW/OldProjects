import random
import string
adjectives = ['adorable','aggressive','alert','attractive','beautiful',  'blushing', 'colorful', 'crowded','cute','drab','distinct', 'dull','excited','fancy','filthy','glamourous','gleaming','gorgeou']
nouns=['year' ,'man' ,'time' ,'business' ,'life' ,'day' ,'hand' ,'work' ,'word' ,'place' ,'question' ,'face' ,'eye' ,'country' ,'friend' ,'side' ,'house' ,'case' ,'child']
print ('Dобро пожаловать!')
while True:
    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    number=random.randrange(0, 100)
    special_char=random.choice(string.punctuation)
    
    password=adjective + noun + str(number) + special_char
    print ('Новый пароль:%s' % password)


    response=input('Cгенерировать другой пароль? Выберите да или нет: ')
    if response == 'нет':
        break









