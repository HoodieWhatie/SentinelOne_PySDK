import requests
from json import loads

url = "https://usea1-swprd1.sentinelone.net/web/api/v2.1/agents/actions/decommission"
api_key = "BR7x96ksc25GhbjkVyoN3eBq0zQujV8vOqM8xWcbTZFyNyULXjB9AZZHtIOgpmvJqYQTD8LqFrfwCiWC"
auth_header={'Authorization': f"ApiToken {api_key}"}
command = loads(str({"data":{}, "filter":  {"ids": ["1195609117427653132"]}}).replace("'", "\""))

response = requests.post(url, headers=auth_header, json=command).json()

print()