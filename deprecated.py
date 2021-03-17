# todo headers start
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains as ac
from bs4 import BeautifulSoup as bs
import requests as req

DRIVER_PATH = "G:\\_Local\\Programming\\Python\\API's\\Reeves\\chromedriver"
DOWNLOAD_PATH = "/downloads"
BASE_URL = "http://www.cs.xxxxxx.ro/studenti/lista-studentilor/"

options = Options()  # init chrome options
options.headless = True  # toggles background run mode
options.add_argument("--window-size=1920,1080")  # runs in full hds mode? why? idgaf honestly
prefs = {'download.default_directory': DOWNLOAD_PATH}  # separating experimental options as dictionary type works? why?
options.add_experimental_option('prefs', prefs)  # adding the chrome default download directory as a ChromeOption
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)  # initializing chromedriver(selenium) with opts


# ------------------------------ update above!!!

# todo -------------------- I won't delete deprecated functions, might need them for bugfixing

def resultCalculatorV1():  # (badly obsolete) - prints excel file list of every math-cs group
    driver.get(BASE_URL)  # using chromedriver (selenium) to get navigate to BASE_URL
    soup = bs(driver.page_source, 'html.parser')  # generating soup using BS html.parser (python special)
    findsList = soup.find_all("td", class_='lyf_td_filename')  # filter 1 - simple td select (deprecated version)
    findsList = [el.find('a') for el in findsList if 'matematica-informatica' in str(el.find('a')['href'])]  # filter 2
    for i, agroup in enumerate(findsList):  # iterating filtered list
        groupTitle = agroup.getText()  # parsing text from html tag iterated -  Any(type).getText . (bs class?)
        groupURL = agroup.get('href')  # generating URL based on href attribute of <a> (html)
        print(f'{i} : {groupTitle} :{groupURL}')  # generating/printing result using fstring formatting and parsed data


def resultCalculatorV2():  # 3 days of learning BS - prints/downloads excel file of every math-cs group
    driver.get(BASE_URL)
    soup = bs(driver.page_source, 'html.parser')
    for td in soup.find_all("td", class_='lyf_td_filename'):  # new way of iterating without 'null-ing'? BS 'Any'(type))
        a = td.find('a')  # presetting <a> by selecting(each) from td(iterated)
        if 'matematica-informatica' in str(a['href']):  # simple condition filter
            groupTitle = a.getText()
            groupURL = a.get('href')
            print(f'{groupTitle} :{groupURL}')  # no need to enumerate, it would just be dumping shit on the code


def resultCalculatorV3():  # 3 days of learning BS - prints/downloads excel file of every math-cs group
    driver.get(BASE_URL)
    soup = bs(driver.page_source, 'html.parser')
    for td in soup.find_all("td", class_='lyf_td_filename'):  # new way of iterating without 'null-ing'? BS 'Any'(type))
        a = td.find('a')  # presetting <a> by selecting(each) from td(iterated)
        if 'matematica-informatica' in str(a['href']):  # simple condition filter
            groupTitle = a.getText()
            groupURL = a.get('href')
            # fDownV3(groupTitle, groupURL)
            print(f'{groupTitle} :{groupURL}')  # no need to enumerate, it would just be dumping shit on the code


def fileDownloaderV2(url):  # deprecated (for project use) same as v1?
    request = req.get(url, allow_redirects=True)  # fuck me this might be the driver caller
    filename = url.rsplit('/', 1)[1]  # filename - until the first '/' is found, using splitter
    open(filename, 'wb').write(request.content)
    # exactly what the fuck does 'wb' mean, guess the rest is simply open raw then save text contents? with given name


def fDownV3(filename, url):  # removed filename getter, set it as function parameter
    request = req.get(url, allow_redirects=True)
    open(filename, 'wb').write(request.content)


def elemClickerV1(driverGet, element):  # trying to click url? version 1
    ac(driverGet).move_to_element(element).click(element).perform()  # wagon-ing selenium usage commands to navigate


# elemClicker was fully deprecated

def resultCalculatorV4():  # 4'th day of learning BS - prints/downloads excel file of every math-cs group
    resultDict = {}
    driver.get(BASE_URL)
    soup = bs(driver.page_source, 'html.parser')
    for td in soup.find_all("td", class_='lyf_td_filename'):  # new way of iterating without 'null-ing'? BS 'Any'(type))
        a = td.find('a')  # presetting <a> by selecting(each) from td(iterated)
        if 'matematica-informatica' in str(a['href']):  # simple condition filter
            groupTitle = a.getText()
            groupURL = a.get('href')
            resultDict[groupTitle] = groupURL
    return resultDict


def resultCalculatorWholeUni():  # get all students from UNI
    resultDict = {}
    driver.get(BASE_URL)
    soup = bs(driver.page_source, 'html.parser')
    for td in soup.find_all("td", class_='lyf_td_filename'):  # new way of iterating without 'null-ing'? BS 'Any'(type))
        a = td.find('a')  # presetting <a> by selecting(each) from td(iterated)
        groupTitle = a.getText()
        groupURL = a.get('href')
        resultDict[groupTitle] = groupURL
    return resultDict


def resultCalculatorGerm():  # Get students learning in German
    resultDict = {}
    driver.get(BASE_URL)
    soup = bs(driver.page_source, 'html.parser')
    for td in soup.find_all("td", class_='lyf_td_filename'):  # new way of iterating without 'null-ing'? BS 'Any'(type))
        a = td.find('a')  # presetting <a> by selecting(each) from td(iterated)
        if 'germana' in str(a['href']):  # simple condition filter
            groupTitle = a.getText()
            groupURL = a.get('href')
            resultDict[groupTitle] = groupURL
    return resultDict


# deprecated by replacing with only one working fuction that uses a parameter

def fDownV4(filename, url):  # removed filename getter, set it as function parameter
    request = req.get(url, allow_redirects=True)
    path = "G:\\_Local\\Programming\\Python\\API's\\stdList\\files\\" + filename
    with open(path, 'wb') as f:
        f.write(request.content)


def dictDownload(dic):
    for grTitle in dic:
        fDownV4(grTitle, dic[grTitle])


# deprecated downloads

def fileCalc(line):
    file1 = open('myfile.txt', 'r')
    lines = file1.readlines()
    new = lines[line].split('; |, |\*|\n')
    print(new)
    fileCalc(line + 1)
# never used recursive function
