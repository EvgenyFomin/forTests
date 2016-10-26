word = str("impressionism")
print(
    """
    ОТГАДАЙТЕ СЛОВО:
    Направление в искусстве последней трети XIX — начала XX веков,
    зародившееся во Франции и затем распространившееся по всему миру,
    представители которого стремились разрабатывать методы и приёмы,
    которые позволяли наиболее естественно и живо запечатлеть реальный мир
    в его подвижности и изменчивости, передать свои мимолётные впечатления.
    """)

print("В слове "+str(len(word))+" букв")
print("Давайте отгадаем слово, у вас есть пять попыток чтобы отгадать буквы")

TRIES = 5
guess_letters = []
star = '*'
comp_word = word
for i in range(TRIES):
    print("\nПопытка №"+str(i + 1)+":")
    letter = input("Ваша буква: ")
    if letter in word:
        print("Буква есть в слове\n")
        guess_letters += letter
    else:
        print("Буквы нет в слове\n")

if len(guess_letters) > 0:
    print("Вы отгадали " + str(len(guess_letters)) + " буквы")
    print("Это буквы: ")
    print(", ".join(guess_letters))
    print("\n\nОткрываем буквы в слове: ")
    for j in word:
        if j not in guess_letters:
            comp_word = comp_word.replace(j, '*')
    print(comp_word)
else:
    print("Вы не отгадали не одной буквы...")