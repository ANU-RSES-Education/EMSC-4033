# Release ID for Jupyterhub

Editing this file triggers a (re)install of the jupyterhub installation.
If the jupyterhub is already installed, it will be refreshed but not forcibly 
upgraded (that needs to be managed from the console). 

There will be errors if the github secrets have not been set up 

 - **IP Address:** http://128.199.153.60
 - **Hostname:** https://test.rses.underworldcloud.org 
 - **Release ID:** 1.0.0
 - **Droplet Name:** ubuntu-rses-earth-sci-dev
 
 ## Comments
   
Rebuilt droplet / test the installer workflow 
  - Note: rebuilding the droplet resets the root password to a temporary value
  - Note: remove old ssh key as well using `ssh-keygen -R [hostname-or-IP]`
  - Switching to ubuntu 19 for testing purposes
  - 2021.02.16 - upgrading to ubuntu 20 and scratching all content
  - 2021.02.16 - pick only the useful dependencies
  
  
