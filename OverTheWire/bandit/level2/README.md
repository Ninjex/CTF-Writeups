#Bandit Level 1 → Level 2

##Level Goal

```
The password for the next level is stored in a file called - located in the home directory

Commands you may need to solve this level

ls, cd, cat, file, du, find

Helpful Reading Material

Google Search for “dashed filename”
Advanced Bash-scripting Guide - Chapter 3 - Special Characters
```

Upon connect to the server, we notice a file named as a single hyphen `-`

If you run `cat -` the program will simply be waiting to get input from STDIN and it will in turn dump that STDIN input to STDOUT. This is a naming convention used by a lot of programs to gather input from STDIN.

There are a few ways in which we can solve this challenge, and I will demonstrate two of them.

We can still use redirection here to dump the file contents:

```
bandit1@melinda:~$ cat < -
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

We could also explicitly call cat on the file name as `./-``

and if you aren't sure what the explicite file name should be, you can always run a find command on the directory:

```
bandit1@melinda:~$ find .
.
./.bashrc
./.profile
./.bash_logout
./-
```

```
bandit1@melinda:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```
