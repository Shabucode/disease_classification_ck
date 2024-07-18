#create the components
#import necessary libraries
import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from src.cnnClassifier.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    
    #load VGG16 model from keras applications with parameters defined in configuration
    #and save base model in artifacts directory
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size, 
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
            )
    
        self.save_model(path=self.config.base_model_path, model=self.model)

    
    #create another method for saving training the pretrained model
    @staticmethod
    def prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till >0):
            for layer in model.layers[: freeze_till]:
                model.trainable = False
        
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation = "softmax"
        )(flatten_in)

        #defining full model
        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        #compiling model with optimizer/loss/metrics
        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
            )
        
        #model summary statistics
        full_model.summary()
        return full_model
    

    #update base model
    def update_base_model(self):
        self.full_model = self.prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        #save model
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)


    #save model
    @staticmethod
    def save_model(path: Path, model:tf.keras.Model):
        model.save(path)   
            