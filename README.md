# Welcome!
This repository is a **work-in-progress** on automatically generating assessments in a College Algebra course. By *automatically*, we mean that assessments are generated (via a combination of technology) with little input from the user. This is achieved by front-loading the creation of question structures and associated conceptions/errors that are later called by a shell script to create PDF versions of assessments for instructors to utilize in the classroom. Published and under-review articles on this project are housed [here](Articles). The related project, an open-source College Algebra online homework system, is housed [here](https://github.com/Darryl-Chamberlain-Jr/mac1105summer2020).

**No coding experience is required to use this work as-is.** If you would like to generate exams through the shell scripts, here is what you will need to do **the first time**. *On subsequent assessments, you'll only need to complete steps 4 and 5.*
------
1. Download the necessary programs.

   This code uses [Python](https://www.python.org/downloads/), [SageMath](https://www.sagemath.org/download.html), and [LaTeX](https://www.latex-project.org/get/) to create the questions and compile the questions into a PDF assessment. All three are open-source and available on Windows, Mac, and Linux.

2. Clone the repository.

   We suggest downloading the repository to a folder in your home directory. As we use many git repositories, we have a git-repos folder in the home directory that we put any downloaded repositories (like this one) in. Instructions on how to clone a repository can be found [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

3. Modify the shell script file *generateExams.sh* to point to your local directory.
    1. Navigate to the *generateExams.sh* file found in the shellScript folder.
    2. Open the file with a text editor. We suggest [Atom](https://atom.io/).
    3. Modify the *DIR* to point to your local directory. Example: *home/yourUsername/git-repos/AAG-College-Algebra*

4. Run the shell script *generateExams.sh*
    1. **Open your command prompt/terminal and navigate to the shellScript folder.** You can achieve this by typing *cd ./git-repos/AAG-Colege-Algebra/shellScript*
    2. **Run the shell script.** You can achieve this by typing *generateExams.sh "Semester" "Password" examNumber* The current version of the script will then generate the PDFs of the assessment and label the PDF with the Semester and Exam Number you input. In this version, it creates the number of Modules currently needed for each assessment, but this can be easily modified for your own uses. Password-protected PDFs are also generated.

5. Check the folder *CompleteExam* for the PDFs, locked PDFs, and keys.

   If all goes well, the collection of PDFs are available in the *CompleteExam* folder!

------
------
### If you would like to contribute to the creation of the assessments, please contact Darryl Chamberlain Jr. at dchamberlain31@ufl.edu.
