from keras.models import Sequential
from keras.layers import Conv2D , MaxPooling2D , Flatten , Dense , Dropout

model=Sequential()
model.add(Conv2D(filters=16 , kernel_size=3 , padding="same" , activation="relu" , input_shape=(35,35,3)))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=32 , kernel_size=3 , padding="same" , activation="relu"))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=64 , kernel_size=3 , padding="same" , activation="relu"))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(.3))
model.add(Flatten())
model.add(Dense(units=500 , activation ="relu"))
model.add(Dropout(.3))
model.add(Dense(units=3 , activation="softmax"))


model.summary()