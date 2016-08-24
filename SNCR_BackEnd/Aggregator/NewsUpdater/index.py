import schedule
import time

from SNCR_BackEnd.configSectionMap import *
from SNCR_BackEnd.Aggregator.NewsUpdater.newsUpdater import *

configSectionMap = ConfigSectionMap()
newsUpdater = newsUpdater()

def schedularRunner():


    sectionsArr = configSectionMap.GetConfigSections()
    for section in sectionsArr:
        link = configSectionMap.ConfigSectionMap(section)['link']
        newsContentClassName = configSectionMap.ConfigSectionMap(section)['newscontentclassname']
        imageClassName = configSectionMap.ConfigSectionMap(section)['imageclassname']

        newsUpdater.job(link,newsContentClassName, imageClassName, section)

schedule.every(0.1).minutes.do(schedularRunner)

while 1:
    schedule.run_pending()
    time.sleep(0.1)