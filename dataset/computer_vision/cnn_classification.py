
import numpy as np


import tensorflow as tf
from keras import layers, models

if __name__ == "__main__":
    
    classifier = models.Sequential()

    
    classifier.add(
        layers.Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation="relu")
    )

   
    classifier.add(layers.MaxPooling2D(pool_size=(2, 2)))

    
    classifier.add(layers.Conv2D(32, (3, 3), activation="relu"))
    classifier.add(layers.MaxPooling2D(pool_size=(2, 2)))

    
    classifier.add(layers.Flatten())

    
    classifier.add(layers.Dense(units=128, activation="relu"))
    classifier.add(layers.Dense(units=1, activation="sigmoid"))

    
    classifier.compile(
        optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
    )

    

    train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1.0 / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True
    )

    test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0 / 255)

    training_set = train_datagen.flow_from_directory(
        "dataset/training_set", target_size=(64, 64), batch_size=32, class_mode="binary"
    )

    test_set = test_datagen.flow_from_directory(
        "dataset/test_set", target_size=(64, 64), batch_size=32, class_mode="binary"
    )

    classifier.fit_generator(
        training_set, steps_per_epoch=5, epochs=30, validation_data=test_set
    )

    classifier.save("cnn.h5")

    

    test_image = tf.keras.preprocessing.image.load_img(
        "dataset/single_prediction/image.png", target_size=(64, 64)
    )
    test_image = tf.keras.preprocessing.image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)
    
    if result[0][0] == 0:
        prediction = "Normal"
    if result[0][0] == 1:
        prediction = "Abnormality detected"
