import io

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from SNCR_BackEnd.Aggregator.DAO import *

class MultinomialNBClassifier:

    def classifier(self, text):

        #instantiate classifier and vectorizer
        clf=MultinomialNB(alpha=.01)
        vectorizer =TfidfVectorizer(min_df=1,ngram_range=(1,2))

        # Reading trining data files
        with open('newsGroups\sport.txt', 'r') as myfile:
            sport=myfile.read().replace('\n', '')

        with open('newsGroups\defence.txt', 'r') as myfile:
            defence=myfile.read().replace('\n', '')

        with open('newsGroups\culture.txt', 'r') as myfile:
            culture = myfile.read().replace('\n', '')

        with open('newsGroups\politics.txt', 'r') as myfile:
            politics = myfile.read().replace('\n', '')

        with open('newsGroups\economy.txt', 'r') as myfile:
            economy = myfile.read().replace('\n', '')

        #Apply vectorizer to training data

        traindata=[sport,defence,economy,culture,politics];
        X_train=vectorizer.fit_transform(traindata)

        #Label Ids
        # sport = 0
        # defence = 1
        # economy = 2
        # culture = 3
        # politics = 4
        y_train=[0,1,2,3,4];

        #Train classifier
        clf.fit(X_train, y_train)


        return clf.predict(vectorizer.transform([text]))

    def classify(self):

        dao = DAO();
        # Get IDs of uncatergerized news to uncatNewsList
        uncatNewsList = dao.selectUncategerizedNews();
        for news in uncatNewsList:

            description = dao.getDescriptionById(news[0])

            wf = io.open('news.txt', 'w', encoding='utf-8')
            x = description[0][0]
            wf.write(x)
            rf = io.open('news.txt', 'r', encoding='utf-8').read()

            category = MultinomialNBClassifier().classifier(rf)
            dao.updateNews(news[0],category[0])
