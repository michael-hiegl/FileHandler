#Programm erstellt alle 10 Sekunden Kopien von allen Dateien im Ordner "Test1" und fügt sie in Ordner "Test2" ein

#importieren der Standartlibraries für die benötigten Funktionen
import os as os
import time as time
import shutil as shutil

#Öffnen der Textdateien, in denen die Ordnerpfade gespeichert sind
s = open("source.txt", "r", encoding="utf-8")
d = open("destination.txt", "r", encoding="utf-8")

#Lest die Inhalte und speichert sie als String in Variablen
source_folder = s.read()
destination_folder = d.read()

#Schließen der TXT-Dateien
s.close()
d.close()

while(True): #Das Argument True führt zu einer endlosen Wiederholung der while-Schleife
    #listdir() erstellt eine Liste von allen Elementen in "Test1"
    #Diese Liste wird in der for-Schleife abgearbeitet und Variablen "file_name" daraus erzeugt
    for file_name_d in os.listdir(destination_folder):
        source_d = destination_folder + file_name_d
        if os.path.isfile(source_d): #path.isfile() übergibt den Wert True, wenn "source" ein real existierender Pfad ist
            os.remove(source_d) #wird sie gelöscht
    for file_name_s in os.listdir(source_folder):
        #Durch das Zusammenfügen von Ordnerpfad und Dateiname wird der Dateipfad erzeugt und in Variablen "source" und "destination" gespeichert
        source_s = source_folder + file_name_s
        destination = destination_folder + file_name_s
        if os.path.isfile(source_s): #path.isfile() übergibt den Wert True, wenn "source" ein real existierender Pfad ist
            shutil.copy(source_s, destination) #Kopieren der Dateien von "source" nach "copy" mittels der Dateipfade
    time.sleep(10) #Programm wird für n Sekunden gestoppt bevor die while-Schleife erneut ausgeführt wird