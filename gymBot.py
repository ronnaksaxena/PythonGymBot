from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC

#launches gymtable on safari
driver = webdriver.Safari()
driver.get('https://hub.ucd.ie/usis/W_HU_MENU.P_PUBLISH?p_tag=GYMBOOK')


if driver.find_element(By.XPATH, '//*[@id="SW300-1|0"]/td[2]').text == 'Performance gym':
    bookButton = driver.find_element(By.XPATH, '//*[@id="SW300-1|0"]/td[6]/a')
    driver.get(bookButton.get_attribute('href'))
elif driver.find_element(By.XPATH, '//*[@id="SW300-1|1"]/td[2]').text == 'Performance gym':
    bookButton = driver.find_element(By.XPATH, '//*[@id="SW300-1|1"]/td[6]/a')
    driver.get(bookButton.get_attribute('href'))
else:
    print('All slots full ;(')
    driver.close()

'''
#test DELETE LATER
driver.get('https://hub.ucd.ie/usis/W_HU_REPORTING.P_RUN_SQL?p_query=SW-GYMANON&p_confirmed=Y&p_parameters=A450F95C75D0F126D32D1FF64557FC5BE3608119B07310D1D9E0C20656AF60AC613D8D39CD5236FDD9B95C7FC606FF4DF4578128C998B02038C6710B5CBFE71922B20249A7A3A24BD6C3D14535B8874157B609FEDFE6F30C8D8E41C60A98A087EEB7ECC20C2CC780F7F9233522FAF848E77698D5910CE2A89B963FB05BAAF0A9A0044C90CFC6FDA99649C067738535C022DDBA1B6A3FE1BAF250185CF2B7CC61B274709E42461C1C287D46E09DAADC6B4707F1ACAE0EBF391C903855AE53639601F170D1BF3BC30EF801E89210ACA8E0697E024BFDD7AE73F0E586FB5DB419101E2A89941F4FFBDE97EB516C947F3CD815381BBB5D9853D338D66B5CADBCCD1F4D4086F7DF22967D8BB26CB9C61D81530830B9017DE83836DF2A7E445C14695A52773EFAE11DCC203F16CE00ECD2158D88B4F2F11327F7AC0FFF44B45331990094B5A50EB7E8A76770D788B8675E4CB5702632C6B41CB0F0BFCBE9A4BCB9B17D')
'''
#accepts cookies
try:
    acceptButton = ui.WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
    acceptButton.click()
except:
    print('First accept Not there ;(')

#types in studentID
studentIDBOX = driver.find_element(By.NAME, 'MEMBER_NO')
studentIDBOX.send_keys('21210918') #Wills UCD ID

proceedBox = driver.find_element(By.XPATH, '//*[@id="single-column-content"]/div/div/div/div[2]/div/form/input[5]')
#ui.WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="single-column-content"]/div/div/div/div[2]/div/form/input[5]')))
proceedBox.submit()

'''
#accepts cookies again
try:
    acceptButton = ui.WebDriverWait(driver,10).until(EC.element_to_be_clickable(By.ID, 'onetrust-accept-btn-handler'))
    acceptButton.click()
except:
    print('Second Accept Not there ;(')
'''

#confirms booking
screenButtons = driver.find_elements(By.CLASS_NAME, 'menubutton')
for button in screenButtons:
    print(button.text)
    if button.text == 'Confirm Booking':
        confirmButton = button
        print(confirmButton.text)
        confirmButton.click()
        print('SNIPED 🎯')

#driver.close()


'''
# To loop through all rows with slots
table = driver.find_element(By.CLASS_NAME, 'datadisplaytable')
rows = table.find_elements(By.TAG_NAME, 'tr')
for r in rows:
    print(r)
'''

'''
#gets first BOOK elem
firstLink = table.find_element(By.XPATH, '//*[@id="SW300-1|0"]/td[6]/a')
firstLink.click()
'''


'''
Example 9:30am
Table XPath:
//*[@id="SW300-1|0"]
Time XPath:
//*[@id="SW300-1|0"]/td[1]
Link to booking:
//*[@id="SW300-1|0"]/td[6]/a


will be idx 4 exactly 3 hrs before open
//*[@id="SW300-1|4"]/td[6]/a


8:15 XPath: //*[@id="SW300-1|1"]/td[6]/a
9:00 Xpath: //*[@id="SW300-1|2"]/td[6]/a
10:45 Xpath: //*[@id="SW300-1|5"]/td[6]/a
//*[@id="SW300-1|2"]/td[6]/a
The time textbook is:   //*[@id="SW300-1|2"]/td[1]

12:00 XPath: //*[@id="SW300-1|5"]/td[6]/a
//*[@id="SW300-1|0"]/td[6]/a
'''