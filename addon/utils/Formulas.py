import math


class Formulas:
    def __init__(self):
        pass

    def cityCost(self, amount):
        return 50000*(amount-1)^3 + 150000 * amount + 75000

    def infraCost(self, amount):
        return (math.pow(math.fabs(amount-10), 2.2)/710) + 310

    def landCost(self, amount):
        return (.002*(amount-20)*(amount-20))+50

    def basePopulation(self, infra):
        return infra * 100

    def population(self, age, infra, hospitals, police_stations, pollution_index):
        return (self.basePopulation(infra) - self.diseaseDeaths(infra, hospitals, pollution_index) - self.crimeDeaths(infra, police_stations)) * self.ageBonus(age)

    def ageBonus(self, age_in_days):
        return 1 + math.log(age_in_days) / 15

    def crime(self, commerce, infra, police_stations):
        return ((103 - commerce)^2 + (self.basePopulation(infra)))/(111111) - self.policeModifier(police_stations)

    def policeModifier(self, police_stations):
        return police_stations * 2.5

    def crimeDeaths(self, infra, police_stations):
        return (self.crime(0, infra, police_stations)/10)*(infra*100)-25

    def disease(self, infra, hospitals, pollution_index):
        return ((((self.population(infra) * 2) * 0.01) - 25)/100) + (self.basePopulation(infra)/100000) + self.pollutionModifier(pollution_index) - self.hospitalModifier(hospitals)

    def pollutionModifier(self, pollution_index):
        return pollution_index * 0.05

    def hospitalModifier(self, hospitals):
        return hospitals * 2.5

    def diseaseDeaths(self, infra, hospitals, pollution_index):
        return self.disease(infra, hospitals, pollution_index) * self.basePopulation(infra)

    def soldiersPerCity(self):
        return 5 * 3000

    def maxSoldiers(self, cities: int):
        return (5 * cities) * 3000

    def currentMaxSoldiers(self, barracks: int):
        return barracks * 3000

    def tanksPerCity(self):
        return 5 * 250

    def maxTanks(self, cities: int):
        return (5 * cities) * 250

    def currentMaxTanks(self, factories: int):
        return factories * 250

    def tankBattleCost(self, tank_count: int):
        gas, munitions = (tank_count / 100) * 1
        return gas, munitions

    def aircraftPerCity(self):
        # 5 hangars per city each factory holds 15 planes
        return 5 * 15

    def maxAircraft(self, cities: int):
        return (5 * cities) * 15

    def currentMaxAircraft(self, hangars: int):
        return hangars * 15

    def aircraftBattleCost(self, plane_count: int):
        gas, munitions = (plane_count / 4) * 1
        return gas, munitions

    def shipsPerCity(self):
        # 3 drydocks per city each drydock holds 5 ships
        return 3 * 5

    def maxShips(self, cities: int):
        return (3 * cities) * 5

    def currentMaxShips(self, drydocks: int):
        return drydocks * 5

    def shipsBattleCost(self, ship_count: int):
        gas = ship_count * 2
        munitions = ship_count * 2.5
        return gas, munitions

    def neededWarchest(self, nation):
        cities = len(nation.get().cities())
        stockpile = nation.get().stockpile()

        money = [stockpile['money'], cities * 1000000]
        food = [stockpile['food'], cities * 600]
        uran= [stockpile['uranium'], cities * 15]
        steel = [stockpile['steel'], cities * 500]
        alum = [stockpile['aluminum'], cities * 400]
        gas = [stockpile['gasoline'], cities * 360]
        munis = [stockpile['munitions'], cities * 720]

        return money, food, uran, steel, alum, gas, munis

    def warchestPercentage(self, nation):
        pass