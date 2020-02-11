#!/bin/bash

mkdir /HDFS
mount -t nfs -o vers=3,proto=tcp,nolock,noacl,sync namenode:/  /HDFS
mkdir /HDFS/MODELS
mkdir /HDFS/DATASETS

cd training && python main.py