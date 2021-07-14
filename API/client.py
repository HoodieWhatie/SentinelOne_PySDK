import requests
from config import Config


class Client:

    def __init__(self, api_token=Config.api_key, limit=10, count_only=False) -> None:
        self.api_token = api_token
        self.base_url = "https://usea1-swprd1.sentinelone.net/web/api/v2.1"
        self.api_key = api_token
        self.auth_header={'Authorization': f"ApiToken {self.api_key}"}
        self.limit = limit
        self.count_only = count_only


    def api_test(self):

        full_url = self.base_url + self.options["agents"]

        response = requests.get(full_url, headers=self.auth_header)
        if response.status_code == 200:
            return "Connection to the API was successfull"
        else:
            return f"Connection to the API has failed with code: {response.status_code}"
            

    def create_account(self):
        pass
        

    def get_accounts(self):
        full_url = self.base_url + "/accounts"
        return requests.get(full_url, headers=self.auth_header)


    def get_account_by_id(self, account_id):
        
        if int(account_id):
            full_url = self.base_url + f"accounts/{account_id}"
            return requests.get(full_url, headers=self.auth_header)
        else:
            TypeError(f"account_id must be of type int and not '{type(account_id)}'")


    def get_activities(self):
        full_url = self.base_url + "/activities"
        return requests.get(full_url, headers=self.auth_header)


    def get_uninstall_password(self, account_id):

        if int(account_id):
            full_url = self.base_url + f"/accounts/{account_id}/uninstall-password/view"
            return requests.get(full_url, headers=self.auth_header)
        else:
            TypeError(f"account_id must be of type int and not '{type(account_id)}'")


    def get_uninstall_password_metadata(self, account_id):

        if int(account_id):
            full_url = self.base_url + f"/accounts/{account_id}/uninstall-password/metadata"
            return requests.get(full_url, headers=self.auth_header)
        else:
            TypeError(f"account_id must be of type int and not '{type(account_id)}'")


# use 'loads(str({"data":{}, "filter":  {"ids": [""]}}).replace("'", "\""))' format for Post requests 