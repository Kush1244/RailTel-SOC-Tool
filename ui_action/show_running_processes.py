from tools import osquery_reponse_generator
import make_table
import threading


def threaded_show_running_processes():
    query = "SELECT name,path FROM processes;"
    solver = osquery_reponse_generator.osquery_spawn_instance()
    col, row = solver.get_query_response(query)
    make_table.make_table(col, row)


def show_running_processes():
    threading.Thread(target=threaded_show_running_processes).start()
    print("detached show_running_processes")
