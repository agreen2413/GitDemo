#@pytest.fixture()  will treat your method as a fixture.
#yield means like a post condition, meaning that code will run last. By adding "yield" in your "setup" fixture, you dont need another
#another method for the post test execution.
#Everytome you have a method or multple methods inside a class, always pass "self" as an argument.
#@pytest.mark.usefixtures("setup") - If you want to pass a method as an argument inside a "class" that IS a type "fixture" eg. "setup" inside the "conftest" file
#You will need to qdd this line @pytest.mark.usefixtures("setup") before writing your class() name. "setup" is the sample fixture here.
#self parameter is only required to pass as a parameter in a method if you are wrapping the "method" in a "class". But if you only write a method w/o a class, self not necessary as an argument.
import pytest

@pytest.mark.usefixtures("setup")
class TestCodeDemo:

    def test_Fixture(self):   #The "setup" method will run first before the test_Fixture by passing it as an argument. Its pre-requisite
        print("test_Fixture method will execute test steps after setup() method has ran first.")

    def test_Fixture2(self):   #The "setup" method will run first before the test_Fixture by passing it as an argument. Its pre-requisite
        print("test_Fixture2 method will execute test steps after setup() method has ran first.")

    def test_Fixture3(self):   #The "setup" method will run first before the test_Fixture by passing it as an argument. Its pre-requisite
        print("test_Fixture3 method will execute test steps after setup() method has ran first.")

    def test_Fixture4(self):   #The "setup" method will run first before the test_Fixture by passing it as an argument. Its pre-requisite
        print("test_Fixture4 method will execute test steps after setup() method has ran first.")