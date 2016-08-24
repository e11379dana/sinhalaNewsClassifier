

class stemm(object):

    def stemminig(doc) :
        doc.sort()
        list = []
        list = doc
        i = 0
        print("list length ==========="+str(len(list)))
        same = []

        while (i < len(list)):
            j = i + 1
            while (j < len(list)):
                u = zip(list[i], list[j])
                d = dict(u)
                x=[]
                for k,m in d.items():
                    if k == m:
                        x.append(j)
                p =len(x)/len(d)
                if p > 0.5:
                    print(doc[i] +" = "+doc[j])
                    del list[j]
                    j -= 1
                j += 1
            i+=1
        n = 0
        while (n < len(list)):
            print('@@@@@@@@@@@@'+list[n])
            n += 1