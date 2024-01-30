import subprocess
import threading


def threaded_run_taskmanger():
    subprocess.run("taskmgr")


def run_taskmanger():
    threading.Thread(target=threaded_run_taskmanger).start()
    print("detached run_taskmanger")
