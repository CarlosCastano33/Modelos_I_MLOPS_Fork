#Se importan las librerías necesarias
from flask import Flask, request, jsonify
import threading
import joblib
import os
import pandas as pd

#Se crea la aplicación Flask
app = Flask(__name__)

#Algunas variables globales para manejar el estado del entrenamiento y las predicciones
train_status = "not training"
prediction_status = "without prediction"
MODEL_PATH = "model.pkl"

#Función para ejecutar el entrenamiento en un hilo separado
def _train():
    global train_status
    train_status = "training"
    import train
    # ejecutar el archivo completo
    # train  # con que se importe, ya se ejecuta todo
    train_status = "not training"

#Endpoint para consultar el estado del entrenamiento
@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": train_status,
        "model_exists": os.path.exists(MODEL_PATH)
    }), 200

#Endpoint para iniciar el entrenamiento
@app.route("/train", methods=["POST"])
def train_endpoint():
    if train_status == "training":
        return jsonify({"error": "Already training"}), 409

    thread = threading.Thread(target=_train)
    thread.start()
    return jsonify({"result": "Training started"}), 202

#Endpoint para realizar una predicción
@app.route("/predict", methods=["POST"])    # Recibe solo un dato
def predict_endpoint():
    
    global prediction_status

    data = request.json
    df = pd.DataFrame([data])
    df.to_csv("data.csv", index=False)

    # Se valida existencia del modelo entrenado
    if not os.path.exists(MODEL_PATH):
        return jsonify({"error": "Model not found"}), 404
    
    import predict
    prediction_status = "prediction made"

    prediction = pd.read_csv('predictions.csv')
    return jsonify({"Prediction": prediction.to_dict(orient="records")}), 200

#Endpoint para consultar la última predicción realizada
@app.route("/predict/last", methods=["GET"])
def predict_made():
    if prediction_status == "without prediction":
        return jsonify({"Error": "There are no predictions yet"}), 404

    prediction = pd.read_csv('predictions.csv')
    return jsonify({"Prediction": prediction.to_dict(orient="records")}), 200

#Se ejecuta la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)