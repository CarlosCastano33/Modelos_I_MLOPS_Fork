import requests
import time

#Consultar el estado inicial
response = requests.get('http://localhost:5000/status')
print("Initial Status:", response.json())

#Inicia el entrenamiento
response = requests.post('http://localhost:5000/train')
print("Train:", response.json())

#Se esoera a que el entrenamiento termine
while True:
    status = requests.get('http://localhost:5000/status').json()
    print("Status:", status)
    
    if status["status"] == "not training" and status["model_exists"] == True:
        print("Training finished and model is ready.")
        break

    time.sleep(2)

#Dato para realizar la predicción
data = {
    "id": 0,
    "user_id": "****589084",
    "age": 44,
    "Gender": "O",
    "Date_Registered": "2020-01-01",
    "Is_current_loyalty_program_member": "NO",
    "loyalty_points_redeemed": 5,
    "loyalty_tier": "",
    "Received_tier_discount_percentage": "",
    "Received_card_discount_percentage": 3.0,
    "Received_coupon_discount_percentage": 3,
    "product_category": "office supplies",
    "Product_value": 1003,
    "transaction_id": "***95994394",
    "order_id": "***242641",
    "payment_method": "visa_c",
    "payment_datetime": "2020-01-05 22:27:16",
    "purchased_datetime": "2020-01-05 22:27:16",
    "purchase_medium": "online",
    "final_payment": 1293.0,
    "released_date": "2020-01-12",
    "estimated_delivery_date": "2020-01-17",
    "received_date": "2020-01-17",
    "shipping_method": "standard",
    "tracking_number": "***9AWDD64SYI"
}

#Se realiza la predicción
response = requests.post('http://localhost:5000/predict', json=data)
print("Prediction:", response.json())

#Se consulta la última predicción realizada
response = requests.get('http://localhost:5000/predict/last')
print("Last Prediction:", response.json())