name: freestyle-vs-pipeline

# What’s Wrong With Freestyle Jobs?

While the Freestyle job type has served the Jenkins community well for years it has some major issues including:

* **UI Bound** - The configuration of a job is limited to what can be expressed via the limits of the Jenkins’ UI and doesn’t allow for building complicated workflows with features like:
    * Control over where builds are executed
    * Flow control (if-then-else, when, try-catch-finally) 
    * Ability to run steps on multiple agents
    * Ability to run steps in parallel
* **Not Auditable** - The creation and editing of jobs isn’t auditable without using additional plugins

---
name: jenkins-pipeline-intro
class: compact

# What is a Jenkins Pipeline?

.no-bullet[
* Jenkins Pipeline (formerly known as Workflow) was introduced in 2014 and built into Jenkins 2.0 when it was released.
* Pipelines are:
]

* **A Job type** - The configuration of the job and steps to execute are defined in a script (Groovy or Declarative based with a Domain Specific Language) that can be stored in an external SCM
* **Auditable** - the Jenkinsfile can be managed in source control and changes can be easily audited via your SCM
* **Durable** - can keep running even if the master fails
* **Versatile** - Pipelines support complex real-world CD requirements, including the ability to fork/join, loop, and perform work in parallel.
* **Distributable** - pipelines can be run across multiple agents including
execution of steps in parallel across multiple agents
* **Pausable** - can wait for user input before proceeding
* **Visualizable** - enables status-at-a-glance dashboards like the built in
Pipeline Stage View and Blue Ocean

---
name: declarative-vs-scripted

#  Why You Should Use Declarative Instead of Scripted?

While Declarative Pipelines use the same execution engine as Scripted pipelines,  Declarative adds the following benefits:

* **Easier to Learn** - the Declarative Pipeline DSL (Domain Specific Language) is more approachable than Groovy making it quicker to get started
* **Richer Syntax** - Declarative provides richer syntactical features over Scripted Pipeline syntax
* **Syntax Checking** - Declarative syntax adds the following types of syntax checking that don’t exist for Scripted pipelines:
    * Immediate runtime syntax checking with explicit error messages.
    * API and CLI based file linting

---
name: multibranch-pipeline

# What is a Multibranch Pipeline?
.no-bullet[
* The **Multibranch Pipeline** project type enables you to implement different Jenkinsfiles for different branches of the same project. In a Multibranch Pipeline project, Jenkins **automatically discovers, manages and executes** Pipelines for branches which contain a Jenkinsfile in source control.
* A Github Organization or Bitbucket Project Pipeline Project scans for repositories that have a Jenkinsfile and creates a Multibranch Pipeline project for each one it finds.
]
---
name: pipeline-template-catalogs

# CloudBees CI Pipeline Template Catalogs

.no-bullet[
* [CloudBees CI Pipeline Template Catalogs](https://docs.cloudbees.com/docs/admin-resources/latest/pipeline-templates-user-guide/setting-up-a-pipeline-template-catalog) provide version controlled, parameterized templates for Multibranch and stand-alone Pipeline jobs, and help ensure that Pipeline jobs conform to organizational standards.
* Benefits of using Pipeline Template Catalogs include:
]

* Providing developers with a simplified and directed experience for configuring Pipeline in “domain specific” terms that make sense for an organization. This allows developers to focus on shipping software.
* Organizing Pipelines per projects and/or teams. Similar-looking jobs that only differ in a few aspects can be easily parameterized on a per job basis. When you change a template, all the jobs created from that template get updated automatically.
* Templates from Pipeline Catalogs are more secure as they don't allow [Pipeline Replay](https://www.jenkins.io/doc/book/pipeline/development/#replay). Anyone with build permissions on a Pipeline Job Template or Custom Pipeline as Code Script based job can Replay it and make changes to the Pipeline script.
 
 
