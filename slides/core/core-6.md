name: core-setup-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees Core Hibernating Masters

---
name:

# CloudBees Core Hibernating Masters

[CloudBees Core Managed Master hibernation](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) takes advantage of running Core on Kubernetes by automatically shutting down or hibernating Team/Managed Masters. This is done by scaling the Kubernetes StatefulSet down to zero replicas.

---
name: hibernating-masters-cost-saving

# How Hibernating Masters Reduce Infrastructure Costs

There are several ways that costs may be reduced with Managed Master hibernation:

1. When using Kubernetes auto-scaling and a Managed Master is hibernated then the Kubernetes cluster has the potential to downscale by removing a node.
2. When a Managed Master is hibernated you immediately gain additional CPU and memory on the node where your Team/Managed Master pod was running - this additional capacity is immediately available for Kubernetes based agents reducing the possibility of agents queueing and/or triggering an upscaling of your Kubernetes cluster. 

---

## Lab

[https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/hibernating-masters/hibernating-masters.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/hibernating-masters/hibernating-masters.md)

???

All presenters should familiarize themselves with the hibernation monitor design document: https://github.com/cloudbees/managed-master-hibernation-monitor/blob/master/design.md 