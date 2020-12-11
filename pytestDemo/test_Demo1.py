#Every test case in pytest file should start with test_ its manadatory
#Evert pytest method should start with test
#Any code should be wrapped in method only
import pytest

@pytest.mark.smoke
def test_firstModule(setup):
    print("Testing the first module program!")

def test_secondModulewithFormula():
    print("Testing the second module program with Formula!")

@pytest.mark.usefixtures("crossBrowser")
def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
