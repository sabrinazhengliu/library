## Create Permanent Alias
```bash
nano ~/.bashrc
    alias ll='ls -l'
source ~/.bashrc
```

## Basics

```bash
bash --version

# capture stdout and stderr
ls /notreal 1>output.txt 2>error.txt

# Output Redirection
ls > list.txt   # truncate
ls >> list.txt  # append

# Input Redirection <
cat < list.txt

# Here Document << (stop limit)
cat << EndOfText
> This is a 
> multiline
> text string
> EndOfText
```

## Echo
```bash
echo hello world!  # quote not needed

```

## Check Command is Program or Built-in
```bash
command -V df
command -V echo
# distable built-in command
enable -n echo    # use the program version
enable echo       # use the built-in version
```

## Bash Expansions
```bash
echo ~             # ~ = $HOME
echo ~-            # ~- = last visited directory
echo c{a,o,u}t     # brace expansion
echo {1..100}
echo {01..100}     # fillin 0s
echo {a..z}
echo {Z..A}
echo {1..30..3}
echo {01..12}{A..Z}
head -n 1 {dir1,dir2,dir3}/lorem.txt    # preview 1st line of each file
```

## Parameter Expansion
```bash
greeting="hello there"            # assign value to parameter
echo $greeting
echo ${greeting:6:5}              # substring
echo ${greeting/there/everybody}  # replace 1st instance
echo ${greeting//e/_}             # replace all instances
echo ${greeting/e/_}
echo $greeting:4:3                # simple concatenation
```

## Command Substitution
```bash
uname -r
echo "The kernel is $(uname -r)."
info=$(uname -r)
echo $info
```

## Arithmetic Expansion
```bash
echo $(( 2 + 2))
echo $(( 4 / 5))    # this returns 0: bash can only compute int
```


