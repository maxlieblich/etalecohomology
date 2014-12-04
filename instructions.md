### Instructions to do things here

In order to follow these instructions, you should have git, python, and pandoc installed on your local computer

**STEP 1**:
First go to https://github.com/ and create a github account.

**STEP 2**:
Now navigate to https://github.com/maxlieblich/etalecohomology
and locate the button in the upper right hand corner called Fork.  Click the button to create a fork.  This should create a new repository on the github server called https://github.com/<your username>/etalecohomology

**STEP 3**:
Next, we want to clone the current repository (meaning get a copy on our local computer).  To do this, 
open a terminal and type
```
git clone https://github.com/<your username>/etalecohomology.git
```
This should create a directory on your local computer called etalecohomology.

**STEP 4**:
Inside the directory etalecohomology, there should be a subdirectory called src.  Inside this directory, you may read and edit the current files, and also create new files.  Look at the file content to determine appropriate syntax.  Make your contribution to the course notes here.

**STEP 5**:
If you made changes to any files, made new files, or deleted old files, you need to tell the git repository (ie. stage the changes).  For example, if you edited or created the file unicorns.md and deleted the file vampires.md, you should run the commands
```  
git add unicorns.md
git del vampires.md
```
If you forgot what files you changed, you can view this by running the command
```
git status
```
Changes that are staged to be committed to the repository and changes which haven't been will be explained by the output.

**STEP 6**:
When you are satisfied with your contribution, you should make a pull request.  To do this, you should first 
commit your changes to the local repository.  This is done with the command
```git commit -m "This is my message about what changes I made"```
Then you should push your changes to the remote repository.  This is done via the command
```git push origin master```
Finally, you should submit a pull request by navigating to https://github.com/<your username>/etalecohomology
and clicking the green button.

NOTES:
You may occasionally want to update your fork of the repository with the trunk.  This is done via the commands
```
git fetch upstream
git checkout master
git merge upstream/master
```

You may want to save your work occasionally to the local repository by running
```
git commit -m "some comment about my latest change"
```
This way if you break something on your local copy, you can go back to a previous version and try again.

