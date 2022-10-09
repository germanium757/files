while True:
    firstname = input("Введите имя:")
    secondname = input("Введите фамилию:")
    dateofbirth = input("Введите дату рождения:")
    file = open("test.txt", "w")
    file.write(firstname+'\n'+secondname+'\n'+dateofbirth)
    file.close()

