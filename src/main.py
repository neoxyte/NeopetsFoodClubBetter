import user
import betting_machine
import betting_ticket
import betting_parser

if __name__ == "__main__":
    print ''
    print ''
    print "Trixreli's Neopets Auto Food club better! Beta Version"
    print ''
    username = raw_input('Neopets Username: ')
    password = raw_input('Neopets Password: ')
    user = user.User(username, password)
    user.login()
    if user.loggedIn:
        machine = betting_machine.BettingMachine()
        ticket = betting_ticket.BettingTicket()
        parser = betting_parser.BettingParser(user.session)
        betList = parser.getBetsAsList()
        for i in range(0,10):
            preparedTicket = machine.prepareTicket(BettingTicket= ticket,
                UserSession = user.session, betList = betList, currentBet = i)
            machine.placeBet(preparedTicket, user.session)
            print 'Placing bet number ' + str(i + 1)
        print ''
        raw_input('Finished! Press Enter to close!')
    else:
        print ''
        raw_input(
            'Error: Unable to login. Please try again later. Press enter to close')