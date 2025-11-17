
from .api_nagios import etat_hotes

class ModuleNagios:
    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password

    def obtenir_etat(self):
        return etat_hotes(self.url, self.user, self.password)
