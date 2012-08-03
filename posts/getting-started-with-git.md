#Getting Started with Git

I've been trying out Git for about 6 month now, using it to source manage my
projects and deploy my websites (this site included!). With free services such
as Github, there really isn't any reason for me to look for anything else such
as Mercurial.

Getting started can be daunting for new programmers, so here are a simple, no bs
guide on how to set up your basic git repository.

##Setup - Installing Git

The easiest way to do this on linux dist. (ie. Ubuntu) is to apt-get it
directly from repo:

    $ apt-get install git-core

You will need the [ expat ]( http://expat.sourceforge.net/ ), [ curl ]( http://curl.linux-mirror.org/ ), 
[ zlib ]( http://www.zlib.net/ ), and [ openssl ]( http://www.openssl.org/ ) libraries installed - though
with the possible exception of expat, these will normally already be there. If
you're still running into trouble,
[here](http://book.git-scm.com/2_installing_git.html) is a good article to get
things started.

## Creating a new Repository

Create a new directory, open it and perform a

    git init

to great a new repository.

## Check out a Repository

Create a working copy of a local repository by running the command

    git clone /path/to/repository

when using a remote server, your command will be

    git clone username@host:/path/to/repository

## Workflow

Your local repository consists of three "trees" maintained by git. The first one
is your <code>working Directory</code> which holds the actual files. The second
one is the <code>Index</code> which acts as a staging area, and finally the
<code>Head</code> which points to the last commit you've made.

## Add & Commit

You can propose change (add it to the <code>Index</code>) using

    git add <filename>
    
    git add *

    git add .

Committing your add by using the commit command:

    git commit -am "Commit Message here"

Now your changes area committed to <code>Head</code>, but not the remote
repository yet.

##Pushing Changes

Your changes are now in <code>Head</code> of your local working copy, to send
these changes to the remote server you would have to "push" the changes there:

    git push origin master

change <code>master</code> to which ever branch you want to push your changes
to.

If you have not cloned an existing repository and want to connect your local
repository to a remote server, you need to execute:

    git remote add origin <server>

Now you are able to push your changes to the remote server.

## Update and Merging

to update your local repository to the newest commit, execute:

    git pull

in your working directory to <code>fetch</code> and <code>merge</code> remote
changes.

to merge another branch into your active branch (e.g. master), use

    git merge <branch>

in both cases git tries to automatically merge changes. Unfortunately, this is
not always possible and results in <code>conflicts</code>. You are responsible
to resolve those conflicts by editing those files indicated by git. After
changing those files, you need to tell git you have <code>resolved</code> the
conflicts by marking them as merged:

    git add <filename>

before merging changes, you can also preview them by using:

    git diff <source_branch> <target_branch>

## Replace Local Changes

sometimes you want to revert changes done to your local working copy, this can
be achieved by using this command:

    git checkout -- <filename>

this replaces the changes in your working tree with the last content in HEAD.
Changes already added to index, as well as new files, will be kept. 

Another thing you might want to do when you screw up is to "Nuke" your local
copy, reverting all changes. This can be done by fetching the latest history
from the server and point your local master branch at it like this:

    git fetch origin

    git reset --hard origin/master


Git is a wonderful and powerful tool for any programming purposes. This is just
a very shallow description of what it can do for us. For further reading, hit up
[github](http://help.github.com/)'s help page and the [simple
guide](http://rogerdudler.github.com/git-guide/) for a more in depth
walkthrough.


