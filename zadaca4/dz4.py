import random
from dz4Error import dz4Error

class RPSLS:
	def __init__(self):
		self.player_input = None
		self.player_number = -1
		self.computer_input = None
		self.computer_number = -1

	def display_title_bar(self):
		print("***********************************************")
		print("**** Rock, paper, scissors, lizard, spock *****")
		print("***********************************************")

	def main_menu(self):
		print("\n[1] Igraj Rock, paper, scissors, lizard, spock.")
		print("[2] Izlaz.")
		self.playerChoice = int(input("Odaberite što želite raditi: "))

	def broj_u_string(self):
		if self.computer_number == 0:
			self.computer_input = "Rock"
		elif self.computer_number == 1:
			self.computer_input = "Paper"
		elif self.computer_number == 2:
			self.computer_input = "Scissors"
		elif self.computer_number == 3:
			self.computer_input = "Lizard"
		elif self.computer_number == 4:
			self.computer_input = "Spock"
		else:
			self.computer_input = None
			print("Greška")
		return self.computer_input
	
	def string_u_broj(self):
		if self.player_input == "rock":
			self.player_number = 0
		elif self.player_input == "paper":
			self.player_number = 1
		elif self.player_input == "scissors":
			self.player_number = 2
		elif self.player_input == "lizard":
			self.player_number = 3
		elif self.player_input == "spock":
			self.player_number = 4
		else:
			self.player_number = -1
			raise RPSLS_Error(102)
		return self.player_number
		
	def Play(self):	
		self.display_title_bar()
		self.main_menu()

		while (self.playerChoice != 2):
			player_score = 0
			computer_score = 0
			
			if(self.playerChoice > 2 or self.playerChoice < 1):
				raise RPSLS_Error(101)
			else:
				while (player_score < 3 and computer_score < 3):
					print("=" * 50)
					self.player_input = input("Odaberite jedno od navedenog (Rock/Paper/Scissors/Lizard/Spock): ").lower()
					self.player_number = self.string_u_broj()

					self.computer_number = random.randrange(0, 5)

					ostatak = (self.player_number - self.computer_number) % 5

					if(self.player_number == -1):
						winner = "Greška"
						raise RPSLS_Error(102)
					else:
						if(ostatak == 0):
							winner = "Neriješeno je!"
						elif(ostatak == 1 or ostatak == 2):
							winner = "Igrač"
							player_score += 1
						elif(ostatak == 3 or ostatak == 4):
							winner = "Računalo"
							computer_score += 1

					self.computer_input = self.broj_u_string()

					print("=" * 50)
					print("Igrač je odabrao: {}".format(self.player_input.capitalize()))
					print("Računalo je odabrao: {}".format(self.computer_input))
					print("=" * 50)
					print("Ovu rundu je dobio: {}".format(winner))
					print("=" * 50)
					print("Igrač ima {} bodova.".format(player_score))
					print("Računalo ima {} bodova.".format(computer_score))

					
				if(player_score == 3):
					print("=" * 50)
					print("Pobjednik igre je Igrač!")
					print("=" * 50)
				elif(computer_score == 3):
					print("=" * 50)
					print("Pobjednik igre je računalo!")
					print("=" * 50)
				
				self.main_menu()

				print("=" * 50)
				print("Hvala na igranju, pozdrav!")
				print("=" * 50)

		

if __name__ == "__main__":
	game = dz4()
	game.Play()