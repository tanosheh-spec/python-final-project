



import random

print( " *** Hads Adad *** ")

emtiaz_kol = 0

while True:
    adad_maakhfi = random.randint (100 , 999)
    tedad_talash = 0
    emtiaz = 100

    print (" *** shoroe bazi *** ")
    print (" ye adad 3 raghami (100 , 999) hads bezan ")

    while True:
        hads = int ( input (" hads: "))

        if hads < 100 or hads > 999 :
            print ( " khata! adad bayad 3 raghami bashad (100 ta 999) dobare talash kon. " )   
            continue

        tedad_talash = tedad_talash + 1

        if hads > adad_maakhfi :
            print ( " kochik tare! ye adad kochik tar hads bezan. " )
            emtiaz = emtiaz - 2
        elif hads < adad_maakhfi : 
            print ( " bozorg tare! ye adad bozorg tar hads bezan. " )    
        else:
            if emtiaz < 0 :
                emtiaz = 0
            print ( " AFRIN! dorost hads zadi. " )
            print ( " tedad talash dr in set: " , tedad_talash )
            print ( " emtiaz in set: " , emtiaz )    

            emtiaz_kol = emtiaz_kol + emtiaz
            print ( " emtiaz kol: " , emtiaz_kol )
            break
    dobare = input ( " dobare bazi mikoni? (yes / no): ") 
    if dobare != "yes":
        print ( " payan " )
        print ( " bay bay " )
        print ( " emtiaz kol: " , emtiaz_kol ) 
        break




