import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    zoom_range=0.1,
    brightness_range=[0.7, 1.3]
)

val_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train = train_datagen.flow_from_directory(
    "dataset",
    target_size=(64, 64),
    batch_size=32,
    class_mode="categorical",
    subset="training"
)

val = val_datagen.flow_from_directory(
    "dataset",
    target_size=(64, 64),
    batch_size=32,
    class_mode="categorical",
    subset="validation"
)

print("Class Indices:", train.class_indices)

model = Sequential()

model.add(Conv2D(32, (3,3), activation="relu", input_shape=(64,64,3)))
model.add(BatchNormalization())
model.add(MaxPooling2D())

model.add(Conv2D(64, (3,3), activation="relu"))
model.add(BatchNormalization())
model.add(MaxPooling2D())

model.add(Conv2D(128, (3,3), activation="relu"))
model.add(BatchNormalization())
model.add(MaxPooling2D())

model.add(Flatten())
model.add(Dense(256, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(3, activation="softmax"))  # 3 classes

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

callbacks = [
    EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True),
    ModelCheckpoint('model.h5', save_best_only=True, monitor='val_accuracy')
]

model.fit(
    train,
    validation_data=val,
    epochs=20,
    callbacks=callbacks
)

print("✅ Model saved!")
print("Class mapping:", train.class_indices)