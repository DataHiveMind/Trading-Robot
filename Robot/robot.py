import pandas as pd

from td.client import TDClient
from td.utils import milliseconds_since_epoch

from datetime import datetime
from datetime import time
from datetime import timezone

from typing import Union
from typing import Dict
from typing import List

class PyRobot(object):
    def __int__(self, client_id: str, redirect_uri: str, credentials_path: str = None, trading_account: str = None, paper_trading: bool = True) -> None:
        self.trading: str = trading_account
        self.client_id: str = client_id
        self.redirect_uri: str = redirect_uri
        self.credentials_path: str = credentials_path
        self.session: TDClient = self._create_session()
        self.trading_account: str = self.get_account_number()
        self.trades: dict = {}
        self.hisstorical_prices: dict = {}
        self.stock_frame = None

    def _create_session(self) -> TDClient:
        td_client = TDClient(
            client_id=self.client_id,
            redirect_uri=self.redirect_uri,
            credentials_path=self.credentials_path
        )
        # Login into the Secceions
        td_client.login()
        return td_client


