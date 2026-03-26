CLUSTER_CONFIG = {
    "master_config": {"num_instances": 1},
    "worker_config": {"num_instances": 2},
    "software_config": {
        "image_version": "2.1-debian11",
        "properties": {
    "spark:spark.dynamicAllocation.enabled": "true",
    "spark:spark.sql.adaptive.enabled": "true",
    "spark:spark.sql.adaptive.coalescePartitions.enabled": "true",
    "spark:spark.sql.adaptive.skewJoin.enabled": "true",
},
    },
    "lifecycle_config": {
        "idle_delete_ttl": {"seconds": 3600}
    },
    "gce_cluster_config": {
        "internal_ip_only": True,
        "service_account": SA_EMAIL,
    },
}