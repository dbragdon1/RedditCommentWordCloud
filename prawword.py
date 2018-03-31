from __future__ import print_function
import praw
import numpy as np
import matplotlib.pyplot as plt
from os import path
from PIL import Image
from wordcloud.wordcloud import WordCloud

#Turn the image into something that numpy can work with
d = path.dirname(__file__)
pictureToMask = np.array(Image.open(path.join(d, "myimage.JPG")))

#Initialize your word cloud
#Set background color and mask
myWordCloud = WordCloud(background_color="white", \
                        mask = pictureToMask)

#Fill in the info for your PRAW bot
#Each line here should be given to you when you request to make a bot on reddit
mybot = praw.Reddit(client_id='your client ID', \
                     client_secret='your secret value', \
                     user_agent='your bot name', \
                     username='your reddit account', \
                     password='your password')

#Thread of your choice
#Each thread has a string of characters in the link, known as the thread's ID.
#You can also directly paste the whole link into the parentheses
targetThread = mybot.submission(id='889wtl')

#Uncomment the following line if you would like to create a new stop word
#Stop words will not show up in the word cloud
#myWordCloud.stopwords.add('enter word as a string here')

#instantiate the list that will hold all of the comments in the thread
commentList = []

#PRAW's notation for parsing the entire thread
from praw.models import MoreComments
for top_level_comment in targetThread.comments:
    try:
        if isinstance(top_level_comment, MoreComments):
            continue
        commentList.append(top_level_comment.body)
        with open('index.txt', 'a') as sourceText:
            sourceText.write(top_level_comment.body)
    except UnicodeEncodeError:
        pass

#Join all of the comments into one string
commentsstring = ' '.join(commentList).lower()

#The following lines of code generate and present the word cloud
#The word cloud is visualized using matplotlib
myWordCloud.generate(commentsstring)
plt.figure()
plt.imshow(myWordCloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#Uncomment the bottom line if you would like to save the image to a file
#myWordCloud.to_file("myfile")