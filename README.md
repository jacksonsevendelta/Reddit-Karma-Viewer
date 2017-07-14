# Reddit Karma Viewer
### Copyright © @jacksonsevendelta (aka [u/gadkaris](https://reddit.com/u/gadkaris))

This code will only work under Python 2x. Python 3 and later is not supported, however, you may edit the code yourself to make it Python 3x compatible. If you do, please fork this project so others can benefit from your program.

## Reddit PRAW Interface Instructions
1. In a terminal, run `sudo pip install --upgrade praw`
    - This will both install PRAW (the Python Reddit API Wrapper) or, if it's already installed, update it.
    - If you ever get the message `Version X.X.X of praw is outdated. Version X.X.X was released X days ago.` run the command again.
2. Go to https://reddit.com/prefs/apps
3. Scroll to the bottom
    - Click "create another app"/"create app"
    - Select the `script` radio button
    - Enter a name (any name)
    - You can put anything in the description.
    - In the "about url"/"redirect uri" text boxes you will have to put a valid URL in both of them. You can use any URL you like, however.

4. Click `Create App`
    - You should now see something like [this.](http://imgur.com/a/rebym)
    - Copy down the `client ID` (in the top right under `personal use script`) and your `secret`.

5. Replace `<YOUR CLIENT ID HERE>` and `<YOUR CLIENT SECRET HERE>` with the appropriate values in [karmaviewer.py](https://github.com/jacksonsevendelta/Reddit-Karma-Viewer/karmaviewer.py) before running it.

## Wiki Pages
[Home](https://github.com/jacksonsevendelta/RedditKarmaViewer/wiki)  
[DEMO](https://github.com/jacksonsevendelta/RedditKarmaViewer/wiki/DEMO)  

## License Information

*The code for this program is copyright © 2017 @jacksonsevendelta. Under the MIT License, you may distribute the software if you give credit to the creator (@jacksonsevendelta), use the same license to distribute it, and accept liability for any damage occurred.*

Click [here](https://github.com/jacksonsevendelta/RedditKarmaViewer/blob/master/LICENSE) to view the full license.

