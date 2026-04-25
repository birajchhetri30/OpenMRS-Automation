from keyword_core.keywords import Keywords, KeywordData
from values.login_info import LoginInfo
from flows.login_flow.login_flow import LoginFlow
from flows.home_flow.home_flow import HomeFlow
from typing import Callable


class KeywordMapping:
    def __init__(self):
        self._mapping_dict: dict[KeywordData, Callable] = {}
        self._mapping()
    
    def _mapping(self):
        self._mapping_dict[Keywords.LOGIN] = self._login
        self._mapping_dict[Keywords.LOGOUT] = self._logout

    
    def _login(self, login_info: LoginInfo):
        login_flow = LoginFlow()
        login_flow.perform_login(
            username=login_info.username,
            password=login_info.password,
            location=login_info.location
        )
    
    def _logout(self, _ignored_arg):
        home_flow = HomeFlow()
        home_flow.perform_logout()
