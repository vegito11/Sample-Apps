import unittest
from app import app
from controllers.memory_controller import players_memory

class TestMemoryController(unittest.TestCase):

    def setUp(self):
        players_memory.clear()
        self.client = app.test_client()

    def test_get_all_players_memory(self):
        players_memory['1'] = {
            'id': '1',
            'name': 'Lionel Messi',
            'matches': 900,
            'goals': 860,
            'assists': 900,
            'club': 'Inter Miami',
            'age': 40,
            'country': 'Argentina'
        }
        response = self.client.get('/memory/players')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]['name'], 'Lionel Messi')

    def test_create_player_memory(self):
        response = self.client.post('/memory/player', json={
            'name': 'Lionel Messi',
            'matches': 900,
            'goals': 860,
            'assists': 900,
            'club': 'Inter Miami',
            'age': 40,
            'country': 'Argentina'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        player_id = response.json['id']
        self.assertEqual(players_memory[player_id]['name'], 'Lionel Messi')

    def test_update_player_memory(self):
        player_id = '1'
        players_memory[player_id] = {
            'id': player_id,
            'name': 'Lionel Messi',
            'matches': 900,
            'goals': 860,
            'assists': 900,
            'club': 'Inter Miami',
            'age': 40,
            'country': 'Argentina'
        }
        response = self.client.put(f'/memory/player/{player_id}', json={
            'name': 'Lionel Messi',
            'matches': 910,
            'goals': 870,
            'assists': 910,
            'club': 'Inter Miami',
            'age': 41,
            'country': 'Argentina'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(players_memory[player_id]['matches'], 910)

    def test_delete_player_memory(self):
        player_id = '1'
        players_memory[player_id] = {
            'id': player_id,
            'name': 'Lionel Messi',
            'matches': 900,
            'goals': 860,
            'assists': 900,
            'club': 'Inter Miami',
            'age': 40,
            'country': 'Argentina'
        }
        response = self.client.delete(f'/memory/player/{player_id}')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(player_id, players_memory)

if __name__ == '__main__':
    unittest.main()
