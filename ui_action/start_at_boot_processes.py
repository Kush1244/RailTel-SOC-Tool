import threading
from tools.osquery_reponse_generator import osquery_spawn_instance
import make_table
import common_queries as cmq
from ui_action import show_info


def threading_processes_start_at_boot():
    solver = osquery_spawn_instance()
    col, row = solver.get_query_response(cmq.start_automatically_at_boot)
    if col == None or row == None:
        threading.Thread(
            target=show_info.show_warning,
            args=["osquery generates empty response", "Empty Response"],
        )
        print("detached show_warning")

    make_table.make_table(col, row)


def processes_start_at_boot():
    threading.Thread(target=threading_processes_start_at_boot).start()
    print("detached processes_start_at_boot")