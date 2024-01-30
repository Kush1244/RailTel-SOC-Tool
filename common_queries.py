suspicious_outbound_network = "select s.pid, p.name, local_address, remote_address, family, protocol, local_port, remote_port from process_open_sockets s join processes p on s.pid = p.pid where remote_port not in (80, 443) and family = 2;"
process_with_admin_token = (
    "select name,path from processes where secure_process = 0 and elevated_token = 1;"
)

dns_cache = "select * from dns_cache"

unsigned_processes = "select processes.name from processes join authenticode on processes.path = authenticode.path where authenticode.issuer_name = '';"

scheduled_task = "SELECT * FROM scheduled_tasks;"

all_programs = "SELECT name,version,publisher FROM programs;"

listening_programs = "select processes.name,listening_ports.port,listening_ports.protocol,listening_ports.address FROM processes LEFT JOIN listening_ports where processes.pid = listening_ports.pid;"

current_processes_and_their_hash = "select hash.sha256,processes.name from processes join hash on processes.path = hash.path where processes.path like 'C:\%' and processes.path != '';"

start_automatically_at_boot = (
    "SELECT * FROM services WHERE start_type='DEMAND_START' OR start_type='AUTO_START';"
)

processes_masquerading_as_legitimate_windows_processes = "SELECT * FROM processes WHERE LOWER(name)='conhost.exe' AND LOWER(path)!='c:\\windows\\system32\\conhost.exe' AND path!='';"

# t = "SELECT * FROM processes WHERE LOWER(name)='conhost.exe' AND LOWER(path)!='c:\\windows\\system32\\conhost.exe' AND path!='';"

automatically_executed_exe = "SELECT * FROM autoexec;"
