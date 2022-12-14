---
layout: default
title: Student Support
nav_order: 3
has_children: false

---



# Student Support
{: .no_toc }

###### Resources to help newcoming computing science students utilize SFU CS resources, setup coding environments and submit coding assignments.
{: .no_toc }



## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}


<br>
# CSIL access

## Accessing CSIL labs
{: .no_toc }

SFU has Computer Labs accessible by all SFU computing students. CSIL are open to all students registered in a computing science (CMPT) course. Information and FAQs on CSIL can be accessed on the [CSIL webpage](http://www.sfu.ca/computing/about/support/csil.html)

***Quick Links***

- [Directions to the CSIL in Burnaby and Surrey ](http://www.sfu.ca/computing/about/support/csil/csil-directions.html)
- [Getting Started for CMPT Undergrads](http://www.sfu.ca/computing/about/support/getting-started.html)
- [General FAQ with regards to CSIL](http://www.sfu.ca/computing/about/support/csil/general.html)
- [CSIL Policies](http://www.sfu.ca/computing/about/support/csil/policies.html)

*TIP: The SFU Snap app has a room location feature and can be used to locate CSIL. View the official SFU app suite [here](http://www.sfu.ca/apps.html).*


<br>
# IDEs & Text/Code Editors  

An IDE (Integrated Development Environment) is an application where you can write code and then compile, execute, and debug your code. A text/code editor on the other hand only provides code/script writing and editing features only. If you write a script with a code editor, you will need to compile/execute it using the terminal or open it in an IDE. IDEs contain programming libraries and integrated tools for programmers to use during the programming process. 
 
Both IDEs and text editors are advantageous for different purposes. The benefit of text editors is that you can quickly modify any script without specifying the programming language. Whereas IDEs assist vastly during the debugging process. The IDE you select to use will depend on the programming language you are using. Below is a comparison of different IDEs and text editors. The table is not exhaustive, and you might find other tools online that better suit your needs.

| [VS Code](https://code.visualstudio.com/) | - Standalone source code editor <br> - Runs on Windows, macOS, and Linux <br> - Contains extensions to support several programming languages (including Python, C++) <br> - Top pick for JavaScript and web developers  |
|[Visual Studio](https://visualstudio.microsoft.com/) | - IDE best used for .NET and C++ developers on windows<br> - Useful for app development<br> - Includes support for web, cloud, and game development |
|[Eclipse](https://www.eclipse.org/getting-started/) | - IDE for any programming language with an available plug-in<br> - Supports Python (PyDev plug-in), C/C++ (CDT plug-in) <br> - Popular for Java development |
|[IntelliJ](https://www.jetbrains.com/idea/)| - Really great IDE specific to Java <br> - Has great testing and debugging tools|
|[Replit](https://replit.com/)| - Free, collaborative, in-browser IDE <br> - Support for 50+ languages (including Python, C++)<br> - GitHub integration which allows you to import GitHub repos<br> - API & plugins|
|Mu editor](https://codewith.mu/en/){:target="_blank"} | - A extremely simple Python editor for beginner programmers|





<br>
# Compiling/Debugging programs

In order to execute the code you've written in order to see if it works it must first be compiled from human readable code to machine language so that computers may execute them. If there are errors in your compilation of the code, you may also need to debug it to pinpoint the errors.

## Compiling Python Programs

1. Set up your environment
    - Open the terminal and check that you have python installed and check which version you have. Enter the following command: 'python --version'
    - If you need to [download python](https://www.python.org/downloads/), you can download the latest version from the official Python website. The website also contains updated documentation, guides, source code, etc.  
    - Install python. Installation guide for [Linux/Unix](https://docs.python.org/3/using/unix.html), [Windows](https://docs.python.org/3/using/windows.html), and [MacOS](https://docs.python.org/3/using/mac.html) 
    - | Linux/Unix| Python should be pre-installed on your machine. If it isn???t you can download and after downloading and extracting the files, run the following commands in the respective directory:`>./configure` then  `>make` then  `>make altinstall` |
    | Windows | Follow the Python installation wizard instructions upon downloading the Python Windows installer version you need. After starting the installer you can select ???Install Now??? to install the default settings.|
    | MacOS   |  Macs come with Python pre-installed. If the version on your Mac is outdated, you can download and install the version you need by using the Python installation wizard. |

2. In interactive mode programming you can invoke the python interpreter by entering:  python. But by using your editor of choice you can write a python script ( ???.py??? file) and run it by entering the following in the terminal: python MyScript.py. This will compile and execute your script. 

3. If you are using an IDE, you can run and debug the script inside the IDE. 

## Compiling C/C++ Programs

1. Set up your environment
    - MacOS and Linux have C++ pre-installed
    - For Windows, you will need to download and install the GCC (GNU Compiler Collection) which is used to compile C/C++. Install the GCC compiler using the following commands in the terminal: 
        1. Get information on updated versions of packages: `sudo apt-get update`
        2. Enter the admin password 
        3. Install packages: `sudo apt install build-essential`
        4. Verify installation by checking the C++ version: `g++ --version `
        5. Verify installation by checking the C version: `gcc --version `
    
2. Once you have written your script, open the terminal in the directory with the script (the cd command can be used to change file paths or you can use your file explorer to go to the folder with the script and then open the terminal from the file) 

3. Use the following command to compile your file: `g++ sourcefile.cpp -o outputfile.exe `

4. Run the executable file/program: `./outputfile.exe `


## Make Files
Coming soon
{: .label .label-yellow }



<br>
# Submitting Files

## How to compress files into a zipped folder

Many courses' assignments require .zip files/folders containing all of the code and its dependencies to be handed over during submission.

***Helpful Links:***

- [Zipping and unzipping in Windows](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-8d28fa72-f2f9-712f-67df-f80cf89fd4e5#:~:text=Locate%20the%20file%20or%20folder,created%20in%20the%20same%20location.)

- [Zipping and unzipping on Mac](https://support.apple.com/en-ca/guide/mac-help/mchlp2528/mac#:~:text=Compress%20a%20file%20or%20folder,zip%20extension.)


`