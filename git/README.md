![xkcd](xkcd.png)

## Frequently Used Commands

Every time I have mistakenly added and/or commited a file

`git rm --cached my_giant.file`

Note that even after removing it from the index with `git rm` or `git reset`,  it still seems to take space in the `.git` directory. If I want to clean it up 

`git gc --prune=now`

Every time I commit but then regret before pushing (replace new message with --no-edit if necessary)

`git commit --amend --no-edit`

Every time I get messed up, give up, and want to go back into past

`git reset --hard`

Every time I want to clean something for now and move back lately

`git stash` / `git stash list` / `git stash apply`

Every time I want check what has happened in a file

`git log -p my.file`



## Some Random Notes I Find Useful

[Merging vs. Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing) / [When do you use Git rebase instead of Git merge?](https://stackoverflow.com/a/36587353)

