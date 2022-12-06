# SFU ISG

How to set up the website and pre-requisites of knowleddge that should be known:

## Steps to Deploy the site:

- Create a public Github repository in which the website would be hosted from with your account
- Clone the repository 
- Copy all the html, markdown files and directories containing exam pdf files and etc. into the local remote repository as is, do not change the heirarchy of any of the directoires or files in relation to one another. Copy it as is.
- Commit and push all the changes
- Make sure you activate Github Pages for the repository and then the website should be up and running. Read more about it here: https://pages.github.com/

## Jekyll Theme and Github Pages

The deployment of this website relies heavily on the relationship between Jekyll and Github Pages, which can be read about here: https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll. There is no need to install Ruby or Jekyll on your local machine and we could derive the benefits of jekyll simply by using hosting our site through Github Pages. A good understanding of how Jekyll works and generates static pages and posts from markdown files using the Liquid templating language would help with modifying the theme and improving the site.

The theme that was chosen to be used for our website was the [Just The Docs theme](https://github.com/just-the-docs/just-the-docs). It is very simple and it allows for searching to quickly find what you are looking for in the website. You should go through the [Just The Docs documentations](https://just-the-docs.github.io/just-the-docs/) to understand how the pages for the webpage are to be structured, how to customize features and also how to use some of the UI components that comes with the theme.

### Overriding the Just The Docs Theme

For even greater customization, to change certain things that you do not like, the theme can be overrid, can be read about here: https://jekyllrb.com/docs/themes/. 

"To replace layouts or includes in your theme, make a copy in your `_layouts` or `_includes` directory of the specific file you wish to modify, or create the file from scratch giving it the same name as the file you wish to override."

Some of the styling of the theme has been modified and can be found in the custom.scss.liquid file found in the css directory in the `_includes` directory. This file can be used to override the different styling and css that is done all over the webpage, you just need to have good knowledge of Just The Docs theme from its repository and be able to figure out which CSS/SCSS selectors to use to style the specific element you wish to modify. 

The `_includes` directory also contains other HTML files that can be "included" into a page's header or footer, more on how it works can be read here: https://jekyllrb.com/docs/includes/. These HTML files can be included when creating the markdown files of the pages you are to make for the site. There are some already in the current `_includes` directory:

- toTopBtn.html allows for a button that is placed on the bottom right of the webpage that scrolls user to the top of the page when clicked on. Example can be seen when viewing the CMPT 120 page.
- 
- home_slides.html is just html code that allows for the an automatic slide show of pictures used for decoration of the home page.
- nav_footer_custom.thml allows for one to include custom text for the footer of the nav bar




## Basic Configuration and Structure

To understand how the static pages are generated with this theme, you must read the documentation: https://just-the-docs.github.io/just-the-docs/.

Some of the important things to learn:

- The YAML metadata on top of markdown files dictate how the page would appear on the navbar, the title of the page, the ordering it appears in the nav and whether the webpage has any children.
- You can change footer content at the _config.yml
- You can change the logo that appears on the top left at _config.yml as well.
- You can choose to have a table of contents for your page if necessary, comes as a component with the theme.
- Other components from the theme can be incorporated.


### Exams 

There is an exams page on the website that displays a library of old exams and practice from the exam bank that have been granted the permission to be publically shared.

The Exams directory contains all of the exam pdf files that would be accessible from the Exams page. Its subdirectories need to be structured and named in the specific way it is in order for the exams page to be loaded correctly. Each subdirectory must follow the convention "CMPT ###" representing the exams from the specific computing course it stores exams for. You can simply copy and paste the pdf files from the CS Exam Bank available in the computing archives and put them in appropriate directories within the exams directory.

In order to avoid extra work it would take to edit and update the exams' markdown file when maintaining the website, a python script was written in which it automatically write the markdown file with the appropriate links, linking exams to the pdf files contianed in the Exams directory. Simply execute the python script on your local machine and it should automatically generate the exams page based on the contents of the exams directory.

#### Maintanence of Exam Bank

Some things to keep in mind when interacting with the Exam Bank:
- The names of each exam follow a certain convention that should be followed to ensure everything remains easy. "CMPT### date ExamType Professor". Each separate word should be capitalized, for example "FinalExam" or "PracticeMidterm". The date follows year-month-day format, if there is no specific date, instead you can put "undated", or at the minimum the "TermYear" in place of the date.
- Whenver a new exam is acquired, ensure to rename accordingly and put it in the correct folder. Also remember to update the information on the excel sheet that is keeping track of all the exams in the exam bank.

### Favicon

The code for the favicon is in the _includes folder named head_custom.html. For the favicon to be present in every page, you must ensure every doc is present in the root directory, not in any other subdirectory, it was the only to go around the bug we found when using the theme for now.

### Google analytics

To enable google analytics, go to head_custom.html in the _includes folder and replace the google measurement ID tag in the script with the ID of your Google analytics account. There are some issues with this

### Disqus comments

To add and manage disqus comments at the bottom of course pages, you need to start up a disqus account. Afterwards, you must embed universal disqus html code in the part of the web page you want the comments to appear in. For example, look at the cmpt120resources.md code at the bottom.
You can simply follow these instructions: https://www.youtube.com/watch?v=Dr6pSdeJgkA 

You can set up moderation for the comments through your disqus site settings and also add other moderators for the site if necessary.

## Pages and Directories




