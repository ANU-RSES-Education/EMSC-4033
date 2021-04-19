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

### Reference links for our class 

  - All of the material for these notes is available at [https://github.com/ANU-RSES-Education/EMSC-4033](https://github.com/ANU-RSES-Education/EMSC-4033)

  - When you ask for one of the live pages to be executed, you are directed to a server which does this;
    - authenticates you (or uses saved credentials)
    - synchronises the changes you have made with any changes that have been made in the original repository
      * If we add an exercise or some new material, it will be copied into your account
      * If we find a bug and change an existing notebook, the changes will be merged
      * If our changes clash with yours, yours are kept
    - The page is then displayed and the code is available for you to try. 

  - To be able to do this complicated merge, the revision control is made to work overtime. The package doing this is called [`nbgitpuller`](https://jupyterhub.github.io/nbgitpuller/). 

  - Because `nbgitpuller` is active and synchronising with the EMSC4033 repository, we won't be using version control ourselves. However, using an online repository is a very sensible habit to get into if you aren't already hooked.

### How to use git for yourself

We recommend this tutorial: [https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud). It focuses on the bitbucket online repository rather than GitHub but the principles are similar.

Even in a single-user project, writing "issues" and using automatic testing is a really good idea. 

Most online repositories have some sort of built-in computation. You can do things like run a test suite every time an important file changes. You can also use it to build web pages when you update your content. 

That's what we are doing to make the online book for this course - the repository rebuilds the web pages if any of the content changes because of some scripts we built in to the repository (see it in action [here](https://github.com/ANU-RSES-Education/EMSC-4033/actions/workflows/deploy_to_gh_pages.yml) ). This takes the concept of literate programming one step further - the programs are self-documenting as well as self executing.

You can read about another example [here](https://www.underworldcode.org/articles/self-updating-repositories/) which shows how to regularly run a notebook that processes some data and uploads an image that is linked within a web page. One of the repositories doing the work is [https://github.com/ANU-RSES-Education/SeismicNoise_AuSIS_UHS](https://github.com/ANU-RSES-Education/SeismicNoise_AuSIS_UHS) and this is the latest image:


```{figure} https://github.com/ANU-RSES-Education/SeismicNoise_AuSIS_UHS/raw/master/results/latest.png
---
width: 80%
name: ulladulla
---
In Australia, the change in human behaviour due to COVID lockdowns was most dramatically observed in the data recorded by the Australian Seismometers in Schools (AuSiS) network. These instruments are research-quality seismometers that are maintained by school students — our next generation of geophysicists. The usual hum of the children (and teachers) during the school day, observed in the movement between classrooms, and during lunchtimes or Saturday morning sports, abruptly stopped at locations such as Ulladulla High School on the south coast of New South Wales (above).
```


