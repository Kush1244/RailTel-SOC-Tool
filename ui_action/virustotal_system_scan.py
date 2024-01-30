from tools.virustotal import virustotal_threaded
import make_table
import threading


def threading_virustotal_system_scan():
    vtotal = virustotal_threaded()
    print("reached")
    make_table.make_table(["processes", "malicious", "total"], vtotal.response_received)


def virustotal_system_scan():
    threading.Thread(target=threading_virustotal_system_scan).start()
    print("detached virustotal_system_scan")
