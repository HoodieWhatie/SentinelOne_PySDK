class SKU:
    
    def __init__(self, total_licenses=int(), _type=str(), unlimited=bool()) -> None:
        self.total_licenses = total_licenses
        self._type = _type
        self.unlimited = unlimited

    def class_validator(self):
        pass


class IOCAttributes:

    def __init__(self, file=None, url=None, login=None, scheduled_task=None, dll_module_load=None, 
                    behavioral_indicators=None, fds=None, registry=None, data_masking=None, cross_process=None,
                    process=None, headers=None, command_scripts=None, autoinstall_browser_extensions=None,
                    dns=None, ip=None) -> None:
        self.file = file
        self.url = url
        self.login = login
        self.scheduled_task = scheduled_task
        self.dll_module_load = dll_module_load
        self.behavioral_indicators = behavioral_indicators
        self.fds = fds
        self.registry = registry
        self.data_masking = data_masking
        self.cross_process = cross_process
        self.process = process
        self.headers = headers
        self.command_scripts = command_scripts
        self.autoinstall_browser_extensions = autoinstall_browser_extensions
        self.dns = dns
        self.ip = ip
    

class Engines:

    def __init__(self, exploits=None, reputation=None, pup=None, remote_shell=None, lateral_movement=None,
                    preexecution_suspicious=None, executables=None, data_files=None, preexecution=None, 
                    penetration=None, application_control=None) -> None:
        self.exploits = exploits
        self.reputation = reputation
        self.pup = pup
        self.remote_shell = remote_shell
        self.lateral_movement = lateral_movement
        self.preexecution_suspicious = preexecution_suspicious
        self.executables = executables
        self.data_files = data_files
        self.preexecution = preexecution
        self.penetration = penetration
        self.application_control = application_control


class AutoFileUpload:

    def __init__(self, max_local_disk_usage_limit=None, max_local_disk_usage=None, 
                    max_daily_file_upload_limit=None, enabled=None, include_benign_files=None,
                    max_file_size_limit=None, max_file_size=None, max_daily_file_upload=None) -> None:
        self.max_local_disk_usage_limit = max_local_disk_usage_limit
        self.max_local_disk_usage = max_local_disk_usage
        self.max_daily_file_upload_limit = max_daily_file_upload_limit
        self.enabled = enabled
        self.include_benign_files = include_benign_files
        self.max_file_size_limit = max_file_size_limit
        self.max_file_size = max_file_size
        self.max_daily_file_upload = max_daily_file_upload


class Policy:

    def __init__(self, agent_notification=None, agent_logging_on=None, antitampering_on=None,
                    network_quarantine_on=None, autodecommission_days=None, ioc_attributes=None,
                    mitigation_mode=None, engines=None, autoimmune_on=None, user_full_name=None, created_at=None, 
                    agent_ui_on=None, updated_at=None, inherited_from=None, scan_new_agents=None,
                    ioc_supported=None, monitor_on_write=None, monitor_on_execute=None, auto_file_upload=None,
                    research_on=None, allow_remote_shell=None, mitigation_mode_suspicious=None, 
                    user_id=None, ioc=None, automitigation_action=None, snapshots_on=None, is_default=None) -> None:
        self.agent_notification = agent_notification
        self.agent_logging_on = agent_logging_on
        self.antitampering_on = antitampering_on
        self.network_quarantine_on = network_quarantine_on
        self.autodecommission_days = autodecommission_days
        self.ioc_attributes = ioc_attributes
        self.mitigation_mode = mitigation_mode
        self.engines = engines
        self.autoimmune_on = autoimmune_on
        self.user_full_name = user_full_name
        self.created_at = created_at
        self.agent_ui_on = agent_ui_on
        self.updated_at = updated_at
        self.inherited_from = inherited_from
        self.scan_new_agents = scan_new_agents
        self.ioc_supported = ioc_supported
        self.monitor_on_write = monitor_on_write
        self.monitor_on_execute = monitor_on_execute
        self.auto_file_upload = auto_file_upload
        self.research_on = research_on
        self.allow_remote_shell = allow_remote_shell
        self.mitigation_mode_suspicious = mitigation_mode_suspicious
        self.user_id = user_id
        self.ioc = ioc
        self.automitigation_action = automitigation_action
        self.snapshots_on = snapshots_on
        self.is_default = is_default


class Account:

    def __init__(self, name=str(), external_id=None, inherits=None, expiration=None, 
                    account_type=None, skus=SKU(), policy=None, unlimited_expiration=None):
        self.name = name
        self.external_id = external_id
        self.inherits = inherits
        self.expiration = expiration
        self.account_type = account_type
        self.skus = skus
        self.policy = policy
        self.unlimited_expiration = unlimited_expiration

        self.class_validator()

    def class_validator(self):
        if self.name == '' or type(self.name) != str:
            return TypeError("Attr 'name' must be of type str and not empty.")
