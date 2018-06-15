import praw

reddit = praw.Reddit(client_id='0GaWref38GyFzg',
                     client_secret='E_fIyNukK3fNRNcrvf2Epntw76o',
                     user_agent='TSVListChecker by /u/lordtuts')

subreddit = reddit.subreddit('SVExchange')

with open("tsvfile.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

f = open("tsvfile.txt", "a")

for submission in subreddit.new(limit=50):
    if len(submission.title) == 4:
        if (str(submission.title) + "\r\n") not in array:
            f.write(str(submission.title) + "\r\n")

f.close()
