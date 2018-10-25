#biblioteki
from time import sleep
from random import *


# zmienne ###########
bateria = 3
pozycja = 1 #globalnie bez sensu

global q
q = 1 #zmienna dla misji

global noc
noc = 0 # dla noc == 0 bedzie jasno, dla noc == 1 będzie ciemno i nie będzie nic widać bez latarki

global on
on = 0 # 1 dla włączonej latarki, 0 dla wyłączonej



######################

def cls(): print ("\n" * 40) # poprawka na python 3.7

def cls2(): print ("\n" * 5)

def quest(q):
    cls()
    if (q == 1):
        print("""
                    == == ==  Misja 1  == == == 
         
         Rozejrzyj się po Kuchni w celu rozpoznania szkód oraz
         oszacuj ilość prowiantu, który Wam pozostał.""")
    cls2()
    menu()

    if (q == 2):
        print("""
                    == == ==  Misja 2  == == == 

         COŚ TU BĘDZIE""")
    cls2()
    menu()

    if (q == 3):
        print("""
                    == == ==  Misja 3  == == == 

         COŚ TU BĘDZIE""")
    cls2()
    menu()

    if (q == 4):
        print("""
                    == == ==  Misja 4  == == == 

         COŚ TU BĘDZIE""")
    cls2()
    menu()


def Test():
    print("""
=============================================================================
=============================================================================

UU        UU     WW           WW       AAAAA         GGGGGG          AAAAA
UU        UU     WWW         WWW     AAA   AAA     GGG     GG      AAA   AAA
UU        UU     WWW    W    WWW    AAA     AAA   GGG             AAA     AAA
UUU      UUU     WWW   WWW   WWW    AAA AAA AAA   GGG    GGGG     AAA AAA AAA
 UUU    UUU       WWW WW WW WWW     AAA     AAA    GGG     GG     AAA     AAA
    UUUU            WWW   WWW       AAA     AAA     GGGGGGGG      AAA     AAA
!
!
!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!
!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!                  
!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!                         
!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!
!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!
!
!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!
!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!     !!!
!
!
!       Dostosuj rozmiar konsoli do tego komunikatu, aby całość była dobrze
!       widoczna.
!
!
!
!
!
!
!
!""")
Test()
uwaga = input("""!
!
!
!
!                   >>> NACIŚNIJ COKOLWIEK, ABY KONTYNUOWAĆ <<<
!
=============================================================================
=============================================================================    
    """)



def flash(): #latarka
    print("""
                   == == ==  LATARKA  == == ==         
                        
                         >> Czy chcesz użyć latarkę?
                  << [1] Tak
                  << [2] Nie
                  """)


    choice = input('                           ')

    if choice == "1":
        cls()
        print(("                 Włączono latarkę. Pozostałe baterie: %s") % bateria)
        cls2()

        on = 1

    if choice == "2":
        print

        on = 0


def mapa(pozycja):
    if pozycja == 1:
        print("""                         >>> Jesteś w Kuchni <<< 


                     == == == ==  MAPA  == == == ==         

                 # # # # # # # # # # # # # # # #
                 #    3    #    2    #    1    #  1. Kuchnia
                 #         #         #         #  2. Moduł Spoczynkowy
                 #         |         |   [X]   #  3. Moduł Serwisowy
                 #         #         #         #  4. Moduł Łącznikowy
                 #         #         #         #  5. Moduł Botaniczny
                 # # # # # # # ___ # # # # # # #  6. Moduł Badawczy
                 #    6    #    4    #    5    #  7. Moduł Energetyczny
                 #         #         #         #  8. Moduł Nawigacyjny
                 #         |         |         #  
                 #         #         #         # [X] -  Twoja pozycja
                 #         #         #         #  |  -  Przejście
                 # # # # # # # ___ # # # # # # #
                 #              7              # 
                 #                             #  
                 #                             #
                 # # # # # # # ___ # # # # # # #
                           #    8    #
                           #         #
                           #         #                          
                           # # # # # #

            """)

    elif pozycja == 2:
        print("""                >>> Jesteś w Module Wypoczynku <<<   

                             == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Spoczynkowy
                         #         |   [X]   |         #  3. Moduł Serwisowy
                         #         #         #         #  4. Moduł Łącznikowy
                         #         #         #         #  5. Moduł Botaniczny
                         # # # # # # # ___ # # # # # # #  6. Moduł Badawczy
                         #    6    #    4    #    5    #  7. Moduł Energetyczny
                         #         #         #         #  8. Moduł Nawigacyjny
                         #         |         |         #  
                         #         #         #         # [X] -  Twoja pozycja
                         #         #         #         #  |  -  Przejście
                         # # # # # # # ___ # # # # # # #
                         #              7              # 
                         #                             #  
                         #                             #
                         # # # # # # # ___ # # # # # # #
                                   #    8    #
                                   #         #
                                   #         #                          
                                   # # # # # #

                """)

    elif pozycja == 3:
        print("""                >>> Jesteś w Module Serwisowym <<<   

                             == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Spoczynkowy
                         #   [X]   |         |         #  3. Moduł Serwisowy
                         #         #         #         #  4. Moduł Łącznikowy
                         #         #         #         #  5. Moduł Botaniczny
                         # # # # # # # ___ # # # # # # #  6. Moduł Badawczy
                         #    6    #    4    #    5    #  7. Moduł Energetyczny
                         #         #         #         #  8. Moduł Nawigacyjny
                         #         |         |         #  
                         #         #         #         # [X] -  Twoja pozycja
                         #         #         #         #  |  -  Przejście
                         # # # # # # # ___ # # # # # # #
                         #              7              # 
                         #                             #  
                         #                             #
                         # # # # # # # ___ # # # # # # #
                                   #    8    #
                                   #         #
                                   #         #                          
                                   # # # # # #

                """)

    elif pozycja == 4:
        print("""                >>> Jesteś w Module łącznikowym <<<   

                             == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Spoczynkowy
                         #         |         |         #  3. Moduł Serwisowy
                         #         #         #         #  4. Moduł Łącznikowy
                         #         #         #         #  5. Moduł Botaniczny
                         # # # # # # # ___ # # # # # # #  6. Moduł Badawczy
                         #    6    #    4    #    5    #  7. Moduł Energetyczny
                         #         #         #         #  8. Moduł Nawigacyjny
                         #         |   [X]   |         #  
                         #         #         #         # [X] -  Twoja pozycja
                         #         #         #         #  |  -  Przejście
                         # # # # # # # ___ # # # # # # #
                         #              7              # 
                         #                             #  
                         #                             #
                         # # # # # # # ___ # # # # # # #
                                   #    8    #
                                   #         #
                                   #         #                          
                                   # # # # # #

                """)

    elif pozycja == 5:
        print("""                >>> Jesteś w Module Botanicznym <<<   

                             == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Spoczynkowy
                         #         |         |         #  3. Moduł Serwisowy
                         #         #         #         #  4. Moduł Łącznikowy
                         #         #         #         #  5. Moduł Botaniczny
                         # # # # # # # ___ # # # # # # #  6. Moduł Badawczy
                         #    6    #    4    #    5    #  7. Moduł Energetyczny
                         #         #         #         #  8. Moduł Nawigacyjny
                         #         |         |   [X]   #  
                         #         #         #         # [X] -  Twoja pozycja
                         #         #         #         #  |  -  Przejście
                         # # # # # # # ___ # # # # # # #
                         #              7              # 
                         #                             #  
                         #                             #
                         # # # # # # # ___ # # # # # # #
                                   #    8    #
                                   #         #
                                   #         #                          
                                   # # # # # #

                """)

    elif pozycja == 6:
        print("""                >>> Jesteś w Module Badawczym <<<   

                             == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Spoczynkowy
                         #         |         |         #  3. Moduł Serwisowy
                         #         #         #         #  4. Moduł Łącznikowy
                         #         #         #         #  5. Moduł Botaniczny
                         # # # # # # # ___ # # # # # # #  6. Moduł Badawczy
                         #    6    #    4    #    5    #  7. Moduł Energetyczny
                         #         #         #         #  8. Moduł Nawigacyjny
                         #   [X]   |         |         #  
                         #         #         #         # [X] -  Twoja pozycja
                         #         #         #         #  |  -  Przejście
                         # # # # # # # ___ # # # # # # #
                         #              7              # 
                         #                             #  
                         #                             #
                         # # # # # # # ___ # # # # # # #
                                   #    8    #
                                   #         #
                                   #         #                          
                                   # # # # # #

                """)

    elif pozycja == 7:
        print("""                >>> Jesteś w Module Energetycznym  <<<   

                             == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Spoczynkowy
                         #         |         |         #  3. Moduł Serwisowy
                         #         #         #         #  4. Moduł Łącznikowy
                         #         #         #         #  5. Moduł Botaniczny
                         # # # # # # # ___ # # # # # # #  6. Moduł Badawczy
                         #    6    #    4    #    5    #  7. Moduł Energetyczny
                         #         #         #         #  8. Moduł Nawigacyjny
                         #         |         |         #  
                         #         #         #         # [X] -  Twoja pozycja
                         #         #         #         #  |  -  Przejście
                         # # # # # # # ___ # # # # # # #
                         #              7              # 
                         #             [X]             #  
                         #                             #
                         # # # # # # # ___ # # # # # # #
                                   #    8    #
                                   #         #
                                   #         #                          
                                   # # # # # #

                """)

    elif pozycja == 8:
        print("""                >>> Jesteś w Module Nawigacyjnym <<<   

                             == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Spoczynkowy
                         #         |         |         #  3. Moduł Serwisowy
                         #         #         #         #  4. Moduł Łącznikowy
                         #         #         #         #  5. Moduł Botaniczny
                         # # # # # # # ___ # # # # # # #  6. Moduł Badawczy
                         #    6    #    4    #    5    #  7. Moduł Energetyczny
                         #         #         #         #  8. Moduł Nawigacyjny
                         #         |         |         #  
                         #         #         #         # [X] -  Twoja pozycja
                         #         #         #         #  |  -  Przejście
                         # # # # # # # ___ # # # # # # #
                         #              7              # 
                         #                             #  
                         #                             #
                         # # # # # # # ___ # # # # # # #
                                   #    8    #
                                   #   [X]   #
                                   #         #                          
                                   # # # # # #

                """)


# poczatkowe wartosci
equipment = {
    "Latarka" : bateria, # liczba określa poziom baterii
    "Krótkofalówka" : " ",
    "Kartki" : [],
    "Mapa" : []
}



# pusta lista przygotowana na ofiary Slendera ;)
dead = []

# nasz gracz zawsze będzie ostatnim elementem listy więc załoga[4]
załoga = ["Dave","Steve","John","Ann"]

# tu będą teksty które mówią poszczególne osoby
# kf= krótkofalówka
Dave_kf = {
    "mod_badawczy ": "Super jest!",
    "mod_botaniczny": "Okej ",
    "mod_ener":"Wszystko Gra",
    "mod_nawig":" Suhe"


}

Dave_dialog = {
    "mod_badawczy ": "",
    "mod_botaniczny": "",
    "mod_ener":"",
    "mod_nawig":""

    }

Steve_kf = {
    "mod_badawczy ": "",
    "mod_botaniczny": "",
    "mod_ener":"",
    "mod_nawig":""

}

Steve_dialog = {
    "mod_badawczy ": "",
    "mod_botaniczny": "",
    "mod_ener":"",
    "mod_nawig":""

}

John_kf = {
    "mod_badawczy ": "",
    "mod_botaniczny": "",
    "mod_ener":"",
    "mod_nawig":""

}

John_dialog = {
    "mod_badawczy ": "",
    "mod_botaniczny": "",
    "mod_ener":"",
    "mod_nawig":""
}

Ann_kf= {
    "mod_badawczy ": "",
    "mod_botaniczny": "",
    "mod_ener":"",
    "mod_nawig":""
}

Ann_dialog = {
    "mod_badawczy ": "",
    "mod_botaniczny": "",
    "mod_ener":"",
    "mod_nawig":""

}

#dictionary z nazwami modułów i listami, na początku resztę załogi przydzielamy
# losowo do modułów = zapisujemy na daną listę

mod = {
    "mod_badawczy": [],
    "mod_botaniczny": [],
    "mod_ener": [],
    "mod_nawig": []

}


def mod1():  # Kuchnia
    print("""                         >>> Jesteś w Kuchni <<<   
        
        Wszystkie zapasy żywności i wody znajdują się tutaj. Dostrzegasz,
        że jest coś nie tak. Niektóre meble są przewrócone. Co się tutaj
        stało?! Ktoś musiał być tutaj wcześniej.

        """)

    global pozycja
    pozycja = 1


def mod2():
    print("""                >>> Jesteś w Module Wypoczynku <<<   

        Widzisz znajdujące się tutaj łóżka, rzeczy załogi oraz sprzęt
        rozrywkowy. Wygląda na to, że nic tutaj się nie działo.

        """)
    global pozycja
    pozycja = 2


def mod3():
    print("""                >>> Jesteś w Module Serwisowym <<<   

          

        """)
    global pozycja
    pozycja = 3


def mod4():
    print("""                >>> Jesteś w Module łącznikowym <<<   

        Moduł ten łączy pozostałe pomieszczenia statku.       

        """)
    global pozycja
    pozycja = 4


def mod5():
    print("""                >>> Jesteś w Module Botanicznym <<<   

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
    global pozycja
    pozycja = 5


def mod6():
    print("""                >>> Jesteś w Module Badawczym <<<   

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
    global pozycja
    pozycja = 6


def mod7():
    print("""                >>> Jesteś w Module Energetycznym  <<<   

        W tym pomieszczeniu znajdują się silniki, paliwo oraz cała
        mechanika i elektronika statku. Ich awaria oznaczałaby katastrofę.  

        """)
    global pozycja
    pozycja = 7


def mod8():
    print("""                >>> Jesteś w Module Nawigacyjnym <<<   

        To tutaj podejmowane są najważniejsze decyzje oraz znajduje
        się tutaj panel sterowania pojazdem. Z tyłu możesz dostrzec
        umieszczone kapsuły ewakuacyjne, które są jednak zablokowane.
        Bez karty - klucza nie uda Ci się ich odblokować.

        """)
    global pozycja
    pozycja = 8


#pozycja = 0  # numer pozycji odpowiada pokojowi




def move():  # funkcja poruszania sie pomiędzy pokojami

    cls()
# jesli jestesmy w kuchni to:
    if pozycja == 1:
        print("""                 == == == ==  MENU  == == == ==

                  << [1] Idź do Modułu Wypoczynku
                  << [2] Wróć
                  
            """)
        choice = input('                           ')  # przypisuje wybór
        if choice == "1":
            #pozycja = 2
            cls()
            mod2()
            menu() # nie ma sensu wywoływać ,,wróć bo sytuacja troche sie komplikuje przy dalszych modulach
        if choice == "2":
            cls()
            mod1()
            menu()
# jesli jestesmy w module wypoczynkowym to:
    elif pozycja == 2:
        print("""         == == == ==  MENU  == == == ==

                          << [1] Idź do Modułu Serwisowego
                          << [2] Idź do Modułu Łącznikowego
                          << [3] Idź do Kuchni
                          << [4] Wróć
                           
                    """)
        choice = input('                           ')  # przypisuje wybór
        if choice == "1":
            #pozycja = 2 # pozycję najlepiej przypisac bezposrednio w modulach
            cls()
            mod3()
            menu()
        elif choice == "2":
            cls()
            mod4()
            menu()
        elif choice == "3":
            cls()
            mod1()
            menu()
        elif choice == "4":
            cls()
            mod2()
            menu()

    # jesli jestesmy w module serwisowym to:
    elif pozycja == 3:
        print("""         == == == ==  MENU  == == == ==

                                  << [1] Idź do Modułu Wypoczynku
                                  << [2] Wróć
                                  
                            """)
        choice = input('                           ')  # tu mozna dac wroc bo nie ma innej opcji
        if choice == "1":
            cls()
            mod2()
            menu()
        if choice == "2":
            cls()
            mod3()
            menu()

    elif pozycja == 4:
        print("""         == == == ==  MENU  == == == ==

                            << [1] Idź do Modułu Botanicznego
                            << [2] Idź do Modułu Energetycznego
                            << [3] Idż do Modułu Badawczego
                            << [4] Idź do Modułu Wypoczynkowego
                            << [5] Wróć

                           """)
        choice = input('                           ')  # przypisuje wybór
        if choice == "1":
            cls()
            mod5()
            menu()
        elif choice == "2":
            cls()
            mod7()
            menu()
        elif choice == "3":
            cls()
            mod6()
            menu()
        elif choice == "4":
            cls()
            mod2()
            menu()
        elif choice == "5":
            cls()
            mod4()
            menu()

    # gdy jestes w module botanicznym lub  w module badawczym lub nawigacyjnym : to
    elif (pozycja == 5):
        print("""         == == == ==  MENU  == == == ==

                                << [1] Idź do Modułu Łącznikowego
                                << [2] Wróć

                                   """)
        choice = input('                           ')
        if choice == "1":
            cls()
            mod4() # mod4!!!!
            menu()
        elif choice == "2":
            cls()
            mod5()
            menu()

    elif (pozycja == 6):
        print("""         == == == ==  MENU  == == == ==

                                        << [1] Idź do Modułu Łącznikowego
                                        << [2] Wróć

                                           """)
        choice = input('                           ')
        if choice == "1":
            cls()
            mod4()  # mod4!!!!
            menu()
        elif choice == "2":
            cls()
            mod6()
            menu()

    elif pozycja == 7:
        print("""         == == == ==  MENU  == == == ==

                            << [1] Idź do Modułu Nawigacyjnego
                            << [2] Idź do Modułu Łącznikowego
                            << [3] Wróć
                                  
                            """)
        choice = input('                           ')
        if choice == "1":
            # pozycja = 2 # pozycję najlepiej przypisac bezposrednio w modulach
            cls()
            mod8()
            menu()
        elif choice == "2":
            cls()
            mod4()
            menu()
        elif choice == "3":
            cls()
            mod7()
            menu()

    elif pozycja == 8:
        print("""         == == == ==  MENU  == == == ==

                            << [1] Wróć

                                           """)
        choice = input('                           ')  # przypisuje wybór
        if choice == "1":
            cls()
            mod7() #mod 7!!!!!!
            menu()
        elif choice == "2":
            cls()
            mod8()
            menu()

# funkcja dodana do menu żeby móc odczytać kartki od Slendera
def view_text():
    cls()
    for kartka in equipment["Kartki"]:
        print ("".join(kartka)),
    menu()

def eq():
    cls()
    # jeśli w ekwipunku nie ma jeszcze żadnej kartki to nie pokazuj
    if len(equipment["Kartki"]) ==  0:
        print("""                   == == == EKWIPUNEK == == ==

                  << [1] Latarka : poziom baterii %d
                  << [2] Mapa
                  << [3] Krótkofalówka """ % bateria)
        choice = input('                           ')  # przypisuje wybór
        if (choice == "2"):
            for i in range(1, 8):
                if pozycja == i:
                    cls()
                    mapa(i)
                    menu()
        elif (choice == "1"):
                    cls()
                    flash()
                    menu()
    else:
        print("""                   == == == EKWIPUNEK == == ==

                  << [1] Latarka : poziom baterii %d
                  << [2] Krótkofalówka
                  << [3] Kartki : %s """ % bateria, equipment["Kartki"])
        choice = input('                           ')  # przypisuje wybór
        if (choice == "2"):
            for i in range(1, 8):
                if pozycja == i:
                    cls()
                    mapa(i)
                    menu()
        elif (choice == "1"):
                    cls()
                    flash()
                    menu()


        # wyświetla tekst kartek:

        view_text()



def call(name):

    cls()
    #funkcja call dla Dave'a
    if name == "Dave":
        for key in mod:
            if name in key:
                print(Dave_kf[key])




    print  # dzwoni


def dialog():
    print  # rozmawia


def menu():

    if len(equipment["Kartki"])>0:
        print("""                  == == == ==  MENU  == == == ==

                         >> Co chcesz zrobić?
                  << [1] Idź gdzieś
                  << [2] Zobacz ekwipunek
                  << [3] Zadzwoń
                  << [4] Rozmawiaj
                  << [5] Czytaj kartki 
                  << [6] Pokaż zadanie""")

        choice = input('                           ')

        if choice == "1":
            move()
        elif choice == "2":
            eq()
        elif choice == "3":
            name = input('Do kogo chcesz zadzwonić? Wprowadź imię: ')
            call(name)
        elif choice == "4":
            dialog()
        elif choice == "5":
            view_text()
        elif choice == "6":
            quest(q)
        elif choice == "7":
            quest(q)



    else:
        print("""                  == == == ==  MENU  == == == ==

                         >> Co chcesz zrobić?
                  << [1] Idź gdzieś
                  << [2] Zobacz ekwipunek
                  << [3] Zadzwoń
                  << [4] Rozmawiaj
                  << [5] Pokaż zadanie""")

        choice = input('                           ')

        if choice == "1":
            move()
        elif choice == "2":
            eq()
        elif choice == "3":
            call()
        elif choice == "4":
            dialog()
        elif choice == "5":
            quest(q)

        #intro()


def intro():  # funkcja wprowadzająca, wczesniej można dac jakieś prawdziwe intro
    global pozycja
    pozycja = 1










    cls2()
    name = input("""Podaj swoje imię: 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """)
    załoga.append(name)
    cls()
    print("""                           

 Witaj %s !!! Jesteś członkiem misji badawczej. 
 Razem z %s'em, %s'em, %s'em i %s byłeś w drodze na 
 jedną z nowo odkrytych planet układu TRAPPIST, gdy 
 nagle z niewiadomej przyczyny rdzeń statku został 
 uszkodzony i dalsza podróż stała się niemożliwa. 
 Z powodu awarii uniemożliwiona została również komunikacja 
 z bazą na Ziemi. Od tej pory jesteście zdani sami na siebie. 
 Statek mknie przez niezbadaną przestrzeń, a co najgorsze
 jesteście na kursie kolizyjnym, gdyż przed wami rozciąga 
 się rozległy pas planetoid! Na szczęście okazało się, 
 że znajdujecie się niedaleko pewnej planety, której pole 
 grawitacyjne stopniowo przyciągało wasz statek i w zaistniałej 
 sytuacji, zdecydowaliście się stacjonować na jej orbicie aż do 
 momentu zlikwidowania awarii. W miarę upływu czasu przestają 
 działać kolejne funkcje statku. %s jako wasz Kapitan, 
 przydzielił wam zadania do wykonania, po czym
 rozdzieliliście się, a Ty zgodnie z rozkazem udałeś się do 
 modułu kuchennego.  


      """ % (załoga[4], załoga[0], załoga[1], załoga[2], załoga[3],załoga[0]))
    # funkcja sleep pozwala graczowi spokojnie przeczytać wstęp i po 35s jest następny cls()
    sleep(1)
    # przypisanie reszty załogi do innych modułów
    osoby = załoga[0:4]
    shuffle(osoby)  # za każdym razem będą mieć inne indeksy na liście załoga

    i = 0
    for key in mod:
        if len(mod[key]) == 0:
            mod[key].append(osoby[i])
            i += 1
    cls()
    mod1()

    print (załoga)
    print (osoby)
    print (mod["mod_botaniczny"])
    print (mod["mod_badawczy"])
    print (mod["mod_ener"])
    print (mod["mod_nawig"]) # to było do kontroli


    menu()



intro()
