def test_get_tickets(client):
    response = client.get('/tickets/')
    assert response.status_code == 200

def test_create_ticket(client):
    response = client.post('/tickets/', json={
        'description': 'Fix brakes',
        'is_complete': False,
        'mechanic_id': 1
    })
    assert response.status_code == 201
