---
title: "Module 1: CloudBees CI Install and Supporting Components"
chapter: true
weight: 1
---

# Module 1: Cluster Creation and CloudBees CI Install with Supporting Components

This module will provide detailed instructions for creating a Google Kubernetes Engine (GKE) cluster on the Google Cloud Platform (GCP) to include an in-depth review of specific features that provide the best foundation for installing and utilizing CloudBees CI on modern platforms. We will also take a look at some useful Kubernetes tools to use with CloudBees CI.

## Container Runtime
Using Docker as the container runtime for Kubernetes has been deprecated with the v1.20 release. And starting with version 1.19, GKE defaults to using **[containerd](https://containerd.io/)** as the default container runtime. This is important from the context on continuous integrations jobs as the Docker daemon will not be available to CloudBees CI agent pods - for example to build and push a container image. We will explore other tools to build and push container images later in this workshop.


## Google Kubernetes Engine (GKE)
For the purposes of this workshop, the Google Cloud Platform provides the most accessible tools and functionality with ease of use for a semi-managed Kubernetes cluster. Where applicable, key differences and similar features between GKE, AWS EKS and Azure AKS will be noted and explained. We are going to use the GCP cloud shell and gcloud CLI to create the GKE cluster.


### GKE Autopilot
The Google Kubernetes Engine, or GKE, offers a more 'managed' experience for a cloud hosted Kubernetes environment called GKE Autopilot. Rather than managing node pools yourself, GKE Autopilot manages your worker nodes and charges you only for the cpu and memory that your pods use.

However, GKE Autopilot does not allow specifying `cluster-autoscaler.kubernetes.io/safe-to-evict: "false"` annotation on a pod, and the CloudBees CI Kubernetes controller provisioning automatically applies that annotation. Therefore, we will be creating a *standard** GKE cluster for this workshop.

{{% notice info %}}
GKE Autopilot is similar to AWS EKS Fargate. Pricing for both is based on the actual CPU, memory and storage used by Kubernetes pods, not based on the nodes (virtual instances) the pods are running on. 
{{% /notice %}}

### Organizational Compliance
Most organizations, including CloudBees, have specific rules in regards to cloud infrastructure utilization. For example, CloudBees only allows GCP VMs (GKE nodes/node pools) to be created in the `useast1` region and does not allow external IPs by default. The Ops team has provided us an exception to allow the use of external IPs in the `core-workshop` GCP project. But we still need to only use the `useast1` region. Therefore, we will be creating our clusters in the `core-workshop` project and in the `useast1` region.

### Container Storage Interface
The Container Storage Interface (CSI), which became GA with Kubernetes v1.13 is the future of storage for Kubernetes. Prior to the introduction of the CSI, plugins for integrating storage (volumes) with Kubernetes were in-tree, that is, they were part of the core Kubernetes code base. So, when support needed to added for a new storage system or new features for an existing one, then it was dependent on the Kubernetes release process. With the adoption of CSI, the storage integration eco-system with Kubernetes is easily extensible and new storage systems and features can be added to Kubernetes without any modifications to the core Kubernetes code.

In addition to being the future direction of volume storage for Kubernetes, CSI provides some additional features that were not available with the in-tree volume plugins. One such feature is [topology awareness](https://kubernetes-csi.github.io/docs/topology.html) that enables Kubernetes to support regions and zone specific volumes. GCP takes advantage of this capability by providing [regional persistent disks](https://cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#regional_persistent_disks) - multi-zonal resources that replicate data between two zones in the same region, and can be used similarly to zonal persistent disks. This feature would allow you to deploy CloudBees CI across two zones with automatic failover if one zone became unavailable. So, one of the first decisions you need to make when creating a GKE cluster is if you want it to be zonal or regional; and it is really a question of required uptime versus cost.

### Installation Tools

We will be using the Google Cloud Shell to create the GKE cluster and install CloudBees CI. One benefit of using Google's Cloud Shell for this workshop is that it comes with the tools we need preinstalled. They include:

- **git**: You won't actually be using it yourself, but when you launch the Cloud Shell with the link mentioned below it will automatically clone the `cloudbees-ci-k8s-cloudshell-tutorials` repository into you Cloud Shell environment. The files include the actual instructions and the different manifest and configuration files we will be using in the workshop.
- **gcloud**: The `gcloud` CLI will be used to create the GKE cluster and set-up/configure other necessary GCP services.
- **kubectl**: Will be used to create and configure necessary Kubernetes resources.
- **helm:** Helm is a tool that makes it easier to install and manage Kubernetes applications via charts that define the Kubernetes resources needed by the application. We will use the `helm` CLI to install every application/tool that has support for helm to include CloudBees CI itself.

## Labs

THe labs for this workshop will leverage the Google Cloud Shell tutorial format. Navigate to the **cloudbees-ci-k8s-cloudshell-tutorials** repository in the GitHub Organization you created for this workshop and click on the **OPEN IN GOOGLE CLOUD SHELL** button.


