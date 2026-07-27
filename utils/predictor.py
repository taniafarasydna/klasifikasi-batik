# ==========================================================
# PREDICTOR
# ==========================================================

import numpy as np

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input as preprocess_v2
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input as preprocess_v3

from PIL import Image


# ==========================================================
# IMAGE SIZE
# ==========================================================

IMG_SIZE = (224, 224)


# ==========================================================
# PREPROCESS IMAGE
# ==========================================================

def preprocess_image(image):

    image = image.convert("RGB")

    image = image.resize(IMG_SIZE)

    image_array = np.array(image)

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    return image_array


# ==========================================================
# PREDICT IMAGE
# ==========================================================

def predict_image(image,
                  model_v2,
                  model_v3):

    image_array = preprocess_image(image)

    img_v2 = preprocess_v2(image_array.copy())

    img_v3 = preprocess_v3(image_array.copy())

    pred_v2 = model_v2.predict(
        img_v2,
        verbose=0
    )[0]

    pred_v3 = model_v3.predict(
        img_v3,
        verbose=0
    )[0]

    return pred_v2, pred_v3


# ==========================================================
# GET TOP 3
# ==========================================================

def get_top3(prediction,
             class_names):

    idx = np.argsort(
        prediction
    )[::-1][:3]

    result = []

    for i in idx:

        result.append({

            "label": class_names[i],

            "confidence": float(
                prediction[i] * 100
            )

        })

    return result


# ==========================================================
# GET RESULT
# ==========================================================

def get_prediction_result(prediction,
                          class_names):

    idx = np.argmax(prediction)

    return {

        "label":
            class_names[idx],

        "confidence":
            float(prediction[idx] * 100),

        "top3":
            get_top3(
                prediction,
                class_names
            )

    }


# ==========================================================
# CONFIDENCE LEVEL
# ==========================================================

def confidence_level(confidence):

    if confidence >= 95:

        return (

            "🟢 Sangat Tinggi",

            "success"

        )

    elif confidence >= 80:

        return (

            "🟡 Tinggi",

            "info"

        )

    elif confidence >= 60:

        return (

            "🟠 Sedang",

            "warning"

        )

    else:

        return (

            "🔴 Rendah",

            "error"

        )


# ==========================================================
# SAME PREDICTION?
# ==========================================================

def same_prediction(result_v2,
                    result_v3):

    return (

        result_v2["label"]

        ==

        result_v3["label"]

    )