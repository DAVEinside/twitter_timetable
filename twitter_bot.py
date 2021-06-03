import tweepy
import  time

consumer_key = '<secret_consumer_key>'
consumer_secret = '<secret_consumer>'
access_token = '<secret_access_token>'
access_token_secret = '<secret_access_token_secret>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


time_table = {
        'monday' :{"9:30" : 'Department Elective',
                   '10:30': 'A1 EC-Lab, A2 TOM-Lab, A3 MCT-Lab, A4 IE-Lab',
                   '11:30': 'A1 EC-Lab, A2 TOM-Lab, A3 MCT-Lab, A4 IE-Lab',
                   '12:30':'Break',
                   '1:15':'EC-Lecture',
                   '2:15':'MCT-Lecture',
                   '3:15':'TOM-Lecture'},
        'tuesday' :{"9:30" : 'Department Elective',
                   '10:30': 'A1 TOM-Lab, A2 MCT-Lab, A3 IE-Lab, A4 EC-Lab',
                   '11:30': 'A1 TOM-Lab, A2 MCT-Lab, A3 IE-Lab, A4 EC-Lab',
                   '12:30':'Break',
                   '1:15':'EC-Lecture',
                   '2:15':'MCT-Lecture',
                   '3:15':'TOM-Lecture'},
        'wednesday':{"9:30" : 'Open Elective Humanities',
                   '10:30': 'Open Elective Technical',
                   '11:30': 'IE-Lecture',
                   '12:30':'Break',
                   '1:15':'A1 IE-Lab, A2 EC-Lab, A3 TOM-Lab, A4 MCT-Lab',
                   '2:15':'A1 IE-Lab, A2 EC-Lab, A3 TOM-Lab, A4 MCT-Lab',
                   '3:15':'MCT-Lecture'},
        'thursday':{"9:30" : 'Open Elective Humanities',
                   '10:30': 'Open Elective Technical',
                   '11:30': 'No Lecture',
                   '12:30':'Break',
                   '1:15':'EC-Lecture',
                   '2:15':'TOM-Lecture',
                   '3:15':'Department Elective Practicals Only CFD',
                   '4:15':'Department Elective Practicals Only CFD'},
        'friday':  {"9:30" : 'Department Elective',
                   '10:30': 'Open Elective Technical',
                   '11:30': 'Mandatory Non-Credit Course',
                   '12:30':'Break',
                   '1:15':'Department Elective Practicals Except CFD',
                   '2:15':'Department Elective Practicals Except CFD',
                   '3:15':'A1 MCT-Lab, A2 IE-Lab, A3 EC-Lab, A4 TOM-Lab',
                   '4:15':'A1 MCT-Lab, A2 IE-Lab, A3 EC-Lab, A4 TOM-Lab'}
    }


FILE_NAME = 'last_seen_id.txt'


def retrieve_last_seen_id(file_name):
    f_read  =open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def time_table_bot():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(last_seen_id)


    for mention in reversed(mentions):
        tweet = mention.text.split()

        last_seen_id = mention.id
        store_last_seen_id(last_seen_id,FILE_NAME)
        if len(tweet) == 3:
            user = tweet[0]
            Day = tweet[1].lower()
            time = tweet[2]
            print(mention.id)
            print(Day, time)
            print(time_table[Day][time])
            print(mention.text)
            api.update_status('@' + mention.user.screen_name + " " +
                              time_table[Day][time], mention.id)


while True:
    time_table_bot()
    time.sleep(10)