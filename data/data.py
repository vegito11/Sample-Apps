class Data:
    players_data = []

    @classmethod
    def get_all(cls):
        return cls.players_data

    @classmethod
    def get_by_id(cls, pid):
        for ply in cls.players_data:
            if str(ply.get("id")) == str(pid):  # Use .get() to safely access the "id" key
                return ply
        return None  # Return None if the player is not found

    @classmethod
    def delete_by_id(cls, pid):
        to_delete = None
        for ply in cls.players_data:
            if str(ply.get("id")) == str(pid):
                to_delete = ply
                break

        if to_delete is not None:
            cls.players_data.remove(to_delete)  # Remove the player
            return to_delete  # Return the deleted player
        else:
            return None  # Return None if the player is not found

    @classmethod
    def add(cls, player):
        cls.players_data.append(player)  # Add a new player to the list
