Memes = {'ЛОЛ':'очень смешно','КРИНЖ':'что-то странное, стыдное','РОФЛ':'шутка','ЩИЩ':'одобрение или восторг','КРИПОВЫЙ':'страшный, пугающий','АГРИТЬСЯ':'злиться'}

run = True
while run:
    word = input("Введите слово, которое хотите узнать:  ")
    if word in Memes.keys():
        print(Memes[word.upper()])
    else:
        print("Такого слова нет")
    
    if input("Завершить работу программы? (1 - да, 0 - нет)") == "1":
        run = False
