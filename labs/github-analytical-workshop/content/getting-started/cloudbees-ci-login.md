---
title: "CloudBees CI Login"
chapter: false
weight: 3
--- 

CloudBees CI for modern platforms takes advantage of Kubernetes by providing dynamic provisioning of team specific Jenkins instances we refer to as ***managed controllers***. A CloudBees ***managed controller*** (Jenkins instance) was provisioned for you with an initial configuration provided by CloudBees CI Configuration-as-Code. We will refer to this initial controllers as your **Operations** or **Ops** controller. The idea of an Ops controller is to provide automation for managing, configuring and updating your entire CloudBees CI cluster. Typically there would just be one Ops controller for an entire CloudBees CI cluster. However, the entire point of this workshop is for you to gain an understanding of how to leverage an Ops controller to automate configuration-as-code for any sized CloudBees CI cluster.

{{% notice note %}}
If you haven't already received the link or password for the CloudBees CI Workshop cluster, then ask your instructor for it. 
{{% /notice %}}

## CloudBees CI Managed Controller

### Login to CloudBees CI

1. Login into the CloudBees CI Workshop cluster at: [https://cbci.workshop.cb-sa.io/cjoc/login](https://cbci.workshop.cb-sa.io/cjoc/login) 
2. Enter your username (same as your GitHub username) and password (provided by your instructor) into the login screen, and click the **Sign in** button. ![CloudBees CI Login](setup-login.png?width=40pc)
3. Click on the link of your CloudBees CI managed controller that will be in a folder with the same name (lower-cased) as the GitHub Organization and the managed controller will be named **ops-controller**. ![managed controller link](managed-controller-link.png?width=70pc) 
4. NOTE: Depending on when you completed the pre-workshop setup, your managed controller may still be **Starting** as seen below. ![managed controller starting](starting.png?width=60pc) 
If that is the case you will have to wait until it is **Approved** and **Connected** as seen in the following screenshot. Once the **Status** is **Approved** and **Connected** click on the link for your Managed Controller. ![managed controller connnected](mc-connected.png?width=60pc)  Or it may be hibernating in which case you just need to click on it to start it again.

{{% notice note %}}
There are a number of ways to create a Managed Controller. We take a very opinionated way to provision attendees Managed Controllers for this workshop in order to pre-configure the components that you will interact with during the workshop, allowing us to jump into the content more quickly.
{{% /notice %}}

