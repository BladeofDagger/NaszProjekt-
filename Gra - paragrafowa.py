#biblioteki
from time import sleep
from random import *
import sys
import threading
lock = threading.Lock()
licznik = True


# zmienne ###########
bateria = 5
pozycja = 1 #globalnie bez sensu
name = ""
Lose = 0
Win = 0
q = 1 #zmienna dla misji
#kontrolka do końca misji
poziom = 0
life = 0

noc = 0 # dla noc == 0 bedzie jasno, dla noc == 1 będzie ciemno i nie będzie nic widać bez latarki


on = 0 # 1 dla włączonej latarki, 0 dla wyłączonej


# śluza do modułu botanicznego i badawczego
door = "open"
#bardzo wazne zmienne potrzebne do wygranej!!!!!!
kod = str(randint(1000,9999))
password = str(randint(1000,9999))
a = str(randint(10,99))
b = str(randint(10,99))
c = str(randint(10,99))
d = str(randint(10,99))
e = str(randint(10,99))
f = str(randint(10,99))

Rcoordinates = [a,b,c]
Wcoordinates = [d,e,f]
right_coordinates = str(".".join(Rcoordinates))
wrong_cooridinates = str(".".join(Wcoordinates))


######################



def cls(): print ("\n" * 40) # poprawka na python 3.7

def cls2(): print ("\n" * 5)


def card():
    input("""
                        == == ==  KARTA  == == ==         


                                314159265


                        == == ==  == ==  == == ==      


                >>> NACIŚNIJ COKOLWIEK, ABY KONTYNUOWAĆ <<<




                              """)


def escape():
    global Lose
    global Win
    cls()
    if (len(equipment["Karta pokładowa"]) > 0):
        choice =input("""       
                        == == ==  UWAGA  == == ==         

                            Wpisz współrzędne:

            """)
        if (choice == right_coordinates):
            cls()
            choice=input("""       
                        == == ==  UWAGA  == == ==         

                                Wpisz kod:

                """)
            if (choice == kod):
                    cls()
                    choice = input("""       
                        == == ==  UWAGA  == == ==         

                               Wpisz hasło:

                            """)
                    if (choice == password):
                            cls()
                            print("""
                        == == ==  UWAGA  == == ==                              
                            
                Możesz udać się do kapsuły ratunkowej
                i opuścić statek!
                            
                            """)
                            Win = 1
                            sleep(2)
                            cls()
                            win()
                            sleep(2)
                            end()
                            quit()


                    else:
                        cls()
                        print("""
                        == == ==  UWAGA  == == ==         

                               Złe hasło!
                                    """)
                        sleep(1)
                        back()
            else:
                cls()
                print("""
                        == == ==  UWAGA  == == ==         

                                 Zły kod!
                                    """)
                sleep(1)
                back()

        elif (choice == wrong_cooridinates):
            Lose = 1
            cls()
            slenderdead()
            sleep(2)
            lose()
            sleep(2)
            end()
            quit()

        else:
            cls()
            print("""
                        == == ==  UWAGA  == == ==         

                            Złe współrzędne!
                    """)
            sleep(1)
            back()
    else:
        cls()
        print("""
                        == == ==  UWAGA  == == ==         

                            Nie masz karty!
        """)
        sleep(1)
        back()





def end():
    cls()
    print("""
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == 

  KKK   KKK      OOOOO        NNN     NNN     III     EEEEEEEE       CCCCCC
  KKK  KKK     OOO   OOO      NNNNN   NNN     III     EEE          CCC     CC
  KKK  KK     OOO     OOO     NNN NN  NNN     III     EEEEEEE     CCC
  KKK KK      OOO     OOO     NNN  NN NNN     III     EEE         CCC
  KKK  KKK     OOO   OOO      NNN   NNNNN     III     EEE          CCC     CC
  KKK   KKK      OOOOO        NNN     NNN     III     EEEEEEEE       CCCCCC

                                D Z I Ę K U J E M Y
                                        Z A
                                    U D Z I A Ł
                                         W
                                      G R Z E        

== == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==                                       
    """)

    sleep(1)




def Uwaga():
    input("""
                        == == ==  UWAGA  == == ==         

                             >> Udało się!


                >>> NACIŚNIJ COKOLWIEK, ABY KONTYNUOWAĆ <<<




                          """)


def Uwaga1():
    input("""
                        == == ==  UWAGA  == == ==         

                    >> Udaj się do Modułu Nawigacyjnego


                >>> NACIŚNIJ COKOLWIEK, ABY KONTYNUOWAĆ <<<




                          """)





def gasnie():  # gaśnie światło
    input("""
                        == == ==  UWAGA  == == ==         

                            Gaśnie światło!
                         Zobacz, co się stało!


                >>> NACIŚNIJ COKOLWIEK, ABY KONTYNUOWAĆ <<<




                          """)

def alarm2():
    cls()
    print("""
                !=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!
                !=!                                   !=!
                !=!   ! ! !   A  L  A  R  M   ! ! !   !=!
                !=!                                   !=!
                !=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!



                >>>Pożar w module botanicznym i badawczym!!!!<<<
                
            
                


        """ )
    sleep(2)
    cls2()

def alarm():
    cls()
    print("""
                !=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!
                !=!                                   !=!
                !=!   ! ! !   A  L  A  R  M   ! ! !   !=!
                !=!                                   !=!
                !=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!






    """)
    sleep(2)
    cls()
    back()

def symbol():
    global on
    if (on == 1):
        print("""       
                                              >> Latarka jest włączona << 
        """)
    for key in gracz_mod:
        if pozycja == gracz_mod[key]:
            if len(kartki_slender[key]) > 0:
                print("""           To dziwne...Jakaś kartka...Trzeba to sprawdzić!""")

    if poziom == 1:
        if pozycja == gracz_mod["mod_serwisowy"]:
            if len(equipment["Karta pokładowa"]) ==  0:
                print("Karta pokładowa leży na łóżku Johna. Raczej będziesz jej potrzebować")


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




def minigra():
    global q
    print("""                        == == ==  DZIAŁAJ  == == == 


                       [1][2][3][4][5][6][7][8][9][X]
                    [1] A  B  C  D  E  F  G  H  I
                    [2] J  K  L  M  N  O  P  Q  R
                    [3] S  T  U  V  W  X  Y  Z  !
                    [4] 1  2  3  4  5  6  7  8  9 
                    [5] 9  8  7  6  5  4  3  2  1
                    [6] X  X  X  X  X  X  X  X  X
                    [7] A  A  B  B  C  C  D  D  !
                    [8] E  E  F  F  G     H  H  !  
                    [9] O  O  O  O  O  O  O  O  O
                    [Y]

                        Wpisz współrzedną X,Y
                        oraz brakujący symbol,
                        np.  2,2,K

        """)
    choice = input('                           ')  # przypisuje wybór
    if choice == "6,8,G":
        cls()
        Uwaga()
        q = 4
        global life
        life += 1
        sleep(2)
        cls()
        back()
    elif choice != "6,8,G":
        cls()
        print("""          Coś poszło nie tak! Spróbuj jeszcze raz.""")
        cls2()
        sleep(2)
        cls()
        minigra()



def action():  # jakaś czynność, np jak w misji 1 trzeba sprawdzic zapasy, to ona bedzie za to odpowiedzialna
    global pozycja
    global q
    global on
    global ok
    global door
    global life
    ok = 0
    cls()
    for key in gracz_mod:
        if (pozycja == gracz_mod[key] and len(kartki_slender[key])>0):
            print("""
                        == == ==  DZIAŁAJ  == == ==         

                            >> Co chcesz zrobić?
                        << [1] Zachowaj kartkę
                        << [2] Nie zabieraj kartki
                                  """)
            wez_kartke()
            cls2()

    if (q == 1 and pozycja == 1):
        print("""
                        == == ==  DZIAŁAJ  == == ==         

                            >> Co chcesz zrobić?
                        << [1] Sprawdź zapasy
                        << [2] Nic
                      """)
        choice = input('                           ')  # przypisuje wybór
        if choice == "1":
            cls()
            q = 2
            Uwaga()
            life += 1
            cls()
            back()
        elif choice == "2":
            back()


    elif (q == 2 and pozycja == 6):
        print("""
                        == == ==  DZIAŁAJ  == == ==         

                            >> Co chcesz zrobić?
                        << [1] Posprzątaj niebezpieczną substancję
                        << [2] Nic
                      """)
        choice = input('                           ')  # przypisuje wybór
        if choice == "1":
            cls()
            Uwaga()
            q = 3

            life += 1
            sleep(2)
            cls()
            gasnie()
            sleep(2)
            cls()
            back()
        elif choice == "2":
            back()

    elif (q == 3 and pozycja == 7 and on == 1):
        print("""
                        == == ==  DZIAŁAJ  == == ==         

                            >> Co chcesz zrobić?
                        << [1] Napraw system elektryczny
                        << [2] Nic
                      """)
        choice = input('                           ')  # przypisuje wybór
        if choice == "1":
            cls()
            minigra()
        elif choice == "2":
            back()

    if poziom == 1:
        if pozycja == gracz_mod["mod_serwisowy"]:
            print ("""          
                            >> Zabierz kartę! <<
                        
                        << [1] Tak
                        << [2] Nie
            """)
            choice = input('   ')
            if choice == "1":
                card()
                equipment["Karta pokładowa"].append("karta pokładowa")
                print(" Karta w ekwipunku ")
            elif choice == "2":
                print ("Karta została na miejscu. ")
        elif (pozycja == gracz_mod["mod_łącznikowy"]) and (door =="open"):

            print("""          
                        >>> Zamknij śluzy do modułów: <<<
                        >>> Botanicznego i Badawczego <<<
                                
                        << [1] Tak
                        << [2] Nie""")
            choice = input("        ")
            if choice == "1":
                door = "closed"
                miejsca.remove("mod_botaniczny")
                miejsca.remove("mod_badawczy")
                Uwaga()

            elif choice == "2":
                cls2()
                print ("""       
                >>> Ogień rozprzestrzenia się w zastraszającym tempie! <<<
                                       
                                Lepiej zamknij śluzy!!!""")
                miejsca.remove("mod_botaniczny")
                miejsca.remove("mod_badawczy")


        elif pozycja == gracz_mod["mod_nawig"]:
            print("""          
                        >>> Przyłóż kartę do czytnika! <<<
                        
                        << [1] Tak
                        << [2] Nie
                        """)
            choice = input("         ")
            if choice == "1":
                if len(equipment["Karta pokładowa"])>0:
                    escape()
                else:
                    print("""          
                        >> Nie masz wystarczających uprawnień <<
                                            
                            Potrzebujesz karty pokładowej!
                                                               
                                            """)
                    sleep(2)
                    back()
            else:
                back()






    else:

        print("""

                        == == ==  DZIAŁAJ  == == == 


                      >> Brak czynności do wykonania <<

                        << [1] Wróć


                              """)

        choice = input('                           ')  # przypisuje wybór

        if choice == "1":
            cls()

            back()




def firedead():
    print("""
                        == == ==  UWAGA  == == ==         



                            Śmierć w pożarze!
    
    
                               (  .      )
                           )           (              )
                                 .  '   .   '  .  '  .
                        (    , )       (.   )  (   ',    )
                         .' ) ( . )    ,  ( ,     )   ( .
                      ). , ( .   (  ) ( , ')  .' (  ,    )
                     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   
    """)




def slenderdead():
    print("""
                        == == ==  UWAGA  == == == 


                          Dopadł Cię Slender!    



                                     .@&%%@                                    
    *                                @     &                                   
    %                               .@     %,                              .,  
    &/                 ./%%%&&%#/,    @//#&,  .(%%%%%@@#*,                ,((  
    (@*..     ,#&&&&&&&&&%&&&#& %%%/%(&&%&&&(#&&@@&&@@&%%/,    ..,#%&&&&&&&   
      &%#&@&&&&(.              .(@%@@%&%&&*               ,(/##&&%&/,    
                                    (@@%#%&&/                                  
                              ./(%&%@@%%&%#&&&&%#*.                            
                         *&@@&%&&(##@#&&@#%@###%%%&%@.                       
                      ,%%@&%,      && &&#(&&      (#@%@%,                    
                    *&@#*         ,&@&%%&(%%%&          #@&%                   
                  .%.         *#%&&.&%&%.,#%&%          %&&%                 
                 (@         *##& /@#* .%&&%%         ,%@%.               
                #&&,         %@&. (# #&&%  %# %&&/         #%%.              
               (@&          &&/  .&% %@&%&%  %&   &         (&&              
              (@%          @#/   ,@. %%%&&&. %#    %(#         #%%             
             /%%*         *    ,@, &&(%&@/ &%     %%#         %@%            
            (&%,         %%/     .@, %&/&@@* %&      &&,         (&&           
           (@&          /      ,@* &@,#&&* &&       &@          .&&.         
          %@(          ,        &( &&./%%/.%/       ,%%           &&(        
  ,    .&&(            &%,        (# &@ .&&(#&         %            %&(    . 
    .,.               %%#          %.&@  &&%@,         .%&.               ...  
                     /&%           ,*&&  %%&             @&                    
                    *&/             (&%  (&%,             &@                   
                   %&.              (&%  .%(#              #%*                 
                .&(                 (@(   @(&                .%(               
                                    ##*   #%&                                      


    """)

def slenderescape():
    print("""
                        == == ==  UWAGA  == == == 


                           Tym razem uszedłeś
                                z życiem!   



                                     .@&%%@                                    
    *                                @ X X &                                   
    %                               .@ --- %,                              .,  
    &/                 ./%%%&&%#/,    @//#&,  .(%%%%%@@#*,                ,((  
    (@*..     ,#&&&&&&&&&%&&&#& %%%/%(&&%&&&(#&&@@&&@@&%%/,    ..,#%&&&&&&&   
      &%#&@&&&&(.              .(@%@@%&%&&*               ,(/##&&%&/,    
                                    (@@%#%&&/                                  
                              ./(%&%@@%%&%#&&&&%#*.                            
                         *&@@&%&&(##@#&&@#%@###%%%&%@.                       
                      ,%%@&%,      && &&#(&&      (#@%@%,                    
                    *&@#*         ,&@&%%&(%%%&          #@&%                   
                  .%.         *#%&&.&%&%.,#%&%          %&&%                 
                 (@         *##& /@#* .%&&%%         ,%@%.               
                #&&,         %@&. (# #&&%  %# %&&/         #%%.              
               (@&          &&/  .&% %@&%&%  %&   &         (&&              
              (@%          @#/   ,@. %%%&&&. %#    %(#         #%%             
             /%%*         *    ,@, &&(%&@/ &%     %%#         %@%            
            (&%,         %%/     .@, %&/&@@* %&      &&,         (&&           
           (@&          /      ,@* &@,#&&* &&       &@          .&&.         
          %@(          ,        &( &&./%%/.%/       ,%%           &&(        
  ,    .&&(            &%,        (# &@ .&&(#&         %            %&(    . 
    .,.               %%#          %.&@  &&%@,         .%&.               ...  
                     /&%           ,*&&  %%&             @&                    
                    *&/             (&%  (&%,             &@                   
                   %&.              (&%  .%(#              #%*                 
                .&(                 (@(   @(&                .%(               
                                    ##*   #%&                                      


    """)








def quest(q):
    cls()
    if (q == 1):
        print("""
                    == == ==  Misja 1  == == == 

         Rozejrzyj się po Kuchni w celu rozpoznania szkód oraz
         oszacuj ilość prowiantu, który Wam pozostał. Następnie
         udaj się do Modułu Nawigacyjnego.""")
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

                    Sprawdź przyczynę ciemności.""")
        cls2()
        menu()

    if (q == 4):
        print("""
                    == == ==  Misja  == == == 

                    Brak misji do wykonania""")
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

def Wstep():
    cls()
    print("""
=============================================================================
                                                         .,*/,. /    
                                                    *((,,,,,/(  ,    
                                                ,(/           /#.    
                                              (#(.            .(.    
                                           .*/  ,(/.           *,    
                                         ,(  ...   ***,       ./,    
                                       *(, .,        ****,.   ,(     
                                     ((  ..             .,,//(#,     
                                   *(  ..                    *,      
                                 ,(, ,,                   .. (       
                               .(   .     .,,             ,,(.       
                             .(*  ,.   ,*,   .*/.        ..(*        
                            ,(   .   .* Slendey /*      ../,         
                          **.  .     ,.          ((    ..*,          
                        ,(,  ..      .   Escape  */    .//           
                       (,   ,        ,*         ./.  ,./.            
              ,*((/(//(.  ..   .,///,  *,.    .**   ..**             
           *(*      **.  ..  .*.     ,*  .,**,.    ..//              
        */.       ,(.   .   ,, Martyna *          . (.               
       /.        .(,   ,    ..         ..        , /,                
     /#,         (   .,     ,,Gruszka  *        , **                 
   .(   *,      (   .        ,,      ,*       ,..(,                  
   ,*    .*.  ,/.  ...*,...,,, ./,.**.       ,  (                    
  ,*(.     .,*(*  ,.,.       .*.           .. ,(                     
  /, *//.    *#, , ,, Kamil   ,/         ..  /,                     
  /,*   ,,/(#*//.  ,,         ,/        .. *((                       
  /,,   .,*.   *(   *  Donda  *.     ,*  ./   (,                     
  ../  *.     ((**   **.   .,*      *   ((    *(                     
  ,/*,*      #, **(*    ,,,       ..  ,(      ,(                     
   .*,    .*//.*  *,,(/.      ...  .(,        //                     
   ,#    .**,(. ,,  *,.,((,...   ,(*         .(,                     
   ..   ,*,.  /*  *,  .,*,,%#/((#//          /.                      
       ,,,,   ,**(.  ,*,,*(   ,((   *.     ./,                       
       /.*   ,,   ,/((((#*    ((,*   .,*. .(,                        
      ,,*, .*   ,,    ,,     ,**  ./,   .**                          
     .*.,    ,*,   .*,       ,.. ,.,/,,**.                           
     ,,,. ,*, ..*,.          /.*.    ,*.                             
     *.*  ,*,.              ,,**,                                    
    ,,.,**                 ,(,             """)
Wstep()
uwaga = input("""                    >>> NAPISZ COKOLWIEK, ABY KONTYNUOWAĆ <<<
=============================================================================""")

def flash():  # latarka
    global bateria
    global on

    if (on == 0):
        print("""
                        == == ==  LATARKA  == == ==         

                         >> Czy chcesz włączyć latarkę?
                  << [1] Tak
                  << [2] Nie
                  """)

        choice = input('                           ')

        if choice == "1":
            cls()
            print(("                 Włączono latarkę. Pozostałe baterie: %s") % bateria)
            cls2()

            on = 1
            bateria -= 1

        if choice == "2":
            cls()

            on = 0

    elif (on == 1):
        print("""
                       == == ==  LATARKA  == == ==         

                            >> Czy chcesz wyłączyć latarkę?
                        << [1] Tak
                        << [2] Nie
                      """)

        choice = input('                           ')

        if choice == "1":
            cls()
            print(("                 Wyłączono latarkę. Pozostałe baterie: %s") % bateria)
            cls2()

            on = 0

        if choice == "2":
            cls()

            on = 1


def mapa(pozycja):
    if pozycja == 1:
        print("""                         
                        >>> Jesteś w Kuchni <<< 


                    == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Wypoczynkowy
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
        print("""                
                    >>> Jesteś w Module Wypoczynku <<<   

                    == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Wypoczynkowy
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
        print("""                
                    >>> Jesteś w Module Serwisowym <<<   

                    == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Wypoczynkowy
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
        print("""                
                    >>> Jesteś w Module łącznikowym <<<   

                    == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Wypoczynkowy
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
        print("""                
                        >>> Jesteś w Module Botanicznym <<<   

                        == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Wypoczynkowy
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
        print("""                
                        >>> Jesteś w Module Badawczym <<<   

                        == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Wypoczynkowy
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
        print("""                
                        >>> Jesteś w Module Energetycznym  <<<   

                        == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Wypoczynkowy
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
        print("""                
                        >>> Jesteś w Module Nawigacyjnym <<<   

                        == == == ==  MAPA  == == == ==         

                         # # # # # # # # # # # # # # # #
                         #    3    #    2    #    1    #  1. Kuchnia
                         #         #         #         #  2. Moduł Wypoczynkowy
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
    "Mapa" : [],
    "Karta pokładowa" : []
}



# pusta lista przygotowana na ofiary Slendera ;)
dead = []
Alive = ["Dave","Steve","John","Ann"]
# nasz gracz zawsze będzie ostatnim elementem listy więc załoga[4]
załoga = ["Dave","Steve","John","Ann"]
osoby = załoga[0:4] # = alive
ogien = [] # osoby które zginęły w pożarze
#pomocnicza lista do funkcji slender()
miejsca = ["mod_kuchenny","mod_serwisowy","mod_wypoczynkowy","mod_łącznikowy","mod_badawczy","mod_botaniczny","mod_ener","mod_nawig"]
# tu będą teksty które mówią poszczególne osoby
# kf= krótkofalówka
Dave_kf = {
    "mod_badawczy": ["Sprzęt w porządku. Muszę zabezpieczyć próbki","Jeszcze wiele pracy przed nami..."],
    "mod_botaniczny": ["Zająłem się oksygenatorem. Na razie działają systemy awaryjne.","Jest dobrze.Odbiór."],
    "mod_ener":["Silniki manewrowe doznały uszkodzeń.","Stabilizatory w normie."],
    "mod_nawig":["Karta do strefy ewakuacyjnej została w module serwisowym.","Przechodzimy na sterowanie ręczne. Nasz kod to %s" % kod]


}






Steve_kf = {
    "mod_badawczy": ["Wszystkie dane są bezpieczne!","Miałem przekazać nowy kod awaryjny: %s..." % kod],
    "mod_botaniczny": ["Rośliny w porządku. Trzeba zająć się zasilaniem.","Wszystkie urządzenia są sprawne"],
    "mod_ener":["Mamy tu poważny wyciek chłodziwa...","Możliwy czasowy zanik zasilania..."],
    "mod_nawig":["Nie można nawiązać kontaktu ze stacją...","Spróbuję nadać sygnał. Hasło do terminala to: %s" % password]

}



John_kf = {
    "mod_badawczy": ["Zawsze to samo...ale bałagan! To przez te turbulencje...","Nadgodziny nas wykończą..."],
    "mod_botaniczny": ["System dostarczania wody sprawny.","To nie tu tkwi problem. Trzeba się rozejrzeć."],
    "mod_ener":["Włączyłem dodatkowe osłony.","Wyrwanie się z tego pola grawitacyjnego to będzie nie lada wyzwanie. Trzeba rzucić okiem na te współrzędne: %s" % right_coordinates],
    "mod_nawig":["Staram się namierzyć sygnał...","Intercom zaciął się, ale zdążył zarejestrować współrzędne: %s" % right_coordinates]

}



Ann_kf= {
    "mod_badawczy": ["Ta planeta wydaje się żyć własnym życiem. Musisz zobaczyć te odczyty!","To wszystko jest niepokojące..."],
    "mod_botaniczny": ["Przekazuję nowe hasło: %s. Odbiór!" % password,"Wszystko jest w porządku."],
    "mod_ener":["Silniki są uszkodzone.","Napęd nadświetlny nie działa. Nasza jedyna szansa to szukanie łączności: %s" % kod],
    "mod_nawig":["Nie mogę nawiązać łączności! Jesteśmy zdani sami na siebie.","Intercom nadal nie działa. Potrzebuję pomocy."]
}




Dialog = {
    "Dave": {
    "mod_badawczy":["Podobno w bazie Intercomu pojawiły się jakieś współrzędne..","Tak, to było... %s." % right_coordinates],
    "mod_botaniczny":["Powtarzam hasło do terminala: %s" % password,"Dużo pracy przede mną, trzeba tutaj uważać..."],
    "mod_ener":["Co raz częściej są jakieś awarie!","Zapamiętaj kod: %s i zejdź mi z oczu..." % kod],
    "mod_nawig":["Obowiązki wzywają! Każdy z nas niech zapamięta nowe hasło: %s" % password,"Sytuacja komplikuje się coraz bardziej. Musimy przygotować się do akcji ewakuacyjnej."]

},
    "Steve": {
    "mod_badawczy":["Jakby co, to karta pokładowa leży na moim łóżku.","No tak,prawie zapomniałem! Przekazuję: %s" % right_coordinates],
    "mod_botaniczny":["Zgodnie z rozkazem przekazuję współrzędne: %s" % right_coordinates,"W obecnej sytuacji, ten ogród botaniczny to nasze jedyne źródło tlenu...Oksygenator przestał działać!"],
    "mod_ener":["Mamy tu spory wyciek chłodziwa...","Słyszałeś o tych tajemniczych współrzędnych? %s" % right_coordinates],
    "mod_nawig":["Na ekranie wyświetlają się współrzędne: %s. Nie wiem co to.." % right_coordinates,"Może Dave jest lepiej zorientowany"]

} ,
    "John": {
    "mod_badawczy":["Nie mogę sobie przypomnieć kodu awaryjnego..","Tak! To było %s." % kod],
    "mod_botaniczny":["Trzeba zabezpieczyć rośliny!","Działamy w trybie awaryjnym; zapamiętaj kod: %s" % kod],
    "mod_ener":["Zająłem się usterkami.","Muszę się skupić! Pamiętaj kod: %s. Tylko dzięki niemu procedura startu w trybie awaryjnym może dojść do skutku." % kod],
    "mod_nawig":["Kapsuły ewakuacyjne są zablokowane.","Karta podobno została w module serwisowym..."]

} ,
    "Ann": {
    "mod_badawczy":["Trochę tu bałaganu...","Na wszelki wypadek podam ci nowe hasło do terminala: %s." % password],
    "mod_botaniczny":["Hej dobrze,że jesteś. Słyszałeś o zmianie hasła?","Nasze nowe hasło to: %s" % password],
    "mod_ener":["System sztucznej grawitacji działa w trybie awaryjnym.","Jesteśmy na sterowaniu ręcznym. Na wszelki wypadek zapamiętaj hasło: %s" % password],
    "mod_nawig":["Mam już dość tego kosmosu!","Zapamiętaj hasło do terminala: %s" % password]

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

# określa pozycję gracza pozycja przypisana do modułu
gracz_mod = {
    "mod_kuchenny": 1,
    "mod_wypoczynkowy": 2,
    "mod_serwisowy": 3,
    "mod_łącznikowy": 4,
    "mod_badawczy": 6,
    "mod_botaniczny": 5,
    "mod_ener": 7,
    "mod_nawig": 8
}

#określa w którym module znajduje się slender
slender_mod = {
    "mod_kuchenny": [],
    "mod_wypoczynkowy": [],
    "mod_serwisowy": [],
    "mod_łącznikowy":[],
    "mod_badawczy": [],
    "mod_botaniczny": [],
    "mod_ener": [],
    "mod_nawig": []

}

#tu jest określone gdzie dana kartka została zostawiona
kartki_slender = {
    "mod_łącznikowy": [],
    "mod_kuchenny": [],
    "mod_wypoczynkowy": [],
    "mod_serwisowy": [],
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
    elif (q == 3 or q == 4):
        if (on == 0):
            print("""                     >>> Jesteś w Kuchni <<<   

        Wszedzie jest ciemno!  Nic nie widać. Poruszaj się
        ostrożnie, ponieważ jest bałagan. Lepiej włącz latarkę.
            """)
        if (on == 1):
            print("""                     >>> Jesteś w Kuchni <<<   

        Możesz wreszcie się bezpiecznie poruszać. Widzisz
        poprzewracane meble. Niewiadomo, co się tutaj stało...

            """)





    global pozycja
    pozycja = 1


def mod2(q):
    if (q == 1):
        print("""                >>> Jesteś w Module Wypoczynku <<<   

        Załoga spędza tu wolny czas na ćwiczeniach indywidualnych
        i zespołowych. Różne formy rozrywki pozwalają
        na odstresowaniu się po cięzkim dniu. 

        """)
    elif (q == 2):
        print("""                >>> Jesteś w Module Wypoczynku <<<   

        Na podłodze leżą małe części zamienne. Sprzęt
        do ćwiczeń jest uszkodzony, nikt nie powinien go
        używać w takim stanie...  

        """)
    elif (q == 3 or q == 4):
        if (on == 0):
            print("""                >>> Jesteś w Module Wypoczynku <<<   

        Wszedzie jest ciemno!  Nic nie widać. Poruszaj się
        ostrożnie, ponieważ jest bałagan. Lepiej włącz latarkę.
            """)
        if (on == 1):
            print("""                >>> Jesteś w Module Wypoczynku <<<   

        Możesz wreszcie się bezpiecznie poruszać. Na podłodze
        leżą małe części zamienne... """)


    global pozycja
    pozycja = 2


def mod3(q):
    if (q == 1):
        print("""                >>> Jesteś w Module Serwisowym <<<   

        Widzisz znajdujące się tutaj łóżka, rzeczy załogi
        oraz sprzęt rozrywkowy. Wygląda na to, że nic tutaj
        się nie działo.   

        """)
    elif (q == 2):
        print("""                >>> Jesteś w Module Serwisowym <<<   

        Widzisz wszechobecny bałagan. Łóżka są poprzesuwane,
        a rzeczy członków załogi porozrzucane. Ktoś musiał
        czegoś szukać...    

        """)
    elif (q == 3 or q == 4):
        if (on == 0):
            print("""                >>> Jesteś w Module Serwisowym <<<   

        Wszedzie jest ciemno!  Nic nie widać. Poruszaj się
        ostrożnie, ponieważ jest bałagan. Lepiej włącz latarkę.
            """)
        if (on == 1):
            print("""                >>> Jesteś w Module Serwisowym <<<   

        Możesz wreszcie się bezpiecznie poruszać. Widzisz
        poprzesuwane łóżka i porozrzucane rzeczy.

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
    elif (q == 3 or q == 4):
        if (on == 0):
            print("""                >>> Jesteś w Module Łącznikowym <<<   

        Wszedzie jest ciemno!  Nic nie widać. Poruszaj się
        ostrożnie, ponieważ jest bałagan. Lepiej włącz latarkę.
            """)
        if (on == 1):
            print("""                >>> Jesteś w Module Łącznikowym <<< 

        Możesz wreszcie się bezpiecznie poruszać. Niewiadomo,
        ile wytrzyma bateria, lepiej ją oszczędzać.

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
    elif (q == 3 or q == 4):
        if (on == 0):
            print("""                >>> Jesteś w Module Botanicznym <<<   

        Wszedzie jest ciemno!  Nic nie widać. Poruszaj się
        ostrożnie, ponieważ jest bałagan. Lepiej włącz latarkę.
        Rośliny bez światła nie są w stanie produkować tlenu,
        jak najszybciej znajdź przyczynę awarii.
            """)
        if (on == 1):
            print("""                >>> Jesteś w Module Botanicznym <<< 

        Możesz wreszcie się bezpiecznie poruszać. Nie wiadomo,
        ile wytrzyma bateria, lepiej ją oszczędzać. Rośliny
        bez światła nie są w stanie produkować tlenu, jak
        najszybciej znajdź przyczynę awarii.

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

        Zauważasz rozlaną na podłodze substancję. Jest
        bardzo toksyczna. To ona jest odpowiedzialny za
        ten zapach. Wdychanie go może spowodować śmierć! 

        """)
    elif (q == 3 or q == 4):
        if (on == 0):
            print("""                >>> Jesteś w Module Badawczym <<<   

        Wszedzie jest ciemno!  Nic nie widać. Poruszaj się
        ostrożnie, ponieważ jest bałagan. Lepiej włącz latarkę.
            """)
        if (on == 1):
            print("""                >>> Jesteś w Module Badawczym <<< 

        Możesz wreszcie bezpiecznie się poruszać. Niewiadomo,
        ile wytrzyma bateria, lepiej ją oszczędzać. Na szczęście
        nie ma już śladu po niebezbiecznej substancji.

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
    elif (q == 3):
        if (on == 0):
            print("""                >>> Jesteś w Module Energetycznym <<<   

        Wszedzie jest ciemno!  Nic nie widać. Poruszaj się
        ostrożnie, ponieważ jest bałagan. Lepiej włącz latarkę.
            """)
        if (on == 1):
            print("""                >>> Jesteś w Module Energetycznym <<< 

        Spróbuj naprawić światło. Bez niego, funkcjonowanie
        będzie niemożliwe!

            """)
    elif (q == 4):
        if (on == 0):
            print("""                >>> Jesteś w Module Energetycznym <<<   

        Wszedzie jest ciemno!  Nic nie widać. Poruszaj się
        ostrożnie, ponieważ jest bałagan. Lepiej włącz latarkę.
            """)
        if (on == 1):
            print("""                >>> Jesteś w Module Energetycznym <<< 

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
    elif (q == 3 or q == 4):
        if (on == 0):
            print("""                >>> Jesteś w Module Nawigacyjnym <<<    

        Wszędzie jest ciemno!  Nic nie widać. Poruszaj się
        ostrożnie, ponieważ jest bałagan. Lepiej włącz latarkę.
            """)
        if (on == 1):
            print("""                >>> Jesteś w Module Nawigacyjnym <<<  

        Nic ciekawego tutaj nie ma. Szukaj gdzie indziej.

            """)

    global pozycja
    pozycja = 8



#pozycja = 0  # numer pozycji odpowiada pokojowi


def move():  # funkcja poruszania sie pomiędzy pokojami
    global Lose
    cls()
    # jesli jestesmy w kuchni to:
    if pozycja == 1:
        print("""                 == == == ==  MENU  == == == ==

                  << [1] Idź do Modułu Wypoczynku
                  << [2] Wróć

            """)
        choice = input('                           ')  # przypisuje wybór
        if choice == "1":
            # pozycja = 2
            cls()
            mod2(q)
            menu()  # nie ma sensu wywoływać ,,wróć bo sytuacja troche sie komplikuje przy dalszych modulach
        elif choice == "2":
            back()
    # jesli jestesmy w module wypoczynkowym to:
    elif pozycja == 2:
        print("""                 == == == ==  MENU  == == == ==

                  << [1] Idź do Modułu Serwisowego
                  << [2] Idź do Modułu Łącznikowego
                  << [3] Idź do Kuchni
                  << [4] Wróć

                    """)
        choice = input('                           ')  # przypisuje wybór
        if choice == "1":
            # pozycja = 2 # pozycję najlepiej przypisac bezposrednio w modulach
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
        print("""                 == == == ==  MENU  == == == ==

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
        print("""                 == == == ==  MENU  == == == ==

                  << [1] Idź do Modułu Botanicznego
                  << [2] Idź do Modułu Energetycznego
                  << [3] Idż do Modułu Badawczego
                  << [4] Idź do Modułu Wypoczynkowego
                  << [5] Wróć

                           """)
        choice = input('                           ')  # przypisuje wybór
        if choice == "1":
            if ("mod_botaniczny" not in miejsca) and ("mod_badawczy" not in miejsca):
                if door == "closed":
                    cls()
                    print("""                 == == == ==  MENU  == == == ==
    
                            >>> Śluza zamknięta <<<
    
                                                """)
                    menu()
                elif door == "open":
                    global Lose
                    Lose = 1
                    firedead()
                    sleep(2)
                    lose()
                    sleep(2)
                    end()
                    sleep(2)
            elif poziom == 1 and door == "open":
                Lose = 1
                firedead()
                sleep(2)
                lose()
                sleep(2)
                end()
                quit()

            else:
                cls()
                mod5(q)
                menu()
        elif choice == "2":
            cls()
            mod7(q)
            menu()
        elif choice == "3":
            if ("mod_botaniczny" not in miejsca) and ("mod_badawczy" not in miejsca):
                if door == "closed":
                    cls()
                    print("""                 == == == ==  MENU  == == == ==
    
                            >>> Śluza zamknięta <<<
    
                                                """)
                    menu()
                elif door == "open":
                    firedead()
                    sleep(2)
                    lose()
                    sleep(2)
                    end()
                    sleep(2)
            elif poziom ==1 and door == "open":
                Lose = 1
                firedead()
                sleep(2)
                lose()
                sleep(2)
                end()
                quit()
            else:
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
        print("""                 == == == ==  MENU  == == == ==

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

    elif (pozycja == 6):
        print("""                 == == == ==  MENU  == == == ==

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
        print("""                 == == == ==  MENU  == == == ==

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
        print("""                 == == == ==  MENU  == == == ==

                  << [1] Idź do Modułu Energetycznego
                  << [2] Wróć

                                           """)
        choice = input('                           ')  # przypisuje wybór
        if choice == "1":
            cls()
            mod7(q)  # mod 7!!!!!!
            menu()
        elif choice == "2":
            back()

# funkcja dodana do menu żeby móc odczytać kartki od Slendera
def view_text():
    cls()
    for kartka in equipment["Kartki"]:
        print ("".join(kartka)),
    cls2()
    menu()

def eq():
    cls()
    # jeśli w ekwipunku nie ma jeszcze żadnej kartki to nie pokazuj
    if len(equipment["Kartki"]) ==  0:
        print("""                   == == == EKWIPUNEK == == ==

                  << [1] Latarka : poziom baterii %d
                  << [2] Mapa
                  << [3] Krótkofalówka """ % (bateria))
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
            cls()
            print("""
                        == == == KRÓTKOFALÓWKA == == ==

                            << Aby zadzwonić do kogoś, >>
                               << użyj opcji z menu >>

                                """)
        elif (choice == "4"):
            back()
    else:
        print("""                   == == == EKWIPUNEK == == ==

                          << [1] Latarka : poziom baterii %d
                          << [2] Mapa
                          << [3] Krótkofalówka
                          << [4] Kartki : %s """ % (bateria, len(equipment["Kartki"])))
        print("                  << [5] Wróć")
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
        elif (choice == "4"):
            view_text()

        elif (choice == "5"):
            back()
        elif (choice == "3"):
            cls()
            print(""" 
                        == == == KRÓTKOFALÓWKA == == ==

                            << Aby zadzwonić do kogoś, >>
                               << użyj opcji z menu >>

                                            """)






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

    if Name in osoby:
        if Name in Alive:
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
            print("""                          Nie ma sygnału...""")
            text_animation()
            sleep(2)
            cls()

    else:
        print('                       Nie ma takiego numeru')
        cls2()

    menu()







    print  # dzwoni

#kontrola ilości wywołań funkcji dialog()
number_of_talks = {
    "Dave": 0,
    "Steve": 0,
    "John": 0,
    "Ann": 0
}

def dialog():
    global pozycja
    cls()

    if pozycja == 5:

        for member in załoga:
            if member in mod["mod_botaniczny"]:
                if number_of_talks[member]<2:
                    if number_of_talks[member] == 0:
                        print (""">>> %s: %s""" % (member, Dialog[str(member)]["mod_botaniczny"][0]))
                        number_of_talks[member] += 1
                        cls2()
                    else:
                        print(""">>> %s: %s""" % (member, Dialog[str(member)]["mod_botaniczny"][1]))
                        number_of_talks[member] += 1
                        cls2()

                else:
                    print ("""           >>> %s nie jest już w nastroju na rozmowę... <<<""" % (member))
                    cls2()
    elif pozycja == 6:

        for member in załoga:
            if member in mod["mod_badawczy"]:
                if number_of_talks[member]<2:
                    if number_of_talks[member] == 0:
                        print (""">>> %s: %s""" % (member, Dialog[str(member)]["mod_badawczy"][0]))
                        number_of_talks[member] += 1
                        cls2()
                    else:
                        print(""">>> %s: %s""" % (member, Dialog[str(member)]["mod_badawczy"][1]))
                        number_of_talks[member] += 1
                        cls2()

                else:
                    print(""">>> %s chce skupić się na swojej pracy...Nie przeszkadzaj! <<<""" % (member))
                    cls2()

    elif pozycja == 7:

        for member in załoga:
            if member in mod["mod_ener"]:
                if number_of_talks[member]<2:
                    if number_of_talks[member] == 0:
                        print (""">>> %s: %s""" % (member, Dialog[str(member)]["mod_ener"][0]))
                        number_of_talks[member] += 1
                        cls2()
                    else:
                        print(""">>> %s: %s""" % (member, Dialog[str(member)]["mod_ener"][1]))
                        number_of_talks[member] += 1
                        cls2()

                else:
                    print("""           >>> Sytuacja jest coraz bardziej napięta.
                                    %s wydaje się mieć już dosyć twojego towarzystwa... <<<""" % (member))
                    cls2()


    elif pozycja == 8:

        for member in załoga:
            if member in mod["mod_nawig"]:
                if number_of_talks[member]<2:
                    if number_of_talks[member] == 0:
                        print (""">>> %s: %s""" % (member, Dialog[str(member)]["mod_nawig"][0]))
                        number_of_talks[member] += 1
                        cls2()
                    else:
                        print(""">>> %s: %s""" % (member, Dialog[str(member)]["mod_nawig"][1]))
                        number_of_talks[member] += 1
                        cls2()

                else:
                    print(""" >>> %s chyba już nie znajdzie dla Ciebie czasu... <<<""" % (member))
                    cls2()



    menu()





    print  # rozmawia

def wez_kartke():

    choice = input("                            ")
    if choice == "1":
        for key in kartki_slender:
            if  pozycja == gracz_mod[key]:
                sleep(1)


                print ("Kartka: ","".join(kartki_slender[key]))
                cls2()
                sleep(2)


                equipment["Kartki"].append(str(kartki_slender[key]))
                kartki_slender[key].clear()
                cls2()
                print ("""                  >>>Zachowałeś kartkę<<<
                    """)


    elif choice == "2":
        print(""">>Nie zachowałeś kartki<<<""")
        # mozna kiedys dodac opcje zeby po nia wrocic
        cls2()

    else:
        print("""              >>>To pewnie nic ważnego...""")
        cls2()


def win():
    print ("""
                        == == ==  ! ! W Y G R A N A ! !  == == ==         


               ,@%     @@     &@         @@@@@@&(         @@*       @@                                 
                @@,   @@@(   /@@         .,*@@%@@         @@@@      @@*                                
                *@@  &@@@@   @@            (@@            @@/@@*    @@(                                
                 @@( @@ @@  @@*            #@@            @@. @@@   @@/                                
                  @@@@( @@%@@%             #@@            @@,   @@@ @@*                                
                  @@@&  .@@@@              #@@%%#         @@,     @@@@,                                
                   @@    @@@             @@@@@@@&         @@        @@   


                                == == ==  == ==  == == ==     

                                                                            """)
    print ("""          >>> Gratulacje % s! Ucieczka zakończona powodzeniem! <<< """ %(",".join(Alive)))
    cls2()
    if len(dead)==1:
        print ("""      >>>Niech %s spoczywa w pokoju... <<<""" % (",".join(dead)))
        cls2()
    elif len(dead)==2:
        print ("""      >>>Niech %s spoczywają w pokoju... <<<""" % (" i ".join(dead)))
        cls2()
    elif len(dead)==3:
        print("""       >>>Niech %s i %s spoczywają w pokoju... <<<""" % (", ".join(dead[0:2]), "".join(dead[2])))
        cls2()
    else:
        print("""       >>>Niech %s i %s spoczywają w pokoju... <<<""" % (", ".join(dead[0:3]), "".join(dead[3])))
        cls2()







#slender atakuje!!!
def slender5():
    global miejsca
    global Lose
    global pozycja
    global Alive
    global dead
    global life
    i = 0
    with lock:
        if Lose == 0:
            while i < 3:
                sleep(5)
                shuffle(miejsca)
                index = randint(0, 5) # z listy zniknely modul botan i badawczy
                slender_mod[miejsca[index]].append("Slender")
                if miejsca[index] in mod:  # jeśli dane pomieszczenie jest w słowniku mod z załogą
                    for key in mod:
                        if key == miejsca[index]:  # sprawdzamy czy nie ma kogoś tam gdzie pojawił się slender(załoga bez gracza)
                            if len(mod[key]) > 0:
                                Alive.remove(mod[key][0])  # przenosimy z listy alive do dead
                                dead.append(mod[key][0])  # dana osoba przenosi się do dead


                                mod[key].clear()
                elif pozycja == gracz_mod[miejsca[index]]:
                    if life > 0:
                        cls()
                        life -= 1
                        slenderescape()
                        sleep(2)
                    else:
                        Lose = 1
                        i = 3
                        slenderdead()
                        sleep(3)
                        lose()
                        sleep(2)
                        end()
                        quit()
                i+=1
                slender_mod[miejsca[index]].clear() # slender znika ze statku
        """else:
            Lose = 1
            slenderdead()
            sleep(3)
            lose()
            sleep(2)
            end()
            sleep(2)"""



def slow_death():
    sleep(15)
    if door =="open":
        global Lose
        Lose = 1
        firedead()
        sleep(2)
        lose()
        sleep(2)
        cls()
        end()
        quit()


    else:
        pass







def fire1():
    global ogien
    global Alive
    global dead
    global name
    global Lose
    global poziom
    global miejsca
    poziom = 1
    with lock:
        sleep(10)
        alarm2()

        #możesz zginąć w pożarze
        for member in Alive:
            if (member in mod["mod_botaniczny"]):
                Alive.remove(member)
                dead.append(member)
                ogien.append(member)
                mod["mod_botaniczny"].clear()


            elif member in mod["mod_badawczy"]:
                Alive.remove(member)
                dead.append(member)
                ogien.append(member)
                mod["mod_badawczy"].clear()

        #usuniete miejsca.remove

        print("""           >>> To niemożliwe! Ktoś musiał podłożyć ogień...<<<""")
        cls2()
        if ((pozycja == gracz_mod["mod_botaniczny"]) or (pozycja == gracz_mod["mod_badawczy"])) and (len(ogien)==2):
            ogien.append(name)
            firedead()
            sleep(2)
            Lose = 1
            lose()
            sleep(2)
            cls()
            end()
            quit()

        elif ((pozycja == gracz_mod["mod_botaniczny"]) or (pozycja == gracz_mod["mod_badawczy"])) and (len(ogien)==1):
            ogien.append(name)
            firedead()
            sleep(2)
            Lose = 1
            lose()
            sleep(2)
            cls()
            end()
            quit()

        elif ((pozycja != gracz_mod["mod_botaniczny"]) or (pozycja != gracz_mod["mod_badawczy"])) and (len(ogien)==2):
            input ("""         
                      >>> Niestety %s nie przeżyli... <<<
                
                
                >>> Działaj zanim ogień opanuje cały statek! <<<
                            
                            
                            
                  >>> UDAJ SIĘ DO MODUŁU ŁĄCZNIKOWEGO!!! <<<
                
                    
                    
                           
                 >>> NACIŚNIJ COKOLWIEK, ABY KONTYNUOWAĆ <<<
                """ % (" i ".join(ogien)))





        elif ((pozycja != gracz_mod["mod_botaniczny"]) or (pozycja != gracz_mod["mod_badawczy"])) and (len(ogien)==1):
            input("""          
                    >>> Niestety %s już nigdy nie wróci... <<<
            
            
                >>> Ogień szaleje na statku! Musisz działać! <<<
                        
                        
                        
                        
                  >>> UDAJ SIĘ DO MODUŁU ŁĄCZNIKOWEGO!!! <<<
            
                
                
                        
                  >>> NACIŚNIJ COKOLWIEK, ABY KONTYNUOWAĆ <<<
            
            """ % ("".join(ogien)))




        elif ((pozycja != gracz_mod["mod_botaniczny"]) or (pozycja != gracz_mod["mod_badawczy"])) and (len(ogien)==0):
            input ("""           
                    >>> Na szczęście nikomu nic się nie stało! <<<


            >>> Ale ogień wciąż szaleje na statku więc musisz działać! <<<
                                
                                
                                
                                
                    >>> UDAJ SIĘ DO MODUŁU ŁĄCZNIKOWEGO!!! <<<



                            
                            
                    >>> NACIŚNIJ COKOLWIEK, ABY KONTYNUOWAĆ <<<

                        """)








def lose():
    print ("""
                     == == ==  ! ! P R Z E G R A N A ! !  == == ==         



           @@*                 .@@@@@&               ,&@%           *@@@@@@@@@                        
           @@(               (@@@   ,@@@           @@@@%@@#          @@                               
           @@/              @@@       @@          @@,               .@@                               
           @@,              @@        @@           &@@@@@@@         (@@@@@@@@                         
           @@               @@       @@@                 @@@        &@@                               
           @@   ,&@,        #@@@   &@@&          @@*   *@@@*        #@@                               
           @@@@@@@*           .@@@@@/             &@@@@@&            @@@@@@@@                         


                               == == ==  == ==  == == ==     
                             """)
    if len(dead)== 1:
        if "Ann" in dead:
            print("""       >>> Razem z %s jesteś już na tamtym świecie... <<<""" % ("".join(dead)))
        elif "Steve" in dead:
            print("""       >>> Razem ze %s jesteś już na tamtym świecie... <<<""" % ("'em ".join(dead)))

        else:
            print("""       >>> Razem z %s jesteś już na tamtym świecie... <<<""" % ("'em ".join(dead)))
    else:
        print("""       >>> Ty, %s - jesteście już na tamtym świecie... <<<""" % (", ".join(dead)))



def slender4():
    global Alive
    global dead
    with lock:
        sleep(20)
        shuffle(miejsca)
        index = randint(0, 7)
        slender_mod[miejsca[index]].append("Slender")
        if miejsca[index] in mod:  # jeśli dane pomieszczenie jest w słowniku mod z załogą
            for key in mod:
                if key == miejsca[index]:  # sprawdzamy czy nie ma kogoś tam gdzie pojawił się slender(załoga bez gracza)
                    if len(mod[key]) > 0:
                        Alive.remove(mod[key][0])  # przenosimy z listy alive do dead
                        dead.append(mod[key][0])  # dana osoba przenosi się do dead
                        kartki_slender[miejsca[index]].append( "Z prochu powstałeś i w proch się obrócisz... %s" % (",".join(dead)))

                        mod[key].clear()
        else:
            kartki_slender[miejsca[index]].append("Zapomnienie boli najbardziej")

        slender_mod[miejsca[index]].clear()



def slender3():
    global Alive
    global dead
    with lock:
        sleep(30)
        shuffle(miejsca)
        index = randint(0, 7)
        slender_mod[miejsca[index]].append("Slender")
        if miejsca[index] in mod:  # jeśli dane pomieszczenie jest w słowniku mod z załogą
            for key in mod:
                if key == miejsca[index]:  # sprawdzamy czy nie ma kogoś tam gdzie pojawił się slender(załoga bez gracza)
                    if len(mod[key]) > 0:
                        Alive.remove(mod[key][0])  # przenosimy z listy alive do dead
                        dead.append(mod[key][0])  # dana osoba przenosi się do dead
                        kartki_slender[miejsca[index]].append(str(",".join(dead)))

                        mod[key].clear()
        else:
            kartki_slender[miejsca[index]].append("Slender")

        slender_mod[miejsca[index]].clear()



def slender2():
    global dead
    global Alive
    with lock:
        sleep(60)
        shuffle(miejsca)
        index = randint(0, 7)
        slender_mod[miejsca[index]].append("Slender")
        if miejsca[index] in mod:  # jeśli dane pomieszczenie jest w słowniku mod z załogą
            for key in mod:
                if key == miejsca[index]:  # sprawdzamy czy nie ma kogoś tam gdzie pojawił się slender(załoga bez gracza)
                    if len(mod[key]) > 0:
                        kartki_slender[miejsca[index]].append("Jedynie grawitacja może wygrać z czasem")
                        Alive.remove(mod[key][0])  # przenosimy z listy alive do dead
                        dead.append(mod[key][0])  # dana osoba przenosi się do dead
                        mod[key].clear()
        else:
            kartki_slender[miejsca[index]].append("Jedynie grawitacja może wygrać z czasem")

        slender_mod[miejsca[index]].clear()



def slender1():
    global dead
    global Alive
    thread2.start()
    sleep(60)
    shuffle(miejsca)
    index = randint(0,7)
    slender_mod[miejsca[index]].append("Slender")
    if miejsca[index] in mod: # jeśli dane pomieszczenie jest w słowniku mod z załogą
        for key in mod:
            if key == miejsca[index]: #sprawdzamy czy nie ma kogoś tam gdzie pojawił się slender(załoga bez gracza)
                if len(mod[key]) > 0:
                    cls2()
                    print ("""            >>> %s dzwoni!
                                """ % (mod[key][0]))
                    cls2()
                    sleep(2)

                    print("""                       
                    == == ==  KRÓTKOFALÓWKA  == == ==         
        
                >>> %s: %s, coś jest nie tak... Ktoś jest... 
                    
                    
                    
                    
                    
                        
                                    
                                    
                                              """ % (mod[key][0], name))




                    kartki_slender[miejsca[index]].append("Wszystko ma swój koniec 23.74.85")
                    Alive.remove(mod[key][0]) # przenosimy z listy alive do dead
                    dead.append(mod[key][0])  # dana osoba przenosi się do dead
                    mod[key].clear()  # czyści listę przypisaną do miejsca czyli dana osoba znika
                    sleep(2)
                    back()
    else:
            # jeśli to np modserwisowy, modkuchenny albo mod wypoczynkowy czy łącznikowy
        kartki_slender[miejsca[index]].append("Wszystko ma swój koniec %s" % wrong_cooridinates)
                # jeśli pojawi się kartka to weź kartkę
                # cyfy to współrzędne środka planety = mają w pewnym sensie
                # zmylić gracza gdy bedzie musial pod koniec wpisac wspolrzedne
    slender_mod[miejsca[index]].clear() #slender znika





def menu():
    global Lose
    global pozycja
    symbol()







    while Lose == 0:
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
                if (Lose == 0) or (Win==0):
                    if choice == "1":
                        move()
                    elif choice == "2":
                        eq()
                    elif choice == "3":

                        print ('Twoi przyjaciele: %s ' % (", ".join(osoby))),

                        Name = input('Do kogo chcesz zadzwonić? Wprowadź imię: ')
                        call(Name)
                    elif choice == "4":
                        if (pozycja == 5 or pozycja == 6 or pozycja == 7 or pozycja == 8):
                            dialog()
                        else:
                            cls2()
                            print ("""          Wygląda na to, że nikogo tu nie ma...""")
                            cls2()
                    elif choice == "5":
                        view_text()
                    elif choice == "6":
                        quest(q)
                    elif choice == "7":
                        back()
                    elif choice == "8":
                        action()
                    else:
                        if (Lose == 1) or (Win ==1):
                            print ("Koniec Gry")
                        else:

                            print("""          Coś poszło nie tak! Spróbuj jeszcze raz.""")
                else:
                    if choice =="1":
                        print ("Koniec Gry")
                    elif choice == "2":
                        print ("Koniec Gry")
                    elif choice =="3":
                        print("Koniec Gry")
                    elif choice =="4":
                        print("Koniec Gry")
                    elif choice =="5":
                        print("Koniec Gry")
                    elif choice =="6":
                        print("Koniec Gry")
                    elif choice =="7":
                        print("Koniec Gry")
                    elif choice=="8":
                        print("Koniec Gry")
                    else:
                        print("Koniec Gry")





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
                if (Lose == 0) or (Win == 0):
                    if choice == "1":
                        move()
                    elif choice == "2":
                        eq()
                    elif choice == "3":

                        print('Twoi przyjaciele: %s ' % (", ".join(osoby))),

                        Name = input('Do kogo chcesz zadzwonić? Wprowadź imię: ')
                        call(Name)

                    elif choice == "4":
                        if (pozycja == 5 or pozycja == 6 or pozycja == 7 or pozycja == 8):
                            dialog()
                        else:
                            cls2()
                            print ("""              Wygląda na to, że nikogo tu nie ma...""")
                            cls2()
                    elif choice == "5":
                        quest(q)
                    elif choice == "6":
                        back()
                    elif choice == "7":
                        action()
                    else:
                        if (Lose == 1) or (Win ==1):
                            print ("Koniec Gry")
                        else:
                            print("""          Coś poszło nie tak! Spróbuj jeszcze raz.""")
                else:
                    if choice =="1":
                        print ("Koniec Gry")
                    elif choice == "2":
                        print ("Koniec Gry")
                    elif choice =="3":
                        print("Koniec Gry")
                    elif choice =="4":
                        print("Koniec Gry")
                    elif choice =="5":
                        print("Koniec Gry")
                    elif choice =="6":
                        print("Koniec Gry")
                    elif choice =="7":
                        print("Koniec Gry")
                    elif choice=="8":
                        print("Koniec Gry")
                    else:
                        print("Koniec Gry")



    cls2()


#threads
thread1 = threading.Thread( target = slender1)
thread2 = threading.Thread( target = menu)
thread3 = threading.Thread( target = slender2)
thread4 = threading.Thread( target = slender3)
thread5 = threading.Thread( target = slender4)
thread6 = threading.Thread( target = fire1)
thread7 = threading.Thread( target = slow_death)
thread8 = threading.Thread( target = slender5)


def intro():  # funkcja wprowadzająca, wczesniej można dac jakieś prawdziwe intro
    global pozycja
    pozycja = 1










    cls2()
    global name
    name = input("""Podaj swoje imię: 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """)
    załoga.append(name)
    Alive.append(name)
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
    global mod
    i = 0
    for key in mod:
        if len(mod[key]) == 0:
            mod[key].append(osoby[i])
            i += 1
    cls()
    mod1(q)


    cls2()
    #threads
    global licznik
    thread1.start() #pierwsza kartka i call()
    thread1.join()
    thread3.start()# 2 kartka
    thread3.join()
    thread4.start()#3 kartka
    thread4.join()
    thread5.start() #4 kartka
    thread5.join()
    thread6.start() #pożar w module botanicznym i badawczym
    thread6.join()
    global Win
    global Lose
    if Lose == 1:

        licznik = False
        quit()
    else:
        thread7.start() # smierc slowdeath jesli nie zamkniesz sluzy
        thread7.join()
        if Lose == 1:

            licznik = False
            quit()


        elif Win == 1:

            quit()

        else:
            thread8.start() # ostatni atak slendera
            thread8.join()
            if Lose == 1:
                licznik = False
                quit()
            elif Win == 1:

                quit()











intro()
