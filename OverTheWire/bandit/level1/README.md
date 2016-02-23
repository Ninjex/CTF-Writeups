#Bandit Level 0 → Level 1

##Level Goal

```
The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH to log into that level and continue the game.

Commands you may need to solve this level

ls, cd, cat, file, du, find
```

Previsously, we connected to the server under the `bandit0` username.

Now it appears we need to read a file in the home directory. By default when you use `ssh` with an account name, you will be in the home directory upon connecting.

So, the first and obvious thing to do is list the contents of the directory:

`bandit0@melinda:~$ ls -al`

It appears to have a readme file in the directory, let's dump the contents to STDOUT using the `cat` command:

```
bandit0@melinda:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
bandit0@melinda:~$
```

This is our password for the `bandit1` user account!

![bandit0](https://github.com/Ninjex/Wargame-Writeups/blob/master/OverTheWire/bandit/level1/bandit1.png?raw=true "bandit1")
