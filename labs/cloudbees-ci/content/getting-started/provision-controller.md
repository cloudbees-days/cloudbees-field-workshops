---
title: "CloudBees CI Setup"
chapter: false
weight: 3
--- 

CloudBees CI for modern platforms takes advantage of Kubernetes to providing dynamic provisioning of team specific Jenkins instances we refer to as ***managed controllers***. In this lab you will provision a CloudBees ***managed controller*** (Jenkins instance) with an initial configuration provided by CloudBees CI Configuration-as-Code.

>NOTE: If you haven't already received the link for the CloudBees CI Workshop cluster, then ask your instructor for it.

## CloudBees CI Managed Controller

### Login to CloudBees CI

1. Login into the CloudBees CI Workshop cluster at: [https://workshop.cb-sa.io/cjoc/login](https://workshop.cb-sa.io/cjoc/login) 
2. Enter the username and password, provided by your instructor, into the login screen and click the **Sign in** button. ![CloudBees CI Login](setup-login.png?width=40pc)
3. Click on the link of your CloudBees CI ***managed controller***.
4. You should see the following repositories copied into your workshop GitHub Organization.
   - https://github.com/cloudbees-days/cloudbees-ci-config-bundle
   - https://github.com/cloudbees-days/pipeline-library
   - https://github.com/cloudbees-days/pipeline-template-catalog
   - https://github.com/cloudbees-days/pipeline-policies
   - https://github.com/cloudbees-days/simple-java-maven-app ![GitHub App Installed](forked-repos.png?width=50pc)

>NOTE: There are a number of ways to create a ***managed controller***. We take a very opinionated way to provision attendees ***managed controllers*** for this workshop in order to pre-configure the components that you will interact with during the workshop.

**For instructor led workshops please return to the workshop slides: https://cloudbees-days.github.io/core-rollout-flow-workshop/cloudbees-ci/#16**