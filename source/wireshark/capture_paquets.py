
import pyshark

def capturer(interface="eth0", duree=3):
    try:
        capture = pyshark.LiveCapture(interface=interface)
        capture.sniff(timeout=duree)
        return capture
    except Exception as e:
        print("Erreur Wireshark :", e)
        return []
