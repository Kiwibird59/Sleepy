
""" ######################################################################################################################################################
    Class Tweet is capable of creating a tweet object with the following properties:                                                                     #
    Attributes:                                                                                                                                          #
	text(str)		The tweet itself                                                                                                                     #
	coord(list)		Give the coordinates from where the tweet originates, if specified                                                                   #
	score(int)		It is a score given to the quality of the sleep that a user has experienced. Parsed from text if user uses the hashtag #SeelpeHealth.#
					Else it is inferred from the text using sentiment analysis. Ranges from 0 to 10. Score of -1 is the default value indicating that    #
					SleepeHealth hashtag has not been used                                                                                               #
	datetime(str)	Gives the date, time and timezone                                                                                                    #
	lang(str)		Indicates language if the tweet if specified                                                                                         #
	hash(dict)		Dictionary with keys representing hashtags if used                                                                                   #
	                                                                                                                                                     #
	Methods:                                                                                                                                             #
	__str__			For pretty printing                                                                                                                  #
	get methods		To access attributes                                                                                                                 #
	set_score		To set calculated sleep score                                                                                                        #
	                                                                                                                                                     #
    Version History:                                                                                                                                     #
    Created by: Rishabh Agnihotri 10/05/2013 (MM/DD/YYYY)                                                                                                #
    Modified by:                                                                                                                                         #
###################################################################################################################################################### """


class Tweet:

    def __init__(self, text, coord, datetime, lang, hash):
        self.text = text
        self.coord = coord
        self.datetime = datetime
        self.lang = lang
        self.hash = hash
        self.phase = None
        self.raw_score = None
        self.Z_score = None
    
    def __str__(self):
        # if self.hash != None:
        s  = 'Text: ' + self.text.encode('utf-8') + '. '
        if self.coord != None:
            s += 'Coordinates: ' + str(self.coord[0]) + ' ,' + str(self.coord[1]) + '. '
        else:
            s += 'Coordinates: Not Specified. '
        s += 'Time: ' + self.datetime.encode('utf-8') + '.'
        s += 'Language: ' + self.lang.encode('utf-8') + '.'
        s += 'Hashtag: ' + str(self.hash) + '.'
        s += 'Score:' + str(self.score) + '.'
        return s

    def get_text(self):
        return self.text

    def get_coord(self):
        return self.coord

    def get_text(self):
        return self.text

    def get_score(self):
        return self.score

    def get_datetime(self):
        return self.datetime

    def get_lang(self):
        return self.lang

    def get_hash(self):
        return self.hash

    def get_raw_score(self):
        return self.raw_score

    def get_Z_score(self):
        return self.Z_score

    def get_phase(self):
        return self.phase

    def calculate_raw_score(self, word_list, word_dict):
        self.raw_score =  sum([word_dict[word] for word in word_list if word_dict.has_key(word)])

    def calculate_phase(self, phase_dict, phase_list):
        day, mon, date, time, tz, year = self.datetime.split()
        thresh_dates = [x for x in phase_dict[mon].keys()]
        thresh_dates.sort()
        for thresh in thresh_dates:
            if int(date) < thresh:
                self.phase = phase_list[phase_dict[mon][thresh]-1]
                break;
            elif int(date) == thresh:
                self.phase = phase_list[phase_dict[mon][thresh]]
                break;