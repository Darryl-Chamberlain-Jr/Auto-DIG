import shutil
import os
import glob

def copyKeys(FileName, version, rootDirectory):
    PDForiginalLocation='/' + str(rootDirectory) + '/Keys/key' + str(FileName) + str(version) + '.pdf'
    PDFnewLocation='/' + str(rootDirectory) + '/CompleteExam/Keys/key' + str(FileName) + str(version) + '.pdf'
    shutil.copyfile(PDForiginalLocation, PDFnewLocation)
    CSVoriginalLocation='/' + str(rootDirectory) + '/Keys/lettersAnswerKey' + str(FileName) + str(version) + '.pdf'
    CSVnewLocation='/' + str(rootDirectory) + '/CompleteExam/Keys/lettersAnswerKey' + str(FileName) + str(version) + '.pdf'
    shutil.copyfile(CSVoriginalLocation, CSVnewLocation)

def clearOldVersions(rootDirectory):
    for dirs in ["Keys", "buildExams", "CompleteExam/Keys", "CompleteExam/PDFs"]:
        files = glob.glob( '/' + str(rootDirectory) + '/' + str(dirs) + '/*')
        print(files)
        for f in files:
            os.remove(f)

# USED TO TEST FILE. DELETE WHEN DONE
#rootDirectory="home/dchamberlain31/git-repos/Auto-DIG"
#copyKeys("Test", "A", rootDirectory)
#clearOldVersions(rootDirectory)
