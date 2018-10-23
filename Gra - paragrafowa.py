def mod1():  # Kuchnia
    print("""                         >>> Jesteś w Kuchni <<<   

          ###################################################
          #
          #
          #
          #        C   O   Ś            1
          #
          #
          #
          #
          ###################################################

  """)


def mod2():
    print("""                >>> Jesteś w Module Wypoczynku <<<   

          ###################################################
          #
          #
          #
          #       Io C   O   Ś            2
          #
          #
          #
          #
          ###################################################

  """)


def mod3():
    print("""                >>> Jesteś w Sypialni <<<   

          ###################################################
          #
          #
          #
          #        C   O   Ś            3
          #
          #
          #
          #
          ###################################################

  """)


def mod4():
    print("""                >>> Jesteś w Module Botanicznym <<<   

          ###################################################
          #
          #
          #
          #        C   O   Ś            4
          #
          #
          #
          #
          ###################################################

  """)


def mod5():
    print("""                >>> Jesteś w Module Łącznikowym <<<   

          ###################################################
          #
          #
          #
          #        C   O   Ś            5
          #
          #
          #
          #
          ###################################################

  """)


def mod6():
    print("""                >>> Jesteś w Module Serwisowym <<<   

          ###################################################
          #
          #
          #
          #        C   O   Ś            6
          #
          #
          #
          #
          ###################################################

  """)


def mod7():
    print("""                >>> Jesteś w Module Energetycznym <<<   

          ###################################################
          #
          #
          #
          #        C   O   Ś            7
          #
          #
          #
          #
          ###################################################

  """)


def mod8():
    print("""                >>> Jesteś w Module Module Ewakuacyjnym <<<   

          ###################################################
          #
          #
          #
          #        C   O   Ś            8
          #
          #
          #
          #
          ###################################################

  """)


pozycja = 0  # numer pozycji odpowiada pokojowi


def cls(): print


"\n" * 40


def cls2(): print


"\n" * 20


def move():  # funkcja poruszania sie pomiędzy pokojami

    cls()
    mod1()

    print("""         == == == ==  MENU  == == == ==

          << [1] Idź do Modułu Wypoczynku
          << [2] Wróć
    """)
    choice = input('                           ')  # przypisuje wybór
    if choice == 1:
        pozycja = 2
        cls()
        mod2()
        menu()

    if choice != 1:
        cls()
        mod1()
        menu()


def eq():
    print  # zeby wyswietlalo zawartosc equipment


def call():
    print  # dzwoni


def dialog():
    print  # rozmawia


def menu():
    print("""         == == == ==  MENU  == == == ==

                 >> Co chcesz zrobić?
          << [1] Idź gdzieś
          << [2] Zobacz ekwipunek
          << [3] Zadzwoń
          << [4] Rozmawiaj """)

    choice = input('                           ')

    if choice == 1:
        move()
    elif choice == 2:
        eq()
    elif choice == 3:
        call()
    elif choice == 4:
        dialog()
    else:
        intro()


def intro():  # funkcja wprowadzająca, wczesniej można dac jakieś prawdziwe intro
    pozycja = 1
    cls()
    mod1()
    menu()
    print
    pozycja  # to w sumie niepotrzebne, tylko do testu


intro()
