from random import randint
import time
import sys
#---------------------------------
x = 0
z = 0
hajs = 0
hp = 5
maxhp = randint(5,10)
moc = randint(2,5)
#---
hpg = 5
mg = 2
#---
hpm = 7
mm = 5
#---
hpk = 3
mk = 2
#---
hpkk = 1
mkk = 1



#---------------------------------

#-----------Zadymiarze------------

#---------------------------------
def zadyma(hpk,mk,hp):
    zadymiarz = 3
    if zadymiarz == (1):
        print('zadymiarz grzesio | hp = 5/5 | moc = 2')
        
    elif zadymiarz == (2):
        
        print('zadymiarz najlepszy | hp = 7/7 | moc = 5')
        
    elif zadymiarz == (4):
        
        print('zadymiarz kaśka | hp = 1/1 | moc = 1')
        print('                               _.._')
        print('                             .'    '.')
        print('                            (____/`\ |')
        print('                           (  |' ' )  )')
        print('                           )  _\= _/  (')
        print('                 __..---.(`_.  ` \    )')
        print('                `;-""-._(_( .      `; (')
        print('                /       `-```--     ;  )')
        print('               /    /  .    ( .  ,| |(')
        print('_.-` ---...__,     /-,..___.- -- _| |_)')
        print(' - `` -.._       ,   |   / ......... ')
        print('          ``;--"`;   |   `-`')
        print('             ``..__.`')
        
    elif zadymiarz == (3):
       
        print('zadymiarz kacper | hp = 3/3 | moc = 2')
        print('                 .--.')
        print('                /.''.|')
        print('                ||   \_)')
        print('          /^\   `.`--,')
        print('        .`_|_`.   `()')
        print('       <   |   >   ||')
        print('        \_____/    ||')
        print('        {/a a\}    ||')
        print('       {/-.^.-\}   (_|')
        print('      .`{  `  }-._/|;\`')
        print('     /  {     }  /; || |')
        print('    /``-{     }-`;  || |')
        print('   ; ``=|{   }|=` _/|| |')
        print('   |   \| |~| |  |/ || |')
        print('   |\   \ | | |  ;  || |')
        print('   | \   ||=| |=<\  || |')
        print('   | /\_/\| | |  \`-||_/')
        print('   `-| `;`| | |  |  ||')
        print('     |  | | | |  |  ||')
        print('     |  |+| |+|  |  ||')
        print('     |  """ """  |  ||')
        print('     |_ _ _ _ _ _|  ||')
        print('     |,;,;,;,;,;,|  ||')
        print('     `|||||||||||`  ||')
        print('      |||||||||||   ||')
        print('      `"""""""""`   ""')
        
        while hpk > 0: 
            
#------------------------------

#----------Walka i napisy------

#------------------------------

            print('a) biję')
            print('b) uciekam')
            walkarespond = input('')
            if walkarespond == ('a'):
                hpk -= moc
                time.sleep(1)
                print("zadajesz " ,moc, " damage i zostaje mu ", hpk, " hp")
                if hpk <=0 :
                    time.sleep(0.5)
                    print('                                                 ')
                    print(' _ _ _  __ __  _____  _____  _____  _____  _____ ')
                    print('| | | ||  |  ||   __|| __  ||  _  ||   | ||  _  |')
                    print('| | | ||_   _||  |  ||    -||     || | | ||     |')
                    print('|_____|  |_|  |_____||__|__||__|__||_|___||__|__|')
                    print('                                                 ')

                
                else: 
                    hp -= mk
                    time.sleep(2)
                    print("dostajesz ",mk, " damage i zostaje ci ", hp, " hp")
                    time.sleep(1)
                    print('                                          ')
                    print('                        //                ')
                    print(' _____  _____  _   _  _____ ______  ______')
                    print('|_   _|/  __ \| | | ||  _  || ___ \|___  /')
                    print('  | |  | /  \/| |_| || | | || |_/ /   / / ')
                    print('  | |  | |    |  _  || | | ||    /   / /  ')
                    print('  | |  | \__/\| | | |\ \_/ /| |\ \ ./ /___')
                    print('  \_/   \____/\_| |_/ \___/ \_| \_|\_____/')
                    print('                                          ')
                    
#---------------------------------
def zadymak(hpkk,mkk,hp):
    print("ZADYMAAAAA!")
    time.sleep(1)
    print('zadymiarz kaśka | hp = 1/1 | moc = 1')
    print('                               _.._')
    print('                             .'    '.')
    print('                            (____/`\ |')
    print('                           (  |' ' )  )')
    print('                           )  _\= _/  (')
    print('                 __..---.(`_.  ` \    )')
    print('                `;-""-._(_( .      `; (')
    print('                /       `-```--     ;  )')
    print('               /    /  .    ( .  ,| |(')
    print('_.-` ---...__,     /-,..___.- -- _| |_)')
    print(' - `` -.._       ,   |   / ......... ')
    print('          ``;--"`;   |   `-`')
    print('             ``..__.`')
    
    while hpkk > 0:
        print('a) biję')
        print('b) uciekam')
        walkakrespond = input('')
        if walkakrespond == ('a'):
            hpkk -= moc
            time.sleep(1)
            print("zadajesz " ,moc, " damage i zostaje mu ", hpkk, " hp")
            if hpkk <=0 :
                time.sleep(0.5)
                print('                                                 ')
                print(' _ _ _  __ __  _____  _____  _____  _____  _____ ')
                print('| | | ||  |  ||   __|| __  ||  _  ||   | ||  _  |')
                print('| | | ||_   _||  |  ||    -||     || | | ||     |')
                print('|_____|  |_|  |_____||__|__||__|__||_|___||__|__|')
                print('                                                 ')
                time.sleep(3)

                
            else: 
                hp -= mkk
                time.sleep(2)
                print("dostajesz ",mkk, " damage i zostaje ci ", hp, " hp")
                time.sleep(1)
                print('                                          ')
                print('                        //                ')
                print(' _____  _____  _   _  _____ ______  ______')
                print('|_   _|/  __ \| | | ||  _  || ___ \|___  /')
                print('  | |  | /  \/| |_| || | | || |_/ /   / / ')
                print('  | |  | |    |  _  || | | ||    /   / /  ')
                print('  | |  | \__/\| | | |\ \_/ /| |\ \ ./ /___')
                print('  \_/   \____/\_| |_/ \___/ \_| \_|\_____/')
                print('                                          ')
        
    
    
                
#---------------------------------

#----------Lokalizacja1-----------

#---------------------------------

def lok1():
    print("-------OKRĄGLAK-------")
    print('a) szukam zadymy')
    print('b) idę do żabki')  #-----żabka=śmierć----
    print('c) spierdalam')      
    respond = input('')
    #---------------------------------
    #-------Odpowiedź a---------------
    #---------------------------------
    if respond == "a":
        zadyma(hpk,mk,hp)
    
    #---------------------------------
    #-------Odpowiedź b---------------
    #---------------------------------

    
    elif respond == "b":
        print('Wybierz produkt')
        print('a) Baton mocy')
        print('b) Kustosz mocne')
        print('c) Woda')
        respond = input('')
        if respond == "b":
            print('Chlejesz Kustosza i zdychasz, bo w twoim organizmie jest 6 promili piwa')
            time.sleep(4)
            sys.exit("GAME OVER")
        
        elif respond == "c":
            print("Na Wrzecionie nie pije się wody ty śmieciu")
            time.sleep(2)
            sys.exit("GAME OVER")
            
        elif respond == "a":
            print('Mmmm smaczne...')
            time.sleep(2)
            print("O kurde ja..ja..EUHGHGHGHG")
            time.sleep(2)
            print("Sprzedawca: O sory niechcący dałem ci Jad kiełbasiany. Zdychaj LOL")
            time.sleep(4)
            sys.exit("GAME OVER")
    
    #---------------------------------
    #-------Odpowiedź c---------------
    #---------------------------------
    
    #---odpowiedź gdy klikniesz c czyli spierdalaj prowadzi automatycznie do move więc nie trzeba tego pisać---
        
    
        
#---------------------------------

#----------Lokalizacja2-----------

#---------------------------------

def lok2():
    print("-------METRO MŁOCINY-------")
    print("a) Wsiadasz do metra")
    print("b) Skaczesz pod metro")
    print("c) Idziesz leżakować na ławce")
    print("d) Szukasz zadymy")
    print("e) Spierdalam")
    Mrespond = input('')
    #---------------------------------
    #-------Odpowiedź a---------------
    #---------------------------------
    if Mrespond == "a":
        print("*Wsiadasz do metra*")
        time.sleep(3)
        print("*Spotykasz Wrzeciono Man*")
        time.sleep(3)
        print("*Kłaniasz się i grzecznie prosisz żeby cię nie zabił*")
        time.sleep(3)
        print("Wrzeciono Man: nie jesteś wart mojego wzroku...")
        time.sleep(3)
        print('                _  ')
        print(' _____ _____ _ //_ ')
        print('|  __ |_   _| \ | |')
        print('| |  \/ | | |  \| |')
        print('| | __  | | | . ` |')
        print('| |_\ \_| |_| |\  |')
        print(' \____/\___/\_| \_/')
        print('                   ')
        time.sleep(5)
        sys.exit("GAME OVER")
    #---------------------------------
    #-------Odpowiedź b---------------
    #---------------------------------
    
    elif Mrespond == "b":
        print("*Skaczesz pod metro*")
        time.sleep(1)
        print("*Metro idealnie się zatrzymuje przed tobą*")
        time.sleep(3)
        print("NIEEEEEEEEEEE!")
        time.sleep(2)
        print("*Nie wiesz co zrobić i wychodzisz z metra*")
        time.sleep(4)
        
    #---------------------------------
    #-------Odpowiedź c---------------
    #---------------------------------
        
    elif Mrespond == "c":
        print("*Kładziesz się na ławce*")
        time.sleep(3)
        print("*Nagle czujesz że ktoś cie dotyka*")
        time.sleep(3)
        print("Eeee panie co ty robisz!?")
        time.sleep(2)
        print("Zaczynasz czuć coś że ostrego wbija ci się w brzuch, a ty niemożesz nic zrobić, ponieważ jesteś przywiązany...")
        time.sleep(6)
        print("Rozglądasz się i widzisz że jesteś w pokoju tortur, a twój portfel jest pusty...")
        time.sleep(3)
        print("Ruszasz się? (tak lub nie)")
        trespond = input('')
        if trespond == ("tak" or "TAK"):
            print("*Drugi menel zauważa cię ruszającego się...*")
            time.sleep(5)
            print("Nie...")
            time.sleep(1)
            print("To nie może być...")
            time.sleep(1)
            print("kaśka? (bijesz się?(tak lub nie))")
            krespond = input('')
            if krespond == ("tak" or "TAK"):
                zadymak(hpkk,mkk,hp)        #----kaśce dałem wcześniejszą formułę zadymy bo ona cie obrabowuje i nie masz żadnych pieniędzy----
                
            else:
                print("*Kaśka do ciebie podchodzi*")
                time.sleep(2)
                print("Kaśka: Od dawno na to czekałam ", heros, "...")
                time.sleep(2)
                print("*Kaśka przebija cię nagle tulipanem z butelki po piwie, i nieżyjesz*")
                time.sleep(4)
                sys.exit("GAME OVER")
                
        elif trespond == ("nie" or "NIE"):
            print("Narzędzie powoli przebija się przez twoją skórę...")
            time.sleep(2)
            print("Zaczyna cię coraz bardziej drażnić...")
            time.sleep(3)
            print("Nagle kaśka podchodzi do ciebie i coś ci wstrzykuje.")
            time.sleep(3)
            print("Narzędzie przebija cię na wylot, i umierasz")
            time.sleep(0.5)
            print("*W tle słychać smiech kaśki*")
            time.sleep(4)
            sys.exit("GAME OVER")
            
    #---------------------------------
    #-------Odpowiedź d---------------
    #---------------------------------
    
    elif Mrespond == "d":
        print("ZADYMAAAAA!")
        #----tutaj będzie zadyma z grzesiem( z tą poprawioną formułą), którą się tam gdzieś wyżej zdefiniuje----
        print("Niestety narazie zadyma nie działa poprawnie więc nic tu nie ma..")
        time.sleep(3)
        print("...i pozwole ci poprostu odejść.")
        time.sleep(2)
        
    #---------------------------------
    #-------Odpowiedź e---------------
    #---------------------------------
        
    elif Mrespond == "e":
        print("Próbujesz wrócić, ale nagle przed tobą staje 6 umięsnionych mężczyzn.")
        time.sleep(2)
        print("Otaczają cię, i każą się ukłonić, poniważ nazywają siebie Wrzeciońskim Gangiem Osiedlowym")
        print("Kłaniasz się?")
        gangrespond = input('')
        if gangrespond == ("tak" or "TAK"):
            print("*Kłaniasz się*")
            time.sleep(2)
            print("*Myślisz że ci się udało i w końcu wyjdziesz*")
            time.sleep(2)
            print("Nagle jeden z gangsterów wyjmuje spluwę i strzela ci w łeb.")
            time.sleep(0.5)
            print("W tle słychać: No co takich tchórzy trzeba tępić.")
            time.sleep(4)
            sys.exit("GAME OVER")
        
        elif gangrespond == ("nie" or "NIE"):
            print("*Nie kłaniasz się*")
            time.sleep(2)
            print("Gangsterzy wnerwiają się, i każdy z nich po kolei wbija ci sztylet w brzuch.")
            time.sleep(4)
            print("Powoli wykrwawiasz się na Wrzeciońskich ziemiach...")
            time.sleep(4)
            sys.exit("GAME OVER")
        
        
        
            
   
#-----------------------------------

#-----------Mapa-------------------

#-----------------------------------
def mapa():
    print("------------------------")
    print('okrąglak x = 50 z = 10')
    print('metro młociny x = -80 z = 20')
    print('las bielański x = 20 z = -40')
    print('szpital bielański x = -30 z = -10')
    print('Kościół Niepokalanego Poczęcia Najświętszej Maryi Panny x = 70 z = 10')
    print("------------------------")

    time.sleep(12)
#------------------------------------------------------------------------------

#---------------------Poruszanie się-------------------------------------------

#------------------------------------------------------------------------------
def move(x,z):
    while True:
        if (x==50) and (z == 10):
            lok1()
        
        elif (x==(-80)) and (z == 20):
            lok2()
        
        print('----------------------------------------------------------------------------------')
        print(heros,"  KOORDYNATY: ", 'x=', x, "z=", z , "|| hajs: ", hajs, "zł || hp: ", hp,"/",maxhp, "|| moc: ", moc)
        print('----------------------------------------------------------------------------------')
        
        print("a) Północ")
        print("b) Południe")
        print("c) Zachód")
        print("d) Wschód")
        print("e) Mapa")
        respond = input('')
        if respond == "a":
            x += 10
        elif respond == "b":
            x -= 10
        elif respond == "c":
            z -= 10
        elif respond == "d":
            z += 10
        elif respond == "e":
            mapa()
#--------------------------------------------------------------

#----------------------Napis ( Logo )-------------------------

#--------------------------------------------------------------
print(' /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$ ')
print('| $$  /$ | $$| $$__  $$|_____ $$ | $$_____/ /$$__  $$|_  $$_/ /$$__  $$| $$$ | $$ /$$__  $$')
print('| $$ /$$$| $$| $$  \ $$     /$$/ | $$      | $$  \__/  | $$  | $$  \ $$| $$$$| $$| $$  \ $$')
print('| $$/$$ $$ $$| $$$$$$$/    /$$/  | $$$$$   | $$        | $$  | $$  | $$| $$ $$ $$| $$  | $$')
print('| $$$$_  $$$$| $$__  $$   /$$/   | $$__/   | $$        | $$  | $$  | $$| $$  $$$$| $$  | $$')
print('| $$$/ \  $$$| $$  \ $$  /$$/    | $$      | $$    $$  | $$  | $$  | $$| $$\  $$$| $$  | $$')
print('| $$/   \  $$| $$  | $$ /$$$$$$$$| $$$$$$$$|  $$$$$$/ /$$$$$$|  $$$$$$/| $$ \  $$|  $$$$$$/')    
print('|__/     \__/|__/  |__/|________/|________/ \______/ |______/ \______/ |__/  \__/ \______/ ')              
print('                           /$$$$$$$$ /$$   /$$ /$$$$$$$$')              
print('                          |__  $$__/| $$  | $$| $$_____/')
print('                             | $$   | $$  | $$| $$      ')
print('                             | $$   | $$$$$$$$| $$$$$   ')
print('                             | $$   | $$__  $$| $$__/   ')
print('                             | $$   | $$  | $$| $$      ')
print('                             | $$   | $$  | $$| $$$$$$$$')
print('                             |__/   |__/  |__/|________/')
print('                      /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$')
print('                      /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/')
print('                     | $$  \__/| $$  \ $$| $$$$  /$$$$| $$      ')
print('                     | $$ /$$$$| $$$$$$$$| $$ $$/$$ $$| $$$$$   ')
print('                     | $$|_  $$| $$__  $$| $$  $$$| $$| $$__/   ')
print('                     | $$  \ $$| $$  | $$| $$\  $ | $$| $$      ')
print('                     |  $$$$$$/| $$  | $$| $$ \/  | $$| $$$$$$$$')
print('                      \______/ |__/  |__/|__/     |__/|________/')
print('------------------------------------------------------------------------------------------')



         
time.sleep(2)
print('jak nazywa się twój menel: ')
heros = input('')
if heros == "wrzeciono man":
    print("O ty szczylu...")
    time.sleep(3)
    print("Nie tym razem...")
    time.sleep(3)
    sys.exit("WRZECIONO MAN JEST TYLKO JEDEN")
else:
    move(x,z)
