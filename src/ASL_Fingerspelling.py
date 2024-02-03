#!pip install tflite-runtime
import tflite_runtime.interpreter as tflite
import json
import pandas as pd
import numpy as np
import pyautogui
PATH=r"C:\Users\liamb\Downloads\weights\cfg_2\fold-1"
class ASL_Model:
    REQUIRED_SIGNATURE = "serving_default"
    REQUIRED_OUTPUT = "outputs"
    def __init__(self):
        self.selected_columns=json.load(open(PATH+"inference_args.json"))['selected_columns']
        interpreter = tflite.Interpreter(PATH+"model.tflite")
        character_map = {"0": 15, "1": 16, "2": 17, "3": 18, "4": 19, "5": 20, "6": 21, "7": 22, "8": 23, "9": 24, " ": 0, "!": 1, "#": 2, "$": 3, "%": 4, "&": 5, "'": 6, "(": 7, ")": 8, "*": 9, "+": 10, ",": 11, "-": 12, ".": 13, "/": 14, ":": 25, ";": 26, "=": 27, "?": 28, "@": 29, "[": 30, "_": 31, "a": 32, "b": 33, "c": 34, "d": 35, "e": 36, "f": 37, "g": 38, "h": 39, "i": 40, "j": 41, "k": 42, "l": 43, "m": 44, "n": 45, "o": 46, "p": 47, "q": 48, "r": 49, "s": 50, "t": 51, "u": 52, "v": 53, "w": 54, "x": 55, "y": 56, "z": 57, "~": 58}       
        self.rev_character_map = {j:i for i,j in character_map.items()}
        self.prediction_fn = interpreter.get_signature_runner("serving_default")
    def predict(self,landmarks):#takes input from MediaPipe holistic
        landmarks = landmarks[self.selected_columns]
        output = self.prediction_fn(inputs=landmarks)
        prediction_str = "".join([self.rev_character_map.get(s, "") for s in np.argmax(output[self.REQUIRED_OUTPUT], axis=1)])
        if prediction_str == '2 a-e -aroe':#then confidence is too low or there are < 15 frames ideally this would be replaced but ...
            return None#Failure
        return prediction_str