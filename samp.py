from mrjob.job import MRJob

import re

WORD_RE = re.compile(r"[\w']+")

i=[]
tot=[]
yyy=[]
def functi(item):
        shortd=0.0
        longd=0.0
        shortt=0
        longt=0
        nos=0
        for x in item:
                #total+=x
                nos+=1
                if x >35:
                        longt+=1
                        longd+=x
                else:
                        shortt+=1
                        shortd+=x

        return nos,shortt,shortd,longt,longd


class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
 
        values=line.split(",")
        value=0.0
        #if not values[9].isalpha():
        value=float(values[9])
        yield(values[2],float(value))


    def combiner(self, word, counts):
#       j=[]
        #countt=functi(counts)
#        j.append(count)
##      x=functi(counts)
        nos,st,sd,lt,ld=functi(counts)
#       tot,yyy= (k,(word,avg,total))
#       yield(word,sum(counts))
  #  def reducer(self, word, counts):
        yield (word,(nos,st,sd,lt,ld))
#       def come(self,abc,x):
#            light = (max(x),abc)
#             print light
#       yield(word,sum(counts))                         


if __name__ == '__main__':
     MRWordFreqCount.run()