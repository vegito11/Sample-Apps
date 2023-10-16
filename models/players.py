
class Player:

	cnt = 1

	def __init__(self, name, age, club, goals, matches):
		self.name = name
		self.age = age
		self.club = club
		self.goals = goals
		self.matches = matches
		self.id = Player.cnt

		Player.cnt += 1
	
	def __str__(self):
		return f"{self.name} ({self.club}) -- {self.matches} -- {self.id} "

    # Add a to_dict method to serialize the Player object to a dictionary
	def to_dict(self):
		return {
			"id": self.id,
			"name": self.name,
			"age": self.age,
			"club": self.club,
			"goals": self.goals,
			"matches": self.matches
		}		

if __name__ == '__main__':
	p = Player("Lionel Messi", 23, "PSG", 734, 819)
	print(p)
	p = Player("Lionel Messi", 23, "PSG", 734, 819)
	print(p)
	
	