class BettingTicket(dict):
    def __init__(self):
        self.PIRATES = {
            'Scurvy Dan the Blade': '1',
            'Young Sproggie': '2',
            'Orvinn the First Mate': '3',
            'Lucky McKyriggan': '4',
            'Sir Edmund Ogletree': '5',
            'Peg Leg Percival': '6',
            'Bonnie Pip Culliford': '7',
            'Puffo the Waister': '8',
            'Stuff-A-Roo': '9',
            'Squire Venable': '10',
            'Captain Crossblades': '11',
            "Ol' Stripey": '12',
            'Ned the Skipper': '13',
            'Fairfax the Deckhand': '14',
            'Gooblah the Grarrl': '15',
            'Franchisco Corvallio': '16',
            'Federismo Corvallio': '17',
            'Admiral Blackbeard': '18',
            'Buck Cutlass': '19',
            'The Tailhook Kid': '20',
        }
        self.update({
            'winner1': None,
            'winner2': None,
            'winner3': None,
            'winner4': None,
            'winner5': None,
            'bet_amount': None,
            'total_odds': None,
            'winnings': None,
            'type': 'bet',
        })

    def formatTicket(self):
        winnerList = []
        if self['winner1'] is not None:
            winnerList.append('1')
        if self['winner2'] is not None:
            winnerList.append('2')
        if self['winner3'] is not None:
            winnerList.append('3')
        if self['winner4'] is not None:
            winnerList.append('4')
        if self['winner5'] is not None:
            winnerList.append('5')
        self.update({'matches[]': winnerList})
        #format odds properly to : whatever as string i.e. '2:1' not 2
        self.update({'total_odds': (str(self['total_odds']) + ':1')})
        self.update({'bet_amount' : str(self['bet_amount'])})
        self.update({'winnings' : str(self['winnings'])})
        return self

    def updateWinnerChoices(self, betList, currentBet = 0):
        arenaDictMap = {
            'Shipwreck': 'winner1',
            'Lagoon': 'winner2',
            'Treasure Island': 'winner3',
            'Hidden Cove': 'winner4',
            "Harpoon Harry's": '',
        }
        betChoices = {
            'winner1': None,
            'winner2': None,
            'winner3': None,
            'winner4': None,
            'winner5': None,
        }
        numberOfArenas= range(len(betList[currentBet][0]))
        for arena in numberOfArenas:
            betChoices.update({
                arenaDictMap[betList[currentBet][0][arena]]:
                    self.PIRATES[betList[currentBet][1][arena]]
            })
        self.update(betChoices)

    def updateBetAmount(self, userSession):
        """Updates bet amount to maximum possible bet"""
        url = 'http://www.neopets.com/pirates/foodclub.phtml?type=bet'
        response = userSession.get(url)
        number1 = response.text.find('You can only place up to <b>') + 28
        number2 = response.text.find('</b> NeoPoints per bet')
        betAmount = int(response.text[number1:number2])
        self.update({'bet_amount': betAmount})

    def updateOdds(self, userSession):
        url = 'http://www.neopets.com/pirates/foodclub.phtml?type=bet'
        response = userSession.get(url)
        text = response.text
        currentOdds = 1
        PIRATES = self.PIRATES
        if self['winner1'] is not None:
            pirateName = PIRATES.keys()[PIRATES.values().index(self['winner1'])]
            number1 = text.find(pirateName) + len(pirateName) + 9
            if text[number1+2] == ':':
                currentOdds *= int(text[number1:number1+2])
            else:
                currentOdds *= int(text[number1])
        if self['winner2'] is not None:
            pirateName = PIRATES.keys()[PIRATES.values().index(self['winner2'])]
            number2 = text.find(pirateName) + len(pirateName) + 9
            if text[number2+2] == ':':
                currentOdds *= int(text[number2:number2+2])
            else:
                currentOdds *= int(text[number2])
        if self['winner3'] is not None:
            pirateName = PIRATES.keys()[PIRATES.values().index(self['winner3'])]
            number3 = text.find(pirateName) + len(pirateName) + 9
            if text[number3+2] == ':':
                currentOdds *= int(text[number3:number3+2])
            else:
                currentOdds *= int(text[number3])
        if self['winner4'] is not None:
            pirateName = PIRATES.keys()[PIRATES.values().index(self['winner4'])]
            number4 = text.find(pirateName) + len(pirateName) + 9
            if text[number4+2] == ':':
                currentOdds *= int(text[number4:number4+2])
            else:
                currentOdds *= int(text[number4])
        if self['winner5'] is not None:
            pirateName = PIRATES.keys()[PIRATES.values().index(self['winner5'])]
            number5= text.find(pirateName) + len(pirateName) + 9
            if text[number5+2] == ':':
                currentOdds *= int(text[number5:number5+2])
            else:
                currentOdds *= int(text[number5])
        self.update({'total_odds': currentOdds})

    def updateWinnings(self):
        if self['bet_amount'] is not None:
            if self['total_odds'] is not None:
                self.update({'winnings': (self['bet_amount'] * self['total_odds'])})
