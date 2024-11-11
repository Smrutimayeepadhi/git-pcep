1- create a folder

2- initialize git init
```
git init
```
3- to check what .git contains
```
cd .git
ls -ltr

drwxr-xr-x   3 himanjan  staff   96 Nov 11 23:02 info
-rw-r--r--   1 himanjan  staff   73 Nov 11 23:02 description
drwxr-xr-x  15 himanjan  staff  480 Nov 11 23:02 hooks
drwxr-xr-x   4 himanjan  staff  128 Nov 11 23:02 refs
-rw-r--r--   1 himanjan  staff   23 Nov 11 23:02 HEAD
-rw-r--r--   1 himanjan  staff  137 Nov 11 23:02 config
drwxr-xr-x   4 himanjan  staff  128 Nov 11 23:02 objects
```
4- Add the global user name and email
```
git config --global user.name "username"
git config --global user.email "useremail"

```
5- add any files