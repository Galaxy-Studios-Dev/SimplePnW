class BuildPlan:
    __name = ""

    __projects = {}
    __land = 0
    __infra = 0

    __power = {'coal': 0, 'oil': 0, 'nuclear': 0, 'wind': 0}
    __raw = {'coal': 0, 'iron': 0, 'lead': 0, 'bauxite': 0, 'oil': 0, 'uranium': 0, 'food': 0}
    __produced = {'steel': 0, 'aluminum': 0, 'gasoline': 0, 'munitions': 0}
    __civil = {'police': 0, 'hospitals': 0, 'recycling': 0, 'subways': 0}
    __commerce = {'markets': 0, 'banks': 0, 'malls': 0, 'stadiums': 0}
    __mmr = {'barracks': 0, 'factories': 0, 'hangars': 0, 'drydocks': 0}

    def __init__(self, name, infra, land, projects, details):
        self.__name = name

        self.__projects = projects
        self.__infra = infra
        self.__land = land

        self.__power = details['power']
        self.__raw = details['raw']
        self.__produced = details['produced']
        self.__civil = details['civil']
        self.__commerce = details['commerce']
        self.__mmr = details['military']

    def name(self):
        return self.__name

    def infra(self):
        return self.__infra

    def land(self):
        return self.__land

    def projects(self):
        return self.__projects

    def power(self):
        return self.__power

    def rawGoods(self):
        return self.__raw

    def producedGoods(self):
        return self.__produced

    def civilBuilds(self):
        return self.__civil

    def commerceBuilds(self):
        return self.__commerce

    def militaryBuilds(self):
        return self.__mmr

    def display(self):
        print(f"Name: {self.__name}\nInfra: {self.__infra}\tLand: {self.__land}\nProjects: {self.__projects}\nRaw Goods: {self.__raw}\nManu Goods: {self.__produced}\nCivil Builds: {self.__civil}\nCommerce Builds: {self.__commerce}\nMil Builds: {self.__mmr}\n")