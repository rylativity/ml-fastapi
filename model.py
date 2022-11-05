import tensorflow as tf
import numpy as np
import PIL.Image

from tensorflow.keras.applications.mobilenet_v3 import decode_predictions

INPUT_SHAPE = (224,224, 3)

model = tf.keras.applications.MobileNetV3Small(
    input_shape = INPUT_SHAPE,
    weights="imagenet"
)

def classify_image(image:bytes):

    img = PIL.Image.open(image)

    img_array = np.array(img)

    img_batch = np.expand_dims(img_array, 0)

    img_batch = tf.image.resize_with_pad(img_batch, *INPUT_SHAPE[:2])

    #preprocessed_img_array = preprocess_image(img_array)
    
    output = model.predict(img_batch)

    prediction_batch = decode_predictions(output)

    response = {pred[1]:float(pred[2]) for pred in prediction_batch[0]}
    return response
