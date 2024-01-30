import json
import requests
import threading
from tools.osquery_reponse_generator import osquery_spawn_instance
import common_queries as cmq


class virustotal_threaded:
    def __init__(self, hash: list = None) -> None:
        solver = osquery_spawn_instance()
        self.clmn_name, self.row_data = solver.get_query_response(
            cmq.current_processes_and_their_hash
        )
        self.headers = {
            "content-type": "application/json",
            #'Authorization': 'Bearer{0}'.format(api_token)
            "X-APIKey": "84206c5ecd36cfac5c3a34234sdfskdfhj232d113c366a9185a07f429e526eb0e08e92c61a"  
        }
        self.hash = self.row_data
        self.response_received = list()
        self.allThreadsGenerated = list()
        self.threaded_response()
        self.joinAllThreads()

    def get_virus_total_score(self, processes: str, hash: str):
        if hash == "" or processes == "":
            return
        response = requests.get(
            f"https://www.virustotal.com/api/v3/files/{hash}", headers=self.headers
        )
        data = json.loads(response.content)
        # print(data)
        malicious = data["data"]["attributes"]["last_analysis_stats"]["malicious"]
        undetected = data["data"]["attributes"]["last_analysis_stats"]["undetected"]
        # x = [processes, malicious, undetected + malicious]
        # print("x = -> ", x)
        self.response_received.append([processes, malicious, undetected + malicious])
        print("got response for {}".format(processes))

    def threaded_response(self):
        j = 0
        for i in self.hash:
            t = threading.Thread(target=self.get_virus_total_score, args=(i[0], i[1]))
            self.allThreadsGenerated.append(t)
            t.start()
            print("detached")
            j += 1

    def joinAllThreads(self):
        print("joining all threads")
        for i in self.allThreadsGenerated:
            i.join()
