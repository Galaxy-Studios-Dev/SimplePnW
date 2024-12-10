from simplepnw.addon.nation.BuildPlan import BuildPlan

class City:
    __name = ""

    __is_infra_land = True
    __is_build = True
    __is_mmr = True

    __infra = 0
    __land = 0

    __power = {}
    __raw = {}
    __produced ={}
    __civil = {}
    __commerce = {}
    __military = {}

    def __init__(self, name, infra: int, land: int):
        self.__name = name

        self.__infra = infra
        self.__land = land

    def name(self):
        return self.__name

    def isInfraLand(self):
        return self.__is_infra_land

    def isBuild(self):
        return self.__is_build

    def isMMR(self):
        return self.__is_mmr

    def infra(self):
        return self.__infra

    def land(self):
        return self.__land

    def buildPlan(self, nation):
        name = nation.buildPlan().name()
        projects = nation.get().projects()

        return BuildPlan(name, self.infra(), self.land(), projects, {'power': self.__power, 'raw': self.__raw, 'produced': self.__produced,
                'civil': self.__civil, 'commerce': self.__commerce, 'military': self.__military})

    def setIsInfraLand(self, value: bool):
        self.__is_infra_land = value

    def setIsBuild(self, value: bool):
        self.__is_build = value

    def setIsMMR(self, value: bool):
        self.__is_mmr = value

    def setBuilds(self, power: dict, raw: dict, produced: dict, civil: dict, commerce: dict, military: dict):
        self.setPower(power)
        self.setRawGoods(raw)
        self.setProducedGoods(produced)
        self.setCivilBuilds(civil)
        self.setCommerceBuilds(commerce)
        self.setMilitaryBuilds(military)

    def setPower(self, value: dict):
        self.__power = value

    def setRawGoods(self, value: dict):
        self.__raw = value

    def setProducedGoods(self, value: dict):
        self.__produced = value

    def setCivilBuilds(self, value: dict):
        self.__civil = value

    def setCommerceBuilds(self, value: dict):
        self.__commerce = value

    def setMilitaryBuilds(self, value: dict):
        self.__military = value