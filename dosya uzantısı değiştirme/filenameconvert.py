# -*- coding: utf-8 -*-
"""
PYTHON DOSYA UZANTISI DEĞİŞTİRME SCRİPTİ

"""

import os,sys

def donustur():
    
    klasor = "C:\\Users\\523372\\Desktop\\test"
    eski=input()
    yeni=input()
    for dosyadi in os.listdir(klasor):
        dosyaicinde = os.path.join(klasor, dosyadi)
        if not os.path.isfile(dosyaicinde): continue
        eskiuzanti = os.path.splitext(dosyadi)
        yeniuzanti = dosyaicinde.replace(str(eski), str(yeni))
        cikti = os.rename(dosyaicinde, yeniuzanti)
        
donustur()