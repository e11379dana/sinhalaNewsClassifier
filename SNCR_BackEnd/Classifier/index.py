import schedule
import time
from MNBclassifier import *

def schedulRunner():
    clssifier = MultinomialNBClassifier()
    clssifier.classify()

schedule.every(0.1).minutes.do(schedulRunner)

while 1:
    schedule.run_pending()
    time.sleep(0.1)