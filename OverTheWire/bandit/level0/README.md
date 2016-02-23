#Bandit Level 0

##Level Goal

```
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

Commands you may need to solve this level

ssh

Helpful Reading Material

Secure Shell (SSH) on Wikipedia
How to use SSH on wikiHow
```

So, the first thing to do here is to use `ssh` to tunnel to the challenge server.

The following command demonstrates how `ssh` is used to connect to a remote server
`ssh <username>@<host>`

Let's connect!

`ssh bandit0@bandit.labs.overthewire.org` and at the password prompt, we supply the password `bandit0`

```
┌─[x509@infosploit] - [~/.gconf/apps] - [2016-02-23 08:32:59]
└─[0] <> ssh bandit0@bandit.labs.overthewire.org
The authenticity of host 'bandit.labs.overthewire.org (178.79.134.250)' can't be established.
ECDSA key fingerprint is 05:3a:1c:25:35:0a:ed:2f:cd:87:1c:f6:fe:69:e4:f6.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'bandit.labs.overthewire.org,178.79.134.250' (ECDSA) to the list of known hosts.
```
