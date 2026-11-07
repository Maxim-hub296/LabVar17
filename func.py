from random import randint


def start_screen():
    print("Добро пожаловать на ферму! Здесь мы будем растить культуры и зарабатывать на этом деньги!")
    print("""
        На этой ферме вы можете:
        Сажать растения (plant)
        Поливать их (water)
        Собирать зрелые культуру (harvest)
        Посмотреть как поживают ваши культуры (status)
        Продовать созревшие культуры (sell)
        Получить справку (help)
        И уйти на выходной (exit) 
        """)


def status(money, stage):
    print(f"Ваш капитал: {money}. Уровень вашего растения: {stage}")


def show_help():
    print("""
    На этой ферме вы можете:
    Сажать растения (plant)
    Поливать их (water)
    Собирать зрелые культуру (harvest)
    Посмотреть как поживают ваши культуры (status)
    И уйти на выходной (exit) 
    """)


def plant(money: int, stage):
    if money >= 10 and stage == 0:
        money -= 10
        stage = 1
        print(f"Вы посадили растение! Его уровень {stage}, а ваш капитал {money}")
    elif money < 10:
        print("У вас недостаточно денег")
    elif stage >= 0:
        print("Растение уже посажено (не логично, но по условию лабы у вас одна грядка)")
    return stage, money


def water(stage):
    if stage < 3:
        stage += 1
        print(f"Вы полили растение! Теперь его уровень {stage}")
    elif stage == 0:
        print("Вы еще не посадили растение! Крайне не выгодно поливать землю!")
    else:
        print(f"Растение не переживет еще одну поливку! Уровень вашего растения максимальный")
    return stage


def harvest(stage, money, bonus=0):
    if stage >= 3:
        money += 15 + bonus
        stage = 0
        print(f"Вы успешно собрали культуру! Ваш капитал {money} (Бонус: {bonus})")
    else:
        print(
            f"Ваша кульутра еще не выросла! Ее уровень {stage}. Вы сможете собрать через {3 - stage} уровня")
    return stage


def random_event(stage):
    random_event = randint(1, 10)
    if random_event % 2 == 0:
        stage += 1
        print(f"Пошел чудесный дождь! Ваши растения растут быстрее! Теперь их уровень: {stage}")
    else:
        stage -= 1
        print(f"На ваш уражай напали злостные вредители! Ваши растения повреждены :( Теперь их уровень: {stage}")
    return stage
