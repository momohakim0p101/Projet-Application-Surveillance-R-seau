
import requests

def etat_hotes(nagios_url, user, password):
    url = f"{nagios_url}/cgi-bin/statusjson.cgi?query=hostlist"
    try:
        r = requests.get(url, auth=(user, password), verify=False)
        return r.json()
    except Exception as e:
        print("Erreur Nagios :", e)
        return None
