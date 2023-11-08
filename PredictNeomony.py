from Model import Model
import numpy as np

# Metodo para precedir la neomonia en la radiografia
def predict(array):
    model_class = Model()
    #   1. call function to pre-process image: it returns image in batch format
    batch_array_img = model_class.preprocess(array)
    #   2. call function to load model and predict: it returns predicted class and probability
    model = model_class.model_fun()
    # model_cnn = tf.keras.models.load_model('conv_MLP_84.h5')
    prediction = np.argmax(model.predict(batch_array_img))
    proba = np.max(model.predict(batch_array_img)) * 100
    label = ""
    if prediction == 0:
        label = "bacteriana"
    if prediction == 1:
        label = "normal"
    if prediction == 2:
        label = "viral"
        #   3. call function to generate Grad-CAM: it returns an image with a superimposed heatmap
    heatmap = model_class.grad_cam(array)
    # Devuelve la etiqueta de la clase, la probabilidad y el mapa de calor
    return (label, proba, heatmap)