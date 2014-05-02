from lxml import html, etree

class BettingParser(object):
    def __init__(self, UserSession):
        self.bettingSourceUrl = 'http://www.neopets.com/~myfoodclubbets'
        self.session = UserSession

    @property
    def bettingSourceText(self):
        response = self.session.get('http://www.neopets.com/~myfoodclubbets')
        responseText = response.text.encode('utf-8')
        return responseText

    def makeFinalBetList(self, arenaList, pirateList):
        finalBetList = []
        currentBet = []
        for betNumber in range(0, 10):
            currentBet = [arenaList[betNumber], pirateList[betNumber]]
            finalBetList.append(currentBet)
        return finalBetList

    def getBetsAsList(self):
        htmlTree = html.fromstring(self.bettingSourceText)
        arenas = []
        pirates = []
        for currentBet in range(3,13):
            currentArenaList = htmlTree.xpath('//body/center[2]/table/tr[' + str(currentBet) + ']/td[2]/b/text()')
            currentPirateList = []
            unformatedPirateList = htmlTree.xpath('//body/center[2]/table/tr[' + str(currentBet) + ']/td[2]/text()')
            for element in unformatedPirateList:
                currentPirateList.append(element[2:])
            currentPirateList.pop()
            currentPirateList.pop(0)
            pirates.append(currentPirateList)
            arenas.append(currentArenaList)
        return self.makeFinalBetList(arenas, pirates)