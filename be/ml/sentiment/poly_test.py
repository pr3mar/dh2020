# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 14:58:55 2020

@author: Bosec
"""

#Import the modules
import text2emotion as te

text = "Brazil, victim of a criminal oil spill.  The criminal Venezuela government, promoted this terrorist act against Brazil. Petrobras has analyzed 23 times the oil spilled on our northeast coast, and proved to be Venezuelan oil. Silence of international press...support the act"



print(te.get_emotion(text))
#Output
{'Angry': 0.0, 'Fear': 0.0, 'Happy': 0.8, 'Sad': 0.0, 'Surprise': 0.2}