from mycroft import MycroftSkill, intent_file_handler


class LeerMensajesCampus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('campus.mensajes.leer.intent')
    def handle_campus_mensajes_leer(self, message):
        self.speak_dialog('campus.mensajes.leer')


def create_skill():
    return LeerMensajesCampus()

