#!/bin/bash

datadir=`echo $HDFS_CONF_dfs_datanode_data_dir | perl -pe 's#file://##'`
if [ ! -d $datadir ]; then
  echo "Datanode data directory not found: $datadir"
  exit 2
fi

cd training
/miniconda/bin/python main.py -test 5e4efe4f079e34674989e1f8