class AllianceQuery:
    __name = ""
    __id = 0
    __acronym = ""
    __date = ""
    __color = ""

    __flag = ""
    
    __avg_score = 0
    __accept_members = False
    __members = {}
    __positions = {}
    
    __resources = {}
    
    def __init__(self, simple_pw, aa_id):
        result = simple_pw.legacyKit().query("alliances", {"id": aa_id, "first": 1},
                                                """
                                                name
                                                id
                                                acronym
                                                date
                                                color
                                                
                                                average_score
                                                flag
                                                accept_members
                                                
                                                coal
                                                iron
                                                lead
                                                bauxite
                                                oil
                                                uranium
                                                food
                                                steel
                                                aluminum
                                                gasoline
                                                munitions
                                                money
                                                
                                                alliance_positions {
                                                    name
                                                    date
                                                    
                                                    withdraw_bank
                                                    manage_treaties
                                                    manage_embargoes
                                                    manage_market_share
                                                    manage_announcements
                                                    promote_self_to_leader
                                                    edit_alliance_info
                                                }
                                                
                                                nations {
                                                    nation_name
                                                    leader_name
                                                    alliance_join_date
                                                    alliance_position
                                                    alliance_seniority
                                                }
                                                """).get()

        alliance = result.alliances[0]
        self.__name = alliance.name
        self.__id = alliance.id
        self.__acronym = alliance.acronym
        self.__date = alliance.date
        self.__color = alliance.color
        
        self.__avg_score = alliance.average_score
        self.__accept_members = alliance.accept_members
        self.__positions = alliance.alliance_positions
        self.__members = alliance.nations
        
        self.__resources = {'coal': alliance.coal, 'iron': alliance.iron, 'lead': alliance.lead, 'bauxite': alliance.bauxite, 'oil': alliance.oil, 'uranium': alliance.uranium, 'food': alliance.food, 'steel': alliance.steel, 'aluminum': alliance.aluminum, 'gasoline': alliance.gasoline, 'munitions': alliance.munitions, 'money': alliance.money}

    def name(self):
        return self.__name

    def id(self):
        return self.__id

    def acronym(self):
        return self.__acronym

    def colorBlock(self):
        return self.__color

    def founded(self):
        return self.__date

    def discordInvite(self):
        return self.__discord_invite
        
    def flag(self):
        return self.__flag

    def averageScore(self):
        return self.__avg_score

    def acceptingMembers(self):
        return self.__accept_members

    def positions(self):
        return self.__positions

    def members(self):
        return self.__members
        
    def stockpile(self):
        return self.__resources
        