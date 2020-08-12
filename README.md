Welcome!
========
This repository is a **work-in-progress** on automatically generating assessments in a College Algebra course. By *automatically*, we mean that assessments are generated (via a combination of technology) with little input from the user. This is achieved by front-loading the creation of question structures and associated conceptions/errors that are later called by a shell script to create PDF versions of assessments for instructors to utilize in the classroom. Published and under-review articles on this project are housed [here](Articles). The related project, an open-source College Algebra online homework system, is housed [here](https://github.com/Darryl-Chamberlain-Jr/mac1105summer2020).

**No coding experience is required to use this work as-is.** If you would like to generate exams through the shell scripts, here is what you will need to do **the first time**. *On subsequent assessments, you'll only need to complete step 4.* The GUI is currently written using Zenity and thus works best on Linux. This project will eventually move to a Python-only code to be widely available.

Steps to generate exams for the first time.
------
1. Download the necessary programs.

   This code uses [Python](https://www.python.org/downloads/), [SageMath](https://www.sagemath.org/download.html), and [LaTeX](https://www.latex-project.org/get/) to create the questions and compile the questions into a PDF assessment. All three are open-source and available on Windows, Mac, and Linux. **In the future, dependencies on SageMath and LaTeX will be removed.**

2. Clone the repository.

   We suggest downloading the repository to a folder in your home directory. As we use many git repositories, we have a git-repos folder in the home directory that we put any downloaded repositories (like this one) in. Instructions on how to clone a repository can be found [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository). **In the future, this will be available as a tar file that can be downloaded and made.**

3. Modify the shell script file *zenityAutoDIG.sh* to point to your local directory. **In the future, this will be completed through the GUI.**
    1. Navigate to the *zenityAutoDIG.sh* file found in the *shellScripts* folder.
    2. Open the file with a text editor. We suggest [Atom](https://atom.io/).
    3. Modify the *DIR* to point to your local directory. Example: *home/yourUsername/git-repos/Auto-DIG*

4. Run the shell script *zenityAutoDIG.sh*. **In the future, this will be a desktop application.**
    1. Open your terminal and navigate to the shellScripts folder.

       If you created the *git-repo* folder in your home directory as we suggested, you can navigate to the *zenityAutoDIG.sh* shell script with *cd ./git-repos/Auto-DIG/shellScripts*

    2. Run the shell script using *./zenityAutoDIG.sh*

       This will bring up the GUI to guide you through the rest of the process.

If all goes well, the collection of PDFs are available in the *CompleteExam* folder! This folder should open immediately after the code has finished.

Contribute to this project!
------
### If you would like to contribute to the creation of the assessments, please contact Darryl Chamberlain Jr. at dchamberlain31@ufl.edu.
