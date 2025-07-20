def test_get_mechanics(client):
    response = client.get('/mechanics/')
    assert response.status_code == 200

def test_create_mechanic(client):
    response = client.post('/mechanics/', json={
        'name': 'John Doe',
        'specialty': 'Engine Repair'
    })
    assert response.status_code == 201
