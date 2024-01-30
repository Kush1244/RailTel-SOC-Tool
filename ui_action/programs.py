from tools.osquery_reponse_generator import osquery_spawn_instance
import common_queries as cmq
import make_table
import threading


def threaded_programs():
    solver = osquery_spawn_instance()
    col, row = solver.get_query_response(cmq.all_programs)
    make_table.make_table(col, row)


def programs():
    threading.Thread(target=threaded_programs).start()
    print("detached programs")
