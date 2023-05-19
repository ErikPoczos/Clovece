#Program vypracoval Erik Póczoš
#Program funguje pre 6 a menej domcekov. Kazdy panak sa musi dostat na volnu poziciu v domceku, inak je tah neplatny
#Panacikovia sa dokazu navzajom vyhadzovat. Maximalna hodnota hodu kocky je 6.
#Pohyb figurky je realizovany tak, ze figurka hlada dalsie policko okolo seba, na ktore moze stupit. Toto sa opakuje tolko-krat, aka je hodnota hodu kocky

from random import *

sachovnica = []

def gensachovnicu(n):
    start = (n-3)//2
    if n<5 or n%2 == 0:                 #Kontroluje sa, či číslo n je vhodný rozmer pre šachovnicu
        print ("Zly rozmer sachovnice (cislo musi byt neparne, vacsie ako 4 a mensie ako 17).")
    else:
        for a in range (n):             #for cyklus vytvorí n*n sachovnicu, ktora je vytvorena pomocou 2D listu
            line = n*["*"]              #kazdy prvok 2D listu je znak *
            sachovnica.append(line)
            line = []

        for y in range(start):
            for x in range (start):               #rohy sachovnice sa nahradia medzerou
                sachovnica[y][x] = " "
                sachovnica[-y-1][-x-1] = " "
                sachovnica[y][x+(n-start)] = " "
                sachovnica[y+(n-start)][x] = " "

        for i in range (start):                               #vytvoria sa domceky
            sachovnica[i+1][n//2] = "D"
            sachovnica[i+start+2][n//2] = "D"
            sachovnica[n//2][i+1] = "D"
            sachovnica[n//2][i+start+2] = "D"

        sachovnica[start+1][start+1] = "X"          #vytvori sa X v strede
        return sachovnica

def tlacsachovnicu(sac):
    print (" ", end=" ")
    for a in range (len(sachovnica)):    #napisu sa cisla v prvom riadko
        print (a%10, end= " ")
    print()
    counter = 0
    for i in sachovnica:                #napise sa cislo riadku + n-ty riadok sachovnice
        print (counter%10, end=" ")
        counter+=1
        for j in i:
            print (j, end =" ")
        print()
    print()

def down (y, x, way, roll, steps, ele):    #funkcia na posuvanie panaka smerom dole
    while roll > 0 and y != (len(sachovnica)-1) and sachovnica[y+1][x] in ele:
        y += 1
        roll -=1
        way = "down"
        steps += 1
    return [y, x, way, roll, steps, ele]

def right(y, x, way, roll, steps, ele):    #funkcia na posuvanie panaka smerom doprava
    while roll > 0 and x != (len(sachovnica)-1) and sachovnica[y][x+1] in ele:
        x += 1
        roll -=1
        way = "right"
        steps += 1
    return [y, x, way, roll, steps, ele]

def left(y, x, way, roll, steps, ele):     #funkcia na posuvanie panaka smerom dolava
    while roll > 0 and x != 0 and sachovnica[y][x-1] in ele:
        x -= 1
        roll -=1
        way = "left"
        steps += 1
    return [y, x, way, roll, steps, ele]

def up(y, x, way, roll, steps, ele):       #funkcia na posuvanie panaka smerom hore
    while roll > 0 and y != 0 and sachovnica[y-1][x] in ele:
        y -= 1
        roll -=1
        way = "up"
        steps += 1
    return [y, x, way, roll, steps, ele]

def rolling():                             #funkcia na hod kocky
    rolled = randint(1,6)
    return rolled
        
def game():
    roll = winner_name = None
    n = len(sachovnica)
    mid = (n-1)//2
    lenght = (3*n)+(n-5)    #dlzka hracieho pola
    fig_AC = fig_BC = houses = (n-3)//2
    dataA = dataAbackup = [0, mid+1, "down", roll, 0, ["*", "b"]]
    dataB = dataBbackup = [n-1, mid-1, "up", roll, 0, ["*", "b"]]
    winner = fig_A = fig_B = False
    counter = 0
    if n != 0:     #ak n je validne, tak sa vykona simulacia
        while winner != True:
            counter += 1
            print("Kolo", counter)
            #Pohyb hrac A

            if fig_A == False:                                      #ak A nema figurku na sachovnici, hodi sa kocka
                dataA = [0, mid+1, "down", roll, 0, ["*", "b"]]
                roll = rolling()
                if roll == 6:                                       #ak padne 6, polozi sa figurka na sachovnicu
                    fig_A = True
                    print("Na kocke hráča A padlo číslo", roll)
                    print()
                    sachovnica[dataA[0]][dataA[1]] = "a"
                    tlacsachovnicu(sachovnica)
                else:
                    print("Na kocke hráča A padlo číslo", roll)
                    print()
                    tlacsachovnicu(sachovnica)

            if fig_A == True:                                       #ak je figurka A na sachovnici, tak sa hadze kockou a vykona sa pohyb figruky
                dataA[3] = rolling()
                print("Na kocke hráča A padlo číslo", dataA[3])
                print()
                if dataA[4]+dataA[3] <= lenght:                     #ak hodom figurka neprejde celu hraciu plochu
                    while dataA[3] != 0:                            #kym hod nieje 0
                        if dataA[0] != (len(sachovnica)-1) and sachovnica[dataA[0]+1][dataA[1]] in dataA[5] and dataA[2] != "up":       #pohyb dole
                            sachovnica[dataA[0]][dataA[1]] = "*"
                            dataA = down(dataA[0], dataA[1], dataA[2], dataA[3], dataA[4], dataA[5])
                            sachovnica[dataA[0]][dataA[1]] = "a"

                        elif dataA[1] != (len(sachovnica)-1) and sachovnica[dataA[0]][dataA[1]+1] in dataA[5] and dataA[2] != "left":     #pohyb doprava
                            sachovnica[dataA[0]][dataA[1]] = "*"
                            dataA = right(dataA[0], dataA[1], dataA[2], dataA[3], dataA[4], dataA[5])
                            sachovnica[dataA[0]][dataA[1]] = "a"

                        elif dataA[1] != 0 and sachovnica[dataA[0]][dataA[1]-1] in dataA[5] and dataA[2] != "right":     #pohyb dolava
                            sachovnica[dataA[0]][dataA[1]] = "*"
                            dataA = left(dataA[0], dataA[1], dataA[2], dataA[3], dataA[4], dataA[5])
                            sachovnica[dataA[0]][dataA[1]] = "a"   

                        elif dataA[0] != 0 and sachovnica[dataA[0]-1][dataA[1]] in dataA[5] and dataA[2] != "down":     #pohyb hore
                            sachovnica[dataA[0]][dataA[1]] = "*"
                            dataA = up(dataA[0], dataA[1], dataA[2], dataA[3], dataA[4], dataA[5])
                            sachovnica[dataA[0]][dataA[1]] = "a"

                    sachovnica[dataA[0]][dataA[1]] = "a"        #vypocitana pozicia figurky sa ulozy

                    if sachovnica[dataA[0]][dataA[1]] == sachovnica[dataB[0]][dataB[1]]:    #vyhadzovanie figurok
                        print ("Hrac A vyhodil hraca B!")
                        print()
                        fig_B = False
                        dataB = dataBbackup
                
                else:                                               #ak by figurka presla hraciu plochu
                    if (lenght + houses) >= (dataA[4] + dataA[3]):  
                        dataAbackup = dataA
                        end = (dataA[4] + dataA[3] - lenght)        #rozdeli sa hod kocky na 2 casti.
                        if dataA[3] == end:                         
                            new_roll = end                         
                        else:
                            new_roll = dataA[3] - end
                        dataA[3] = new_roll

                        while dataA[4]+ new_roll <= lenght:         # 1. cast posunie panaka na koniec svojho hracieho pola (pozicia pred domcekami)
                            while dataA[3] != 0:
                                if dataA[0] != 0 and sachovnica[dataA[0]-1][dataA[1]] in dataA[5] and dataA[2] != "down":     #hore
                                    sachovnica[dataA[0]][dataA[1]] = "*"
                                    dataA = up(dataA[0], dataA[1], dataA[2], dataA[3], dataA[4], dataA[5])

                                elif dataA[1] != (len(sachovnica)-1) and sachovnica[dataA[0]][dataA[1]+1] in dataA[5] and dataA[2] != "left":     #doprava
                                    sachovnica[dataA[0]][dataA[1]] = "*"
                                    dataA = right(dataA[0], dataA[1], dataA[2], dataA[3], dataA[4], dataA[5])

                        dataA[3] = end                             # 2. cast posunie panaka do domceka
                        dataA[5] = ["D", "A"]
                        sachovnica[dataA[0]][dataA[1]] = "*"
                        dataA = down(dataA[0], dataA[1], dataA[2], dataA[3], dataA[4], dataA[5])

                        if sachovnica[dataA[0]][dataA[1]] == "A":   #ak je domcek obsadeny, tah sa rusi
                            dataA = dataAbackup
                            sachovnica[dataA[0]][dataA[1]] = "a"
                            pass

                        else:                                       #ak je domcek volny, obsadi
                            fig_AC -= 1
                            if fig_AC == 0:
                                winner = True
                                winner_name = "A"
                            sachovnica[dataA[0]][dataA[1]] = "A"
                            dataA = [0, mid+1, "down", roll, 0, ["*", "b"]]
                            fig_A = False

                if sachovnica[dataB[0]][dataB[1]] != sachovnica[dataBbackup[0]][dataBbackup[1]]:   #ulozy sa pozicia figurky B do 2D zoznamu, kedze figurka A prepise poziciu v pripade
                    sachovnica[dataB[0]][dataB[1]] = "b"                                           #kedy fig A prejde cez fig B
                tlacsachovnicu(sachovnica)
            #pohyb hráča B

            if fig_B == False:                                          #to isté ako pri fig A
                dataB = [n-1, mid-1, "up", roll, 0, ["*", "a"]]
                roll = rolling()
                if roll == 6:
                    fig_B = True
                    print("Na kocke hráča B padlo číslo", roll)
                    print()
                    sachovnica[dataB[0]][dataB[1]] = "b" 
                    tlacsachovnicu(sachovnica)
                else:
                    print("Na kocke hráča B padlo číslo", roll)
                    print()
                    tlacsachovnicu(sachovnica)

            if fig_B == True and winner == False:
                dataB[3] = rolling()
                print("Na kocke hráča B padlo číslo", dataB[3])
                print()
                if dataB[4]+dataB[3] <= lenght:
                    while dataB[3] != 0:
                        if dataB[0] != 0 and sachovnica[dataB[0]-1][dataB[1]] in dataB[5] and dataB[2] != "down":     #hore
                            sachovnica[dataB[0]][dataB[1]] = "*"
                            dataB = up(dataB[0], dataB[1], dataB[2], dataB[3], dataB[4], dataB[5])
                            sachovnica[dataB[0]][dataB[1]] = "b"

                        elif dataB[1] != 0 and sachovnica[dataB[0]][dataB[1]-1] in dataB[5] and dataB[2] != "right":     #dolava
                            sachovnica[dataB[0]][dataB[1]] = "*"
                            dataB = left(dataB[0], dataB[1], dataB[2], dataB[3], dataB[4], dataB[5])
                            sachovnica[dataB[0]][dataB[1]] = "b" 

                        elif dataB[0] != (len(sachovnica)-1) and sachovnica[dataB[0]+1][dataB[1]] in dataB[5] and dataB[2] != "up":       #dole
                            sachovnica[dataB[0]][dataB[1]] = "*"
                            dataB = down(dataB[0], dataB[1], dataB[2], dataB[3], dataB[4], dataB[5])
                            sachovnica[dataB[0]][dataB[1]] = "b"

                        elif dataB[1] != (len(sachovnica)-1) and sachovnica[dataB[0]][dataB[1]+1] in dataB[5] and dataB[2] != "left":     #doprava
                            sachovnica[dataB[0]][dataB[1]] = "*"
                            dataB = right(dataB[0], dataB[1], dataB[2], dataB[3], dataB[4], dataB[5])
                            sachovnica[dataB[0]][dataB[1]] = "b"
                    sachovnica[dataB[0]][dataB[1]] = "b"
                    if sachovnica[dataB[0]][dataB[1]] == sachovnica[dataA[0]][dataA[1]]:
                        print ("Hrac B vyhodil hraca A!")
                        print()
                        fig_B = False
                        dataB = dataBbackup
                else:
                    if (lenght + houses) >= (dataB[4] + dataB[3]):
                        dataBbackup = dataB
                        end = (dataB[4] + dataB[3] - lenght)
                        if dataB[3] == end:
                            new_roll = end
                        else:
                            new_roll = dataB[3] - end
                        dataB[3] = new_roll

                        while dataB[4]+ new_roll <= lenght:
                            while dataB[3] > 0:
                                if dataB[0] != (len(sachovnica)-1) and sachovnica[dataB[0]+1][dataB[1]] in dataB[5] and dataB[2] != "up":       #dole 
                                    sachovnica[dataB[0]][dataB[1]] = "*"
                                    dataB = down(dataB[0], dataB[1], dataB[2], dataB[3], dataB[4], dataB[5])

                                elif dataB[1] != 0 and sachovnica[dataB[0]][dataB[1]-1] in dataB[5] and dataB[2] != "right":     #dolava
                                    sachovnica[dataB[0]][dataB[1]] = "*"
                                    dataB = left(dataB[0], dataB[1], dataB[2], dataB[3], dataB[4], dataB[5])

                        dataB[5] = ["D", "B"]
                        dataB[3] = end
                        sachovnica[dataB[0]][dataB[1]] = "*"
                        dataB = up(dataB[0], dataB[1], dataB[2], dataB[3], dataB[4], dataB[5])
                        if sachovnica[dataB[0]][dataB[1]] == "B":
                            dataB = dataBbackup
                            sachovnica[dataB[0]][dataB[1]] = "b"
                            pass
                        else:
                            fig_BC -= 1
                            if fig_BC == 0:
                                winner = True
                                winner_name = "B"
                            sachovnica[dataB[0]][dataB[1]] = "B"
                            dataB = [n-1, mid-1, "up", roll, 0, ["*", "a"]]
                            fig_B = False

                if sachovnica[dataA[0]][dataA[1]] != sachovnica[dataAbackup[0]][dataAbackup[1]]:
                    sachovnica[dataA[0]][dataA[1]] = "a"
                tlacsachovnicu(sachovnica)

        print("Vitazom sa stal hrac", winner_name, "po",counter,"koloch!")

gensachovnicu(int(input("Zadajte rozmer šachovnice: ")))
print()
tlacsachovnicu(sachovnica)
game()