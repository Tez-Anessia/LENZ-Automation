# Workspace Creation Automation

## Overview
This repository contains the framework for the Lenz automation. This will include housing the data that the scripts will read from and the logs of each run. This is currently under development and will most likely undergo several changes to structure and functionality. Each final update will be outlined and updated here. 

## Structure
Below you can find a quick overview and description of the project structure and contents. 

* commonUtils - this directory will house files with common functions and usability 
* config - this directory is responsible for housing configuration files like logger
* data - any file that needs to be read or updated will live here, this will be split between csv's and images
* locators - locators for web elements will be housed here and grouped in different classes
* pages - sets of methods and actions that can be used to build scripts and tests
* scripts - will house any scripts which perform a complex action like mass updating all workspaces with a new report
* tests - inside this directory any tests created like workspace QA will be found here

## Features 
- Automation: Automate the creation of workspaces
- Customization: Dynamically add in contents for the workspaces
- Flexibility: Supports different approaches and needs 

## Requirements
* The driver will only work with Selenium version 14.0.0 listed in the requirments. 
* All files will need to be housed in the same data folder. 
* This currently works with the chrome browser

