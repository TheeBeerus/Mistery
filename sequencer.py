import keras
import numpy as np


class Sequencer(keras.utils.Sequence):
    def __init__(self, x_set, y_set, nb_classes, batch_size, is_categorical):
        self.x, self.y = x_set, y_set
        self.nb_classes = nb_classes
        self.batch_size = batch_size
        self.is_categorical = is_categorical

    def __len__(self) -> int:
        return int(np.ceil(len(self.x) / float(self.batch_size)))

    def __getitem__(self, idx) -> tuple:
        batch_x = self.x[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_y = self.y[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_y[batch_y < 0] = 0
        batch_y[batch_y < 0.5] = 0
        batch_y[batch_y >= 0.5] = 1
        if self.is_categorical:
            batch_y = keras.utils.to_categorical(batch_y, self.nb_classes)
        return batch_x, batch_y


def element(array, is_input):
    if array.size > 1000:
        array_size = 1000
    else:
        array_size = array.size
    elements = []
    for i in range(array_size):
        if array[i] not in elements:
            if is_input:
                elements.append(array[i])
            else:
                elements.append(array[i][0])
    return elements
