# Текстовая ферма
from time import sleep
from func import *

crop_stage = 0
money = 15

while True:
    action = input("Что хотите сделать? Введите ваш выбор: ").lower().strip()
    match action:

        case "status":
            status(money, crop_stage)
        case "exit":
            print("До новых встреч!")
            break
        case "help":
            show_help()
        case "plant":
            crop_stage, money = plant(money, crop_stage)
        case "water":
            crop_stage = water(crop_stage)
            sleep(1)
            crop_stage = random_event(crop_stage)
        case "harvest":
            crop_stage = harvest(crop_stage, money, randint(1, 10))
        case _:
            print("Неизвестная комманда, старайтесь лучше")
