from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import requests as req
from fileParser import *

# constants
DRIVER_PATH = "driver\\chromedriver.exe"  # update driver when obsolete
DOWNLOAD_PATH = "\\files"
BASE_URL = "http://www.cs.xxxxxxx.ro/studenti/lista-studentilor/"  # censored website name

# driver init
options = Options()  # init chrome options
options.headless = True  # toggles background run mode
options.add_argument("--window-size=1920,1080")
prefs = {'download.default_directory': DOWNLOAD_PATH}
options.add_experimental_option('prefs', prefs)  # adding the chrome default download directory as a ChromeOption
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)  # initializing chromedriver(selenium) with opts


# todo ----------- Simple Functions

def dictDownloadV5(dic):  # mashed dictD and fDown, why were they split?
    """
    Downloads a group file from a link in the given dictinary, and titles it by it's mathing value.

    :param dict dic: dictionary of link and group name
    """
    for grTitle in dic:
        request = req.get(dic[grTitle], allow_redirects=True)
        path = "G:\\_Local\\Programming\\Python\\API's\\stdList\\files\\" + grTitle
        with open(path, 'wb') as f:
            f.write(request.content)


# todo ------------------- Un-separable Functions
# extend the use of the app by parsing all data from xlsx file?, not going to yet

def resultCalculatorV5(QUERY):  # 4'th day of learning BS - prints/downloads excel file of every math-cs group
    """
    Calculates result from a given query:
    matematica-informatica, germana, engleza, etc. or NULL to get all

    :param str QUERY : string to be searched for in titles

    :rtype: dict
    :return: dict of files and group names
    """
    resultDict = {}
    driver.get(BASE_URL)
    soup = bs(driver.page_source, 'html.parser')
    for td in soup.find_all("td", class_='lyf_td_filename'):  # new way of iterating without 'null-ing'? BS 'Any'(type))
        a = td.find('a')  # presetting <a> by selecting(each) from td(iterated)
        if QUERY in str(a['href']):  # simple condition filter
            groupTitle = a.getText()
            groupURL = a.get('href')
            resultDict[groupTitle] = groupURL
    return resultDict


def printResults(inDict):  # print results from given dict
    """
    prints results from a given dict, that was created and downloaded by past fct.

    :param dict inDict : parsed dict
    """
    students = 0  # contor de studenti
    for gTitle in inDict:
        fPath = 'files/' + gTitle
        print('grupa ' + gTitle.split()[1])
        print(str(cellToInt(xlsxParse(fPath))) + ' studenti\n')
        students += cellToInt(xlsxParse(fPath))
        # remove(fPath)
    print('total studenti la Facultatea aleasa: ' + str(students))


# todo ------------------- Main
# this is the way to call all functions, could mash in one base fct

newDict = resultCalculatorV5("")  # create dict
dictDownloadV5(newDict)  # donwload dict
printResults(newDict)  # print results

driver.quit()
