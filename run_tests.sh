#!/bin/sh

SCRIPTPATH=`pwd`

echo $SCRIPTPATH

# creating manifests
cd $SCRIPTPATH/$17_final_a && ls *.png > manifest.txt
cd $SCRIPTPATH/$17_final_b && ls *.png > manifest.txt
cd $SCRIPTPATH/$17_final_a_200 && ls *.png > manifest.txt
cd $SCRIPTPATH/$17_final_b_200 && ls *.png > manifest.txt

# run
python eval.py -p ~/.config/kraken/arabic-bairut.clstm $SCRIPTPATH/$17_final_a
cat $SCRIPTPATH/$17_final_a/*.gt.txt > $SCRIPTPATH/$1g_a.txt
cat $SCRIPTPATH/$17_final_a/*.rec.txt > $SCRIPTPATH/$1r_a.txt
ocrevalutf8 accuracy $SCRIPTPATH/$1g_a.txt $SCRIPTPATH/$1r_a.txt

echo $SCRIPTPATH/$1": folder has been processed!"


