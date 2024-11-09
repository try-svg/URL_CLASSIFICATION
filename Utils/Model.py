import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, Embedding, GRU, Input, concatenate
from tensorflow.keras.models import Model

def create_model(Sequence_length,max_tokens, input_shape_numeric ):
    # define nlp model
    text_input = Input(shape=(Sequence_length,),)
    x = Embedding(max_tokens, 128, input_length=Sequence_length)(text_input)
    x = GRU(128, dropout=0.002, recurrent_dropout=0.002,return_sequences=True)(x)
    x = Dropout(0.002)(x)
    x = GRU(128, dropout=0.002, recurrent_dropout=0.002,return_sequences=True)(x)
    x = Dropout(0.002)(x)
    x = GRU(128, dropout=0.002, recurrent_dropout=0.002)(x)
    x = Dropout(0.002)(x)
    text_model = Model(inputs=text_input, outputs=x)

    # define numeric model
    numeric_input = Input(shape=(input_shape_numeric,),)
    y = Dense(128, activation='relu')(numeric_input)
    y = Dropout(0.002)(y)
    y = Dense(256, activation='relu')(y)
    y = Dropout(0.002)(y)
    y = Dense(512, activation='relu')(y)
    y = Dropout(0.002)(y)
    y = Dense(512, activation='relu')(y)
    y = Dropout(0.002)(y)
    y = Dense(256, activation='relu')(y)
    y = Dropout(0.002)(y)
    y = Dense(128, activation='relu')(y)
    y = Dropout(0.002)(y)
    numeric_model = Model(inputs=numeric_input, outputs=y)

    # concatenate the two models
    combined_input = concatenate([text_model.output, numeric_model.output])
    z = Dense(64, activation='relu')(combined_input)
    z = Dropout(0.002)(z)
    output = Dense(1, activation='sigmoid')(z)

    return Model(inputs=[text_model.input, numeric_model.input], outputs=output)
