apiVersion: jobset.x-k8s.io/v1alpha2
kind: JobSet
metadata:
  generateName: {job_name}-
  namespace: {gke_namespace}
  labels:
    kueue.x-k8s.io/queue-name: {cluster_queue}
spec:
  ttlSecondsAfterFinished: 86400
  network:
    enableDNSHostnames: true
    publishNotReadyAddresses: true
  replicatedJobs:
    - name: w
      template:
        spec:
          parallelism: {n_nodes}
          completions: {n_nodes}
          template:
            metadata:
              annotations:
                kueue.x-k8s.io/podset-preferred-topology: "kubernetes.io/hostname"
                networking.gke.io/default-interface: '{default_network_interface}'
                networking.gke.io/interfaces: |
                  {network_interfaces_json}
            spec:
              restartPolicy: Never
              
              # -- Node Selector (Generic Injection) --
              nodeSelector:
{node_selector_yaml}

              # -- Tolerations (Generic Injection) --
              tolerations:
{tolerations_yaml}

              setHostnameAsFQDN: true
              
              # -- Volumes (Generic Injection) --
              volumes:
              - name: mpi-id
                secret:
                  secretName: {ssh_secret_name}
                  items:
                  - key: ssh-privatekey
                    path: "id_rsa"
                  - key: ssh-publickey
                    path: "id_rsa.pub"
              # User defined volume list
{volumes_yaml}

              # -- Init Containers (Generic Injection) --
              initContainers:
{init_containers_yaml}

              containers:
              - name: {gke_container_name}
                stdin: true
                tty: true
                image: {container_image}
                env:
                - name: OMPI_ALLOW_RUN_AS_ROOT
                  value: "1"
                - name: OMPI_ALLOW_RUN_AS_ROOT_CONFIRM
                  value: "1"
                - name: MY_NODE_NAME
                  valueFrom:
                    fieldRef:
                      fieldPath: spec.nodeName
                command:
                - bash
                - -c
                - |
                  # --- Launcher Script (Generic) Logic injected by Ramble ---
                  if [[ "$JOB_COMPLETION_INDEX" -eq "0" ]]; then
                    {launcher_execute_script}
                  else
                    {worker_execute_script}
                  fi
                  # ----------------------------------------------------------

                # -- Volume Mounts (Generic Injection) --
                volumeMounts:
                - name: mpi-id
                  mountPath: "/secrets/ssh"
                  readOnly: true
                # User defined mounts (indented by 16 spaces)
{volume_mounts_yaml}

                resources:
                  limits:
                    {container_resources_limits}
                  requests:
                    {container_resources_requests}
              restartPolicy: Never
