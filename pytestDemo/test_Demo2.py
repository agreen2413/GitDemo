#Every test case in pytest file should start with test_ its manadatory
#Evert pytest method should start with test
#Any code should be wrapped in method only
#Method name should makes sense
#Command -k stands for method key names execution (Key names of the test cases you only want to run, -s stands for logs in output, -v stands for more info metadata
#You can run specific file with py.test <filename>
#The command -m stands for mark e.g. @pytest.mark.smoke, @pytest.mark.regression etc -m <keyword name e.g smoke>
#You can skip test case by adding this line @pytest.mark.skip just before your test case / method name.
#@pytest.fixture()  will treat your method as a fixture.
#yield means like a post condition, meaning that code will run last. By adding "yield" in your "setup" fixture, you dont need another
#another method for the post test execution.

import pytest


@pytest.mark.smoke
@pytest.mark.skip           #Skip means that this test case will not be executed cause there is an error. So we skip this one until fix.
def test_firstModule():
    msg = "Testing the first module program!"
    assert msg == "Testing the fifth module program!", "Test Failed because string do not match!"       #This should fail cause msg is Testing first module NOT fifth module


def test_secondModulewithFormula():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition and formula do not match!"    #But this will passed because a + 2 is eqaul to 6

