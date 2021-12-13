---
title: "CloudBees CI Kubernetes RBAC"
chapter: true
weight: 2
---

#  CloudBees CI Kubernetes RBAC

By default, with `rbac` and `hibernation` enabled, the CloudBees CI Helm chart creates four `ServiceAccounts` in your CloudBees CI `Namespace` (in addition to the `default` `ServiceAccount` that is automatically created for all `Namespaces`):

1. `cjoc`: the service account that the Operations Center `pod` runs as. It must have RBAC permissions to manage the lifecycle of managed controllers in Kubernetes.
2. `jenkins`: the service account that managed controller `pods` run as. It must have RBAC permissions to provision `pod` based agents.
3. `jenkins-agents`: 
4. `managed-master-hibernation-monitor`: the service account that the hibernation monitor service `pod` runs as. It must have permissions to scale the replicas of the managed controller `statefulsets` to 0 and scale them back up to 1.

The permissions for these service accounts are defined in 4 Kubernetes `roles`:

1. `cjoc-master-management`: bound to the `cjoc` service account with the `cjoc-role-binding` `RoleBinding`; it provides the most extensive set of permissions for any CloudBees CI component, to include: 
    - full CRUD for `statefulsets` so that CJOC is able to manage the entire life-cycle of managed controllers.
    - full CRUD for `persistentvolumeclaims` so that CJOC is able to manage the `persistentvolumeclaims` of managed controllers.
    - full CRUD for `ingresses` so that CJOC is able to manage `ingresses` for managed controllers.
    - 
2. `cjoc-agents`: bound to the `jenkins` service account with the `cjoc-master-role-binding` `RoleBinding`; it provides the necessary permissions to provision and interact with `pod` based agents.
3. `managed-master-hibernation-monitor`: bound to the `managed-master-hibernation-monitor` service account

There is also 1 `clusterrole` that is optionally enabled:

1. `cjoc-master-management-{{ .Release.Namespace }}`: bound to the `cjoc` service account; it provides the ability to select a `storageclass` from the managed controller config when creating a managed controller via the UI.

