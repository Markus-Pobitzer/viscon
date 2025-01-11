#!/bin/bash

DATASET_PATH=$1
COCO_SPLIT=$2

ZIP_PATH=$DATASET_PATH/$COCO_SPLIT.zip
mkdir -p $DATASET_PATH


wget -c http://images.cocodataset.org/zips/$COCO_SPLIT.zip -O $ZIP_PATH
unzip $ZIP_PATH -d $DATASET_PATH
rm $ZIP_PATH
