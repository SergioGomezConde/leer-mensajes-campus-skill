import json
import os

from mycroft import MycroftSkill, intent_file_handler

# Fichero JSON donde almacenar la informacion
ficheroJSON = "/home/serggom/scraping/datos.json"

class LeerMensajesCampus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('campus.mensajes.leer.intent')
    def handle_campus_mensajes_leer(self, message):

        # Lectura de la informacion del fichero JSON
        if os.path.exists(ficheroJSON):
            # Lectura de la informacion del fichero JSON
            with open(ficheroJSON) as ficheroMensajes:
                data = json.load(ficheroMensajes)

                numero_mensajes = data['numero_mensajes'][0]['total_privados']

                if int(numero_mensajes) > 0:
                    self.speak("Tienes " + numero_mensajes + " mensajes")

                    for mensaje in data['mensajes']:
                        self.speak("Mensaje de " + mensaje['autor'] + " el " + mensaje['fecha'] + ":")
                        self.speak(mensaje['contenido'])

                else:
                    self.speak("No tienes mensajes que leer")

            ficheroMensajes.close()

        else:
            self.speak("Lo siento, no dispongo de esa información")

def create_skill():
    return LeerMensajesCampus()

