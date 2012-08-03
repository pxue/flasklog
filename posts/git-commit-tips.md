A couple tricks I picked up are listed below:

## Prevent a file from being committed after initialization

stackoverflow: [Git: Never Commit Changed Files (But still keep original
revision)](http://stackoverflow.com/questions/8485451/git-never-commit-changed-files-but-still-keep-original-revisioned/8485503#8485503)

    git update-index --assume-unchanged <file>

To make it commit again,

    git update-index --no-assume-unchanged <file>

This is different from gitignore because you would have to remove the file
first,

    git rm --cache 'file_name'
    echo file_name >> .gitignore

## View outgoing commits

stackoverflow: [Viewing unpushed Git
commits](http://stackoverflow.com/questions/2016901/viewing-unpushed-git-commits/3338774#3338774)

For anyone familiar with hg, they'd know that <code>hg outgoing</code> allows
you to view unpushed commits. Unfortunately, git doesn't as convenient of
a command, but by no means it's impossible.

    git log --branches --not --remotes

or I prefer this way to list commits that are on your local <code><branch></code> but not on
remote branch:

    git fetch origin        # update origin/<branch> if needed
    git log origin/<branch>..<branch>

if you want to look up what's new on remote that's not local, do the opposite:

    git log <branch>..origin/<branch>




