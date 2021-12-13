---
title: "Module 2: Managing Controllers and Security"
chapter: true
weight: 1
---

# Module 2: Managing Controllers and Security

This module will provide an overview of the default Kubernetes RBAC configuration for CloudBees CI. We will also explore the provisioning and  management of CloudBees CI Managed Controllers in separate Kubernetes `namespaces` with Kubernetes network policies. Using controller specific Kubernetes `namespaces` aligns with the best practice of distributing software delivery workload across multiple controllers by providing additional isolation and security. What's the point of using CloudBees CI RBAC to limit access to individual managed controllers, when a `pod` based agent used by any of those managed controllers have access complete and total access to all of the managed controller `pods`?