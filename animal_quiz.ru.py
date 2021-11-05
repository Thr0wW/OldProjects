def check_guess(guess, answer):
    global score
    still_guessing=True
    attemp=0
    while still_guessing and attemp < 3:
        if guess.lower()==answer.lower():
            print('Ответ верный!')
            score=score+1
            still_guessing=False
        else:
            if attemp<2:
                guess = input('Ответ неверный.Попробуйте еще раз.')
            attemp=attemp+1

        if attemp==3:
            print('Правильный ответ:')


            
score=0
print('Тест "Животные"')
guess1=input('Какой медведь живет за полярнычм кругом? ')
check_guess(guess1,'Белый медведь')
guess2=input('Какое сухопутное животное самое быстрое? ')
check_guess(guess2,'Гепард')
guess3=input('Какое животное самое большое? ')
check_guess(guess3,'Китовая акула')
print('Bы набрали очков:' + str(score))
