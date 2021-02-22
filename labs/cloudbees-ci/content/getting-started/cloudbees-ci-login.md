---
title: "CloudBees CI Login"
chapter: false
weight: 3
--- 

CloudBees CI for modern platforms takes advantage of Kubernetes to providing dynamic provisioning of team specific Jenkins instances we refer to as ***managed controllers***. In this lab you will provision a CloudBees ***managed controller*** (Jenkins instance) with an initial configuration provided by CloudBees CI Configuration-as-Code.

>NOTE: If you haven't already received the link for the CloudBees CI Workshop cluster, then ask your instructor for it.

## CloudBees CI Managed Controller

### Login to CloudBees CI

1. Login into the CloudBees CI Workshop cluster at: [https://cbci.workshop.cb-sa.io/cjoc/login](https://cbci.workshop.cb-sa.io/cjoc/login) 
2. Enter the username and password, provided by your instructor, into the login screen and click the **Sign in** button. ![CloudBees CI Login](setup-login.png?width=40pc)
3. Click on the link of your CloudBees CI ***managed controller*** that will have the same name (lowercased) as the GitHub Organization you are using for this workshop.
4. NOTE: Depending on when you completed the pre-workshop setup your ***managed controller*** may still be **Starting** as seen below. ![managed controller starting](starting.png?width=40pc) 
If that is the case you will have to wait until it is **Approved** and **Connected** as seen in the following screenshot.  ![managed controller connnected](mc-connected.png?width=40pc) 

>NOTE: There are a number of ways to create a ***managed controller***. We take a very opinionated way to provision attendees ***managed controllers*** for this workshop in order to pre-configure the components that you will interact with during the workshop to allow us to jump into the hands on content more quickly.

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-ci/#cbci-setup-review">return to the workshop slides</a>**
