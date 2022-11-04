from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

model = keras.Sequential(
    [
        layers.Input(shape=(1,1)),
        layers.Conv1D(
            filters=32, kernel_size=7, padding="same", strides=2, activation="relu"
        ),
        layers.Dropout(rate=0.2),
        layers.Conv1D(
            filters=16, kernel_size=7, padding="same", strides=2, activation="relu"
        ),
        layers.Conv1DTranspose(
            filters=16, kernel_size=7, padding="same", strides=2, activation="relu"
        ),
        layers.Dropout(rate=0.2),
        layers.Conv1DTranspose(
            filters=32, kernel_size=7, padding="same", strides=2, activation="relu"
        ),
        layers.Conv1DTranspose(filters=1, kernel_size=7, padding="same"),
    ]
)
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss="mse")
model.load_weights("./tf_model_weights/model.ckpt")

scaling_std = 121303.322537
scaling_mean = 514973.708333

def scale(values: np.array, scale_std:float=scaling_std, scale_mean:float = scaling_mean):
    return (values - np.array([scale_mean])) / np.array([scale_std])

def run_inference(values):
    scaled = scale(np.array([[values]]))
    
    output = model.predict(scaled)
    
    mae_loss = np.mean(np.abs(output - scaled), axis=1)
    mae_loss = mae_loss.reshape((-1))

    reconstruction_error_thresh = .2

    if mae_loss >= reconstruction_error_thresh:
        is_anomaly = True
    else:
        is_anomaly = False

    return {"anomalous":is_anomaly}

def rescale(values, scale_std=scaling_std, scale_mean=scaling_mean):
    rescaled_vals = np.copy(values)
    rescaled_vals[:,0] = np.add(np.multiply(values[:,0], np.array([scale_std])), np.array([scale_mean]))
    return rescaled_vals