import common_queries as cmq
from tools.osquery_reponse_generator import osquery_spawn_instance
import make_table
import threading


def threaded_scheduled_task():
    solver = osquery_spawn_instance()
    col, row = solver.get_query_response(cmq.scheduled_task)
    make_table.make_table(col, row)


def scheduled_task():
    threading.Thread(target=threaded_scheduled_task).start()
    print("detached scheduled_task")
