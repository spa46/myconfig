#!/bin/sh
rm -rf cscope.out cscope.files
#find ./ -name '*.c' -o -name '*.cpp' -o -name '*.cc' -o -name '*.h' -o -name '*.s' -o -name '*.S' > cscope.files
find `pwd` -name '*.c' -o -name '*.cpp' -o -name '*.cc' -o -name '*.h' -o -name '*.s' -o -name '*.S' > cscope.files

cscope -i cscope.files
