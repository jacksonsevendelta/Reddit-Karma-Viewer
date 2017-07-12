# Reddit Karma Viewer
### Copyright (c) @jacksonsevendelta (aka [u/gadkaris](https://reddit.com/u/gadkaris))

*note: **will only work using Python 2x.** This comes default on most Raspbian images, so you should be fine.*

## Reddit PRAW Interface Instructions
1. Go to https://reddit.com/prefs/apps
2. Scroll to the bottom
    - Click "create another app"/"create app"
    - Select the `script` radio button
    - Enter a name (any name)
    - You can put anything in the description.
    - In the "about url"/"redirect uri" text boxes you will have to put a valid URL in both of them. You can use https://example.com.

3. Click `Create App`
    - You should now see something like [this.](http://imgur.com/a/rebym)
    - Copy down the `client ID` (in the top right under `personal use script`) and your `secret`.

4. Replace `<YOUR CLIENT ID HERE>` and `<YOUR CLIENT SECRET HERE>` with the appropriate values in karmaviewer.py before running it.
