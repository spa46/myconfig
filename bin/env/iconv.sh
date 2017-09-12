#iconv -f EUC-KR -t UTF-8 $1 > $1.8
iconv -c -f EUC-KR -t UTF-8 $1
