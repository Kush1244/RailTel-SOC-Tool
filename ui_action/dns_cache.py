import common_queries as cmq
from tools.osquery_reponse_generator import osquery_spawn_instance
import make_table
import threading


def threaded_get_dns_cache():
    solver = osquery_spawn_instance()
    col, row = solver.get_query_response(cmq.dns_cache)
    make_table.make_table(col, row)


def get_dns_cache():
    threading.Thread(target=threaded_get_dns_cache).start()
    print("detached get_dns_cache")
