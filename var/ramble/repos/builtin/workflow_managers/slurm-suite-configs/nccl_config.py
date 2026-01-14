from ramble.wmkit import *


class NCCLConfig:
    """Helper class for NCCL configurations."""

    @staticmethod
    def a3_high():
        """Define environment variables for A3 High NCCL configuration."""
        environment_variable(
            "OMPI_MCA_btl",
            "tcp,self",
            description="Set OMPI_MCA_btl",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_DEBUG",
            "INFO",
            description="Set NCCL_DEBUG",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_DEBUG_SUBSYS",
            "INIT,NET,ENV,COLL,GRAPH",
            description="Set NCCL_DEBUG_SUBSYS",
            method="set",
            workload=None,
        )
        environment_variable(
            "USE_TCPX",
            "yes",
            description="Set USE_TCPX",
            method="set",
            workload=None,
        )
        environment_variable(
            "UDS_PATH",
            "/run/tcpx-${SLURM_JOB_ID}",
            description="Set UDS_PATH",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_NET",
            "GPUDirectTCPX_v7",
            description="Set NCCL_NET",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_SOCKET_IFNAME",
            "enp0s12",
            description="Set NCCL_SOCKET_IFNAME",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_GPUDIRECTTCPX_CTRL_DEV",
            "enp0s12",
            description="Set NCCL_GPUDIRECTTCPX_CTRL_DEV",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_GPUDIRECTTCPX_SOCKET_IFNAME",
            "enp6s0,enp12s0,enp134s0,enp140s0",
            description="Set NCCL_GPUDIRECTTCPX_SOCKET_IFNAME",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_CROSS_NIC",
            "0",
            description="Set NCCL_CROSS_NIC",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_ALGO",
            "Ring",
            description="Set NCCL_ALGO",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_PROTO",
            "Simple",
            description="Set NCCL_PROTO",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_NSOCKS_PERTHREAD",
            "4",
            description="Set NCCL_NSOCKS_PERTHREAD",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_SOCKET_NTHREADS",
            "1",
            description="Set NCCL_SOCKET_NTHREADS",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_DYNAMIC_CHUNK_SIZE",
            "524288",
            description="Set NCCL_DYNAMIC_CHUNK_SIZE",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_P2P_NET_CHUNKSIZE",
            "524288",
            description="Set NCCL_P2P_NET_CHUNKSIZE",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_P2P_PCI_CHUNKSIZE",
            "524288",
            description="Set NCCL_P2P_PCI_CHUNKSIZE",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_P2P_NVL_CHUNKSIZE",
            "1048576",
            description="Set NCCL_P2P_NVL_CHUNKSIZE",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_BUFFSIZE",
            "4194304",
            description="Set NCCL_BUFFSIZE",
            method="set",
            workload=None,
        )
        environment_variable(
            "CUDA_VISIBLE_DEVICES",
            "0,1,2,3,4,5,6,7",
            description="Set CUDA_VISIBLE_DEVICES",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_NET_GDR_LEVEL",
            "PIX",
            description="Set NCCL_NET_GDR_LEVEL",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_P2P_PXN_LEVEL",
            "0",
            description="Set NCCL_P2P_PXN_LEVEL",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_GPUDIRECTTCPX_UNIX_CLIENT_PREFIX",
            "/run/tcpx-${SLURM_JOB_ID}",
            description="Set NCCL_GPUDIRECTTCPX_UNIX_CLIENT_PREFIX",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_GPUDIRECTTCPX_PROGRAM_FLOW_STEERING_WAIT_MICROS",
            "500000",
            description="Set NCCL_GPUDIRECTTCPX_PROGRAM_FLOW_STEERING_WAIT_MICROS",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_GPUDIRECTTCPX_TX_BINDINGS",
            "enp6s0:8-21,112-125;enp12s0:8-21,112-125;enp134s0:60-73,164-177;enp140s0:60-73,164-177",
            description="Set NCCL_GPUDIRECTTCPX_TX_BINDINGS",
            method="set",
            workload=None,
        )
        environment_variable(
            "NCCL_GPUDIRECTTCPX_RX_BINDINGS",
            "enp6s0:22-35,126-139;enp12s0:22-35,126-139;enp134s0:74-87,178-191;enp140s0:74-87,178-191",
            description="Set NCCL_GPUDIRECTTCPX_RX_BINDINGS",
            method="set",
            workload=None,
        )

    



        
