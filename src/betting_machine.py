class BettingMachine(object):
    """Betting Machine for Neopets Food Club."""
    def prepareTicket(self, BettingTicket, UserSession, betList, currentBet):
        BettingTicket.updateWinnerChoices(betList, currentBet)
        BettingTicket.updateBetAmount(UserSession)
        BettingTicket.updateOdds(UserSession)
        BettingTicket.updateWinnings()
        return BettingTicket

    def placeBet(self, BettingTicket, UserSession):
        """Takes a BettingTicket as an argument an attempts to place the bet"""
        url = 'http://www.neopets.com/pirates/process_foodclub.phtml'
        return UserSession.post(url, data=BettingTicket.formatTicket())
