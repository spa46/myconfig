#Usage: ext.sh in_file skip_num out_size
dd if=$1 of=$1.out bs=1 skip=$2 count=$3
