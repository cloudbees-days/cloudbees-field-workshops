name: pipeline-template-catalog-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI Pipeline Template Catalogs

---
name: agenda-templates
# Agenda

1. Workshop Tools Overview
2. CloudBees CI Overview
3. Setup for Labs
4. .blue-bold[Pipeline Manageability & Governance with Templates]
5. Configuration as Code (CasC) with CloudBees CI
6. Pipeline Manageability & Governance with Policies
7. Configuration as Code (CasC) for Developers
8. Contextual Feedback for Pipelines
9. Cross Team Collaboration
10. Hibernating Managed Controllers

---
name: pipeline-template-catalog

# Pipeline Template Catalogs

Pipeline Template Catalogs provide version controlled parameterized templates for Multibranch and stand-alone Pipeline jobs, and help ensure that Pipeline jobs conform to organizational standards.

Benefits of using Pipeline Template Catalogs include:

* Providing developers with a simplified and directed experience for configuring Pipeline in “domain specific” terms that make sense for an organization. This allows developers to focus on shipping software.
* Organizing Pipelines per projects and/or teams. Similar-looking jobs that only differ in a few aspects can be easily parameterized on a per job basis. When you change a template, all the jobs created from that template get updated automatically.

When combined with Pipeline Shared Libraries, Pipeline Template Catalogs provide an easy way to make your organization's Pipelines reusable — boosting cross-team collaboration, saving time and reducing errors.

???
Pipeline Template Catalogs help ensure that Pipeline jobs conform to organizational standards and when used in combination with Shared Libraries provide reusable Pipelines — boosting cross-team collaborations, saving time and reducing errors.

Pipeline Shared Libraries and Pipeline Template Catalogs can 'live' in the same source code repository.

---
name: pipeline-template-catalog-lab-link

# Lab - Pipeline Template Catalog

* In this lab you will use the CloudBees CI CLI to create a Pipeline Template Catalog from the `pipeline-template-catalog` repository that was forked (copied) into your workshop GitHub Organization.
* The *Pipeline Template Catalog* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/module-1/pipeline-template-catalog/

---
name: pipeline-template-catalog-overview

# Pipeline Template Catalog Overview

* Imported a Pipeline Template Catalog from a GitHub repository
* Used a CloudBees Folders Plus feature to restrict what type of jobs can be created in a folder
