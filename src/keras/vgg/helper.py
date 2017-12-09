from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense

target_size = 224, 224
batch_size = 16
num_classes = 10 # the same for all cases of training, testing and predicting
class_labels = ['safe_driving', 'texting_right', 'talking_on_phone_right', 'texting_left', 'talking_on_phone_left',
                'operating_radio', 'drinking', 'reaching_behind', 'doing_hair_makeup', 'talking_to_passanger']

def create_top_model(activation_func, input_shape):
    
    model = Sequential()
    
    model.add(Flatten(input_shape=input_shape))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation=activation_func))
    
    return model