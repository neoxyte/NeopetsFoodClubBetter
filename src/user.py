import requests


class User(object):
    """User class

       Represents a Neopets user account.

       Initialization:
          User(username, password)

       Attributes:
          email (str): GPXPlus Account Email )
          password (str): GPXPlus Account Password
          isLoggedIn (Bool): Returns true if account is logged in

        TODO:
        -Add assertions for proper input of username/password
        -Hash password/username
        -Add header to config file
        -create exceptions for 404, etc
        -PIN?
    """
    USERHEADER = {
        'Accept': (
            'text/html,application/xhtml+xml,application/xml;q=0.9,'
            'image/webp,*/*;q=0.8'
            ),
        'Origin': 'http://www.neopets.com',
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
            '(KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'
            ),
        'Content-Type': 'application/x-www-form-urlencoded',
        'DNT': '1',
        'Referer': 'http://www.neopets.com/pirates/foodclub.phtml?type=bet',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'en-US,en;q=0.8',
    }

    def __init__(self, account_username='', account_password=''):
        self.username = account_username
        self.password = account_password
        self.session = requests.Session()
        self.session.headers.update(self.USERHEADER)

    @property
    def loggedIn(self):
        """Returns True if logged in."""
        response = self.session.get('http://www.neopets.com')
        return 'Logout' in response.text

    def login(self):
        """Attemps to log in to Neopets. Returns true if successful"""
        credentials = {'username': self.username,
                       'password': self.password}
        login_response = self.session.post(
            'http://www.neopets.com/login.phtml', data=credentials)
        return self.loggedIn

    def logout(self):
        """Attempts to log out of Neopets. Returns true if successful"""
        logout_response = self.session.get(
            "http://www.neopets.com/logout.phtml")
        return not self.loggedIn
