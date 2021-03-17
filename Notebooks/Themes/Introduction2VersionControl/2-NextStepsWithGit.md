---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# An introduction to Version Control pt 2

  > Version control is good for the soul
  
## Some setup is required

We can run all this from the notebook (though perhaps it is easier in the terminal)

```bash
git config --global credential.helper store
git config --global user.email "profdiablo@underworldcode.org"
git config --global user.name  "profdiablo"
```

We also need to do one operation (in the terminal) that needs a password.
The obvious thing is to try to obtain a copy of a private repository from our
shared space ...

## How do we get a copy of the information on github ? 

We can 'download' the sandbox repository to a local directory using the following command.
(Change to the relevant directory as needed)

```bash
cd /home/jovyan/VIEPS-PYE/Notebooks/Introduction2VersionControl
git clone https://github.com/vieps-pye-class-2019/shared-sandbox.git 
```

Use the **GIT > Open Terminal** menu option above to make this work.

```{code-cell} ipython3
%%sh

# Type your code in this cell
```

Take a look to see if this worked. What files are in the `shared-sandbox` directory. 

```bash
# check if it worked
ls -a shared-sandbox
```

There should be a (hidden) directory `.git` that actually contains the database of changes, the original files and all manner of logs that allow you to replay changes and check them.

```{code-cell} ipython3
%%sh

# Type your code here
```

## Example 

Here is a typical run through of what we do with git. First we can ask what has been changed / added etc

```bash
git status 
```
```text
bash-3.2$ git status


    On branch master
    Your branch is up to date with 'origin/master'.

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

            modified:   README.md

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

            .ipynb_checkpoints/
            People.txt

    no changes added to commit (use "git add" and/or "git commit -a")
```

We can ask git to start taking notice of a file that has been added:

```bash
git add People.txt --verbose
```
```text
   bash-3.2$ git add People.txt --verbose 
   # but it is very quiet anyway
```

We can issue lots of git commands such as:

   - `git rm`
   - `git mv`
   - `git add`
   - `git help`
   
but when we are done telling git all about the changes we already made when we edited the files, we now tell it to take a snapshot of the state of our project and **commit** these changes. We must add a message when we make this commit and this tell us what changes we made.

```bash
 git commit -m "I have added my name to the People.txt list"
```

```text
    bash-3.2$ git commit -m "I have added my name to the People.txt list"
    [master fdc97b1] I have added my name to the People.txt list
     1 file changed, 7 insertions(+)
     create mode 100644 People.txt
```

We can repeat this cycle of edit / commit as much as we like but we have not yet uploaded these changes for anyone else to see. This is done by **pushing** the changes back to the repository. This requires a network connection of course. Even if you are offline, though, it can be helpful to commit changes in little chunks with helpful messages because you can ALWAYS go back and recover **all the files in the state they were in when you made the commit**. 

```bash
git push
```

```text
    bash-3.2$ git push
    Enumerating objects: 4, done.
    Counting objects: 100% (4/4), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (3/3), 447 bytes | 447.00 KiB/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/vieps-pye-class-2019/shared-sandbox.git
       242d062..fdc97b1  master -> master
```

```{code-cell} ipython3
!git help 
```

## Exercise

You can browse the directory in the file browser and you can add your name to the `People.txt` file. Now you should be able to commit your changes by following the pattern above:

```{code-cell} ipython3
%%sh

# git status etc etc 
```

Discuss this as a class - does it work ? Do you expect it to work ? 

+++

[Pt 3 - Going off on your own](3-YourOwnRepositories.ipynb)

```{code-cell} ipython3

```
