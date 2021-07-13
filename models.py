from marshmallow import *

class SKU:
    
    def __init__(self, total_licenses, type, unlimited):
        self.total_licenses = total_licenses
        self.type = type
        self.unlimited = unlimited

class Policy:

    def __init__(self, agent_notification, agent_logging_on):
        pass

class Account:

    def __init__(self, name, external_id, inherits, expiration, 
                    account_type, skus, policy, unlimited_expiration):
        self.name = name
        self.external_id = external_id
        self.inherits = inherits
        self.expiration = expiration
        self.account_type = account_type
        self.skus = skus
        self.policy = policy
        self.unlimited_expiration = unlimited_expiration