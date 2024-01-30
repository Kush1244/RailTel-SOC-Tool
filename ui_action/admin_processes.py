from tools.osquery_reponse_generator import osquery_spawn_instance
import common_queries as cmq
import make_table
import threading


def threaded_admin_processes():
    solver = osquery_spawn_instance()
    col, row = solver.get_query_response(cmq.process_with_admin_token)
    make_table.make_table(col, row)


def admin_processes():
    threading.Thread(target=threaded_admin_processes).start()
    print("detached admin_processes")
