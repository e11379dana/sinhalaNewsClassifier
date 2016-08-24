from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


class MultinomialNBClassifier:

    def classify(self, text):

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

        # Reading testing data file
        with open('newsGroups\classify.txt', 'r') as myfile:
            news=myfile.read().replace('\n', '')

        return clf.predict(vectorizer.transform([text]))
