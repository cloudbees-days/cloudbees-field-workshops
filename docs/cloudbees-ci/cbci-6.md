name: using-templates-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI<br>Using Pipeline Templates

---
name: agenda-setup
class: compact

# Agenda

1. <a class="no-style" href="#workshop-tools">Workshop Tools Overview</a>
2. <a class="no-style" href="#core-overview-title">CloudBees CI Overview</a>
3. <a class="no-style" href="#core-setup-overview">Setup for Labs</a>
4. <a class="no-style" href="#pipeline-template-catalog-title">Pipeline Manageability & Governance with Templates</a>
5. <a class="no-style" href="#casc-title">Configuration as Code (CasC) with CloudBees CI</a>
6. <a class="no-style" href="#pipeline-policies-title">Pipeline Manageability & Governance with Policies</a>
7. <a class="no-style" href="#dev-centric-title">A Developer Centric Experience</a>
8. .blue-bold[Using Pipeline Templates]
9. <a class="no-style" href="#casc-dev-title">Configuration as Code (CasC) for Developers</a>
10. <a class="no-style" href="#contextual-feedback-title">Contextual Feedback for Pipelines</a>
11. <a class="no-style" href="#cross-team-title">Cross Team Collaboration</a>
12. <a class="no-style" href="#hibernate-title">Hibernating Managed Controllers</a>

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
name: dev-casc-overview
class: compact

# Using Pipeline Templates

### Labs - Using Pipeline Templates
* In the following labs:
  *  Create a Pipeline from a template and learn how to use custom marker files.
* The *Using Pipeline Templates* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/module-2/using-pipeline-templates/