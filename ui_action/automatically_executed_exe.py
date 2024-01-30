import common_queries as cmq
from tools.osquery_reponse_generator import osquery_spawn_instance
import make_table
import threading
import ui_action.show_info


def threaded_autoexec():
    solver = osquery_spawn_instance()
    col, row = solver.get_query_response(cmq.automatically_executed_exe)
    if col is None or col is None:
        ui_action.show_info.show_warning(message="empty response", title="osquery")
        return
    make_table.make_table(col, row)


def autoexec():
    threading.Thread(target=threaded_autoexec).start()
    print("detached autoexec")
