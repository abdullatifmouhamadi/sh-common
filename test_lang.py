#!/usr/bin/env python



print("salut")


#from pygoogletranslation import Translator
from googletrans import Translator



translator = Translator()
t = translator.translate("Salut comment tu vas. Bien et toi.", src='fr', dest='en')

print(t.text)














