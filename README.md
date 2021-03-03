# Jupyterhub on DigitalOcean to serve notebooks for a course

Many of us use jupyter notebooks to teach classes and we often serve them through `mybinder.org` because all of our students experience the same environment no matter what platform they use. The only problem with binder is that any changes the students make to their notebooks are not recorded if their session times out - the student session on binder is *not persistent* across sessions. 

Persistence does introduce some complications - every user has to be identified so that their session can be restored. Someone has to provide secure access and long-lived storage on top of the required computational environment.   

This is an attempt to provide a template to build a cheap-and-cheerful jupyter-notebook server that can handle the needs of a medium sized class. Following this template means that the class coordinator can focus on the content rather than the setup. 

## Description

This repository can build itself into a digital ocean droplet that runs (the littlest) jupyterhub with the underlying dependencies that you specify in a conda environment `yml` file. The configuration of the droplet
is stored in the repository secret variables. Github actions are configured to monitor the repository and update
the content of the server when changes to the configuration are pushed. The actions also check to see if the server
is alive and well. 

This template repository contains sample content that runs on a dedicated droplet ... the status of that droplet
is autoatically monitored:
 
![Health check](https://github.com/ANU-RSES-Education/droplet-template/workflows/Health%20check/badge.svg)


## How to use this template

The full set of instructions is given in the [Documentation](Documentation) folder. The steps are:

  - Create a suitable server ([instructions are for a Digital Ocean droplet](Documentation/DigitalOcean.md))
     - NOTE - the installation that is used here does not build in the smallest D.O droplet size of 1Gb no matter how
              many times we messed with the configuration options so please use a minimum 2Gb size ... 
  - Make a clone of this template repository (See [Github.md](Documentation/Github.md))
  - Update the cloned repository with information about the server that you have set up:
     - Update the SECRETS in the settings for the new repository to include these:
        - DROPLET_IP :: either the numerical IP or the hostname if available (must be hostname for https to be enabled)
        - DROPLET_PASS ::  root password for the droplet (needed for installation of tljh)
        - HUBADMIN_USER :: the admin user when you first log into jupyter hub (to add more users)
        - HUBADMIN_PASS :: corresponding password 
     - In the /github/workflows directory there is an installer file that can change some of the tljh defaults
     - Update the ubuntu packages and conda / pip packages in the 
  - Commit the updates on Github to trigger the build / rebuild of the content of the server.
       Note that you may trigger failing builds if you do all your editing on github the first time around -but that can be ignored.
  - Update any details in the SERVER_ID file if you need to trigger a new build at any time
  - Create links for `nbgitpuller` for users of the server and test them (See [nbgitpuller.md](Documentation/nbgitpuller.md )) 
  - Add your users to the `jupyterhub` ([ManagingUsers.md](Documentation/ManagingUsers.md))



## Using Jupyterbook

This repository also contains the information for building a jupyterbook using the notebooks that are in
the Notebooks directory.

There is some additional configuration to make this work smoothly and you can read what needs to be done 
in [Jupyterbook/README.md](Jupyterbook/README.md)

For this example, you can see the [online version](https://underworld-geodynamics-cloud.github.io/self-managing-jupyterhub/FrontPage.html) which is automatically built by github using this repository.

## Try out the Nbgitpuller

To make a "binder-like" link to a repository on a droplet that you have set up, you can read the [nbgitpuller documentation](https://jupyterhub.github.io/nbgitpuller/link.html) or fill out a form here:

[![https://img.shields.io/badge/<LABEL>-<MESSAGE>-<COLOR>](https://img.shields.io/badge/Admin-LinkMaker-Red)](https://jupyterhub.github.io/nbgitpuller/link.html?hub=https://test.rses.underworldcloud.org&repo=https://github.com/ANU-RSES-Education/droplet-template)

You can launch this example particular example to try it out by clicking on this link. Your work is persistent. 

[![https://img.shields.io/badge/<LABEL>-<MESSAGE>-<COLOR>](https://img.shields.io/badge/Launch-Demo-blue)](https://test.rses.underworldcloud.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FANU-RSES-Education%2Fdroplet-template&urlpath=tree%2Fdroplet-template%2FStartHere.ipynb&branch=master)
    
## Administration tasks
    
If the hub has a signup page it can be reached here:
    
[![Signup](https://img.shields.io/badge/User-Signup-blue)](https://test.rses.underworldcloud.org/hub/signup)

And the corresponding page for an admin user to authorise the users after they sign-up is
    
[![Authorize](https://img.shields.io/badge/Admin-Authorize-Red)](https://test.rses.underworldcloud.org/hub/authorize)
   
Admin users also have access to the hub control panel to shut down wayward servers and add / remove users. 
    
[![ControlPanel](https://img.shields.io/badge/Admin-HubControlPanel-Red)](https://test.rses.underworldcloud.org/hub/admin)
    
    


