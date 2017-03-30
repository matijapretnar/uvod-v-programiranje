import os

def relevantne_datoteke(imenik, koncnice={'.mp4', '.mkv', '.avi'}):
    for datoteka in os.listdir(imenik):
        _, koncnica = os.path.splitext(datoteka)
        if koncnica in koncnice:
            print(datoteka)
