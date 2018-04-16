import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)


afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.


def get_sentiment_score(s):
    terms = s.split()
    score = 0
    for term in terms:
        if term in scores:
            score += scores['term']
    return score


def get_tweets(file):
    for line in file.readlines():
        tweet = json.loads(line)
        if 'text' in tweet:
            tweet_text = tweet['text']
            score = get_sentiment_score(tweet_text)
        else:
            tweet_text = ''
            score = 0
        print score # and save to a file


if __name__ == '__main__':
    main()
