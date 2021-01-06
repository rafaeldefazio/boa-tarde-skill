from mycroft import MycroftSkill, intent_file_handler


class BoaTarde(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tarde.boa.intent')
    def handle_tarde_boa(self, message):
        self.speak_dialog('tarde.boa')


def create_skill():
    return BoaTarde()

