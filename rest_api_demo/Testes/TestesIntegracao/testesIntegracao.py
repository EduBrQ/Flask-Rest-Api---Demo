from app import app
import unittest
from flask import Flask, abort, jsonify, request

class FlaskTestCase(unittest.TestCase):

	# assegure-se de que o Flask foi configurado corretamente
	def test_home(self):
		tester = app.test_client(self)
		response = tester.get('/home', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

	def test_predict_pressao(self):
		tester = app.test_client(self)
		response = tester.post('/pressao', json={
        'Batimentos': 35, 'Calorias': 50
    }, follow_redirects=True)
		json_data = response.get_json()
		self.assertEqual(json_data, {'results': 'Sua Pressao esta muito Baixa'})

	def test_predict_diabetes(self):
		tester = app.test_client(self)
		response = tester.post('/diabetes', json={
        'Glucose': 35, 'BloodPressure': 50, 'Insulin': 50, 'BMI': 50, 'Age': 50
    }, follow_redirects=True)
		json_data = response.get_json()
		self.assertEqual(json_data, {'results': 'Sem Diabetes'})

if __name__ == '__main__':
	unittest.main()