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

# How to use git for yourself

  > _I recommend this tutorial: [https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud) even though it focuses on bitbucket rather than github._


We saw how git works in collaboration and also how that will cause some interesting things to happen when people work together on a set of files. The rest of this tutorial is a discussion using the team's github site to add files to our shared repository and create individual repositories. 

  > [https://github.com/vieps-pye-class-2019](https://github.com/vieps-pye-class-2019)

Here are some of the approaches we will look at to manage shared files for our course:

  - We can each have our own directory in the sandbox and keep ourselves to ourselves 
     - What issues might this cause with commit logs
     - Can each person commit when they like ?
     
  - We can all make a repository of our own in the VIEPS-PYE team area
     - How does this work in terms of collaboration on a project ?
     - Would it be better to do more repositories and use them for a specific task ?
     
  - Because you all signed up for github, you also have personal repositories
     - At the moment these are all public unless you registered as a student user
     - Even if they are public, other people can only read them ... not change things
     - Which is fine unless you want to collaborate. Can you see how to do that ?

Think about how these approaches might be useful for you in the following cases:

  - Writing a paper or report with coauthors
  - Writing drafts of a thesis with comments from a supervisor
  - Working on some python code in your own project
  - Working on some python code with other people
  
What are the problems that are likely to come up and how do you think you might approach dealing with them ?


## Different file types and text editing

Our previous exercise in combining files showed how git tries to merge information from different version of files when it can parse the file and understand what it actually is. The tools that it uses are reasonable in the case of text files but largely meaningless in the case of binary files (like images, .docx files, etc). Git can only work out that there is a new version of the file and complain, it cannot try to merge. You can tell git to ignore specific types of files (using a `.gitignore` file in the project) and if you are planning a project with a lot of image files you might want to read about it [here](https://www.atlassian.com/git/tutorials/saving-changes/gitignore).

Line-by-line comparison is also not ideal for writing code where **code-blocks** span multiple lines. Git's merging strategy may have problems if edits are made in the middle of a code block that might, in principle mess up the syntax. For example, imagine if you change a line which has a closing parenthesis for a multi-line function definition. 

These are issues that are avoided by 

  - Not trying to version inappropriate file types
  - Making regular commits of small changes
  - Anticipating trouble and working around it
  - Using the other tools available in github to communicate with your collaborators and plan changes carefully.
  - Branches (see [this page in the tutorial](https://www.atlassian.com/git/tutorials/using-branches)

    


```{code-cell} ipython3

```
