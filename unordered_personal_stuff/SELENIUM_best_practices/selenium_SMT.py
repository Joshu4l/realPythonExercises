from selenium import webdriver  # purpose: make sure to use the chromedriver.exe we saved under  "C:\bin\"
from selenium.webdriver.common.by import By  # purpose: selenium's proprietary module for finding elements on websites
from userConfig import config  # purpose: used for safely accessing our secret user credentials
import time  # purpose: enables us to set 'waiting' times for actions within our code

# Set up some <ChromeOptions>, which our session will rely on
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


def login():

	# using the '.config()' method from our 'userConfig.py' module in order to retrieve our credentials
	user_credentials = config()

	try:
		# Now that we're ready to interact with our browser, let's start a session and visit our first page
		driver.get('https://www.eis-scmt.com/home/lib/Controller.php')

		# Identify and assign relevant elements from the webpage
		usr = driver.find_element(By.ID, "username")
		pw = driver.find_element(By.ID, "password")
		login_button = driver.find_element(By.NAME, "Login")

		# Actually fill in the login credentials
		usr.click()
		usr.send_keys(user_credentials['username'])
		pw.click()
		pw.send_keys(user_credentials['password'])

		# specify how long we want to wait before proceeding to actually click the login button
		time.sleep(0.3)
		# Finally, sign in
		login_button.click()

		# let some time pass again before closing the browser
		time.sleep(3)
		# As a last step, close the browser
		driver.close()

		print(f"Login successful! Check your browser.")

	except (Exception):
		return f"Error: login was not successful\n" \
			   f"{Exception}"

# START THE SHOW
login()
