import sys
import json

afinnfile = open(sys.argv[1])
scores = {} # initialize an empty dictionary
for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.


def get_sentiment_score(s):

    score = 0
    terms = s.split()
    for term in terms:
        if term in scores:
            score += scores[term]
    return score


tweet_file = open(sys.argv[2])
def get_tweets(file):
    for line in file.readlines():
        line = line.encode('utf-8')
        tweet = json.loads(line)
        if 'text' in tweet:
            tweet_text = tweet['text']
            score = get_sentiment_score(tweet_text)
        else:
            tweet_text = ''
            score = 0
        print score 


if __name__ == '__main__':
    get_tweets(tweet_file)
