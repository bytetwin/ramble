# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
# https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
# <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
# option. This file may not be copied, modified, or distributed
# except according to those terms.

import os
from ramble.wmkit import *

class GkeJobset(WorkflowManagerBase):
    """Generic GKE Workflow Manager using JobSet"""

    name = "gke-jobset"
    maintainers("google-cloud")
    tags("workflow", "gke", "jobset", "generic")

    # -- Basic Metadata --

    workflow_manager_variable(
        name="job_name",
        default="{application_name}-{workload_name}-{experiment_name}",
        description="JobSet name (will act as prefix)",
    )

    workflow_manager_variable(
        name="gke_namespace",
        default="default",
        description="Kubernetes Namespace",
    )

    workflow_manager_variable(
        name="cluster_queue",
        default="cluster-queue",
        description="Kueue ClusterQueue name",
    )

    # -- Scheduling (Generic Injection) --

    workflow_manager_variable(
        name="node_selector_yaml",
        default='cloud.google.com/gke-nodepool: default-pool',
        description="Raw YAML string for spec.template.spec.nodeSelector",
    )

    workflow_manager_variable(
        name="tolerations_yaml",
        default='',
        description="Raw YAML string for spec.template.spec.tolerations",
    )

    # -- Networking --

    workflow_manager_variable(
        name="network_interfaces_json",
        default='[{\"interfaceName\":\"eth0\",\"network\":\"default\"}]',
        description="JSON string for networking.gke.io/interfaces annotation",
    )

    workflow_manager_variable(
        name="default_network_interface",
        default="eth0",
        description="Value for networking.gke.io/default-interface",
    )

    # -- Container Spec --

    workflow_manager_variable(
        name="gke_container_name",
        default="main-container",
        description="Name of the main container",
    )

    workflow_manager_variable(
        name="container_image",
        default="",
        description="Container image URI",
    )

    workflow_manager_variable(
        name="ssh_port",
        default="222",
        description="Port to run SSH server on",
    )

    workflow_manager_variable(
        name="ssh_secret_name",
        default="mpi-ssh-nccl",
        description="Name of the K8s Secret containing SSH keys",
    )

    workflow_manager_variable(
        name="container_resources_limits",
        default="nvidia.com/gpu: 8",
        description="Resource limits (YAML block)",
    )

    workflow_manager_variable(
        name="container_resources_requests",
        default="nvidia.com/gpu: 8",
        description="Resource requests (YAML block)",
    )

    # -- Volumes & Mounts (Generic Injection) --

    workflow_manager_variable(
        name="volumes_yaml",
        default="",
        description="Raw YAML string for spec.template.spec.volumes",
    )

    workflow_manager_variable(
        name="volume_mounts_yaml",
        default="",
        description="Raw YAML string for container.volumeMounts",
    )

    # -- Init Containers (Generic Injection) --

    workflow_manager_variable(
        name="init_containers_yaml",
        default="",
        description="Raw YAML string for spec.template.spec.initContainers",
    )

    # -- Scripts --

    workflow_manager_variable(
        name="pre_launch_cmd",
        default="",
        description="Command(s) to run on head node before payload (e.g. source env)",
    )

    # -- Templates --

    register_template(
        name="launcher_execute_script",
        src_path="launcher.tpl",
    )

    register_template(
        name="worker_execute_script",
        src_path="worker.tpl",
    )

    register_template(
        name="jobset_yaml",
        src_path="jobset.yaml.tpl",
        dest_path="jobset.yaml",
    )

    register_template(
        name="batch_submit",
        src_path="batch_submit.tpl",
        dest_path="batch_submit",
    )
