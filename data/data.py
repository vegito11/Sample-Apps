class Data:
	players_data = []

	@classmethod
	def get_by_id(cls, pid):
		for ply in cls.players_data:
			if str(ply["id"]) == str(pid):
				return ply
		return None

	@classmethod
	def delete_by_id(cls, pid):
		ind = 0
		for ply in cls.players_data:
			if str(ply["id"]) == str(pid):
				del Data.players_data[ind]
			ind += 1
		return None
