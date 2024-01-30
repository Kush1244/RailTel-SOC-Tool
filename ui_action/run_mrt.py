import subprocess
import threading


def threaded_run_mrt():
    subprocess.run("mrt")


def run_mrt():
    threading.Thread(target=threaded_run_mrt).start()
    print("detached mrt")
