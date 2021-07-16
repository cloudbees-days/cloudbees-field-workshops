---
title: "Configuring RBAC and Folders with CloudBees CI CasC"
chapter: false
weight: 6
--- 

CloudBees CI CasC provides support for managing the configuration of CloudBees CI Role Based Access Control (RBAC) and folders.

In this lab we will explore updating your controller specific configuration bundle to manage RBAC and create a folder with RBAC configuration.

>NOTE: Using CasC for RBAC requires that you allow Managed Controllers to opt-out of inheriting the Operations Center authorization strategy meaning that the Managed Controller will not inherit roles or groups from Operations Center but will still authenticate through Operations Center. As noted in the previous lab, your dev controller was provisioned with the setting already configured to opt out of inheriting the Operations Center authorization strategy.





