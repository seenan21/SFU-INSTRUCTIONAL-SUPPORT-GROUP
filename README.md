# SFU ISG

How to set up the website:

## Basic Config
- You can change footer content at the _config.yml
- You can change the logo that appears on the top left at _config.yml as well

## favicon

The code for the favicon is in the _includes folder named head_custom.html. For the favicon to be present in every page, you must ensure every doc is present in the root directory, not in any other subdirectory.

## Google analytics

To enable google analytics, go to head_custom.html in the _includes folder and replace the google measurement ID tag in the script with the ID of your Google analytics account.

## Disqus comments

To add and manage disqus comments at the bottom of course pages, you need to start up a disqus account. Afterwards, you must embed universal disqus html code in the part of the web page you want the comments to appear in. For example, look at the cmpt120resources.md code at the bottom.
You can simply follow these instructions: https://www.youtube.com/watch?v=Dr6pSdeJgkA 

You can set up moderation for the comments through your disqus site settings and also add other moderators for the site if necessary.