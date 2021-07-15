import requests
from requests.api import request
from config import Config

# TEST after Redirection
class Client:

    # Establishes key components
    def __init__(self, api_token=Config.api_key, limit=10, count_only=False) -> None:
        self.api_token = api_token
        self.base_url = "https://usea1-swprd1.sentinelone.net/web/api/v2.1"
        self.api_key = api_token
        self.auth_header={'Authorization': f"ApiToken {self.api_key}"}
        self.limit = limit
        self.count_only = count_only


    # Sends a "Get Agents" request and confirms a 200 status code is returned
    def api_test(self):
        full_url = self.base_url + self.options["agents"]

        response = requests.get(full_url, headers=self.auth_header)
        if response.status_code == 200:
            return "Connection to the API was successfull"
        else:
            return f"Connection to the API has failed with code: {response.status_code}"
    

    # Expire an Account immediately
    def expire_an_account(self, account_id):
        if int(account_id):
            full_url = self.base_url + f"/web/api/v2.1/accounts/{account_id}/expire-now"
            return requests.post(full_url, headers=self.auth_header)


    # Get the Accounts, and their data, that match the filter.
    def get_accounts(self):
        full_url = self.base_url + "/accounts"
        return requests.get(full_url, headers=self.auth_header)

    # Get Account data from a given Account ID. 
    def get_account_by_id(self, account_id):
        if int(account_id):
            full_url = self.base_url + f"accounts/{account_id}"
            return requests.get(full_url, headers=self.auth_header)
        else:
            TypeError(f"account_id must be of type int and not '{type(account_id)}'")

    # Get the activities, and their data, that match the filters. 
    def get_activities(self):
        full_url = self.base_url + "/activities"
        return requests.get(full_url, headers=self.auth_header)

    # Get a list of activity types 
    def get_activity_types(self):
        full_url = self.base_url + "/activities/types"
        return requests.get(full_url, headers=self.auth_header) 


    # Get the Syslog message that corresponds to the last activity that matches the filter.
    def get_last_syslog_activity(self):
        full_url = self.base_url + "/last-activity-as-syslog"
        return requests.get(full_url, headers=self.auth_header)

    
    # Get the uninstall password to uninstall several Agents of one Account with one command.
    def get_uninstall_password(self, account_id):
        if int(account_id):
            full_url = self.base_url + f"/accounts/{account_id}/uninstall-password/view"
            return requests.get(full_url, headers=self.auth_header)
        else:
            TypeError(f"account_id must be of type int and not '{type(account_id)}'")


    # Get the uninstall password metadata, such as which user created and revoked it and when.
    def get_uninstall_password_metadata(self, account_id):
        if int(account_id):
            full_url = self.base_url + f"/accounts/{account_id}/uninstall-password/metadata"
            return requests.get(full_url, headers=self.auth_header)
        else:
            TypeError(f"account_id must be of type int and not '{type(account_id)}'")
