from ui_action import run_mrt
from ui_action import run_taskmanger
from ui_action import switch_stacked_widget
from ui_action import switch_stacked_widget
from ui_action import show_running_processes
from ui_action import virustotal_system_scan
from ui_action import dns_cache
from ui_action import admin_processes
from ui_action import programs
from ui_action import scheduled_task
from ui_action import listening_processes
from ui_action import start_at_boot_processes
from ui_action import pretending_processes
from ui_action import automatically_executed_exe


def attach(ui):
    ui.run_taskmanager_btn.clicked.connect(run_taskmanger.run_taskmanger)
    ui.run_mrt_btn.clicked.connect(run_mrt.run_mrt)
    ui.running_process_btn.clicked.connect(
        show_running_processes.show_running_processes
    )
    ui.admin_processes_btn.clicked.connect(admin_processes.admin_processes)
    ui.programs_btn.clicked.connect(programs.programs)
    ui.scheduled_task_btn.clicked.connect(scheduled_task.scheduled_task)
    ui.start_at_boot_processes.clicked.connect(
        start_at_boot_processes.processes_start_at_boot
    )
    # ui.pretending_to_be_legitimate_windows_processes.clicked.connect(
    #     pretending_processes.pretending_process
    # )
    ui.autoexec_btn.clicked.connect(automatically_executed_exe.autoexec)
    ui.scan_virustotal_btn.clicked.connect(
        virustotal_system_scan.virustotal_system_scan
    )
    ui.dns_cache_btn.clicked.connect(dns_cache.get_dns_cache)
    ui.listening_processes_btn.clicked.connect(listening_processes.listening_processes)
    """ Buttons To Switch Between Stacked Widget """
    ui.virustotal_btn.clicked.connect(lambda: switch_stacked_widget.show_virustotal(ui))
    ui.system_monitoring_btn.clicked.connect(
        lambda: switch_stacked_widget.show_system_administration(ui)
    )

    ui.networking_btn.clicked.connect(lambda: switch_stacked_widget.show_networking(ui))
