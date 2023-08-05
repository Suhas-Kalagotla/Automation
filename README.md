# Automation

In this Repository I will be writing the automation code that I wrote or will write to automate the daily tasks I will be facing 


1) file read & write.py
   this is an python automation code :
   Problem Statement : To copy All the programms into one file to submit or to share to do this each file need to be opened and manually copy
                       into one file
   Solution : when you enter the direct path of the parent directory all the files with ".py" extention with in the parent directory will be
              copied into one file

2) startproject.sh
   it is an bash automation script :
   Problem Statement : Every time to open or start working on the website I am creating using mern I need to run 5-6 set of commands
   Solution : This bash Script contains all the commands that I need to run and executes them one after the other 
   To run In linux : first save the file in "/usr/local/bin/" and give execution permission using chmod +x <filename>
      command : ./<filename> // name of the file you saved or ./startproject.sh
   output :
      1) Server and Client will be started
      2) source code will be open in vscode 
