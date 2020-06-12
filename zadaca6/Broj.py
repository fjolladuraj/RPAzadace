from random import randint
from brojError import brojError

class Broj:
    def display_title_bar(self):
        print("\t******************************************")
        print("\t*** Igra pogađanja - Razvoj poslovnih aplikacija ***")
        print("\t******************************************")

    def get_user_choice(self):
        print("\n [1] Igraj igru pogađanja broja.")
        print("[x] Izlaz.")
        return input("Odaberite što želite napraviti?")
           
    def start_game(self):
        tajni_broj = randint(1,100)
        broj_pokusaja = 1
        while True:
            pokusaj = int(input("Pogodite broj:"))
            if pokusaj > tajni_broj:
                print("Vaš broj je veći od traženog broja!")
            elif pokusaj < tajni_broj:
                print("Vaš broj je manji od traženog broja!")
            elif pokusaj == tajni_broj:
                print("Pogodili ste broj koji je odabralo računalo! Čestitamo.")
                break

            if broj_pokusaja == 10:
                print("Potrošili ste 10 pokušaja, traženi broj je bio {}".format(tajni_broj))
                break
            broj_pokusaja = broj_pokusaja + 1

    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                self.start_game()
            elif choice == 'x':
                print("Hvala na igranju. Pozdrav!")
            else:
                raise brojError(101)

if __name__ == '__main__':
    game = Broj()
    game.play()