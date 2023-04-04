# n1 = int(input("Введите начало диапазона: "))
# n2 = int(input("Введите конец диапазона: "))
# i = n1
# while i <= n2:
#     print(i)
#     i = i + 1
# i = n2
# while i >= n1:
#     print(i)
#     i = i - 1
# i = n1
# while i <= n2:
#     if i % 7 == 0:
#         print(i)
#     i = i + 1



# n1 = int(input("Введите начало диапазона: "))
# n2 = int(input("Введите конец диапазона: "))
#
# i = n1
# s = i + n2
# while i <= n2:
#         if i % 2 == 0:
#                 print(i)
#         i = i + 1

# n = 1
# s = 0
# while n != 0:
#         n = int(input())  #складываем вводные числа
#         s = s + n
#         if n == 0:
#                 print(s)

# n1 = int(input())  #начало
# n2 = int(input())    #конец диапазона
# s1 = 0   #сумма чётных
# s2 = 0   #сумма нечётных
# s3 = 0   #сумма кратных 9
# k1 = 0   #кол-во чётных
# k2 = 0   #кол-во нечётных
# k3 = 0   #кол-во кратных 9
# i = n1
#
# while i <= n2:
#     if i % 9 == 0:
#         s3 += i        #если это условие ставлю на третье место с пометкой elif оно не работает
#         k3 += 1           #почему не понятно, это логика???
#     elif i % 2 == 0:
#         s1 += i
#         k1 += 1
#     elif i / 2:
#         s2 += i
#         k2 += 1
#
#     i = i + 1
# print("Сумма чётных: ", s1)
# print("Сумма нечётных: ", s2)
# print("Сумма кратных 9: ", s3)
# print("Среднеарифмическое чётных: ", s1 // k1)
# print("Среднеарифмическое нечётных: ", s2 // k2)
# print("Среднеарифмическое кратных 9: ", s3 // k3)




# while True:
#     a = int(input("Введите первое число: "))
#     if a == 7:
#         print("Good buy")
#         break
#     b = int(input("Введите второе число: "))
#     if b == 7:
#         print("Good buy")
#         break
#     # if a == 7 or b == 7:
#     #     print("Good buy")
#     #     break
#     if a > b:
#         print("max", a)
#         print("min", b)
#     else:
#         print("min", a)
#         print("max", b)
#     print("summa", a + b)
#     break

# string = "!world!"
# symbol = "!"
# count = 0
# for element in string:
#     if element == symbol:
#         count += 1
# print(count)

# string = "? who ? you ?"
# symbol = "?"
# count = 0
# for element in string:
#     if element == symbol:
#         count += 1
# print(count)


# string = "ships tacked"
# s = string.replace("tacked", "military")
# print(s)


# count = 0
# list_ = [0, 3, 6, 10, 15, 101, 74, 105, 110, 0]
# for i in (list_):
#     if i % 10 == 0:
#         count += 1
# print(count)


# string_ = "Sasha walked along the highway and sucked dry"
# print(string_.count("a"))
# #print(string_[1])
# string_ = string_.replace("a", "b", 1)
# print(string_)



#string = "? who ? you ?"
# symbol = "?"
# count = 0
# for element in string:
#     if element == symbol:
#         count += 1
# print(count)


# import random
#
# list_ = []
# sum1 = 0 # sum chet
# sum2 = 0 # sum ne chet
# sum3 = 0 # sum otric
#
# list_ = [random.randint(-5, 20) for i in range(1, 10)]
# print(list_)
# for i in list_:
#     if i % 2 == 0 and i > 0:
#         sum1 += i
#     if i % 2 != 0 and i > 0:   # and добавил для удобства
#         sum2 += i
#     if i < 0:
#         sum3 += i
# print(sum1)
# print(sum2)
# print(sum3)


# class Customer:  #Фамилия, Имя, Отчество, Номер банковского счета
#     def __init__(self, name1, name2, name3, number_bank):
#         self.name1 = name1
#         self.name2 = name2
#         self.name3 = name3
#         self.number_bank = number_bank
# Petrov = Customer("Петров", "Иван", "Сергеевич", 4563525256872131)
# print(Petrov.name1, Petrov.name2, Petrov.name3, Petrov.number_bank)
#
# Ivanov = Customer("Иванов", "Сергей", "Владиславович", 45636748572131)
# print(Ivanov.name1, Ivanov.name2, Ivanov.name3, Ivanov.number_bank)
#
# Tkach = Customer("Ткач", "Елена", "---", 435365471223)
# print(Tkach.name1, Tkach.name2, Tkach.name3, Tkach.number_bank)


    #return




#
# def parametr(parameter_1, parameter_2):
#     i = parameter_1
#     while i <= parameter_2 - 2:
#         i += 1
#         if i % 2 == 0:
#             print(i)
# parameter_1 = int(input("Введите первое число параметра: "))
# parameter_2 = int(input("Введите второе число параметра: "))
# parametr(parameter_1, parameter_2)
#
#
# def square(n, s, f):
#     r = s * n
#     if not f:
#         m = s + " " * (n - 2) + s
#     else:
#         m = r
#     print(r)
#     for i in range(n - 2):
#         print(m)
#     print(r)
#
# square(5, "#", True)
# print("")
# square(5, "*", False)



# spisok = [1,70,33,4,5]
# for i in range(len(spisok)):
#     if(spisok[i]==33):
#         break
#     print(i)

b =2
if b > 4:
    b = b = b + 2
    print(b)

#sshbdbdbdb