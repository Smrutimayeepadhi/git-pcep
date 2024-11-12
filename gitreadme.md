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
```
git add <file_name>
git commit -m "message"
git push
```

6- add a branch
```
git branch -M main
```
7- add remote origin

```
git remote add origin https://github.com/Smrutimayeepadhi/git-pcep.git
```
8-  push the changes to remote
```
git push -u origin main
```

9- adding SSH key gitlab

https://docs.gitlab.com/ee/user/ssh.html#add-an-ssh-key-to-your-gitlab-account

```
ssh-keygen -t ed25519-sk -C "<comment>"

cat /Users/himanjan/.ssh/id_ed25519_gitlab.pub

eval $(ssh-agent -s)
ssh-add /Users/himanjan/.ssh/id_ed25519_gitlab
ssh -T git@gitlab.com

Welcome to GitLab, @Smrutimayeepadhi!


```