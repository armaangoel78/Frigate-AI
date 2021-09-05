from frigate_ai.wrapper.wrapper import frigate_model
from tensorflow.keras import models, preprocessing
import numpy as np
import json

@frigate_model("img.jpeg", "output.json")
def main():
    img = preprocessing.image.load_img('img.jpeg')
    img = np.array(img)[:, :, 0].reshape((1, 28, 28))
    model = models.load_model('saved_model/my_model')
    predictions = model.predict(img)
    prediction = int(np.argmax(predictions))
    with open('output.json', 'w') as f:
        json.dump({
            'prediction': prediction
        }, f)


if __name__ == '__main__':
  main('frigate-ship', 'img_105.jpeg')
