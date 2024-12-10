from simplepnw.addon.utils.auditting.Audit import Audit
from simplepnw.addon.nation.City import City

class BuildAudit(Audit):
    __nation = {}

    def __init__(self, nation):
        super().__init__("Build Audit")
        self.__nation = nation

    def run(self):
        results = {}
        cities = self.__nation.cities()

        complete_infraland = True
        complete_build = True
        complete_mmr = True

        for city in cities:
            city = cities[city]
            cbplan = city.buildPlan(self.__nation)

            if not self.__checkInfraLand(cbplan):
                city.setIsInfraLand(False)
                complete_infraland = False

            if not self.__checkBuilds(cbplan):
                city.setIsBuild(False)
                complete_build = False

            if not self.__checkMilitaryBuilds(cbplan):
                city.setIsMMR(False)
                complete_mmr = False

        results = self.__removeGoodCities(cities)

        if complete_infraland and complete_build and complete_mmr:
            self.setStatus(True)
        else:
            self.setStatus(False)

        return results

    def __checkInfraLand(self, cbplan):
        infra = self.__nation.buildPlan().infra()
        land = self.__nation.buildPlan().land()

        if cbplan.infra() == infra and city_bplan.land() >= land:
            return True
        else:
            return False

    def __checkProjects(self):
        pass

    def __checkBuilds(self, cbplan):
        if self.__checkPowerBuilds(cbplan) and self.__checkRawGoodBuilds(cbplan) and self.__checkProducedGoodBuilds(cbplan) and self.__checkCivilBuilds(cbplan) and self.__checkCommerceBuilds(cbplan):
            return True
        else:
            return False

    def __checkPowerBuilds(self, cbplan):
        power = self.__nation.buildPlan().power()
        city_power = cbplan.power()

        if city_power['coal'] == int(power['coal']) and city_power['oil'] == int(power['oil']) and city_power['nuclear'] == int(power['nuclear']) and city_power['wind'] == int(power['wind']):
            return True
        else:
            return False

    def __checkRawGoodBuilds(self, cbplan):
        raw = self.__nation.buildPlan().rawGoods()
        city_raw = cbplan.rawGoods()

        if city_raw['coal'] == int(raw['coal']) and city_raw['iron'] == int(raw['iron']) and city_raw['lead'] == int(raw['lead']) and city_raw['bauxite'] == int(raw['bauxite']) and city_raw['oil'] == int(raw['oil']) and city_raw['uranium'] == int(raw['uranium']) and city_raw['food'] == int(raw['food']):
            return True
        else:
            return False

    def __checkProducedGoodBuilds(self, cbplan):
        produced = self.__nation.buildPlan().producedGoods()
        city_produced = cbplan.produced()

        if city_produced['steel'] == int(produced['steel']) and city_produced['aluminum'] == int(produced['aluminum']) and city_produced['gasoline'] == int(produced['gasoline']) and city_produced['munitions'] == int(produced['munitions']):
            return True
        else:
            return False

    def __checkCivilBuilds(self, cbplan):
        civil = self.__nation.buildPlan().civilBuilds()
        city_civil = cbplan.civilBuilds()

        if city_civil['police'] == int(civil['police']) and city_civil['hospitals'] == int(civil['hospitals']) and city_civil['recycling'] == int(civil['recycling']) and city_civil['subways'] == int(civil['subways']):
            return True
        else:
            return False

    def __checkCommerceBuilds(self, cbplan):
        commerce = self.__nation.buildPlan().commerceBuilds()
        city_commerce = cbplan.commerceBuilds()

        if city_commerce['markets'] == int(commerce['markets']) and city_commerce['banks'] == int(commerce['banks']) and city_commerce['malls'] == int(commerce['malls']) and city_commerce['stadiums'] == int(commerce['stadiums']):
            return True
        else:
            return False

    def __checkMilitaryBuilds(self, cbplan):
        mil_builds = self.__nation.buildPlan().militaryBuilds()
        city_mil = cbplan.militaryBuilds()

        if city_mil['barracks'] >= int(mil_builds['barracks']) and city_mil['factories'] >= int(mil_builds['factories']) and city_mil['hangars'] >= int(mil_builds['hangars']) and city_mil['drydocks'] >= int(mil_builds['drydocks']):
            return True
        else:
            return False

    def __removeGoodCities(self, list):
        temp = list.copy()
        list.clear()

        for key in temp.keys():
            city = temp[key]
            good_city = True

            if not city.isInfraLand() or not city.isBuild() or not city.isMMR():
                good_city = False

            if not good_city:
                list[key] = city

        return list
