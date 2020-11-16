---
title: "CloudBees CI Role-Based Access Control"
chapter: false
weight: 3
---

Role-Based Access Control (RBAC) for CloudBees CI provides the ability to restrict access and delegate administration. And when combined with CloudBees CI CasC you have complete audit history of any changes to access control captured by your source control tool such as Git.

For the purpose of this lab we will be using the Jenkins database security realm but CloudBees CI supports number of external security realms, such as LDAP, Active Directory and SAML based security realms.

>NOTE: Using CasC for RBAC requires that you allow managed controllers to opt-out of inheriting the Operations Center authorization strategy and you will no longer be able to inherit roles or groups from Operations Center.



