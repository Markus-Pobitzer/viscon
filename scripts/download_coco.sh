#!/bin/bash

DATASET_PATH=dataset/coco

# Validation set
if ! ls $DATASET_PATH/val2017/*.jpg 1> /dev/null 2>&1; then
    bash scripts/dataset_import/coco.sh $DATASET_PATH val2017
fi

# Training set
if ! ls $DATASET_PATH/train2017/*.jpg 1> /dev/null 2>&1; then
    # bash scripts/dataset_import/coco.sh $DATASET_PATH train2017
fi

# Annotations
if ! ls $DATASET_PATH/annotations/*2017.json 1> /dev/null 2>&1; then
    wget -c http://images.cocodataset.org/annotations/annotations_trainval2017.zip -O $DATASET_PATH/annotations_trainval2017.zip
    unzip $DATASET_PATH/annotations_trainval2017.zip -d $DATASET_PATH/
    rm $DATASET_PATH/annotations_trainval2017.zip
fi
