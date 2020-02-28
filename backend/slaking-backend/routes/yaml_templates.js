
function getTrainingDeploymentYaml(training_job_id) {
    yamlString = `
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: model-training-${training_job_id}
    spec:
      template:
        spec:
          containers:
          - env:
            - name: SLAKING_JOB_ID
              value: ${training_job_id}
            - name: CORE_CONF_fs_defaultFS
              valueFrom:
                configMapKeyRef:
                  key: CORE_CONF_fs_defaultFS
                  name: datanode-hadoop-env
            - name: CORE_CONF_hadoop_http_staticuser_user
              valueFrom:
                configMapKeyRef:
                  key: CORE_CONF_hadoop_http_staticuser_user
                  name: datanode-hadoop-env
            - name: CORE_CONF_hadoop_proxyuser_hdfs_groups
              valueFrom:
                configMapKeyRef:
                  key: CORE_CONF_hadoop_proxyuser_hdfs_groups
                  name: datanode-hadoop-env
            - name: CORE_CONF_hadoop_proxyuser_hdfs_hosts
              valueFrom:
                configMapKeyRef:
                  key: CORE_CONF_hadoop_proxyuser_hdfs_hosts
                  name: datanode-hadoop-env
            - name: CORE_CONF_hadoop_proxyuser_hue_groups
              valueFrom:
                configMapKeyRef:
                  key: CORE_CONF_hadoop_proxyuser_hue_groups
                  name: datanode-hadoop-env
            - name: CORE_CONF_hadoop_proxyuser_hue_hosts
              valueFrom:
                configMapKeyRef:
                  key: CORE_CONF_hadoop_proxyuser_hue_hosts
                  name: datanode-hadoop-env
            - name: CORE_CONF_hadoop_proxyuser_root_groups
              valueFrom:
                configMapKeyRef:
                  key: CORE_CONF_hadoop_proxyuser_root_groups
                  name: datanode-hadoop-env
            - name: CORE_CONF_hadoop_proxyuser_root_hosts
              valueFrom:
                configMapKeyRef:
                  key: CORE_CONF_hadoop_proxyuser_root_hosts
                  name: datanode-hadoop-env
            - name: CORE_CONF_io_compression_codecs
              valueFrom:
                configMapKeyRef:
                  key: CORE_CONF_io_compression_codecs
                  name: datanode-hadoop-env
            - name: HDFS_CONF_dfs_namenode_datanode_registration_ip___hostname___check
              valueFrom:
                configMapKeyRef:
                  key: HDFS_CONF_dfs_namenode_datanode_registration_ip___hostname___check
                  name: datanode-hadoop-env
            - name: HDFS_CONF_dfs_permissions_enabled
              valueFrom:
                configMapKeyRef:
                  key: HDFS_CONF_dfs_permissions_enabled
                  name: datanode-hadoop-env
            - name: HDFS_CONF_dfs_webhdfs_enabled
              valueFrom:
                configMapKeyRef:
                  key: HDFS_CONF_dfs_webhdfs_enabled
                  name: datanode-hadoop-env
            - name: MAPRED_CONF_mapred_child_java_opts
              valueFrom:
                configMapKeyRef:
                  key: MAPRED_CONF_mapred_child_java_opts
                  name: datanode-hadoop-env
            - name: MAPRED_CONF_mapreduce_framework_name
              valueFrom:
                configMapKeyRef:
                  key: MAPRED_CONF_mapreduce_framework_name
                  name: datanode-hadoop-env
            - name: MAPRED_CONF_mapreduce_map_env
              valueFrom:
                configMapKeyRef:
                  key: MAPRED_CONF_mapreduce_map_env
                  name: datanode-hadoop-env
            - name: MAPRED_CONF_mapreduce_map_java_opts
              valueFrom:
                configMapKeyRef:
                  key: MAPRED_CONF_mapreduce_map_java_opts
                  name: datanode-hadoop-env
            - name: MAPRED_CONF_mapreduce_map_memory_mb
              valueFrom:
                configMapKeyRef:
                  key: MAPRED_CONF_mapreduce_map_memory_mb
                  name: datanode-hadoop-env
            - name: MAPRED_CONF_mapreduce_reduce_env
              valueFrom:
                configMapKeyRef:
                  key: MAPRED_CONF_mapreduce_reduce_env
                  name: datanode-hadoop-env
            - name: MAPRED_CONF_mapreduce_reduce_java_opts
              valueFrom:
                configMapKeyRef:
                  key: MAPRED_CONF_mapreduce_reduce_java_opts
                  name: datanode-hadoop-env
            - name: MAPRED_CONF_mapreduce_reduce_memory_mb
              valueFrom:
                configMapKeyRef:
                  key: MAPRED_CONF_mapreduce_reduce_memory_mb
                  name: datanode-hadoop-env
            - name: MAPRED_CONF_yarn_app_mapreduce_am_env
              valueFrom:
                configMapKeyRef:
                  key: MAPRED_CONF_yarn_app_mapreduce_am_env
                  name: datanode-hadoop-env
            - name: SERVICE_PRECONDITION
              value: namenode:9870
            - name: YARN_CONF_mapred_map_output_compress_codec
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_mapred_map_output_compress_codec
                  name: datanode-hadoop-env
            - name: YARN_CONF_mapreduce_map_output_compress
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_mapreduce_map_output_compress
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_log___aggregation___enable
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_log___aggregation___enable
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_log_server_url
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_log_server_url
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_nodemanager_aux___services
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_nodemanager_aux___services
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_nodemanager_disk___health___checker_max___disk___utilization___per___disk___percentage
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_nodemanager_disk___health___checker_max___disk___utilization___per___disk___percentage
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_nodemanager_remote___app___log___dir
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_nodemanager_remote___app___log___dir
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_nodemanager_resource_cpu___vcores
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_nodemanager_resource_cpu___vcores
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_nodemanager_resource_memory___mb
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_nodemanager_resource_memory___mb
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_resourcemanager_address
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_resourcemanager_address
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_resourcemanager_fs_state___store_uri
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_resourcemanager_fs_state___store_uri
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_resourcemanager_hostname
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_resourcemanager_hostname
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_resourcemanager_recovery_enabled
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_resourcemanager_recovery_enabled
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_resourcemanager_resource__tracker_address
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_resourcemanager_resource__tracker_address
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_resourcemanager_scheduler_address
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_resourcemanager_scheduler_address
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_resourcemanager_scheduler_class
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_resourcemanager_scheduler_class
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_resourcemanager_store_class
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_resourcemanager_store_class
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_resourcemanager_system___metrics___publisher_enabled
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_resourcemanager_system___metrics___publisher_enabled
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_scheduler_capacity_root_default_maximum___allocation___mb
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_scheduler_capacity_root_default_maximum___allocation___mb
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_scheduler_capacity_root_default_maximum___allocation___vcores
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_scheduler_capacity_root_default_maximum___allocation___vcores
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_timeline___service_enabled
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_timeline___service_enabled
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_timeline___service_generic___application___history_enabled
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_timeline___service_generic___application___history_enabled
                  name: datanode-hadoop-env
            - name: YARN_CONF_yarn_timeline___service_hostname
              valueFrom:
                configMapKeyRef:
                  key: YARN_CONF_yarn_timeline___service_hostname
                  name: datanode-hadoop-env
            image: websterbei/trainnode:v1
            name: trainnode
            imagePullPolicy: Always
            ports:
            - containerPort: 9866
              protocol: TCP
            - containerPort: 9867
              protocol: TCP
            - containerPort: 9864
              protocol: TCP
          restartPolicy: Never
    `;
    return yamlString;
}

module.exports = {getTrainingDeploymentYaml};