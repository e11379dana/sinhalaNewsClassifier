from __future__ import division


import json


class Classifier:
    __spamKB = {}
    __hamKB = {}
    __jamKB = {}
    __pamKB = {}
    __tamKB = {}

    def __init__(self, spamKB, hamKB, jamKB, pamKB, tamKB):
        self.__hamKB = hamKB
        self.__jamKB = jamKB
        self.__spamKB = spamKB
        self.__pamKB = pamKB
        self.__tamKB = tamKB

    def __prob_of_sms_being_spam(self):

        spam_key_count = len(self.__spamKB.items())
        ham_key_count = len(self.__hamKB.items())
        jam_key_count = len(self.__jamKB.items())
        pam_key_count = len(self.__pamKB.items())
        tam_key_count = len(self.__tamKB.items())
        return spam_key_count / (spam_key_count + ham_key_count + jam_key_count + pam_key_count + tam_key_count)

    def __prob_of_sms_being_ham(self):

        spam_key_count = len(self.__spamKB.items())
        ham_key_count = len(self.__hamKB.items())
        jam_key_count = len(self.__jamKB.items())
        pam_key_count = len(self.__pamKB.items())
        tam_key_count = len(self.__tamKB.items())

        return spam_key_count / (spam_key_count + ham_key_count + jam_key_count + pam_key_count + tam_key_count)

    def __prob_of_sms_being_jam(self):

        spam_key_count = len(self.__spamKB.items())
        ham_key_count = len(self.__hamKB.items())
        jam_key_count = len(self.__jamKB.items())
        pam_key_count = len(self.__pamKB.items())
        tam_key_count = len(self.__tamKB.items())

        return spam_key_count / (spam_key_count + ham_key_count + jam_key_count + pam_key_count + tam_key_count)

    def __prob_of_sms_being_pam(self):

        spam_key_count = len(self.__spamKB.items())
        ham_key_count = len(self.__hamKB.items())
        jam_key_count = len(self.__jamKB.items())
        pam_key_count = len(self.__pamKB.items())
        tam_key_count = len(self.__tamKB.items())

        return spam_key_count / (spam_key_count + ham_key_count + jam_key_count + pam_key_count + tam_key_count)

    def __prob_of_sms_being_tam(self):

        spam_key_count = len(self.__spamKB.items())
        ham_key_count = len(self.__hamKB.items())
        jam_key_count = len(self.__jamKB.items())
        pam_key_count = len(self.__pamKB.items())
        tam_key_count = len(self.__tamKB.items())

        return spam_key_count / (spam_key_count + ham_key_count + jam_key_count + pam_key_count + tam_key_count)

    def prob_of_word_being_spam(self, word):

        v = len(list(self.__spamKB.keys()) + list(self.__hamKB.keys()) + list(self.__jamKB.keys()) + list(self.__pamKB.keys()) +list(self.__tamKB.keys())) - 1

        count_w_c = 0

        if word in self.__spamKB:
            count_w_c = int(self.__spamKB[word])

        count_c = int(sum(self.__spamKB.values()))

        p = (count_w_c + 1) / (count_c + v)
        return p

    def prob_of_word_being_ham(self, word):

        v = len(list(self.__spamKB.keys()) + list(self.__hamKB.keys()) + list(self.__jamKB.keys()) + list(self.__pamKB.keys()) + list(self.__tamKB.keys())) - 1

        count_w_c = 0

        if word in self.__hamKB:
            count_w_c = int(self.__hamKB[word])

        count_c = int(sum(self.__hamKB.values()))

        p = (count_w_c + 1) / (count_c + v)
        return p

    def prob_of_word_being_jam(self, word):

        v = len(list(self.__spamKB.keys()) + list(self.__hamKB.keys()) + list(self.__jamKB.keys()) + list(self.__pamKB.keys())+list(self.__tamKB.keys())) - 1

        count_w_c = 0

        if word in self.__jamKB:
            count_w_c = int(self.__jamKB[word])

        count_c = int(sum(self.__jamKB.values()))

        p = (count_w_c + 1) / (count_c + v)
        return p

    def prob_of_word_being_pam(self, word):

        v = len(list(self.__spamKB.keys()) + list(self.__hamKB.keys()) + list(self.__jamKB.keys()) + list(self.__pamKB.keys())+list(self.__tamKB.keys())) - 1

        count_w_c = 0

        if word in self.__pamKB:
            count_w_c = int(self.__pamKB[word])

        count_c = int(sum(self.__pamKB.values()))

        p = (count_w_c + 1) / (count_c + v)
        return p

    def prob_of_word_being_tam(self, word):

        v = len(list(self.__spamKB.keys()) + list(self.__hamKB.keys()) + list(self.__jamKB.keys()) + list(self.__pamKB.keys())+list(self.__tamKB.keys())) - 1

        count_w_c = 0

        if word in self.__tamKB:
            count_w_c = int(self.__tamKB[word])

        count_c = int(sum(self.__tamKB.values()))

        p = (count_w_c + 1) / (count_c + v)
        return p

    def __sms_spam_prob(self, sms):
        p = 1
        # tokens = [x for x in sms.split(' ') if x]
        tokens = sms.split(' ')

        for word in tokens:
            p *= self.prob_of_word_being_spam(word)

        p *= self.__prob_of_sms_being_spam()

        return p

    def __sms_ham_prob(self, sms):
        p = 1
        # tokens = [x for x in sms.split(' ') if x]
        tokens = sms.split(' ')

        for word in tokens:
            p *= self.prob_of_word_being_ham(word)

        p *= self.__prob_of_sms_being_ham()

        return p

    def __sms_jam_prob(self, sms):
        p = 1
        # tokens = [x for x in sms.split(' ') if x]
        tokens = sms.split(' ')

        for word in tokens:
            p *= self.prob_of_word_being_jam(word)

        p *= self.__prob_of_sms_being_jam()

        return p
    def __sms_pam_prob(self, sms):
        p = 1
        # tokens = [x for x in sms.split(' ') if x]
        tokens = sms.split(' ')

        for word in tokens:
            p *= self.prob_of_word_being_pam(word)

        p *= self.__prob_of_sms_being_pam()

        return p

    def __sms_tam_prob(self, sms):
        p = 1
        # tokens = [x for x in sms.split(' ') if x]
        tokens = sms.split(' ')

        for word in tokens:
            p *= self.prob_of_word_being_tam(word)

        p *= self.__prob_of_sms_being_tam()

        return p

    def is_spam(self, sms):

        s = self.__sms_spam_prob(sms)
        h = self.__sms_ham_prob(sms)
        j = self.__sms_jam_prob(sms)
        k = self.__sms_pam_prob(sms)
        l = self.__sms_tam_prob(sms)

        p = s / (s + h + j + k +l) * 100

        if s >= h and s >= j and s>=k and s>=l:
            return {'result': True, 'probability': p}
        return {'result': False, 'probability': p}

    def is_ham(self, sms):

        s = self.__sms_spam_prob(sms)
        h = self.__sms_ham_prob(sms)
        j = self.__sms_jam_prob(sms)
        k = self.__sms_pam_prob(sms)
        l = self.__sms_tam_prob(sms)

        p = h / (s + h + j +k +l) * 100
        if h >= s and h >= j and h>=k and h>=l:
            return {'result': True, 'probability': p}
        return {'result': False, 'probability': p}

    def is_jam(self, sms):

        s = self.__sms_spam_prob(sms)
        h = self.__sms_ham_prob(sms)
        j = self.__sms_jam_prob(sms)
        k = self.__sms_pam_prob(sms)
        l = self.__sms_tam_prob(sms)

        p = j / (s + h + j +k +l) * 100

        if j >= s and j >= h and j>=k and j>=l:
            return {'result': True, 'probability': p}
        return {'result': False, 'probability': p}

    def is_pam(self, sms):

        s = self.__sms_spam_prob(sms)
        h = self.__sms_ham_prob(sms)
        j = self.__sms_jam_prob(sms)
        k = self.__sms_pam_prob(sms)
        l = self.__sms_tam_prob(sms)

        p = k / (s + h + j +k +l) * 100

        if k >= s and k >= h and k>=j and k>=l:
            return {'result': True, 'probability': p}
        return {'result': False, 'probability': p}

    def is_tam(self, sms):

        s = self.__sms_spam_prob(sms)
        h = self.__sms_ham_prob(sms)
        j = self.__sms_jam_prob(sms)
        k = self.__sms_pam_prob(sms)
        l = self.__sms_tam_prob(sms)

        p = l / (s + h + j +k +l) * 100

        if l >= s and l >= h and l>=j and l>=k:
            return {'result': True, 'probability': p}
        return {'result': False, 'probability': p}
