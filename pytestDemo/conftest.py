#@pytest.fixture()  will treat your method as a fixture.
#yield means like a post condition, meaning that code will run last. By adding "yield" in your "setup" fixture, you dont need another
#another method for the post test execution.
#conftest file is the correct file where you write your "setup() fixtures so whatever test cases needs to run this first all you
#need to do is pass the "setup()" method as an argument to any of the test cases that will need to run this setup() method first.
#but place the setup() fixture method inside the "conftest" file.
#By doing this @pytest.fixture(scope="class") passing scope="class", the whatever the class that is using the "setup" fixture
#it will only run the setup once at the beginning and it wont run the post execution "until" all the test cases are run, then the
#post execution code will run last. So the beginning and last execution wont be repetitive. Pre-requisite and post execution will only run once.
#You only use request as a parameter inside your method if your @pytest is like this e.g  @pytest.fixture(params=["chrome", "Firefox", "IE"])
#Fixtures are use for setup and tear down methods for test cases - conftest file for generalization
#Fixtures make it available to all test cases - (fixture name into parameter of methods)
#Datadriven and parameterization can be done with "return" statements in a tuple format. Tuple is immutable and can't be modified.
#When you define fixture to scope="class", it will only "run once" before class is initiated and at the end.

import pytest

@pytest.fixture(scope="class")                                              #@pytest.fixture()  will treat your method as a fixture.
def setup():
    print("This code will be executed first...Before running any test cases.")
    yield                                                                   #yield means like a post test execution, meaning that code will run last.
    print("The code here will be executed last. This is post test execution.")

@pytest.fixture()
def dataLoad():
    print("User profile is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]

#@pytest.fixture(params=["chrome","Firefox","IE"])     #This if you only want to run the three types of browsers w/o other string parameters with it.
@pytest.fixture(params=[("chrome","Rahul","Shetty"), ("Firefox","Rahul"),("IE", "IX")])  #Use () around the [] if your passing more strings as a parameter
def crossBrowser(request):  #You only use request as a parameter inside your method if your @pytest is like this @pytest.fixture(params=["chrome", "Firefox", "IE"])
    return request.param



