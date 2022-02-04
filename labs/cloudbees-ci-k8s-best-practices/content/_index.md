---
title: "CloudBees CI on Kubernetes Workshop"
chapter: true
weight: 1
---

# CloudBees CI on Kubernetes Workshop

The CloudBees CI on Kubernetes Workshop provides a detailed hands-on tutorial for installing and managing the CloudBees CI solution on Kubernetes to include best practices for running CloudBees CI in a production Kubernetes cluster.

## High-level Architecture

A CloudBees CI deployment on Kubernetes primarily consists of workload and networking related resources. CloudBees CI Operations Center and all managed controllers are deployed as a Kubernetes **StatefulSet**, along with a Kubernetes **Service** and **Ingress** network resource.

### StatefulSet
Like a **Deployment**, a StatefulSet manages Pods that are based on an identical container spec. Unlike a Deployment, a StatefulSet maintains a sticky identity for each of their Pods. A Kubernetes **StatefulSet** provides persistent **Pod** identifiers that make it easier to match existing persistent volumes to new **Pods** that replace any that have failed.

### Service and Ingress
A Kubernetes **Service** resource is an abstraction which defines a logical set of **Pods** and a policy by which to access them, usually determined by a selector.

A Kubernetes **Ingress** resource exposes HTTP and HTTPS routes from outside the cluster to Kubernetes **Service** resources.

## Module 1: CloudBees CI Install and Supporting Components

1. Creating the GKE Cluster via the CLI
    1. Auto-scaling and Scheduling
    2. Single Zone vs Multi-Zone Clusters
    3. Container Storage Interface 
        1. Regional Disk
        2. Resize Volumes
        3. Snapshots
    4. Workload Identity
2. Install Supporting Components
    1. Nginx Ingress
    2. Certmanager
3. Installation of CloudBees CI
    1. Helm Values
    2. CasC for Operations Center
    3. Additional Automation - Init Groovy Startup Scripts
    4. Helm Install

## Module 2: Managed Controllers and Security

1. CloudBees CI RBAC Overview
2. Provision Controllers in Separate Namespaces
3. Kubernetes Network Policies

## Module 3: CloudBees CI Workload on Kubernetes

1. Jenkins Agents on Kubernetes
2. Resource Requests, Limits and Quotas
3. Cloud IAM for Agents
    1. Workload Identity for Jenkins Agent Pods
3. Building Container Images without Docker
4. Cloud Secrets Managers

## Module 4: Advanced Topics

1. Creating GKE Cluster with Terraform
2. OPA - Open Policies Agent
2. Multi-Region Disaster Recovery
    1. Install Velero
    2. Create Backup Schedule
    3. Restore Backup in Another Region
3. Vault Integration
4. Multi Cloud
5. Hybrid Cloud


## Other
Use Namespaces for Organization and Management of Resources

Use Resource Requests and Limits



