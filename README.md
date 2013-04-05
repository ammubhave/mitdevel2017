MIT Developers Group - Class of 2017
============

This repository is where all the website related stuff can go on.

Getting Started
============

1 On the top right corner of your screen is a 'Fork' button. Click it and form this repository in your account.

2 You will need git installed at your machine. You will get a fork of this repository in your account. Clone it into your local machine by typing
     
       
       git clone https://github.com/<your username>/mitdevel2017.git openshift
       git remote add upstream https://github.com/ammubhave/mitdevel2017.git


3 A directory 'openshift' will be created at your machine. You can edit it, add new files, etc.etc. Do not rename this directory else the code won't work.

4 Once done editing you can push the changes on your Github account by the commands (you need to be in the root of the repository):


       git add .
       git commit -m "<any message describing your change>"
       git push origin master
     
     
5 Once the changes are pushed go to the online github repository and issue a pull request using the 'Pull request' button on the top right and continuing further. A pull request will be issued which I can later accept and the code changes will be reflected.

Fetching updates in the original repo with your local repo
=============

       git fetch upstream
       git merge upstream/master

Running the website at your machine
=============

Make sure that the directory is called openshift, or else it will not work locally.

You can run the website at your local machine too. Get into the root of the repository where the manage.py file resides and type in the shell:

       python manage.py runserver
       
Now open the web browser and goto http://localhost:8000/ and there you have the website running.

Creating super user
=============
Your local Django site will need a super user. Goto the root of the repository and execute

       python manage.py createsuperuser
       
Enter details and it will create a local super user.
Now goto http://localhost:8000/admin/ and enter the details and you will log into admin.
