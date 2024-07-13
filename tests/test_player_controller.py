import unittest
from unittest.mock import patch, MagicMock
from app import app

class TestPlayerController(unittest.TestCase):

    @patch('controllers.player_controller.collection')
    def test_get_all_players(self, mock_collection):
        mock_collection.find.return_value = [
            {
                '_id': '60c72b2f4f1a2567f8d6b6c0',
                'name': 'Lionel Messi',
                'matches': 900,
                'goals': 860,
                'assists': 900,
                'club': 'Inter Miami',
                'age': 40,
                'country': 'Argentina'
            }
        ]
        with app.test_client() as client:
            response = client.get('/api/players')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            self.assertEqual(response.json[0]['name'], 'Lionel Messi')

    @patch('controllers.player_controller.collection')
    def test_create_player(self, mock_collection):
        mock_collection.insert_one.return_value.inserted_id = '60c72b2f4f1a2567f8d6b6c0'
        with app.test_client() as client:
            response = client.post('/api/player', json={
                'name': 'Lionel Messi',
                'matches': 900,
                'goals': 860,
                'assists': 900,
                'club': 'Inter Miami',
                'age': 40,
                'country': 'Argentina'
            })
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['_id'], '60c72b2f4f1a2567f8d6b6c0')

    @patch('controllers.player_controller.collection')
    def test_update_player(self, mock_collection):
        mock_collection.update_one.return_value.matched_count = 1
        with app.test_client() as client:
            response = client.put('/api/player/60c72b2f4f1a2567f8d6b6c0', json={
                'name': 'Lionel Messi',
                'matches': 910,
                'goals': 870,
                'assists': 910,
                'club': 'Inter Miami',
                'age': 41,
                'country': 'Argentina'
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], 'Player updated')

    @patch('controllers.player_controller.collection')
    def test_delete_player(self, mock_collection):
        mock_collection.delete_one.return_value.deleted_count = 1
        with app.test_client() as client:
            response = client.delete('/api/player/60c72b2f4f1a2567f8d6b6c0')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], 'Player deleted')

if __name__ == '__main__':
    unittest.main()
