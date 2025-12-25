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

# 3. Load CUDA Libs (Generic check)
if [ -x /sbin/ldconfig ]; then
  /sbin/ldconfig
fi

# 4. Define Hostname/Rank Variables (Generic JobSet Logic)
export POSTFIX=$(hostname | cut -d . -f 2-)
export WORKERS_BASENAME=$(hostname | cut -d . -f 1 | rev | cut -d - -f 2- | rev )
export NODE_RANK=$JOB_COMPLETION_INDEX

# 5. Populate Hostfile (Discovery)
echo "Discovering hosts..."
for i in `seq 0 $(( {n_nodes} - 1 ))`; do
  OTHER=${WORKERS_BASENAME}-${i}.${POSTFIX}
  until ssh -p {ssh_port} -o StrictHostKeyChecking=no $OTHER hostname; do
    echo "Waiting for ${OTHER}..."
    sleep 5
  done
  echo "${OTHER} port={ssh_port} slots=8" >> /tmp/hostfile
done

echo "Hostfile defined:"
cat /tmp/hostfile

# 6. Run Pre-Launch Payload (e.g. source env scripts)
{pre_launch_cmd}

# 7. Run the Command (Injected by Ramble)
cd "{experiment_run_dir}"
{command}
