from tools.osquery_reponse_generator import osquery_spawn_instance
import threading
import make_table
import common_queries as cmq


def threading_listening_processes():
    solver = osquery_spawn_instance()
    col, row = solver.get_query_response(cmq.listening_programs)
    make_table.make_table(col, row)


def listening_processes():
    threading.Thread(target=threading_listening_processes).start()
    print("detached listening_processes")
