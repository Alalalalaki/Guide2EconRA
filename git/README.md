## Frequently Used Commands

![xkcd](xkcd.png)

Every time you have mistakenly added and/or commited a file

`git rm --cached your_giant.file`

Note that even after removing it from the index with `git rm` or `git reset`,  it still seems to take space in the `.git` directory. If you want to clean it up 

`git gc --prune=now`

Every time you commit but then regret before pushing (replace new message with --no-edit if necessary)

`git commit --amend --no-edit`

Every time you get messed up, give up, and want to go back into past

`git reset --hard`

Every time you want to clean something for now and move back lately

`git stash` / `git stash list` / `git stash apply`

Every time you want check what has happened in a file

`git log -p your.file`

