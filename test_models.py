from models import Driver

leclerc = {'driver_num':'19','full_name':'charls leclerc','team_name':'ferrari','country_code':'ita'}
lewis = {'driver_num':'44','full_name':'lewis hamellton','team_name':'ferrari','country_code':'usa'}

driver1 = Driver(leclerc)
driver2 = Driver(lewis)

print(driver1.to_tuple())
driver1.display_drivers()