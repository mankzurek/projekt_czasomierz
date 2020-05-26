import time


while True:
    godz = int(input("wpisz godzine "))
    min = int(input("wpisz minute"))
    sek = int(input("Wpisz sekunde "))
    while sek >= 0 and sek < 60 and min >= 0 and min < 60 and godz >= 0 and godz < 24:
        m, s = divmod(sek, 60)              # te zmienne s m h maja byc nowe nie takie jak sek min czy godz!!!!
        h, m = divmod(min, 60 )
        d, h = divmod(godz, 24)
        czas = str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)
        print("\r", end=czas)
        sek += 1
        time.sleep(1)
    print("wysz wlasciwe cyfry ")



