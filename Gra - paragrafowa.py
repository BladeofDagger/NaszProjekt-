# zmienne
bateria = 3
pozycja = 1


equipment = {
    "latarka" : bateria, # liczba określa poziom baterii
    "krótkofalówka" : " ",
    "kartki" : []
}







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

    pozycja = 1


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

    pozycja = 2


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

    pozycja = 3


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

    pozycja = 4


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

    pozycja = 5


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

    pozycja = 6


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

    pozycja = 7


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

    pozycja = 8


#pozycja = 0  # numer pozycji odpowiada pokojowi


def cls(): print ("\n" * 40) # poprawka na python 3.7





#def cls2(): print


#"\n" * 20


def move():  # funkcja poruszania sie pomiędzy pokojami

    cls()
# jesli jestesmy w kuchni to:
    if pozycja == 1:
        print("""         == == == ==  MENU  == == == ==

                  << [1] Idź do Modułu Wypoczynku
                  << [2] Wróć
            """)
        choice = input('                           ')  # przypisuje wybór
        if choice == 1:
            #pozycja = 2
            cls()
            mod2()
            menu()
        elif choice == 2:
            cls()
            mod1()
            menu()

# jesli jestesmy w module wypoczynkowym to:
    elif pozycja == 2:
        print("""         == == == ==  MENU  == == == ==

                          << [1] Idź do Modułu Serwisowego
                          << [2] Idź do Modułu Łącznikowego
                          << [3] Wróć
                           
                    """)
        choice = input('                           ')  # przypisuje wybór
        if choice == 1:
            #pozycja = 2 # pozycję najlepiej przypisac bezposrednio w modulach
            cls()
            mod3()
            menu()
        elif choice == 2:
            cls()
            mod4()
            menu()
        elif choice == 3:
            cls()
            mod1()
            menu()
    elif pozycja == 3:
        








def eq():
    # jeśli w ekwipunku nie ma jeszcze żadnej kartki to nie pokazuj
    if len(equipment["kartki"])== 0:
        print (""" == == == EKWIPUNEK == == ==
                
                latarka : poziom baterii %d 
                krótkofalówka""" % bateria )
    else:
        print ("""  == == == EKWIPUNEK == == ==
        
                latarka : poziom baterii %d 
                krótkofalówka
                kartki : %s """ % bateria, equipment["kartki"] )



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


        #intro()


def intro():  # funkcja wprowadzająca, wczesniej można dac jakieś prawdziwe intro

    cls()
    mod1()
    menu()
    print (pozycja)
      # to w sumie niepotrzebne, tylko do testu


intro()
