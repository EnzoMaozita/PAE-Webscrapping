from app.run import RunClass
from infra.driver import Driver

driver_class = Driver()
driver1 = driver_class.set_webdriver()

def run_task():
    ny_search = RunClass(driver1, "Santos", "Any", 3)
    ny_search.run_search()

run_task()