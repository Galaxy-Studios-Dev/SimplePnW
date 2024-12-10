import os
import shutil

import discord

from simplepnw.addon.Nation import Nation
from simplepnw.addon.Bank import Bank
from simplepnw.addon.alliance.Coalition import Coalition

class Alliance:
    __kit = {}
    __query = {}
    __runs_audits = False
    __audit_channels = {}
    
    __discord = {}
    __discord_roles = {'LEADER': 0, 'HEADDEPT': 0, 'FA': 0, 'IA': 0, 'MILCOM': 0, 'ECON': 0, 'ECONNB': 0, 'MEMBER': 0}
    __webhook_urls = {}
    
    __mmr_reqs = {'raider': {'barracks': 0, 'factories': 0, 'hangars': 0, 'drydocks': 0}, 'production': {'barracks': 0, 'factories': 0, 'hangars': 0, 'drydocks': 0}}
    
    __members = {}
    
    __bank = {}
    __offshores = {}
    
    __coalitions = {}
    
    def __init__(self, simplepnw, aa_id):
        self.__kit = simplepnw
        self.__query = self.__kit.query('alliance', aa_id)
        
        self.__bank = Bank(self)
        
        # self.createDirectory()
        
    def get(self):
        return self.__query
        
    def runsAudits(self):
        return self.__runs_audits
        
    def discord(self):
        return self.__discord
        
    def discordId(self):
        return self.__discord.id
        
    def discordRoles(self):
        return self.__discord_roles
        
    def discordRole(self, ctx, key):
        role = discord.utils.get(ctx.guild.roles, id=int(self.__discord_roles[key]))
        return role

    def auditChannel(self, key):
        return self.__audit_channels[key]
        
    def webhook(self, key):
        return self.__webhook_urls[key]
        
    def webhooks(self):
        return self.__webhook_urls
        
    def bank(self):
        return self.__bank
        
    def MMR(self):
        return self.__mmr_reqs
        
    def specificMMR(self, key):
        return self.__mmr_reqs[key]
        
    def specificMMR(self, key):
        return self.__mmr_reqs[key]
        
    def members(self):
        return self.__members
        
    def specificMember(self, key):
        return self.__members[key]

    def specificCoalition(self, key):
        return self.__coalitions[key]

    def coalitions(self):
        return self.__coalitions

    def setRunsAudits(self, value: bool):
        self.__runs_audits = value
        
    def setDiscord(self, discord_user):
        self.__discord = discord_user

    def setAuditChannel(self, key: str, value):
        self.__audit_channels[key] = value
        
    def setSpecificDiscordRole(self, key, value):
        self.__discord_roles[key] = value

    def setDiscordRoles(self, role_ids):
        temp = {}
        for key in self.__discord_roles:
            for x in range(len(role_ids)):
                temp[key] = role_ids[x]

        self.__discord_roles = temp
        
    def addWebhook(self, key, value):
        self.__webhook_urls[key] = value
        
    def setMMR(self, required_mmr):
        self.__mmr_reqs = required_mmr
        
    def setSpecificMMR(self, key, required):
        self.__mmr_reqs[key] = required
        
    def setMembers(self, nations):
        self.__members = {}
        self.__members = nations
        
    def addMember(self, key, nation):
        self.__members[key] = nation
        
    def setCoalitions(self, value):
        self.__coalitions = value
        
    def addCoalition(self, key, coalition):
        self.__coalitions[key] = coalition

    def createCoalition(self, name):
        new_coalition = Coalition(name, self)
        self.__coalitions[new_coalition.name()] = new_coalition
        
    def generalStats(self):
        stats = {'land': 0, 'infra': 0, 'population': 0, 'GDP': 0}
        
        for member in self.__members:
            member = self.__members[member]
            land = member.get().land()
            infra = member.get().infrastructure()
            
            stats['land'] = stats['land'] + land
            stats['infra'] = stats['infra'] + infra
            stats['population'] = stats['population'] + member.get().population()
            
        return stats
        
    def warStats(self):
        stats = {'won': 0, 'lost': 0, 'total': 0}
        
    def militaryStats(self):
        pass
        
    def createDirectory(self):
        data_manager = self.__kit.dataManager()
        desired_path = f"{data_manager.data_path}{self.get().id()}/"
        
        if os.path.exists(desired_path):
            if os.path.exists(f"{desired_path}settings.json"):
                pass
            else:
                shutil.rmtree(desired_path)
                data_manager.defaultAllianceFiles(desired_path)
        else:
            data_manager.defaultAllianceFiles(desired_path)
            
    def setup(self):
        data_manager = self.__kit.dataManager()
        desired_path = f"{data_manager.data_path}{self.get().id()}/"
        
        if os.path.exists(desired_path):
            settings_file = f"{desired_path}settings.json"
            discord_roles_file = f"{desired_path}discord_roles.json"
            members_file = f"{desired_path}members.json"
            
            settings = data_manager.load(settings_file)
            self.__mmr_reqs = settings['mmr_reqs']
            
            discord_roles = data_manager.load(discord_roles_file)
            self.__discord_roles = discord_roles
            
            members = data_manager.load(members_file)
            
            for key in members.keys():
                member = members[key]
                member_path = f"{desired_path}treasury/{member['nation_id']}"
                discord_user = discord.utils.get(self.discord().members, id=int(member['discord_id']))
                
                nation = Nation(self.__kit, member['nation_id'])
                nation.setDiscord(discord_user)
                nation.bank().setup(member_path)
                
                self.__members[nation.discordId()] = nation
                
            self.__bank = Bank(self.__kit, self)
            self.__bank.setup(f"{desired_path}treasury/main")
            
    def save(self):
        data_manager = self.__kit.dataManager()
        
        desired_path = f"{data_manager.data_path}{self.get().id()}/"
        main_bank_path = f"{desired_path}treasury/main.json"
        bank_settings_path = f"{desired_path}treasury/settings.json"
        
        data_manager.save(f"{desired_path}settings.json", {'mmr_reqs': self.__mmr_reqs})
        data_manager.save(f"{desired_path}discord_roles.json", self.__discord_roles)
        
        temp = {}
        
        for member in self.members():
            member = self.members()[member]
            nation_id = member.get().id()
            
            temp[member.discord().global_name] = {'nation_id': nation_id, 'discord_id': member.discordId()}
            member.bank().save(f"{desired_path}treasury/{nation_id}.json")
            
        data_manager.save(f"{desired_path}members.json", temp)
        
        data_manager.save(bank_settings_path, {})
        data_manager.save(main_bank_path, self.__bank.resources())
        