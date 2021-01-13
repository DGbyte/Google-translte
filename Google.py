from textblob import TextBlob
import requests
from google_trans_new import google_translator
from selenium import webdriver
from selenium.webdriver.common.by import By

translator = google_translator()

# The locally path of the web driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
# Using Chrome
driver = webdriver.Chrome(PATH)

# Reach Google Translate web page for testing by Selenium
driver.get("https://translate.google.co.il/?hl=iw")

# Get the input area (the input that we would like to translate)
inputElement = driver.find_element_by_class_name('er8xn')
inputElement.send_keys('שלום')
input_text = inputElement.get_attribute('value')

# Opens the window with all the languages
openView = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[5]/button')
openView.click()

# Function that checks if given text is recognized correctly
def check_input_lang():
# Extracts recognized language (right side)
    t = driver.find_element(By.XPATH, '//*[@id="i9"]')
    rec_code = t.get_attribute('data-language-code')
    b = TextBlob(input_text)
    actual_code = b.detect_language()
    if actual_code == rec_code:
        print('Recognized correctly')
    else:
        print('Incorrect recognization')

# Function that runs from the second language-code that appears on 'Google Translate' website
# (the first is 'Auto') checks if given text translated to appropriate language
# and compares it to expected result
def check_lang_code_all_options():
    detectedLang2 = driver.find_element_by_class_name('SL5JTc')
    subclass = detectedLang2.find_elements_by_class_name('ordo2')

    for elem in range(1, len(subclass)):
        curr_code = subclass[elem].get_attribute('data-language-code')
        print(subclass[elem].get_attribute('data-language-code'))
        translate_text = translator.translate(input_text, lang_tgt=curr_code)
        print(translate_text)
        check_c = TextBlob(translate_text)
        check_code = check_c.detect_language()
        print(check_code)
        if check_code == curr_code:
            print('Translated to appropriate language')
        else:
            print('Translated to incorrect language')


# Main function
def main():
  check_input_lang()
  check_lang_code_all_options()

if __name__ == "__main__":
  main()