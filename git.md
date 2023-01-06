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

## Git Push
```bash
git push [<options>] [<repository> [<refspec>...]]
    -v, --verbose         be more verbose
    -q, --quiet           be more quiet
    --repo <repository>   repository
    --all                 push all refs
    --mirror              mirror all refs
    -d, --delete          delete refs
    --tags                push tags (can't be used with --all or --mirror)
    -n, --dry-run         dry run
    --porcelain           machine-readable output
    -f, --force           force updates
    --force-with-lease[=<refname>:<expect>]
                          require old value of ref to be at this value
    --force-if-includes   require remote updates to be integrated locally
    --recurse-submodules (check|on-demand|no)
                          control recursive pushing of submodules
    --thin                use thin pack
    --receive-pack <receive-pack>
                          receive pack program
    --exec <receive-pack>
                          receive pack program
    -u, --set-upstream    set upstream for git pull/status
    --progress            force progress reporting
    --prune               prune locally removed refs
    --no-verify           bypass pre-push hook
    --follow-tags         push missing but relevant tags
    --signed[=(yes|no|if-asked)]
                          GPG sign the push
    --atomic              request atomic transaction on remote side
    -o, --push-option <server-specific>
                          option to transmit
    -4, --ipv4            use IPv4 addresses only
    -6, --ipv6            use IPv6 addresses only
```

## Manage Remote Session
```bash
git remote
git remote [-v | --verbose]
git remote add [-t <branch>] [-m <master>] [-f] [--tags | --no-tags] [--mirror=<fetch|push>] <name> <url>
git remote rename <old> <new>
git remote remove <name>
git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
git remote [-v | --verbose] show [-n] <name>
git remote prune [-n | --dry-run] <name>
git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
git remote set-branches [--add] <name> <branch>...
git remote get-url [--push] [--all] <name>
git remote set-url [--push] <name> <newurl> [<oldurl>]
git remote set-url --add <name> <newurl>
git remote set-url --delete <name> <url>
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
