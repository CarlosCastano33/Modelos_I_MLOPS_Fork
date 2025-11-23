from flask import Flask, request, jsonify
import threading
import joblib
import os
import padas as pd

app = Flask(__name__)

train_status = "not training"
MODEL_PATH = "model.pkl"

def _train():
    global train_status
    train_status = "training"
    # Se importa el script de entrenamiento y se ejecuta
    import train
    train.main()
    # Como el script guarda el modelo entrenado, cambiamos el estado del entrenamiento
    train_status = "not training"

def _predict(): # Leer linea 47-49
    return  

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": train_status})

@app.route("/train", methods=["POST"])
def train_endpoint():
    if train_status == "training":
        return jsonify({"error": "Already training"}), 400

    thread = threading.Thread(target=_train)
    thread.start()
    return jsonify({"result": "Training started"}), 202

@app.route("/predict", methods=["POST"])    # Recibe solo un dato
def predict_endpoint():
    data = request.json
    df = pd.DataFrame([data])

    # Se carga el modelo
    if not os.path.exists(MODEL_PATH):
        return jsonify({"error": "Model not found"}), 500
    model = joblib.load('model.pkl')

    prediction = model.predict(df)[0]  # TODO Transformar columnas del DataFrame como se hace en predict.py
                                    # TODO Puede ser en una funcion interna _predict()
                                # TODO O puede ser modificar el predict.py e importarlo (Más limpio)

    mapping = {0: 'bad', 1: 'neutral', 2: 'good'}
    label = mapping.get(prediction, "unknown")

    return jsonify({"prediction": int(prediction), "label": label})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)