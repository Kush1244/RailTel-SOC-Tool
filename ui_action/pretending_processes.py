import common_queries as cmq
from tools.osquery_reponse_generator import osquery_spawn_instance
import make_table
import threading
import ui_action.show_info


def threading_pretending_process():
    solver = osquery_spawn_instance()
    col, row = solver.get_query_response(
        cmq.processes_masquerading_as_legitimate_windows_processes
    )
    if row == None or col == None:
        ui_action.show_info.show_warning(message="empty response", title="osquery")
        return
    make_table.make_table(col, row)


def pretending_process():
    threading.Thread(target=threading_pretending_process).start()
    print("detached pretending_processes")
