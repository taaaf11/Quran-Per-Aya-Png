"""
Author: Muhammad Altaaf
Contact Email: taafuuu@gmail.com
Description: A simple Quran per Ayah png generator. This script uses images from everyayah.com   ,   though it has no affiliations with the mentioned site.
"""

import os
import urllib.request

suras = [sura for sura in range(1,115)]
aya_s = ['7', '286', '200', '176', '120', '165', '206', '75', '129', '109', '123', '111', '43', '52', '99', '128', '111', '110', '98', '135', '112', '78', '118', '64', '77', '227', '93', '88', '69', '60', '34', '30', '73', '54', '45', '83', '182', '88', '75', '85', '54', '53', '89', '59', '37', '35', '38', '29', '18', '45', '60', '49', '62', '55', '78', '96', '29', '22', '24', '13', '14', '11', '11', '18', '12', '12', '30', '52', '52', '44', '28', '28', '20', '56', '40', '31', '50', '40', '46', '42', '29', '19', '36', '25', '22', '17', '19', '26', '30', '20', '15', '21', '11', '8', '8', '19', '5', '8', '8', '11', '11', '8', '3', '9', '5', '4', '7', '3', '6', '3', '5', '4', '5', '6']

sura_aya = {}

# Create dir with name so as to put images in that directory
os.mkdir("Aya Images")
os.chdir("Aya Images")

for i in range(len(suras)):
    sura_aya.update({str(suras[i]) : str(aya_s[i])})
for sura, aya in sura_aya.items():
    for i in range(1, int(aya)+1):
        r = urllib.request.urlopen(f'http://www.everyayah.com/data/images_png/{sura}_{i}.png')
        open(f'{sura} {i}.png', 'wb').write(r.read())
