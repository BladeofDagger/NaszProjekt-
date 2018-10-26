#biblioteki
from time import sleep
from random import *
import sys



# zmienne ###########
bateria = 3
pozycja = 1 #globalnie bez sensu


q = 1 #zmienna dla misji


noc = 0 # dla noc == 0 bedzie jasno, dla noc == 1 będzie ciemno i nie będzie nic widać bez latarki


on = 0 # 1 dla włączonej latarki, 0 dla wyłączonej





######################



def cls(): print ("\n" * 40) # poprawka na python 3.7

def cls2(): print ("\n" * 5)

def alarm():
    cls()
    print("""
            !=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!
            !=!                                   !=!
            !=!   ! ! !   A  L  A  R  M   ! ! !   !=!
            !=!                                   !=!
            !=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!
    """)
    cls2()

def back():
    cls()
    if (pozycja == 1):
        mod1(q)
        menu()
    if (pozycja == 2):
        mod2(q)
        menu()
    if (pozycja == 3):
        mod3(q)
        menu()
    if (pozycja == 4):
        mod4(q)
        menu()
    if (pozycja == 5):
        mod5(q)
        menu()
    if (pozycja == 6):
        mod6(q)
        menu()
    if (pozycja == 7):
        mod7(q)
        menu()
    if (pozycja == 8):
        mod8(q)
        menu()

def action(): #jakaś czynność, np jak w misji 1 trzeba sprawdzic zapasy, to ona bedzie za to odpowiedzialna
    print

def quest(q):

    cls()
    if (q == 1):
        print("""
                    == == ==  Misja 1  == == == 
         
         Rozejrzyj się po Kuchni w celu rozpoznania szkód oraz
         oszacuj ilość prowiantu, który Wam pozostał. Następnie
         udaj się do dowódcy.""")
        cls2()
        menu()

    if (q == 2):
        print("""
                    == == ==  Misja 2  == == == 

         W powietrzu unosi się nieprzyjemny zapach. Sprawdź źródło
         podejrzanej woni!""")
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
    global on
    if choice == "1":
        cls()
        print(("                 Włączono latarkę. Pozostałe baterie: %s") % bateria)
        cls2()

        on = 1

    if choice == "2":
        cls()

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
    "mod_badawczy": ["Super jest!","Spoko"],
    "mod_botaniczny": ["Okej","Mega"],
    "mod_ener":["Wszystko Gra","Ej"],
    "mod_nawig":["Suhe","Wow"]


}


Dave_dialog = {
    "mod_badawczy": ["",""],
    "mod_botaniczny": [""],
    "mod_ener":[""],
    "mod_nawig":[""]

    }

Steve_kf = {
    "mod_badawczy": ["Spoko","Super"],
    "mod_botaniczny": ["Eureka",""],
    "mod_ener":["Dej mi spokój!!!",""],
    "mod_nawig":["Won!",""]

}

Steve_dialog = {
    "mod_badawczy": ["Nic"],
    "mod_botaniczny": ["Coś tam"],
    "mod_ener":["Alert"],
    "mod_nawig":["Mapa"]

}

John_kf = {
    "mod_badawczy": ["Rosół",""],
    "mod_botaniczny": ["Kotlet",""],
    "mod_ener":["Ama",""],
    "mod_nawig":["Zupa",""]

}

John_dialog = {
    "mod_badawczy": ["Slon",""],
    "mod_botaniczny": ["Omlet",""],
    "mod_ener":["garnek",""],
    "mod_nawig":["rolada",""]
}

Ann_kf= {
    "mod_badawczy": ["super",""],
    "mod_botaniczny": ["Nie wiem",""],
    "mod_ener":["Nie mam ochoty ",""],
    "mod_nawig":["Fajna pogoda",""]
}

Ann_dialog = {
    "mod_badawczy": [""],
    "mod_botaniczny":[""],
    "mod_ener":[""],
    "mod_nawig":[""]

}

dialog = {
    "Dave": {
    "mod_badawczy": ["Widzę cię"],
    "mod_botaniczny":["Słyszę cię"],
    "mod_ener":["Cieszę się"],
    "mod_nawig":["Pamiętam cię"]

},
    "Steve": {
    "mod_badawczy": [""],
    "mod_botaniczny":[""],
    "mod_ener":[""],
    "mod_nawig":[""]

} ,
    "John": {
    "mod_badawczy": [""],
    "mod_botaniczny":[""],
    "mod_ener":[""],
    "mod_nawig":[""]

} ,
    "Ann": {
    "mod_badawczy": [""],
    "mod_botaniczny":[""],
    "mod_ener":[""],
    "mod_nawig":[""]

}

}

#dictionary z nazwami modułów i listami, na początku resztę załogi przydzielamy
# losowo do modułów = zapisujemy na daną listę

mod = {
    "mod_badawczy": [],
    "mod_botaniczny": [],
    "mod_ener": [],
    "mod_nawig": []

}

#
gracz_mod = {
    "mod_badawczy": [],
    "mod_botaniczny": [],
    "mod_ener": [],
    "mod_nawig": []
}

def mod1(q):  # Kuchnia
    if (q == 1):
        print("""                         >>> Jesteś w Kuchni <<<   
        
        Wszystkie zapasy żywności i wody znajdują się tutaj.
        Nic się nie dzieje.

        """)
    elif (q == 2):
        print("""                         >>> Jesteś w Kuchni <<<   

        Dostrzegasz, że jest coś nie tak. Niektóre meble
        są przewrócone. Co się tutaj stało?! Ktoś musiał
        być tutaj wcześniej. Spiżarnia jest prawie pusta,
        oznacza to poważne kłopoty...

        """)
    elif (q == 3):
        if (on == 0):
            print("""                         >>> Jesteś w Kuchni <<<   

        Ciemność!
            """)
        if (on == 1):
            print("""                         >>> Jesteś w Kuchni <<<   

        Światło!

            """)
    global pozycja
    pozycja = 1


def mod2(q):
    if (q == 1):
        print("""                >>> Jesteś w Module Wypoczynku <<<   

        Widzisz znajdujące się tutaj łóżka, rzeczy załogi
        oraz sprzęt rozrywkowy. Wygląda na to, że nic tutaj
        się nie działo.

        """)
    elif (q == 2):
        print("""                >>> Jesteś w Module Wypoczynku <<<   

        Widzisz wszechobecny bałagan. Łóżka są poprzesuwane,
        a rzeczy członków załogi porozrzucane. Ktoś musiał
        czegoś szukać...

        """)
    global pozycja
    pozycja = 2


def mod3(q):
    if (q == 1):
        print("""                >>> Jesteś w Module Serwisowym <<<   

        Załoga spędza tu wolny czas na ćwiczeniach indywidualnych
        i zespołowych. Różne formy rozrywki pozwalają
        na odstresowaniu się po cięzkim dniu.     

        """)
    elif (q == 2):
        print("""                >>> Jesteś w Module Serwisowym <<<   

        Na podłodze leżą małe części zamienne. Sprzęt
        do ćwiczeń jest uszkodzony, nikt nie powinien go
        używać w takim stanie...    

        """)
    global pozycja
    pozycja = 3


def mod4(q):
    if (q == 1):
        print("""                >>> Jesteś w Module Łącznikowym <<<   

        Moduł ten łączy pozostałe pomieszczenia statku. Jego
        blokada może oznaczać brak możliwości poruszania się
        po obiekcie. Wszystkie drzwi powinny być sprawne.

        """)
    elif (q == 2):
        print("""                >>> Jesteś w Module Łącznikowym <<<   
        
        Zauważyć można liczne uszkodzenia ścian. Co się tutaj
        wydarzyło? Nie wygląda to dobrze. Czujesz intensywny
        zapach, lepiej sprawdzić, skąd on pochodzi.

        """)
    global pozycja
    pozycja = 4


def mod5(q):
    if (q == 1):
        print("""                >>> Jesteś w Module Botanicznym <<<   

        Tutaj znajdują się rośliny, których owoce potem jemy,
        a także produkują tlen niezbędny do życia.

        """)
    elif (q == 2):
        print("""                >>> Jesteś w Module Botanicznym <<<   

         W powietrzu unosi się dziwny zapach. Miejmy nadzieję,
         że rośliny nie zostały uszkodzone. Skąd on może pochodzić?

        """)
    global pozycja
    pozycja = 5


def mod6(q):
    if (q == 1):
        print("""                >>> Jesteś w Module Badawczym <<<   

        Wszelkie próbki i dokumenty rozmieszczone są
        w schowkach w tym pomieszczeniu. Przeróżne chemikalia
        mogą w nieodpowiednich rękach narobić wielkie szkody.
        Nikt by tego nie chciał.

        """)
    elif (q == 2):
        print("""                >>> Jesteś w Module Badawczym <<<   

        Zauważasz rozlany na podłodze siarkowodór. Jest
        bardzo toksyczny. To on jest odpowiedzialny za
        ten zapach. Wdychanie go może spowodować śmierć! 

        """)
    global pozycja
    pozycja = 6


def mod7(q):
    if (q == 1):
        print("""                >>> Jesteś w Module Energetycznym  <<<   

        W tym pomieszczeniu znajdują się silniki, paliwo
        oraz cała mechanika i elektronika statku. Ich
        awaria oznaczałaby katastrofę.  

        """)
    elif (q == 2):
        print("""                >>> Jesteś w Module Energetycznym  <<<   

        Silniki pracują coraz głośniej. Ciekawe ile będą
        w stanie jeszcze pracować. Może lepiej tego nie
        sprawdzać... 

        """)
    global pozycja
    pozycja = 7


def mod8(q):
    if (q == 1):
        print("""                >>> Jesteś w Module Nawigacyjnym <<<   

        To tutaj podejmowane są najważniejsze decyzje oraz znajduje
        się tutaj panel sterowania pojazdem. Z tyłu możesz dostrzec
        umieszczone kapsuły ewakuacyjne.

        """)
    elif (q == 2):
        print("""                >>> Jesteś w Module Nawigacyjnym <<<   

        Kapsuły ewakuacyjne są zablokowane. Bez karty - klucza nie uda Ci się
        ich odblokować.

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
            mod2(q)
            menu() # nie ma sensu wywoływać ,,wróć bo sytuacja troche sie komplikuje przy dalszych modulach
        elif choice == "2":
            back()
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
            mod3(q)
            menu()
        elif choice == "2":
            cls()
            mod4(q)
            menu()
        elif choice == "3":
            cls()
            mod1(q)
            menu()
        elif choice == "4":
            back()

    # jesli jestesmy w module serwisowym to:
    elif pozycja == 3:
        print("""         == == == ==  MENU  == == == ==

                                  << [1] Idź do Modułu Wypoczynku
                                  << [2] Wróć
                                  
                            """)
        choice = input('                           ')  # tu mozna dac wroc bo nie ma innej opcji
        if choice == "1":
            cls()
            mod2(q)
            menu()
        elif choice == "2":
            back()

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
            mod5(q)
            menu()
        elif choice == "2":
            cls()
            mod7(q)
            menu()
        elif choice == "3":
            cls()
            mod6(q)
            menu()
        elif choice == "4":
            cls()
            mod2(q)
            menu()
        elif choice == "5":
            back()

    # gdy jestes w module botanicznym lub  w module badawczym lub nawigacyjnym : to
    elif (pozycja == 5):
        print("""         == == == ==  MENU  == == == ==

                                << [1] Idź do Modułu Łącznikowego
                                << [2] Wróć

                                   """)
        choice = input('                           ')
        if choice == "1":
            cls()
            mod4(q) # mod4!!!!
            menu()
        elif choice == "2":
            back()

    elif (pozycja == 6):
        print("""         == == == ==  MENU  == == == ==

                                        << [1] Idź do Modułu Łącznikowego
                                        << [2] Wróć

                                           """)
        choice = input('                           ')
        if choice == "1":
            cls()
            mod4(q)  # mod4!!!!
            menu()
        elif choice == "2":
            back()

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
            mod8(q)
            menu()
        elif choice == "2":
            cls()
            mod4(q)
            menu()
        elif choice == "3":
            back()

    elif pozycja == 8:
        print("""         == == == ==  MENU  == == == ==

                            << [1] Idź do Modułu Energetycznego
                            << [2] Wróć

                                           """)
        choice = input('                           ')  # przypisuje wybór
        if choice == "1":
            cls()
            mod7(q) #mod 7!!!!!!
            menu()
        elif choice == "2":
            back()

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
        print("                  << [4] Wróć")
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
        elif (choice == "3"):
            print
        elif (choice == "4"):
            back()
    else:
        print("""                   == == == EKWIPUNEK == == ==

                  << [1] Latarka : poziom baterii %d
                  << [2] Krótkofalówka
                  << [3] Kartki : %s """ % bateria, equipment["Kartki"])
        print("                  << [4] Wróć")
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
        elif (choice == "3"):
                    print
        elif (choice == "4"):
                    back()


        # wyświetla tekst kartek:

        view_text()

def text_animation():
    animation = "."

    for i in range(19):
        sleep(0.1)
        sys.stdout.write("\t" + animation[i % len(animation)])
        sys.stdout.flush()

#kontroluje ilość wykonanych połączeń dla każdej osoby
number_of_phonecalls = {
    "Dave" : 0,
    "John" : 0,
    "Steve" : 0,
    "Ann" : 0
}


def call(Name):
    cls()
    print("""                          Oczekiwanie na połączenie...""")
    text_animation()
    sleep(2)
    cls()

    if Name in załoga:
        if number_of_phonecalls[Name] < 2:
            # funkcja call dla Dave'a
            if Name == "Dave":

                for key in mod:

                    if Name in mod[key]:
                        if number_of_phonecalls[Name] == 0:
                            print("""                       Dave: """, Dave_kf[key][0])
                        else:
                            print("""                       Dave: """, Dave_kf[key][1])
                        number_of_phonecalls[Name] += 1

                        cls2()
            elif Name == "John":

                for key in mod:
                    if Name in mod[key]:
                        if number_of_phonecalls[Name] == 0:
                            print("""                       John: """, John_kf[key][0])
                        else:
                            print("""                       John: """, John_kf[key][1])
                        number_of_phonecalls[Name] += 1

                        cls2()
            elif Name == "Steve":

                for key in mod:
                    if Name in mod[key]:
                        if number_of_phonecalls[Name] == 0:
                            print("""                       Steve: """, Steve_kf[key][0])
                        else:
                            print("""                       Steve: """, Steve_kf[key][1])
                        number_of_phonecalls[Name] += 1

                        cls2()
            elif Name == "Ann":

                for key in mod:
                    if Name in mod[key]:
                        if number_of_phonecalls[Name] == 0:
                            print("""                       Ann:  """, Ann_kf[key][0])
                        else:
                            print("""                       Ann:  """, Ann_kf[key][1])

                        number_of_phonecalls[Name] += 1
                        cls2()
        else:
            print("""                          Nie ma sygnału...""")
            text_animation()
            sleep(2)
            cls()

    else:
        print('                       Nie ma takiego numeru')
        cls2()

    menu()







    print  # dzwoni


def dialog():

    if pozycja == 5:
        gracz_mod["mod_botaniczny"].append(1)
        for member in załoga:
            if member in mod["mod_botaniczny"]:
                print (dialog[member]["mod_botaniczny"])
    elif pozycja == 6:
        gracz_mod["mod_badawczy"].append(1)
        for member in załoga:
            if member in mod["mod_badawczy"]:
                print (dialog[member]["mod_badawczy"])
    elif pozycja == 7:
        gracz_mod["mod_ener"].append(1)
        for member in załoga:
            if member in mod["mod_ener"]:
                print (dialog[member]["mod_ener"])

    elif pozycja == 8:
        gracz_mod["mod_nawig"].append(1)
        for member in załoga:
            if member in mod["mod_nawig"]:
                print (dialog[member]["mod_nawig"])

    cls2()
    menu()





    print  # rozmawia


def menu():
    #licznik kontrolny
    licznik = True
    while licznik:
        if len(equipment["Kartki"])>0:
            print("""                  == == == ==  MENU  == == == ==
    
                             >> Co chcesz zrobić?
                      << [1] Idź gdzieś
                      << [2] Zobacz ekwipunek
                      << [3] Zadzwoń
                      << [4] Rozmawiaj
                      << [5] Czytaj kartki 
                      << [6] Pokaż zadanie
                      << [7] Wróć
                      << [8] Działaj""")

            choice = input('                           ')

            if choice == "1":
                move()
            elif choice == "2":
                eq()
            elif choice == "3":
                Name = input('Do kogo chcesz zadzwonić? Wprowadź imię: ')
                call(Name)
            elif choice == "4":
                dialog()
            elif choice == "5":
                view_text()
            elif choice == "6":
                quest(q)
            elif choice == "7":
                back()
            elif choice == "8":
                action()
            else:
                print("""          Coś poszło nie tak! Spróbuj jeszcze raz.""")





        else:
            print("""                  == == == ==  MENU  == == == ==
    
                             >> Co chcesz zrobić?
                      << [1] Idź gdzieś
                      << [2] Zobacz ekwipunek
                      << [3] Zadzwoń
                      << [4] Rozmawiaj
                      << [5] Pokaż zadanie
                      << [6] Wróć
                      << [7] Działaj""")

            choice = input('                           ')

            if choice == "1":
                move()
            elif choice == "2":
                eq()
            elif choice == "3":
                Name = input('Do kogo chcesz zadzwonić? Wprowadź imię: ')
                call(Name)

            elif choice == "4":
                dialog()
            elif choice == "5":
                quest(q)
            elif choice == "6":
                back()
            elif choice == "7":
                action()
            else:
                print("""          Coś poszło nie tak! Spróbuj jeszcze raz.""")

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
    shuffle(osoby)  # za każdym razem będą mieć inne indeksy na liście osoby

    i = 0
    for key in mod:
        if len(mod[key]) == 0:
            mod[key].append(osoby[i])
            i += 1
    cls()
    mod1(q)

    print (załoga)
    print (osoby)
    print (mod["mod_botaniczny"])
    print (mod["mod_badawczy"])
    print (mod["mod_ener"])
    print (mod["mod_nawig"]) # to było do kontroli

    #alarm()


    menu()



intro()
