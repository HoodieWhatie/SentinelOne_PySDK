from config import Config
from json import loads

class Call:

    url = "https://usea1-swprd1.sentinelone.net/web/api/v2.1"
    options = {"agents": "/agents","decommission": "/agents/actions/decommission"}
    api_key = Config.api_key
    auth_header = {'Authorization': f"ApiToken {api_key}"}

    def PushCall(ids):

        if type(ids) == list:
            return loads(str({"data":{}, "filter":  {"ids": ids}}).replace("'", "\""))
        else: 
            raise TypeError(f"PushCall() takes one argument 'ids' that should be of type 'list' instead of '{type(ids)}'")