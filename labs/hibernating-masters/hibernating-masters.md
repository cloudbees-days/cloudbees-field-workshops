# <img src="images/cloudbeescore_logo.png" alt="CloudBees Core Logo" width="40" align="top"> CloudBees Core - Hibernating Masters

The [CloudBees Core Managed Master hibernation](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) feature takes advantage of running Core on Kubernetes by automatically shutting down or hibernating Team/Managed Masters. This is done by scaling the Kubernetes StatefulSet down to zero replicas.

There are several ways that costs are reduced with Managed Master hibernation:

1. When using Kubernetes auto-scaling and a Managed Master is hibernated then the Kubernetes cluster has the potential to downscale by removing a node.
2. When a Managed Master is hibernated you immediately gain additional CPU and memory on the node where your Team/Managed Master pod was running - this additional capacity is immediately available for Kubernetes based agents reducing the possibility of agents queueing and/or triggering an upscaling of your Kubernetes cluster. 

## Configure Hibernation
The Master Hibernation is managed at the global Jenkins configuration level.

## Hibernation Proxy for Webhooks
The hibernating monitor service provides a post proxy for things like GitHub webhooks.

## Waking Your Master
Just click on it silly :) But seriously, it will take a few minutes to wake-up as Jenkins is a heavy sleeper. So, while your Team Master is waking from its gentle slumber, let's find something to divert our attention from how long it actually takes a Core Managed Master to un-hibernate.

You may proceed to the next lab: [*Cross Team Collaboration*](../cross-team-collaboration/cross-team-collaboration.md) or choose another lab on the [main page](../../README.md#workshop-labs).