from ramble.wmkit import *
from ramble.context import create_context_from_dict
from itertools import combinations
import copy

class TestHelper:

  @staticmethod
  def dcgm_diag(variables, experiment_name):
    variables['node'] = variables.get("nodes")
    variables['process_per_node'] = "1"
    variables['n_ranks'] = "1"
    variables['diag_level'] = [1, 2]
    variables["extra_sbatch_headers"] = '#SBATCH -w {node}'

    experiment_template_name = experiment_name + "-dcgm-r{diag_level}-{node}"
    exp_context = create_context_from_dict(
        experiment_template_name,
        {
            "variables": variables,
            "matrix": ["node", "diag_level"],
        }
    )
    return exp_context

  @staticmethod
  def nccl_test(variables, experiment_name, workload):
    variables['n_nodes'] = len(variables.get("nodes"))
    
    machine_type = variables.get("machine_type")
    

    modifiers = [{"name": "pyxis-enroot"}]
    if machine_type == "a3-ultra":
        modifiers.append({"name": "nccl-gib"})
    
    experiment_template_name = experiment_name + f"-nccl-{workload}"
    exp_context = create_context_from_dict(
        experiment_template_name,
        {
            "variables": variables,
            "modifiers": modifiers,
        }
    )
    return exp_context

  @staticmethod
  def nccl_pairwise(variables, experiment_name, workload="all-reduce"):
    nodes = variables.get("nodes")
    

    if not nodes or len(nodes) < 2:
        return []
    
    machine_type = variables.get("machine_type")
    
    modifiers = [{"name": "pyxis-enroot"}]
    if machine_type == "a3-ultra":
        modifiers.append({"name": "nccl-gib"})

    contexts = []
    
    for i, (n1, n2) in enumerate(combinations(nodes, 2)):
        pair_vars = copy.deepcopy(variables)
        pair_vars["nodes"] = [n1, n2]
        pair_vars["n_nodes"] = 2
        pair_vars["extra_sbatch_headers"] = '#SBATCH -w "{n1},{n2}"'
        
        pair_template_name = f"{experiment_name}-nccl-pairwise-{workload}-{n1}-{n2}"
        ctx = create_context_from_dict(
            pair_template_name,
            {
                "variables": pair_vars,
                "modifiers": modifiers,
            }
        )
        contexts.append(ctx)
        
    return contexts
