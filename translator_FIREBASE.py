import firebase_admin
from firebase import firebase
from firebase_admin import db
import speech_recognition as sr
import os
from googletrans import Translator
from gtts import gTTS
from PIL import Image
import cv2
import pytesseract

firebase = firebase.FirebaseApplication("https://janaparvani-default-rtdb.firebaseio.com/",None)
# Translation Part
translator = Translator()

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
mic = sr.Microphone()
while(True):
    finaldata = firebase.get('Conversion', '')
    item = finaldata.items()
    for key, val in finaldata.items():
        flag = (val["flag"])
        text = (val["text"])
        flag1 = (val["flag1"])
        to_lang = (val["to_lang"])
        rid = (val["Reciever_ID"])
        sid = (val["Sender_ID"])
        code1 = (val["Chat-Code"])

        if (flag ==0):
            def output_type(x):
                    print(x)
            def translation_lang(text, to_lang):
                translation = translator.translate(text, dest=to_lang)
                x = translation.text
                data={'trs_text': x,'text' :text}
                firebase_upload(data,x,text)
                return x
            def firebase_upload(data,x,text):
                firebase.put('/Conversion/' + key ,'trans_text',x)
                firebase.put('/Received/' + code1, "Sid", sid)
                firebase.put('/Received/' + code1, 'trans_text', x)
                firebase.put('/Received/' + code1, "Rid", rid)
                firebase.put('/Received/' + code1, "Chat-Code", code1)
                firebase.put('/Received/' + code1, "istranslated", '0')
            translation_lang(text, to_lang)
            flag = 1
            firebase.put('/Conversion/' + key , "flag", flag)



















