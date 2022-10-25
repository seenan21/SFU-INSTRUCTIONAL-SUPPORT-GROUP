---
layout: default
title: CMPT 120 
parent: Course Resources
---

{% include head_custom.html %}
{% include toTopBtn.html %}



<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.0.0-beta.83/dist/themes/light.css" />
<script type="module" src="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.0.0-beta.83/dist/shoelace.js"></script>

# CMPT 120
{: .no_toc .flex-justify-between}

<sl-tree>
        <sl-icon name="plus-square" slot="expand-icon"></sl-icon>
        <sl-icon name="dash-square" slot="collapse-icon"></sl-icon>
    <sl-tree-item><a href="https://seenan21.github.io/SFU-INSTRUCTIONAL-SUPPORT-GROUP/docs/courseresources/cmpt120resources.html#setting-up-python">Setting Up Python</a>
        <sl-tree-item><a href="https://seenan21.github.io/SFU-INSTRUCTIONAL-SUPPORT-GROUP/docs/courseresources/cmpt120resources.html#installing-python">Installing Python </a></sl-tree-item>   
        <sl-tree-item><a href="https://seenan21.github.io/SFU-INSTRUCTIONAL-SUPPORT-GROUP/docs/courseresources/cmpt120resources.html#compiling-python-programs">Compiling Python Programs</a></sl-tree-item>
        <sl-tree-item><a href="https://seenan21.github.io/SFU-INSTRUCTIONAL-SUPPORT-GROUP/docs/courseresources/cmpt120resources.html#recommended-python-ides"> Recommended Python IDEs</a></sl-tree-item>
    </sl-tree-item>
    <sl-tree-item><a href="https://seenan21.github.io/SFU-INSTRUCTIONAL-SUPPORT-GROUP/docs/courseresources/cmpt120resources.html#assignment-downloadsubmission">Submitting Assignments</a>
        <sl-tree-item><a href="https://seenan21.github.io/SFU-INSTRUCTIONAL-SUPPORT-GROUP/docs/courseresources/cmpt120resources.html#downloading-repl-code">Downloading Repl Code</a></sl-tree-item>
        <sl-tree-item><a href="https://seenan21.github.io/SFU-INSTRUCTIONAL-SUPPORT-GROUP/docs/courseresources/cmpt120resources.html#zipping-files">Zipping files</a></sl-tree-item>
    </sl-tree-item>
    <sl-tree-item><a href="https://seenan21.github.io/SFU-INSTRUCTIONAL-SUPPORT-GROUP/docs/courseresources/cmpt120resources.html#course-resources">Course Resources</a>
    </sl-tree-item>
     <sl-tree-item>
    <a href="https://seenan21.github.io/SFU-INSTRUCTIONAL-SUPPORT-GROUP/docs/courseresources/cmpt120resources.html#accessing-csil-labs">CSIL and Peer Tutoring</a>
    </sl-tree-item>
</sl-tree>







# Setting up Python

## Installing Python

If you need to [download python](https://www.python.org/downloads/){:target="_blank"}, you can download the latest version from the official Python website. The website also contains updated documentation, guides, source code, etc. You can check the installation guide for [Linux/Unix](https://docs.python.org/3/using/unix.html){:target="_blank"}, [Windows](https://docs.python.org/3/using/windows.html){:target="_blank"}, and [MacOS](https://docs.python.org/3/using/mac.html){:target="_blank"}. 
    
 | Linux/Unix| Python should be pre-installed on your machine. If it isn’t you can download and after downloading and extracting the files, run the following commands in the respective directory:`>./configure` then  `>make` then  `>make altinstall` |
    | Windows | Follow the Python installation wizard instructions upon downloading the Python Windows installer version you need. After starting the installer you can select “Install Now” to install the default settings.|
    | MacOS   |  Macs come with Python pre-installed. If the version on your Mac is outdated, you can download and install the version you need by using the Python installation wizard. |

- To install Python on an iPad you would need to buy it from the Apple Store, but you are  NOT required to buy this! Ideally, you should  work on a laptop or desktop as you will need to do considerable typing (in a normal keyboard). 

- We will also work with web-based environments (such as Replit,.) that allow that you use Python even if it is not installed in your machine.

- If you cannot install Python consult during office hours. You can also use computers in the CSIL labs, where Python and development environments are already installed.

## Compiling Python Programs
{: .no_toc}

1. Set up your environment. Open the terminal and check that you have python installed and check which version you have. Enter the following command: `python --version`. If you do not have python, make sure you install it before proceeding.

2. In interactive mode programming you can invoke the python interpreter by entering:  python. But by using your editor of choice you can write a python script ( “.py” file) and run it by entering the following in the terminal: `python MyScript.py`. This will compile and execute your script. 

3. If you are using an IDE, you can run and debug the script inside the IDE. 

## Recommended Python IDEs

An IDE (Integrated Development Environment) is an application where you can write code and then compile, execute, and debug your code. A text/code editor on the other hand only provides code/script writing and editing features only. If you write a script with a code editor, you will need to compile/execute it using the terminal or open it in an IDE. IDEs contain programming libraries and integrated tools for programmers to use during the programming process.

Although any IDE can be used, we recommend in using the following beginner friendly IDEs for CMPT 120 students:

### IDLE
[IDLE](https://docs.python.org/3/library/idle.html){:target="_blank"} is Python's “Integrated Development and Learning Environment”. This is installed when Python is installed (both in PC's and in Macs). When you work with IDLE you work locally in your own computer.

### Replit
[Replit.com, the online IDE,](https://replit.com/site/ide){:target="_blank"} is a web-based tool to execute programs in different programming languages. It is convenient to use when you do not have access to a machine with Python installed on it (though installation of Python is straightforward). It is not recommended to use Replit for assignments and tests unless you use a paid account (about $5 fee per month last time we checked).

#### Demo Video for IDLE and Replit
Watch this [demo video](https://stream.sfu.ca/Media/Play/ad14caf6bdc6488893b1539698a15f5d1d){:target="_blank"} to get a gist of how to set up these two IDEs commonly used for CMPT 120. Note that at the time of recording the video, it was possible to work anonymously with Replit. Currently you need to create a paid account in Replit. You may use any id and email for such account.

### Mu Editor

The [Mu editor](https://codewith.mu/en/){:target="_blank"} is another free environment, offline (to work locally), and really straightforward to use that you may want to download it - can be used later on in the course.

### Spyder
[spyder](https://www.spyder-ide.org/){:target="_blank"} is a free, more advanced development offline environment which can also be potentially utilized in the course.
 


<sl-divider style="--width: 4px;"></sl-divider>

# Submitting Assignments


## Downloading Repl Code

If code is written on the online IDE Repl, Repl allows for python program files to be exported as a ZIP.

![Repl export of python files](./CMPT%20120/extractingFromRepl.png "Repl allows export of python files")

## Copying code into local file

You can also copy & paste the code into a local text file on your computer if needed:

1. Open a plain text editor (e.g. Notepad on Windows).
2. Mark the entire program code you wrote in repl.it by dragging your mouse over it while holding the left button clicked.
3. Right click -> Copy, in repl.it.  (CTRL C)
4. Right click -> Paste, in the text editor.  (CTRL V)
5. Menu -> "Save as" in the text editor, and choose a filename with the file extension ".py"

Recall that Python program files are just regular plain text files. They are just like other such files whose names usually end in ".txt". The only difference is that we use the ".py" extension to indicate to the operating system that the text in this file constitutes a Python program, and hence should be run by the Python interpreter.

## Zipping files

Many courses' assignments require .zip files/folders containing all of the code and its dependencies to be handed over during submission.

- [Zipping and unzipping in Windows](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-8d28fa72-f2f9-712f-67df-f80cf89fd4e5#:~:text=Locate%20the%20file%20or%20folder,created%20in%20the%20same%20location.){:target="_blank"}

- [Zipping and unzipping on Mac](https://support.apple.com/en-ca/guide/mac-help/mchlp2528/mac#:~:text=Compress%20a%20file%20or%20folder,zip%20extension.){:target="_blank"}



<sl-divider style="--width: 4px;"></sl-divider>

# Course Resources


[**Python Cheat sheet**](./CMPT%20120/CMPT120PythonCheatSheet.pdf){:target="_blank"} <br>
[**Python Style Guide**](https://legacy.python.org/dev/peps/pep-0008/#code-lay-out){:target="_blank"} <br>
[**Python built-in Functions**](https://docs.python.org/3/library/functions.html){:target="_blank"}


## Past exams

- [Midterm 1 Review Spring 2018](./CMPT%20120/CMPT120Midterm1ReviewSpring2018.pdf){:target="_blank"}
- [Midterm 2 Review Spring 2018](./CMPT%20120/CMPT120Midterm2ReviewSpring2018.pdf){:target="_blank"}
- [Final Exam Coding Spring 2018](./CMPT%20120/CMPT120FinalSpring2018.pdf){:target="_blank"}
- [Final Exam Practice with Solutions Summer 2019](./CMPT%20120/CMPT120PracticeExamSolutionsSummer2019.pdf){:target="_blank"}
- [Midterm Practice Fall 2022](./CMPT%20120/CMPT120MidtermSampleFall2022.pdf) [(Solutions)](./CMPT%20120/CMPT120MidtermSampleSolutionsFall2022.pdf)


## Textbooks 

### Python Textbooks

- [How to think like a Computer Scientist - Learning With Python](./CMPT%20120/Python%20Textbooks/TextbookPython%20-%20How%20to%20Think%20Like%20a%20Computer%20Scientist.pdf){:target="_blank"}
- [Automate The Boring Stuff With Python](./CMPT%20120/Python%20Textbooks/TextbookPython%20-%20AutomateTheBoringStuffWithPython.pdf){:target="_blank"}
- [Python Basics: A Practical Introduction to Python 3](https://static.realpython.com/python-basics-sample-chapters.pdf)
- [Learning Python by Mark Lutz](https://cfm.ehu.es/ricardo/docs/python/Learning_Python.pdf)
- [Advanced Guide to Python 3 Programming by John Hunt](https://warin.ca/ressources/books/2019_Book_AdvancedGuideToPython3Programm.pdf)
- [Introduction to Programming in Python: An Interdisciplinary Approach](https://introcs.cs.princeton.edu/python/home/)

## Extra Python Coding Practice

You can use the exercises/examples in the following sites for more practice. Keep in mind however that some content might not be covered in the lectures -- the idea is not to learn new things, but to practice using what you have learned from the lectures to solve the problems there.

You can visit [CodingBat](https://codingbat.com/python){:target="_blank"}, [LearnPython](https://www.learnpython.org/){:target="_blank"} or [PythonFromScratch UWaterloo](https://open.cs.uwaterloo.ca/python-from-scratch/6/){:target="_blank"}.


<sl-divider style="--width: 4px;"></sl-divider>

## Accessing CSIL labs

SFU has Computer Labs accessible by all SFU computing students. CSIL are open to all students registered in a computing science (CMPT) course. Information and FAQs on CSIL can be accessed on the [CSIL webpage](http://www.sfu.ca/computing/about/support/csil.html){:target="_blank"}

- [Directions to the CSIL in Burnaby and Surrey ](http://www.sfu.ca/computing/about/support/csil/csil-directions.html){:target="_blank"}
- [Getting Started for CMPT Undergrads](http://www.sfu.ca/computing/about/support/getting-started.html){:target="_blank"}
- [General FAQ with regards to CSIL](http://www.sfu.ca/computing/about/support/csil/general.html){:target="_blank"}
- [CSIL Policies](http://www.sfu.ca/computing/about/support/csil/policies.html){:target="_blank"}

*TIP: The SFU Snap app has a room location feature and can be used to locate CSIL. View the official SFU app suite [here](http://www.sfu.ca/apps.html){:target="_blank"}.*

## Peer Tutoring
SFU CS also provides a [peer tutoring](https://www.sfu.ca/computing/current-students/undergraduate-students/student-resources/cs_peer_tutoring1.html){:target="_blank"} program to provide extra support in learning difficult concepts or assignments. Peer tutors can be accessed both remote and in person.

<sl-divider style="--width: 6px;"></sl-divider>

<!--### Past assignments

Coming soon
{: .label .label-yellow } -->


# Discussion

<div id="disqus_thread"></div>
<script>
    var disqus_config = function () {
    this.page.url = 'https://seenan21.github.io/SFU-INSTRUCTIONAL-SUPPORT-GROUP/docs/courseresources/cmpt120resources.html';  
    this.page.identifier = '/SFU-INSTRUCTIONAL-SUPPORT-GROUP/docs/courseresources/cmpt120resources.html'; 
    };
    (function() { 
    var d = document, s = d.createElement('script');
    s.src = 'https://sfuisg.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>