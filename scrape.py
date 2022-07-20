from selenium import webdriver
import pandas as pd

browser = webdriver.Chrome()

df = pd.read_excel('Warehouse_shipper_sample.xlsx', usecols=['Location','Map '])

lat = []
def maps(urls):
    browser.get(urls)
    for i in browser.find_elements_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/h2/span'):
        lat.append(i.text)
    df1 = pd.DataFrame(lat)
    df1.to_csv('lat.csv')

for x in df['Map ']:
    maps(x)


browser.quit()

