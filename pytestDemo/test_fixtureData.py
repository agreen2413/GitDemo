import pytest
import logging
from pytestDemo.BaseClass import BaseClass

@pytest.mark.usefixtures("dataLoad")
class MyPrifle(BaseClass):
    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[2])
        # print(dataLoad)