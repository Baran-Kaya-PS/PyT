import os
from datetime import datetime

ui = input("Quel est le nom de fichier ")
tfn = f"{ui}.txt"
def overwrite(log,tf):
    with open(tf,'w',encoding="utf-8") as tf:
        tf.write(f"{log}\n")
        print("message ajouté au journal")

def addlog(log,tf):
    with open(tf,'a',encoding="utf-8") as tf:
        tf.write(f"{log}\n")
        print("message ajouté au journal")

def create_file(log,path):
    with open(path,'w',encoding="utf_8") as tf:
        tf.write(f"{log}\n")
        print("fichier créer et message ajouté")

if os.path.exists(tfn):
    print("Souhaitez vous reécrire le fichier ou ajouter des éléments : overwrite/append")
    mode = input().strip().lower()
    while mode not in ["append","overwrite"]:
        mode = input().strip().lower()
    if mode == "append":
        log = "{:%y-%m-%d %H:%M:%S} {}".format(datetime.today(), input("Ecrivez votre message "))
        addlog(log,tfn)
    if mode == "overwrite":
        log = "{:%y-%m-%d %H:%M:%S} {}".format(datetime.today(), input("Ecrivez votre message "))
        overwrite(log,tfn)
else:
    log = "{:%y-%m-%d %H:%M:%S} {}".format(datetime.today(), input("Ecrivez votre message "))
    create_file(log,tfn)