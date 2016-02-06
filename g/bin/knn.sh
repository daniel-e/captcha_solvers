#!/bin/bash

# imported variables
# - CAPTCHA_IMAGES_PATH  : contains the images to be classified
# - DATASET_PATH         : contains the model
# - KNN_BIN
# - KNN_SUMMARY

T=$(mktemp -d)

c=0
for i in `ls $CAPTCHA_IMAGES_PATH`; do
  d=`printf %04d $c`
  c=$((c+1))
  echo $i $d
  cp $CAPTCHA_IMAGES_PATH/$i $T/$d.$i
  $KNN_BIN -i $CAPTCHA_IMAGES_PATH/$i -d $DATASET_PATH > $T/$d.$i.txt
  convert $T/$d.$i.txt $T/$d.$i.jpg
  rm -f $T/$d.$i.txt
  convert -trim $T/$d.$i.jpg $T/$d.$i.jpg
done

convert $T/* $KNN_SUMMARY
rm -rf $T
