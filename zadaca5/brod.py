import random
from rocket import Rocket
class Brodovi(Rocket):
    # brodovi simuliraju ratne brodove, ali zapravo koristi sve metode rakete
    # pa ga možemo zvati simulacija rakete
    def __init__(self, x=0, y=0, route = 0):
        super().__init__(x, y)
        self.route = route
    

    def fight_brod(self):
        # kreiram nekoliko brodova i raketa s pozicijama slučajnog odabira (biblioteka random)
        # brodovi imaju random broj odrađenih/napravljenih ruta na ratnom polju
        brodNum = int(input("Unesite broj broda na ratnom polju:")) # upisao broj 5
        brodovi = []
        rockets = []
        for x in range(0,brodNum): # for petlja se vrti od 0 do 5
            x = random.randint(0,100)
            y = random.randint(1,100)
            self.route = random.randint(0,10)
            brodovi.append(Brodovi(x,y,self.route))

        for x in range(0, brodNum): # for petlja se vrti od 0 do 5
            x = random.randint(0, 100)
            y = random.randint(1,100)
            rockets.append(Rocket(x, y))
        
        # prikazivanje/ispis napravljene rute svakog broda u listi na ratnom polju
        for index, brod in enumerate(brodovi):
            print("Brod {} je napravio {} rutu/e".format(index+1, brod.route))
        
        print("\n")
        yourBrod = int(input("Od {} Broda, vaš brod je pod brojem:".format(brodNum)))

        chosenBrod = brodovi[yourBrod-1]
        # prikazivanje/ispis udaljenosti vašeg broda od ostalih brodova
        for index, brod in enumerate(brodovi):
            distance = chosenBrod.get_distance(brod)
            print("Vaš brod je udaljen {} kilometara od broda broj {}.".format(distance, index+1))
        
        print("\n")
        # prikazivanje/ispis udaljenosti vašeg broda od raketa u listi raketa
        for index, rocket in enumerate(rockets):
            distance = chosenBrod.get_distance(rocket)
            print("Vaš brod je udaljen {} kilometara od rakete broj {}.".format(distance, index+1))

    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            # na temelju korisnikova odabira izvršavamo programsku logiku naše igrice ovisno o tome
            #što je korisnik odabrao
            self.display_title_bar()
            if choice == '1':
                self.fight()
            elif choice =='2':
                Brodovi().fight_brod()
            elif choice == 'x':
                print("\nHvala na igri i poštenoj borbi :) . Pozdrav.")
            else:
                raise dz_5Error(101)