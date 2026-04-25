from keyword_core.page_provider import get_page
from screens.home.home_screen import HomeScreen

class HomeFlow:
    def __init__(self):
        self.page = get_page()
        self.home_screen = HomeScreen(self.page)
    
    def perform_logout(self):
        self.home_screen.logout_button.click()