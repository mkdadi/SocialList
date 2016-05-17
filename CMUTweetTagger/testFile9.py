import CMUTweetTagger as cmu
import wordsegment as ws

def test9(idiomset,postags,scount):
    i=0
    stags=0
    itags=0
    for line, idiom in zip(postags, idiomset):
        postagsent = " ".join(line)
        if ('R' in postagsent) and idiom[1] == '1':
            stags+=1
        elif ('R' in postagsent) and idiom[1] == '0':
            itags+=1
        i+=1

    print "Probablity of Social Lists containing Adverbs is ",str(stags)+'/'+str(scount),str(float(stags)/scount)
    print "Probablity of Non-Social Lists containing Adverbs is ",str(itags)+'/'+str(i-scount),str(float(itags)/(i-scount))