from selenium import webdriver  # purpose: make sure to use the chromedriver.exe we saved under  "C:\bin\"
from selenium.webdriver.common.by import By  #
from userConfig import config
import time  # purpose: enables us to set 'waiting' times for actions within our code

# Set up some <ChromeOptions> which our session will rely on
chrome_options = webdriver.ChromeOptions()

# now, using our <ChromeOptions>, we populate them with our preferences for cookie-handling
chrome_options.add_experimental_option(
	"prefs", {"profile.default_content_setting_values.cookies": 1}
	)
		# IMPORTANT HERE:
		# value 2 means -> disable all cookies
		# value 1 means -> accept all cookies

# Declare TWO things here
driver = webdriver.Chrome(options=chrome_options)
	# 1st: the browser which selenium.webdriver is focussing on is CHROME
	# 2nd: the webdriver shall consider the <chrome_options> we defined above as an argument in here



# using the '.config()' method from our 'userConfig.py' module in order to retrieve our credentials
user_credentials = config()

def login():
	# Now that we're able to interact with our browser, let's start a session and visit our first page
	# driver.get('https://google.com')  # specify the page we want to open up initially
	driver.get('https://www.eis-scmt.com/home/lib/Controller.php')

	# Fill in the login data
	eis_user = driver.find_element(By.ID, "username")
	eis_user.click()
	eis_user.send_keys("albertjoshua5@gmail.com")

	eis_pw = driver.find_element(By.ID, "password")
	eis_pw.click()
	eis_pw.send_keys("Meadows_01!")

	login_button = driver.find_element(By.NAME, "Login")
	# specify how long we want to wait before proceeding to actually click the login button
	time.sleep(3)

	login_button.click()

	driver.close()

print(user_credentials)










