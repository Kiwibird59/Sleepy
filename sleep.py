import json
import sys
from Tweet import *
from helper import create_afinn_dict, MOON_PHASE, MOON_DICT_13

""" Parses a single tweet at a time and creates a tweet object with the relevant information
"""
def create_tweet_objects():

    tweets_json = open(sys.argv[1])
    tweet_list = []
    t_text = None
    t_coord = None
    t_datetime = None
    t_lang = None
    AFINN_DICT = create_afinn_dict()
    
    # Code to parse and collect all non derived attributes of a tweet. eg. text, datetime, language, etc
    for jtweet in tweets_json:
        ptweet = json.loads(jtweet)
        if ptweet.has_key('text'):
            #parsing the tweet for trigger words in ['sleep', 'sleeping', 'slept'] ,calculating a sentiment score and extracting other meta data.
            word_list_raw = ptweet['text'].split()
            word_list = [word.strip('!@#$%^&*,?.').lower() for word in word_list_raw]
            
            if 'sleep' in word_list or 'sleeping' in word_list or 'slept' in word_list:
                t_score = sum([AFINN_DICT[word] for word in word_list if AFINN_DICT.has_key(word)])
            
                try:
                    t_coord = ptweet['coordinates']['coordinates']
                except:
                    t_coord = None
            
                try:
                    t_datetime = ptweet['created_at']
                except:
                    t_datetime = None
            
                try:
                    t_lang = ptweet['lang']
                except:
                    t_lang = None
            
                try:
                    t_hash = ptweet['entities']['hashtags']
                except:
                    t_hash = None
            
                tweet_object = Tweet(ptweet['text'], t_coord, t_datetime, t_lang, t_hash) #creating tweet object
                #Calculating derived attributes
                tweet_object.calculate_raw_score(word_list, AFINN_DICT)
                tweet_object.calculate_phase(MOON_DICT_13, MOON_PHASE)
                #Adding tweet_object to a list
                tweet_list.append(tweet_object)
    return tweet_list

def main():
    tweet_list = create_tweet_objects()
    print len(tweet_list)
    # for tweet in tweet_list:
        # print str(tweet.get_raw_score()), tweet.get_text().encode('utf-8')
        # print tweet.get_datetime(), tweet.get_phase()
    #writing to file
    analysis_file = open('analysis.txt', 'w')
    analysis_file.write('MOON_PHASE RAW_SCORE' + '\n')
    for tweet in tweet_list:
        analysis_file.write(tweet.get_phase() + ' ' + str(tweet.get_raw_score()) + '\n')
        # analysis_file.write('\n')
    analysis_file.close()

if __name__ == '__main__':
    main()