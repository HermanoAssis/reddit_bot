import praw
import random
import time

reddit = praw.Reddit(
    client_id="jT-FuG5lQwo4__MgQR0m-w",
    client_secret="duKcELgsBbhi4VN-Q64bemP3mgtRvw",
    user_agent="<console:ELDENRING:1.0>",
    username="elden-ring-bot",
    password="MicksGG156"
)

subreddit = reddit.subreddit("Eldenring")

eldenring_quotes = ["O, Dearest Miquella, My brother...I'm Sorry. I Finally Met My Match… - Malenia, Blade of Miquella",
                    "Thank You, From The Bottom Of My Heart. I'm Sure I'll Be A Finger Maiden. - Lightseeker Hyetta",
                    "Victory Was Impossible… This Vessel Was Found Lacking… But The Great Alexander Lived As A Warrior To His Last! - Iron Fist Alexander",
                    "Quite A Lot Of Us Got Broken... I Won't Cry Thought... I'm A Warrior Jar! Even If I'm Scared, I'll Still Fight To Protect Everyone. - Jar Bairn"]

for submission in subreddit.hot(limit=10):
    # print('----------------')
    # print(submission.title)   
    
    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " hard " in comment_lower:
                print('----------')
                print(comment.body)
                random_index = random.randint(0, len(eldenring_quotes) - 1)
                comment.reply(eldenring_quotes[random_index])
                time.sleep(660)