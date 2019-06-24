from pages.Loginpage import Login
from data.Testdata import *
import pytest

# launch the browser and the URL
@pytest.mark.usefixtures("test_setup")
class Test_acttime:
    def test_loginactime(self):
        driver=self.driver
        time=Login(driver)
        time.actlogin(USERNAME,PASSWORD)


# logut from the website
# def test_logutactime():
#     driver.implicitly_wait(30)
#     driver.find_element_by_id("logoutLink").click()

