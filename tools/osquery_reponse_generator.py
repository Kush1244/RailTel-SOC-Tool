import osquery


class osquery_spawn_instance(osquery.SpawnInstance):
    def __init__(self):
        super().__init__()
        print("osquery client generated")
        self.open()

    def get_query_response(self, t_query: str) -> list:
        clmn_name, row_data = None, None
        resp = self.client.query(t_query).response

        if resp == []:
            return None, None

        clmn_name = [i for i in resp[0]]
        row_data = [[i[j] for j in clmn_name] for i in resp]
        return clmn_name, row_data
