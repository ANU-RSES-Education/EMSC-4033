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

# An introduction to Version Control

  > Version control is good for the soul
  
## What is version control ? 

Version control is the practice of keeping a record of all the times you edit a file, all the changes you make and a record of the intent of those changes. This is a form of version control:

```text
% ls

    my_thesis_v0.0.tex
    my_thesis_v1.0.tex
    my_thesis_v1.1.tex
    my_thesis_v1.0+supervisor_comments.tex
    my_thesis_v1.0+supervisor_comments_v1.1_merged.tex
    my_thesis_v1.2.tex
    
% diff my_thesis_v1.tex my_thesis_v1.2.tex

    ... (lots of changes appear) 

```

This is great because you have a record of all of your changes but already you can see that there are problems when you make multiple sets of changes at once. Version control **software** packages aim to help with this. They formalise common practices like tagging file names (the example above) and they add a whole suite of extra tools to make collaboration easier. 

The other form of version control that you may already have encountered is *track changes* in microsoft word or the *time machine* version system that you can find on the Mac. 

These kinds of backup-based version control ideas are fine but they are very linear in the way changes are managed. As you can see above, there can be genuine issues when two people contribute to a file. While you are waiting for your supervisor to comment on draft version 1.0 of your thesis you almost certainly would like to start work on v1.1. When you have changes in v1.0 suggested by your supervisor you have to go through and figure out what changes you need to make to v1.1 to make a new version before you can get cracking on v1.2.

Imagine how much more complicated this becomes when many people are working on a single project and may all be editing a single file together. 

## What tools can you use ?

There are a number of different packages that you can use and they all have their advantages and disadvantages. Some examples you might run across are:

   - git: (`git`)
   - subversion: (`svn`)
   - mercurial: (`hg`)
   
They are all approximately equivalent and differ slightly in how they distribute out the repository (the database of the entire history of the project). `git` (by default) puts the entire history of all files on every machine and that does make for extra safety. You can read more about different styles of repository [here](http://guides.beanstalkapp.com/version-control/intro-to-version-control.html) (it's a bit technical though !). 


## What is `git` and what is `github`

You can use the software `git` by yourself on your own computer to manage version control of a project. However, the real benefits to using a tool like `git` come when you use a networked **repository** of your software which you can access from multiple machines and synchronise from machine to machine when you are ready. Not only can *you* do this, but your collaborators can access and edit files and then, later, you can merge the changes in an organised way. 

We have a shared space on `github` which is a centralised web site that coordinates various git repositories. We will have a shared repository and I will also show you how to manage your own repositories using `git` and `github`. There are other sites quite like github (gitlab and bitbucket spring to mind) but that is for you to investigate and make a choice later. You can stick with git on these other sites.

`github` also bundles a host of project management tools alongside your files and that is something that can be very helpful for teams of people or a class. 

## Reference links for our class 

  - We have a github site that you can access directly at [https://github.com/vieps-pye-class-2019](https://github.com/vieps-pye-class-2019)
  - There is a shared "sandbox" repository that we can experiment with and generally wreck: [https://github.com/vieps-pye-class-2019/shared-sandbox](https://github.com/vieps-pye-class-2019/shared-sandbox)
  - There is a github 'team' for the class too - it's a way to give us all the relevant permissions to work together without always having to add everyone individually. The team has a home page for discussions and stuff: [https://github.com/orgs/vieps-pye-class-2019/teams/vieps-pye-2019](https://github.com/orgs/vieps-pye-class-2019/teams/vieps-pye-2019)


## Using the command line tools in a notebook

`git` is a command line / terminal tool that is not running within python (of course there are also python/git integrations but we will only use a minimum few features and so we'll mostly just use the web site. 


```{code-cell} ipython3
%%sh

git help
```

```{code-cell} ipython3
print("Mixing python and shell commands:")

!git help
```


## Next steps

  - [Pt 2 - Using git to access our repository](2-NextStepsWithGit.ipynb)
