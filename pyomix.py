##########################################################################
#  - PyOmiX - Analysis Workflow                                          #
#  - Python Script                                                       #
#  - Mar 22.2019                                                         #
#  - Copyright: Ahmed Omar, Mohamed Magdy, Usama Bakry, and Waleed Amer  #
#  - Nile University                                                     #
##########################################################################

# Importing libraries
import os


# Function to make directories for swiss-prot ids
def makdirs(file):
    os.mkdir(os.getcwd() + "/working-dir", int(0o755))
    os.chdir(os.getcwd()+"/working-dir")
    print(os.getcwd())
    for line in file:
        os.mkdir(os.getcwd()+"/"+line,int(0o755))
