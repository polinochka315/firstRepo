import random 
 
password = "" 

def gen_password(password, count):
    password_gen = ""
    for i in range(int(count)): 
        index = random.randint(0, len(password)-1)
        password_gen += password[index]
    return password_gen

while password == "":
    current_password = input("Введите символы для пароля: ")
    if (current_password == ""):
        print("Вы ничего не ввели")
    else:
        password = current_password
        count = input("Введите длину пароля числом: ") 
        if (count.isdigit()): 
            gen_pass = gen_password(password, count)
            print("Получившийся пароль: ", gen_pass) 
        else: 
            print('Вы ввели не число')