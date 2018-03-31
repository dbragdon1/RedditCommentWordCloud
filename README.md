# Reddit Comment Word Cloud Generator

prawword.py scrapes all of the comments from a reddit thread using **PRAW**, then creates a word cloud using the **WordCloud** library. </br>

The word cloud is shaped by whatever mask you choose to overlay it with, so I suggest using a larger image as a mask. Otherwise, the wordcloud might come out looking very blurry. </br> </br>

I also included (but commented out) the line to save the word cloud to a file type of your choice.</br> </br>
If certain words are showing up in your word cloud that you don't want, I suggest using the **stopwords** feature from the **WordCloud** library. I have also left this line commented out in prawword.py, but you'll have to create a new line for every word you wish to comment out. </br> </br>
**PRAW Documentation:** https://praw.readthedocs.io/en/latest/ </br>
</br>
**WordCloud Documentation:** https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html </br>
