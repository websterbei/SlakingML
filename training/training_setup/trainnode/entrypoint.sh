#!/bin/bash

mkdir /HDFS
mount -t nfs -o vers=3,proto=tcp,nolock,noacl,sync namenode:/  /HDFS

# Retrieve pytorch model file
# Start training + Serialization
# Save model to HDFS
# Exit
