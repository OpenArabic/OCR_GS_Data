#!/bin/sh

SCRIPTPATH=`pwd`

echo $SCRIPTPATH/$1/

# creating manifests
cd $SCRIPTPATH/$1/7_final/ && ls *.png > manifest.txt
cd $SCRIPTPATH/$1/7_final_200/ && ls *.png > manifest.txt
cd $SCRIPTPATH/$1/7_final_a/ && ls *.png > manifest.txt
cd $SCRIPTPATH/$1/7_final_b/ && ls *.png > manifest.txt
cd $SCRIPTPATH/$1/7_final_a_200/ && ls *.png > manifest.txt
cd $SCRIPTPATH/$1/7_final_b_200/ && ls *.png > manifest.txt

# run a
VAR="_a"
FOLDER="7_final"$VAR
MODEL="~/.config/kraken/arabic-beirut.clstm"

python $SCRIPTPATH/eval.py $MODEL $SCRIPTPATH/$1/$FOLDER
cat $SCRIPTPATH/$1/$FOLDER/*.gt.txt > $SCRIPTPATH/$1/g$VAR.txt
cat $SCRIPTPATH/$1/$FOLDER/*.rec.txt > $SCRIPTPATH/$1/r$VAR.txt
ocrevalutf8 accuracy $SCRIPTPATH/$1/g$VAR.txt $SCRIPTPATH/$1/r$VAR.txt > $SCRIPTPATH/$1/report$VAR.txt
echo $SCRIPTPATH/$1/$FOLDER": folder has been processed!"

# run b
VAR="_b"
FOLDER="7_final"$VAR
MODEL="~/.config/kraken/arabic-beirut.clstm"

python $SCRIPTPATH/eval.py $MODEL $SCRIPTPATH/$1/$FOLDER
cat $SCRIPTPATH/$1/$FOLDER/*.gt.txt > $SCRIPTPATH/$1/g$VAR.txt
cat $SCRIPTPATH/$1/$FOLDER/*.rec.txt > $SCRIPTPATH/$1/r$VAR.txt
ocrevalutf8 accuracy $SCRIPTPATH/$1/g$VAR.txt $SCRIPTPATH/$1/r$VAR.txt > $SCRIPTPATH/$1/report$VAR.txt
echo $SCRIPTPATH/$1/$FOLDER": folder has been processed!"

# run a_200
VAR="_a_200"
FOLDER="7_final"$VAR
MODEL="~/.config/kraken/arabic-beirut-200.clstm"

python $SCRIPTPATH/eval.py $MODEL $SCRIPTPATH/$1/$FOLDER
cat $SCRIPTPATH/$1/$FOLDER/*.gt.txt > $SCRIPTPATH/$1/g$VAR.txt
cat $SCRIPTPATH/$1/$FOLDER/*.rec.txt > $SCRIPTPATH/$1/r$VAR.txt
ocrevalutf8 accuracy $SCRIPTPATH/$1/g$VAR.txt $SCRIPTPATH/$1/r$VAR.txt > $SCRIPTPATH/$1/report$VAR.txt
echo $SCRIPTPATH/$1/$FOLDER": folder has been processed!"

# run b_200
VAR="_b_200"
FOLDER="7_final"$VAR
MODEL="~/.config/kraken/arabic-beirut-200.clstm"

python $SCRIPTPATH/eval.py $MODEL $SCRIPTPATH/$1/$FOLDER
cat $SCRIPTPATH/$1/$FOLDER/*.gt.txt > $SCRIPTPATH/$1/g$VAR.txt
cat $SCRIPTPATH/$1/$FOLDER/*.rec.txt > $SCRIPTPATH/$1/r$VAR.txt
ocrevalutf8 accuracy $SCRIPTPATH/$1/g$VAR.txt $SCRIPTPATH/$1/r$VAR.txt > $SCRIPTPATH/$1/report$VAR.txt
echo $SCRIPTPATH/$1/$FOLDER": folder has been processed!"

# run 0 --- may not work (too large)
VAR="_all"
FOLDER="7_final"
MODEL="~/.config/kraken/arabic-beirut.clstm"

python $SCRIPTPATH/eval.py $MODEL $SCRIPTPATH/$1/$FOLDER
cat $SCRIPTPATH/$1/$FOLDER/*.gt.txt > $SCRIPTPATH/$1/g$VAR.txt
cat $SCRIPTPATH/$1/$FOLDER/*.rec.txt > $SCRIPTPATH/$1/r$VAR.txt
ocrevalutf8 accuracy $SCRIPTPATH/$1/g$VAR.txt $SCRIPTPATH/$1/r$VAR.txt > $SCRIPTPATH/$1/report$VAR.txt
echo $SCRIPTPATH/$1/$FOLDER": folder has been processed!"

# run 0-200 --- may not work (too large)
VAR="_all_200"
FOLDER="7_final_200"
MODEL="~/.config/kraken/arabic-beirut-200.clstm"

python $SCRIPTPATH/eval.py $MODEL $SCRIPTPATH/$1/$FOLDER
cat $SCRIPTPATH/$1/$FOLDER/*.gt.txt > $SCRIPTPATH/$1/g$VAR.txt
cat $SCRIPTPATH/$1/$FOLDER/*.rec.txt > $SCRIPTPATH/$1/r$VAR.txt
ocrevalutf8 accuracy $SCRIPTPATH/$1/g$VAR.txt $SCRIPTPATH/$1/r$VAR.txt > $SCRIPTPATH/$1/report$VAR.txt
echo $SCRIPTPATH/$1/$FOLDER": folder has been processed!"

echo $SCRIPTPATH/$1": folder has been processed!"


