#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive

# 1. Setup SSH Keys (Mounted from Secret)
mkdir -p /run/sshd ~/.ssh
chmod 700 ~/.ssh
cp /secrets/ssh/* ~/.ssh/
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/*

# 2. Start SSH Server
mkdir -p /run/sshd
/sbin/sshd

# 3. Load CUDA Libs
/sbin/ldconfig

# 4. Wait Loop
#    Just like wait_worker_nodes, we ping the head node to stay alive.
export POSTFIX=$(hostname | cut -d . -f 2-)
export WORKERS_BASENAME=$(hostname | cut -d . -f 1 | rev | cut -d - -f 2- | rev )
HEAD_NODE="${WORKERS_BASENAME}-0.${POSTFIX}"

echo "Worker started. Waiting for head node ${HEAD_NODE}..."

# We sleep in a loop so the pod doesn't exit. 
# The Head Node will eventually SSH into us and run the MPI wrapper.
# When the JobSet finishes (head node exits), Kubernetes will terminate us.
while ping -c 1 ${HEAD_NODE} > /dev/null 2>&1; do
  sleep 5
done

# Fallback: If ping fails (network issue or head node gone), wait a bit then exit
sleep 60
