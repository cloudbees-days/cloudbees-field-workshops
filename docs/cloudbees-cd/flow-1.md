
name: cloudbees product naming
# Cloudbees Product Naming

 ##  Cloudbees products have been renamed.

 - ElectricCloud ElectricFlow, now called Cloudbees CD/RO

 - Cloudbees EJC now called Cloudbees CI

 - All come together to make the SDA - Software Delivery Automation platform


---
layout: true

.header[
]

.footer[
- © 2020 CloudBees, Inc.
- ![:scale 100%](../img/CloudBees-Submark-Full-Color.svg)
]
---
name: cloudbees cd fundamentals
# Cloudbees CD/RO Fundamentals
- Overview of Release Orchestration
- Overview of Deployment Automation
- Cloudbees CD/RO Architecture Overview
 - Single Server Architecture
 - Clustered Server Architecture
---
layout: true

.header[
]

.footer[
- © 2020 CloudBees, Inc.
- ![:scale 100%](../img/CloudBees-Submark-Full-Color.svg)
]
---
name: enterprise landscape

![:scale 100%](../../img/cloudbees-cd/enterprise_application_landscape.png)

---
name: enterprise landscape emerging technologies

# R&D / Emerging Technologies:
Highly-innovative teams using simplified CI/CD and thoroughly modern architecture and infrastructure, building applications from scratch
Attributes:
- Building microservice and/or cloud-native applications
- Adopting Kubernetes and other emerging technology
- Focus on innovation over governance - centralized control less important than developer flexibility
- Need to select best tools for the job and each team may have unique needs
- Need ways of proving and promoting successful efforts

---
name: enterprise landscape modernization targets

# Modernization Target Applications
Modernization of/within heritage applications as part of a Digital and/or DevOps Transformation.
Attributes:
 - Re-architecting a heritage application (or brand new development) to be able to leverage modernized CI & CD practices and/or cloud platforms for faster delivery of features to market
- Typically lots of dependencies on heritage systems and services
- Impacted applications/components are selected and prioritized based on impact to the business (risk vs reward)
- Looking into appropriate emerging technologies such as Kubernetes, cloud providers

---
name: enterprise landscape critical apps

# Mission-Critical/Revenue-Generating Apps
Applications that hold higher value, and risk, for the organization
Attributes:
- Typically heritage applications; monolithic; complex (but not always)
- Longer release cycles with a combination of automated and manual tasks - risk to the business to miss gates, fail audit, etc.
- Need to centralize and consolidate processes
- May be considering “lift and shift” to cloud (re-host) migration
- Need really scalable, stable CI & CD tooling, auditing, governance, and strong analytics
- Want to improve practices, but with control

---
name: enterprise landscape internal systems

# Internal Systems
Systems with indirect customer value and not customer-facing (e.g. billing, CRM, HR)
Attributes:
- Internal applications (usually COTS e.g. CRM, Oracle, Sharepoint, ETL, payroll)
- Typically older technology with traditional infrastructure
- Replacement with SaaS/PaaS could be under consideration
- Highly necessary for business, but does not directly interface with customer so seen as cost center
- Need specific domain knowledge and tooling to maintain - limited SMEs and bandwidth for changes
- Not as iterative, longer release cycles; Focus on repeatability and reliability

---
name: enterprise landscape phasing out

# Phasing Out
No longer business-relevant functions
Attributes:
- New ways of doing business have made the functions here obsolete
- Something of technical value may still be present or required
- May have low touch development in the meantime
- Established business processes that may/may not be worth automating
- Poor/long CI & CD practices and very manual; no need for investment in improvement
