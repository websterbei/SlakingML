mkdir hdfs
mount -t nfs -o vers=3,proto=tcp,nolock,noacl,sync namenode:/  hdfs/
