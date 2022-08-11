# ## Part 1
# # variables
# x = 42
# y = "Coucou !"
#
# print(x)
# print(y)
#
# # type de variable
# z = "42"
# w = 1063
# print(w + x) # OK
# print(y + z) # OK
# # print(y + x) # Not OK
# # print(z + w) # Not OK
# print(y + str(x)) # OK
# print(int(z) + w) # OK
#
# a = 42
# print(a)
# a = 1063
# print(a)
# a = a + 42
# print(a)

# ## Part 2
# # Condition
#
# import random
#
# x = random.randint(1, 20)
#
# if (x >= 10) :
#     print("Bravo tu as au dessus de la moyenne ! tu as eu : " + str(x))
# else :
#     print("Dommage mais ne perds pas espoir ! Ton " + str(x) + " va s'envoler vers des sommets la prochaine fois.")
#
# if (x >= 15) :
#     print("Bravo tu as au dessus de 15 ! tu as eu : " + str(x))
# elif (x < 15 and x >= 10):
#     print("Bravo, entre 10 et 15 ! Tu as eu : " + str(x))
# else :
#     print("Dommage mais ne perds pas espoir ! Ton " + str(x) + " va s'envoler vers des sommets la prochaine fois.")
#
# y = random.randint(1, 4)
#
# if (y == 2 or y == 3) :
#     print("Tu as un nombre premier, et ça c'est beau ! Festoye avec ton " + str(y))
# else :
#     print("Tu n'as pas un nombre premier, la vie peut être triste parfois. Mais ne rejette pas ton " + str(y))


# ## Part 3
# # Boucles
#
# for i in range(10) :
#     print(i)
#
# for i in range(10) :
#     print("Tabla multiplication de " + str(i) + " : ")
#     for j in range(10) :
#         print(str(i) + "x" + str(j) + " = " + str(i*j))
#
# fruits = ["pomme", "banane", "cerise"]
# for x in fruits:
#   if x == "banane":
#     continue
#   print(x)
#
# for x in range(10) :
#     if x == 6:
#         continue
#     print(x)
#
# for x in range(10) :
#     if x == 6:
#         break
#     print(x)
#
# i = 1
# while i < 6:
#   print(i)
#   i += 1
#
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1
#
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
#
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# ## Part 4
# # Classes and objects
#
# class Chien() :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def showInfo(self):
#         print("Je m'apelle " + self.name)
#         print("J'ai " + str(self.age) + " années.")
#     def sound(self):
#         print("Wouf !")
#
# medor = Chien("Médor", "5")
# medor.showInfo()
# medor.sound()
#
# class Chat() :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def showInfo(self):
#         print("Je m'apelle " + self.name)
#         print("J'ai " + str(self.age) + " années.")
#     def sound(self):
#         print("Miaou !")
#
# felix = Chat("Félix", "4")
# felix.showInfo()
# felix.sound()

# class Animal() :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def showInfo(self):
#         print("Je m'apelle " + self.name)
#         print("J'ai " + str(self.age) + " années.")
#     def sound(self):
#         print("Regard gêné car on ne sait pas quel son cela fait. Déguerpis !")
#
# class Chien(Animal) :
#     def sound(self):
#         print("Wouf !")
# class Chat(Animal) :
#     def sound(self):
#         print("Miaou !")
# class Renard(Animal) :
#     def renarder(self):
#         print("Renart sacripant, sacripouille, coquet, coquin. Renart chenapan, chacripouille, sacré vaurien Renart")
#
#
# medor = Chien("Médor", 5)
# medor.showInfo()
# medor.sound()
#
# felix = Chat("Félix", 4)
# felix.showInfo()
# felix.sound()
#
# renart = Renard("Renart", 23)
# renart.showInfo()
# renart.sound()
# renart.renarder()

