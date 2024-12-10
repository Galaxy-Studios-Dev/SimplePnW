import datetime
import discord

from simplepnw.addon.utils.auditting.Audit import Audit

class ActivityAudit(Audit):
    __nation = {}
    __check_against = {'day': 0, 'color': ""}
    __results = {'days_passed': 0, 'color': "", 'checks': {}}

    def __init__(self, check_against, nation):
        super().__init__("Activity Audit")
        self.__nation = nation
        self.__check_against = {'day': check_against['day'], 'color': check_against['color']}

    def result(self, key):
        return self.__results[key]

    def results(self):
        return self.__results

    def run(self):
        date = datetime.datetime.now()
        color_block = self.__nation.get().colorBlock()
        last_seen = self.__nation.get().lastActive()

        if color_block == self.__check_against['color']:
            self.__results['color'] = color_block
            if last_seen.day > date.day:
                days_passed = last_seen.day - date.day

                if days_passed < self.__check_against['day']:
                    self.__setResults(days_passed, color_block, self.__check_against)
                    self.setStatus(True)
                elif days_passed > self.__check_against['day']:
                    self.__setResults(days_passed, color_block, self.__check_against)
                    self.setStatus(False)
            elif last_seen.day < date.day:
                days_passed = date.day - last_seen.day

                if days_passed < self.__check_against['day']:
                    self.__setResults(days_passed, color_block, self.__check_against)
                    self.setStatus(True)
                elif days_passed > self.__check_against['day']:
                    self.__setResults(days_passed, color_block, self.__check_against)
                    self.setStatus(False)
        else:
            self.__results['color'] = color_block
            self.setStatus(False)
            if last_seen.day > date.day:
                days_passed = last_seen.day - date.day

                if days_passed < self.__check_against['day']:
                    self.__setResults(days_passed, color_block, self.__check_against)
                elif days_passed > self.__check_against['day']:
                    self.__setResults(days_passed, color_block, self.__check_against)
            elif last_seen.day < date.day:
                days_passed = date.day - last_seen.day

                if days_passed < self.__check_against['day']:
                    self.__setResults(days_passed, color_block, self.__check_against)
                elif days_passed > self.__check_against['day']:
                    self.__setResults(days_passed, color_block, self.__check_against)

    def __setResults(self, passed, color, checks):
        self.__results['days_passed'] = passed
        self.__results['color'] = color
        self.__results['checks'] = checks
