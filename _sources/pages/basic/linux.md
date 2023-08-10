# Command line

Here, we learn command line. The command line is a text interface to computers. You input text commands to your computer to do some operations, for example making or removing files, and changing files permissions, etc.

In Mac, you can use the command line in `terminal.app`

## Basic

To begin with, we check shortcuts.

| Command | Description |
| :-----: | :---------: |
|Ctrl + C| Interrupt the current process|
|Ctrl + Z| Suspend the current process|
|Ctrl + S| Stop command output to the screen|
|Ctrl + Q| resume output to the screen paused by Ctrl+S|
|Ctrl + L| Clear the screen|
|Ctrl + D| Exit the shell|
|Ctrl + A| Move the cursor to the start of a line|
|Ctrl + E| Move the cursor to the end of the line|
|Ctrl + W| Cut the word before the cursor|
|Ctrl + U| Cut the part of the line before the cursor|
|Ctrl + K| Cut the part of the line after the cursor|
|Ctrl + Y| Paste the last thing you cut|

---
### Special symbols

There are 4 special symbols and each of them represents a location.

|Symbol|Meaning|
|:----:|:-----:|
|`/`|root directory|
|`.`|current directory|
|`..`|parent directory|
|`~`|home directory|


### basics commands

`pwd`:	show the current directory

`mkdir`: make directory
```bash
mkdir ~/tmp
```

`cd`: change directory
```bash
cd ~/tmp
```

`touch`: make files
```bash
touch file
```

`ls`: list files or directories
```bash
ls
# file
```

`mkdir -p`; make parent directories as needed
```bash
mkdir -p dir/subdir/ssubdir
ls
# file dir
```

`rm`: remove files\
`rm -r`: remove directories and their contents
```bash
rm file
rm -r dir
```

cf.
```bash
rm -v file # show filename when removed
rm -i file # comfirm whether to rmove
rm -f file # force remove
```

`rmdir`: remove empty directory
```bash
mkdir dir
ls
# dir
rmdir dir
ls
# (nothing)
```

cf.
```bash
mkdir -p dir/subdir/ssubdir

rmdir -p dir/subdir/ssubdir
```


`echo`:
- print strings
    ```bash
    echo $PATH
    ```
- make files with contents
    - Make new file or overwrite a existing file : `>`
        ```bash
        echo [Strings] > [filename]
        ```
    - Append : `>>`
        ```bash
        echo [Strings] >> [filename]
        ```

`cat`: print file contents
```bash
echo hello > file1
cat file1
# hello
```

```bash
cat > file2
asdf  (input something)
Ctrl + D (end input)
cat file2
# asdf
```

`cp`: copy file(s) or directory(ies)
```bash
cp file1 file3
cat file3
# hello
```

```bash
mkdir dir1
touch dir1/file4
cp -r dir1 dir2
ls dir2
# file4
```

```{note}
When doing `cp file1 file2` and the `file2` already exists,
you will be asked whether to overwrite the contents of `file2`.

If the `file2` does not exist, the contents of `file1` will be copied to `file2`.

When doing `cp -r dir1 dir2` and the `dir2` already exists, new `dir1` will be created in `dir2`.

If the `dir2` does not exist, the contents of `dir1` will be copied to `dir2`. So the contents of these directories are the same.
```

`mv`: move file(s) or directory(ies). If `file5` does not exist, the following operation is rename
```bash
mv file1 file5
```

`file5` will be moved to `dir3`.
```bash
mkdir dir3
mv file5 dir3
```

If `dir4` does not exist, the following operation is rename. Otherwise `dir1` will be moved to `dir4`.
```bash
mv dir1 dir4
```


`tree`: print contents of the current directory in a tree-like format. You can use `tree -d` to print directory contents. You can use `tree -L` to print directory contents up to a certain level.

You have to install `tree` command in bash first.
```bash
brew install tree
```

```bash
tree
test
├── dir2
│   └── file4
├── dir3
│   └── file5
├── dir4
│   └── file4
├── file2
└── file3
```

```bash
# print directory contents up to level 2
tree -L 2
```

`chomd`: change file modes(permissions)
```bash
chmod 755 file
```

**You can specify the mode with octal numbers.**

When you specify the mode with octal number;\
4 stands for "read"\
2 stands for "write"\
1 stands for "execute" \
0 stands for "no permission"

If you permit all operations(4+2+1) to everyone, you can use `777` for example.
If you permit all operations(4+2+1) to owner and read and execute(4+1) to group and others, you can use `755` for example.

**You can specify the mode with symbol like `u+x` for user, `g+x` for group, `o+x` for others.**

|target|meaning|operation|meaning|mode|meaning|
|:-:|:---:|:-:|:------------:|:-:|:----:|
|u|	User  |=| set the modes  |r| read   |
|g| Group |+| add the mode   |w| write  |
|o| Others|-| remove the mode|x| execute|
|a|	All   | |                | |        |


For example,
```bash
chmod u=rwx,g=rx,o=r file

chmod u+x file
```

You can use `chmod -R` to change permissions recursively.

---
### Shell globbing

`globbing patterns` specify sets of filenames with wildcard characters. `globbing patterns` is a powerful way to find files that match a pattern. For example, `*.txt` means all files with the extension `.txt` in the current directory.

There are several common wildcard characters:
```
* : matches zero or more characters
? : matches any single character
[abc] : matches any character in set
[a-z] : matches any character in range
[!abc] : matches any character not in set
[!a-z] : matches any character not in range
```

**extended pattern matching**

- *(pattern)    more than 0 times
- ?(pattern)    0,1 times
- @(pattern)   only 1 times
- +(pattern)    more than 1 times
- !(pattern)     not in the pattern

```bash
ls
# file1 file2 file3 file4 file11 file123
ls !(file1)
# file2 file3 file4 file11 file123
ls !(file1|file2)
# file3  file4 file11 file123
ls file[0-9]
# file1 file2 file3 file4
ls file[0-9]+([0-9])
# file11 file123
```


`find`: find files and directories
```bash
# search the current directory for filename(not recursively)
find filename

# search target directory recursively for lecture0~lecture9 directories (cf. -type f)
find target -name lecture[0-9] -type d

# search the current directory recursively for files accessed within 1 day
find . -atime -1

# search the current directory recursively for files modified within 1 day
find . -mtime -1

# search the current directory recursively for files with size between 30kB and 1MB
find . -size +30k -size -1M -name '*.py'

# search target directory recursively for files or directories that match condition1 and condition2 (cf. -or, -not)
find target condtion1 -and condition2

# search the current directory recursively for .txt files and remove them all.
find . -name '*.txt' -exec rm {} +
```

`grep`: search files for patterns
```bash
# Search any line that contains `word` in filename
grep [-Options] 'word' filename

grep 'word' file1 file2 file3
grep 'string1 string2'  filename
```

| Options |	Description |
|:-------:|:-----------:|
|-i | Ignore case distinctions|
|-w | The expression is searched for as a word|
|-v | Select non-matching lines|
|-n | Print line number with output lines|
|-h | Suppress the Unix file name prefix on output|
|-H | Print file name with output lines|
|-r | Search directories recursivly|
|-R | Just like -r but follow all symlinks|
|-l | Print only names of FILEs with matches
|-L | Print only names of FILEs without matches|
|-c | Print only a count of selected lines per FILE|
|--color | Display matched pattern in colors|
|-m NUMBER | Stop grep command NUMBER selected lines|
|-o | Display only matched parts of lines|

### Brace Expansion
You can generate arbitrary strings using brace expansion.
```bash
echo a{d,c,b}e
ade ace abe

echo {1,2}{3,4}
13 14 23 24
```

Some examples:
```bash
# move all files and directories to `dir`
mv * dir

mv ./path/{foo,bar,baz}.txt dir
# = mv ./path/foo.txt ./path/bar.txt ./path/baz.txt `dir`

# move all pyhon and shell files to `dir`
mv *{.py,.sh} dir
```

---
### Pipeline and redirect
```
`|`: pipe
`>`: redirect
```

In Unix-like systems, there are three types of streams, which
connect computer programs and its environment; standard input (`stdin`), standard output (`stdout`), and standard error (`stderr`). The input stream is the stream that receives data from the user. The output stream is the stream that sends data to the user. The error stream is the stream that sends error messages to the user.
A `pipe` and a `redirect` are techniques that connects two programs by sending output from one command to the input of the other command.

**pipeline**

`|` stdout to stdin. Second command will take the stdout of the previous command as stdin.

```bash
history | head
```

**redirect**

``>`` stdout to file

```bash
history > hist.txt
cat hist.txt | head
```

 `>>`  add contents

```bash
echo asdf > test.txt
cat test.txt
# asdf

echo fdsa >> test.txt
cat test.txt
# asdf
# fdsa
```


To remove stderr, add `2>/dev/null` to the end of the command.

---
### Combine commands

%`;` `&` `&&` `||` `$()` `xargs`

- `command2` after `commmand1`\
    `command2` is executed even when `command1` puts stderr
    ```bash
    command1 ; command2
    ```

- `command2` and `commmand1` at the same time
    ```bash
    command1 & command2
    ```

- `command2` after `commmand1` succeeded
    ```bash
    command1 && command2
    ```

- `command2` after `commmand1` failed
    ```bash
    command1 || command2
    ```

**command using the other stdout** `$()`

```bash
date +%Y%D
touch file_`date +%Y%D`
# touch file_$(date +%Y%D)

# nested command
dirname $(which cat)
ls $(dirname $(which cat))
```


---
### Symbolic links
`ln -s`: make symbolic links  
Symbolic links is the file that refers to another file.
```bash
ln -s original_file link_file
ls -l
# lrwxr-xr-x  1 user  group  12 Aug  4 15:18 link_file -> original_file
```

```{note}
Aliases are similar to symlinks, but they are valid after you move the original files unlike symlinks. Although it seems aliases are more useful, aliases are not compatible with unix system. You cannot use like `cd alias` but `cd syslink`.
```

```{note}
`ln` options:\
-s, --symbolic    make symbolic links instead of hard links\
-f, --force       make links even if the file exists
```



## Reference

- [The Unix Shell](https://swcarpentry.github.io/shell-novice/)
- [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)

