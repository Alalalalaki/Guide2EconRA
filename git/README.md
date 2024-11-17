<img src="xkcd.png"  width="400">

## My Frequently Used Commands

Every time I have mistakenly added and/or commited a file

`git rm --cached my_giant.file`

Note that even after removing it from the index with `git rm` or `git reset`,  it still seems to take space in the `.git` directory. If I want to clean it up 

`git gc --prune=now`

Every time I commit but then I want to add something to this commit before pushing

`git commit --amend --no-edit`

Every time I commit but then I want to change the commit comment before pushing

`git commit --amend -m "new message"`

Every time I get messed up and want to go back into last commit

`git reset` / `git reset --hard`

Every time I want to clean something for now and move back lately

`git stash` / `git stash list` / `git stash pop` / `git stash apply` / `git stash drop`

Every time I want check what has happened in a file

`git log -p my.file`

Every time I want see the difference statistics either before and after commit

`git diff --stat` / `git show --compact-summary`

Every time I want to list all the commits (even ones that have been reseted or rebased)

`git reflog `

Every time I want to fetch a pull request so that I can checkout as a local branch  

`git fetch origin pull/<PR NUMBER>/head:<LOCAL BRANCH NAME> `



## Random Notes I Find Useful

[Git mergetool tutorial](https://gist.github.com/karenyyng/f19ff75c60f18b4b8149#setting-up-different-editors--tool-for-using-git-mergetool) 

[Git Forks and Upstreams: How-to and a cool tip](https://www.atlassian.com/git/tutorials/git-forks-and-upstreams)

[Merging vs. Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing) / [When do you use Git rebase instead of Git merge?](https://stackoverflow.com/a/36587353)

[Collaborative Models in GitHub](http://www.goring.org/resources/project-management.html) / [Collaborating on GitHub](https://uoftcoders.github.io/studyGroup/lessons/git/collaboration/lesson/) / [The Ultimate Github Collaboration Guide](https://medium.com/@jonathanmines/the-ultimate-github-collaboration-guide-df816e98fb67)

[Scientific Collaboration and Project Management in GitHub](https://rabernat.medium.com/scientific-collaboration-and-project-management-in-github-d74f2255ae5f) / [Learn How To Use GitHub to Collaborate on Open Science Projects](https://www.earthdatascience.org/courses/intro-to-earth-data-science/git-github/github-collaboration/)

[GitHub for Collaboration On Open Projects ](https://mozillascience.github.io/working-open-workshop/github_for_collaboration/) / [Development workflow](https://docs.scipy.org/doc/numpy-1.15.1/dev/gitwash/development_workflow.html) / [GitHub Standard Fork & Pull Request Workflow](https://gist.github.com/Chaser324/ce0505fbed06b947d962)

[Set up your digital classroom with GitHub Classroom](https://github.blog/2020-03-18-set-up-your-digital-classroom-with-github-classroom/) / [Manage coursework with GitHub Classroom](https://docs.github.com/en/education/manage-coursework-with-github-classroom)

[(Collaboration) Infrastructure](https://www.notion.so/Infrastructure-452e6e478ff846cca9dd73445a431a3c)

[Using git and Dropbox](https://www.math.cmu.edu/~gautam/sj/blog/20160406-dropbox-git.html)

[Git for Economists: A Practical Guide](https://medium.com/codex/git-for-economists-a-practical-guide-7d10faf4224f)
