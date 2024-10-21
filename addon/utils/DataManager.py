import os
import json

class DataManager:
    __default_path = f"{os.path.expanduser('~')}"
    main_path = ""
    data_path = ""
    log_path = ""
    
    
    def __init__(self, main_path):
        self.main_path = f"{self.__default_path}/{main_path}"
        self.data_path = f"{self.main_path}data/"
        self.log_path = f"{self.main_path}logs/"
        
        if os.path.exists(self.main_path):
            pass
        else:
            os.mkdir(self.main_path)
            os.mkdir(self.data_path)
            os.mkdir(self.log_path)
            
    def defaultAllianceFiles(self, desired_path):
        os.mkdir(desired_path)
        discord_roles_path = f"{desired_path}discord_roles.json"
        settings_path = f"{desired_path}settings.json"
        members_data_path = f"{desired_path}members.json"
            
        self.save(discord_roles_path, {'LEADER': 0, 'HEADDEPT': 0, 'FA': 0, 'IA': 0, 'MILCOM': 0, 'ECON': 0, 'ECONNB': 0, 'MEMBER': 0})
        self.save(settings_path, {'mmr_reqs': {'raider': {'barracks': 0, 'factories': 0, 'hangars': 0, 'drydocks': 0},
                                                'production': {'barracks': 0, 'factories': 0, 'hangars': 0, 'drydocks': 0}}})
        self.save(members_data_path, {})
            
        self.__defaultBankFiles(desired_path)
        
    def __defaultBankFiles(self, desired_path):
        bank_path = f"{desired_path}treasury/"
        
        os.mkdir(bank_path)
        bank_settings_path = f"{bank_path}settings.json"
        main_account_path = f"{bank_path}main.json"
        
        with open(bank_settings_path, 'w') as bank_settings:
            json.dump({}, bank_settings)
            
        with open(main_account_path, 'w') as main_account:
            json.dump({}, main_account)
            
    def save(self, path, obj):
        with open(path, 'w') as file:
            json.dump(obj, file)
            
    def load(self, path):
        with open(path, 'r') as file:
            return json.load(file)