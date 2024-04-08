#!/usr/bin/python

import os, sys

#src = []
#dst = []

homedir = os.path.expanduser('~') +'/'
confdir = 'myconfig/'


############## Customization  ##############

# clists=["bin", ".tmux.conf", ".vimrc.local", ".vimrc.old", ".vimrc.org", ".vimrc",".vimrc.before", ".vimrc.bundles"]
clists=["bin", ".tmux.conf"]

############################################

os.chdir(homedir)

# Installation: spacevim 
curl -sLf https://spacevim.org/install.sh | bash
#######################

for i in range(len(clists)):
    src = confdir+clists[i]
    dst = clists[i]
    print ("src: " + src)
    print ("  => dst: " + dst)
    if not os.path.exists(src):
        print (". . . . . . Skip. ( No source file )")
        continue
    if not os.path.exists(dst):
        os.symlink(src, dst)
        print (". . . . . . Done.")
    else:
        question="File already exists, overwrite? (y/n)"

        while True:
            ans = input(question)

            if ans == "y":
                os.remove(dst)
                os.symlink(src, dst)
                print (". . . . . . Overwrite Done.")
                break
            elif ans == "n":
                print (". . . . . . Skip.")
                break

