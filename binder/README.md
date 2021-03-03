# Notes for binder deployment

This repository is set up to manage it's own jupyterhub but it can also run on an existing environment like binder.

In that case, it is necessary to populate this folder with build instructions for binder. That could be a dockerfile or a requirement.txt file for pip or a conda environment. 

It seems to be fine to make a link from to the `conda_packages.yml` file in the home directory to `environment.yml` but, if you need a different setup, you can break that link and edit the environment file. 

The packages file that is in the home directory has comments that are removed before use but binder does not do that so the `apt.txt` file here is a copy of what is likely to be needed. Watch out for this !

For information see LINK on mybinder.org  