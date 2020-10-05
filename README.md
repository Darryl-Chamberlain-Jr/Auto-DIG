Welcome!
========
This repository is a **work-in-progress** on automatically generating assessments in a College Algebra course. By *automatically*, we mean that assessments are generated (via a combination of technology) with little input from the user. This is achieved by front-loading the creation of question structures and associated conceptions/errors that are later called by a shell script to create PDF versions of assessments for instructors to utilize in the classroom. Published and under-review articles on this project are housed [here](Articles). The related project, an open-source College Algebra online homework system, is housed [here](https://github.com/Darryl-Chamberlain-Jr/ufmac1105).

**No coding experience is required to use this work as-is.** The GUI is currently written using Zenity and thus works best on Linux. This project will eventually move to a cross-platform application for widespread use.

Steps to create the desktop app.
------
1. Download the necessary open-source programs: Python and LaTeX.

   This code uses [Python](https://www.python.org/downloads/) and [LaTeX](https://www.latex-project.org/get/) to create the questions and compile the questions into a PDF assessment. Both are open-source and available on Windows, Mac, and Linux.

2. Clone the repository.

   We suggest downloading the repository to a folder in your home directory. As we use many git repositories, we have a git-repos folder in the home directory that we put any downloaded repositories (like this one) in. Instructions on how to clone a repository can be found [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

3. Run the installer shell script *install_AutoDIG*.

    *./git-repos/Auto-DIG/ShellScripts/./install_AutoDIG*

------

This will bring up the GUI to guide you through the rest of the process. If all goes well, the collection of PDFs are available in the *CompleteExam* folder! This folder should open immediately after the code has finished.

Contribute to this project!
------
### If you would like to contribute to the creation of the assessments, please contact Darryl Chamberlain Jr. at dchamberlain31@ufl.edu.
