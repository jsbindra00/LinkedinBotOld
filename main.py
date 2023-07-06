from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def wait_for_page_load(driver, timeout=10):
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def ScrollOnElement(element, element_css_selector, sleep_duration=0):
    JS_injection = """

    var fDialog = document.querySelector('{}');
    fDialog.scrollTop = fDialog.scrollHeight
        """.format(
        element_css_selector
    )

    browser.execute_script(JS_injection)
    if sleep_duration != 0:
        time.sleep(sleep_duration)


# f = open("C://Users//jasbi//Desktop//creds.txt").readlines()
f = []
username = f[0].strip()
password = f[1].strip()
# print(username)
# print(password)
browser = webdriver.Chrome()


def Login():
    browser.get("https://www.linkedin.com/uas/login")
    browser.find_element(By.ID, "username").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]').click()

    try:
        if (
            browser.find_element(By.CSS_SELECTOR, "h1").text
            == "Let's do a quick security check"
        ):
            print("Found security check.")
            input("Press enter when completed.")
    except:
        pass
    pass


def VisitConnections():
    Login()
    browser.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
    connection_class = "li.mn-connection-card.artdeco-list"

    WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, connection_class))
    )
    browser.get()

    print("Found connections...")
    connections = browser.find_elements(By.CSS_SELECTOR, connection_class)
    print(len(connections))

    for connection in connections:
        a_tag_class_name = "a.ember-view mn-connection-card__link"
        click = connection.find_element(By.CSS_SELECTOR, "a")
        click.send_keys(Keys.COMMAND + Keys.RETURN)
        time.sleep(0.5)
        # click.click()


def ScrollAllTheWayDown():
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def WaitTillJavaScriptLoaded():
    WebDriverWait(browser, 20).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def CheckIfConnectInvitationPhoneVerificationRequired(dismiss):
    time.sleep(1)
    href_value = "https://www.linkedin.com/help/linkedin/suggested/1239/email-address-needed-for-an-invitation"
    # Check if the specific a tag exists
    href_exists = False
    cross_button = browser.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
    return_val = True
    try:
        element = WebDriverWait(browser, 2).until(
            EC.presence_of_element_located((By.XPATH, f"//a[@href='{href_value}']"))
        )
        if cross_button:
            cross_button.click()
        return True
    except:
        return False

    # buttons = browser.find_elements(By.CLASS_NAME, "artdeco-button")
    # for button in buttons:
    #     children = button.find_elements(By.XPATH, ".//*[text()='Add a note']")
    #     if children:
    #         cross_button = browser.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
    #         if cross_button:
    #             cross_button.click()
    #             return True
    # return False


def SnipeUser(user_connection_page):
    def ClickNextPage():
        ScrollAllTheWayDown()
        WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "button.artdeco-pagination__button")
            )
        )
        next_buttons = browser.find_elements(
            By.CSS_SELECTOR, "button.artdeco-pagination__button"
        )
        next_buttons[1].click()
        return
        for button in next_buttons:
            nextText = browser.find_elements(
                By.XPATH, "//button[.//span[text()='Previous']]"
            )
            if not nextText:
                button.click()
                return
            else:
                continue

    Login()

    running = True
    browser.get(user_connection_page)

    while running:
        WaitTillJavaScriptLoaded()
        time.sleep(2)
        WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "artdeco-button"))
        )

        time.sleep(1)
        buttons = browser.find_elements(By.CLASS_NAME, "artdeco-button")
        connect_buttons = []
        for button in buttons:
            children = button.find_elements(By.XPATH, ".//*[text()='Connect']")
            if children:
                connect_buttons.append(button)

        print("Found {} connections".format(len(connect_buttons)))
        time.sleep(1)
        for button in connect_buttons:
            try:
                button.click()

                try:
                    if CheckIfConnectInvitationPhoneVerificationRequired(True) is True:
                        print("damn")
                        continue
                    WebDriverWait(browser, 1).until(
                        EC.presence_of_all_elements_located(
                            (By.CSS_SELECTOR, "h2#send-invite-modal")
                        )
                    )
                    print("found send confirmation modal")
                    send_buttons = browser.find_elements(
                        By.CLASS_NAME, "artdeco-button"
                    )
                    for send_button_possibility in send_buttons:
                        send_button_children = send_button_possibility.find_elements(
                            By.XPATH, ".//*[text()='Send']"
                        )
                        if send_button_children:
                            print("found")
                            send_button_possibility.click()
                            break
                except Exception as e:
                    print(e)
                    continue
            except Exception as newExcept:
                continue
        ClickNextPage()


def FindConnections():
    Login()
    browser.get("https://www.linkedin.com/mynetwork/")
    while True:
        try:
            # wait_for_page_load(browser)
            # wait = WebDriverWait(browser, 10)
            button_xpath = "/html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/ul/li[2]/div/button"

            wait = WebDriverWait(browser, 10)
            element = wait.until(
                EC.presence_of_element_located((By.XPATH, button_xpath)),
            )
            element = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
            browser.execute_script("arguments[0].click();", element)
            # button = browser.find_element(By.CSS_SELECTOR, "button[aria-label='See all People you may know from University of Bath']")
            # browser.execute_script("document.querySelector('{}').click()".format("button[aria-label='See all People you may know from University of Bath']"))

            pop_up_box_selector = ".artdeco-modal__content.discover-cohort-recommendations-modal__content.ember-view"
            pop_up_box = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, pop_up_box_selector))
            )

            while True:
                ActionChains(browser).move_to_element(pop_up_box).click()
                WebDriverWait(browser, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[.//span[text()='Connect']]")
                    )
                )

                buttons = browser.find_elements(
                    By.XPATH, "//button[.//span[text()='Connect']]"
                )
                for button in buttons:
                    try:
                        button.click()
                        time.sleep(0.5)
                    except:
                        continue
                for i in range(0, 5):
                    ScrollOnElement(pop_up_box, pop_up_box_selector, 1)

            time.sleep(10000)
        except Exception as e:
            break
            print(e)


FindConnections()
# VisitConnections()
# SnipeUser(
#     f"https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAABZECjMBbg_GCEGPDRUqMv_x0ydOeyGALO8%22%5D&network=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&page=34&sid=o-f"
# )

time.sleep(2000)
browser.quit()
