import sys
import os
from ramble.repository import ObjectTypes, paths

config_dir = paths[ObjectTypes.workflow_managers].repo_for_obj("slurm-suite-configs").dirname_for_object_name("slurm-suite-configs")
sys.path.append(config_dir)

from nccl_config import NCCLConfig
from ramble.wmkit import *
from ramble.experiment_result import ExperimentStatus
from ramble.wm.builtin.slurm import Slurm

class SlurmSuiteConfigs(Slurm):
  """Configurations for the various machine types supported by CHS"""

  name = "slurm-suite-configs"

  tags("gcp-configs")

  maintainers("bytewin")

  variant(
      "machine_type",
      default="{machine_type}",
      description="Machine type for the suite",
  )

  variable(
      "machine_type",
      default="a3-ultra",
      description="Machine type for the suite",
      values=["a3-high", "a3-mega", "a3-ultra", "a4", "a4x", "tpuv7x"],
  )

  # variable(
  #     "n_nodes",
  #     default="1",
  #     description="Number of nodes",
  # )

  # variable(
  #     "processes_per_node",
  #     default="1",
  #     description="Default processes per node",
  # )

  with when("machine_type=a3-high"):
    with when("application_name=nccl-tests"):
      NCCLConfig.a3_high()

  with when("machine_type=a3-ultra"):
    variable("gpus_per_node", default="8", description="A3U gpus per node")
    
    with when("application_name=nccl-tests"):
      environment_variable(
          "NCCL_NET",
          "gIB",
          description="Set NCCL_NET",
          method="set",
          workload=None,
      )

      environment_variable(
          "OMPI_MCA_btl_tcp_if_include",
          "enp0s19",
          description="Set OMPI_MCA_btl_tcp_if_include",
          method="set",
          workload=None,
      )

      environment_variable(
          "OMPI_MCA_btl",
          "tcp,self",
          description="Set OMPI_MCA_btl",
          method="set",
          workload=None,
      )
      environment_variable(
          "LD_LIBRARY_PATH",
          "/usr/local/gib/lib64:/usr/local/nvidia/lib",
          description="Set LD_LIBRARY_PATH",
          method="set",
          workload=None,
      )

      variable(
        "processes_per_node",
        default="{gpus_per_node}",
        description="A3U nccl-tests processes per node",
      )
      
      variable(
          "container_name",
          default="nccl-plugin-gib-diagnostic:v1.1.0",
          description="slurm pyxis container name for nccl diagnostics",
      )
      variable(
          "container_uri",
          default="docker://us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic:v1.1.0",
          description="slurm pyxis container url for nccl diagnostics",
      )

      variable("nccl-tests_path", default='None', description="path to nccl tests")

      workflow_manager_variable(
          "srun_args",
          default="--mpi=pmix --container-workdir /third_party/nccl-tests/build/ --container-image {container_path} --container-mounts \"/usr/local/gib,/var/tmp\" --container-writable --wait=60",
          description="srun args for a3 ultra nccl test",
      )

      workflow_manager_variable("mpi_command", default="srun {srun_args}", description="slurm mpi command")
  
  # def get_status(self, workspace):
  #   return ExperimentStatus.UNRESOLVED