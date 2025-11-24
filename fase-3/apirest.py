from flask import Flask, request, jsonify
import threading
import joblib
import os
import pandas as pd

app = Flask(__name__)

train_status = "not training"
prediction_status = "without prediction"
MODEL_PATH = "model.pkl"
import predict

def _train():
    global train_status
    train_status = "training"
    # Se importa el script de entrenamiento y se ejecuta
    import train
    train.main()
    # Como el script guarda el modelo entrenado, cambiamos el estado del entrenamiento
    train_status = "not training"

# ------------------------------------------------------
#        ENDPOINTS
# ------------------------------------------------------

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": train_status}), 200

@app.route("/train", methods=["POST"])
def train_endpoint():
    if train_status == "training":
        return jsonify({"error": "Already training"}), 409

    thread = threading.Thread(target=_train)
    thread.start()
    return jsonify({"result": "Training started"}), 202

@app.route("/predict", methods=["POST"])    # Recibe solo un dato
def predict_endpoint():
    global prediction_status

    data = request.json
    df = pd.DataFrame([data])
    df.to_csv("data.csv", index=False)

    # Se valida existencia del modelo entrenado
    if not os.path.exists(MODEL_PATH):
        return jsonify({"error": "Model not found"}), 404
    
    predict.main()
    prediction_status = "prediction made"

    prediction = pd.read_csv('predictions.csv')
    return jsonify({"Prediction": prediction.to_dict(orient="records")}), 200

@app.route("/predict/last", methods=["GET"])    # Devuelve la última predicción
def predict_made():
    if prediction_status == "without prediction":
        return jsonify({"Error": "There are no predictions yet"}), 404

    prediction = pd.read_csv('predictions.csv')
    return jsonify({"Prediction": prediction.to_dict(orient="records")}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)