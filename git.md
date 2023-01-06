## New Repo
```bash
git init
git remote add origin http://...
git branch -M master
git push --set-upstream --force origin master    (same as: git push -uf origin master)
```

## Commit Changes
```bash
git add .
git commit -m 'my changes'
git push origin master    (or simply: git push)
```

## Create a Branch
```bash
# check all branches
git branch --all

# check current branch
git branch

# check the last commit on each branch
git branch -v

# see the branches merged or not-merged
git branch --merged
git branch --no-merged

```
