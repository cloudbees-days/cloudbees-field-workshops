---
title: "CloudBees CI Configuration Bundle Management"
chapter: false
weight: 3
--- 

CloudBees CI configuration bundles are centrally managed and stored in the `jcasc-bundles-store` directory in the Operations Center Jenkins home directory. In order to make a bundle available for a controller or to update an existing bundle the bundle files must be copied to the `jcasc-bundles-store` directory.

>NOTE: While Operations Center simplifies the management of bundles, it is possible to configure a controller with a bundle without Operations Center using the `-Dcore.casc.config.bundle=/path/to/casc-bundle` Java system property.

The labs in this section will explore:

- storing configuration bundles on Operations Center
- setting a default bundle
- using the CasC HTTP API with GitOps for CloudBees CI configuration bundles

## GitOps for CloudBees CI Configuration Bundles
 
1. Navigate to the top-level of your operations controller - it will be in the Operations Center **operations** folder and have the same name as your workshop GitHub Organization name (lower-cased) and prefixed with **ops-**.
2. Create a Mulitbranch project.
3. Configure Multibranch project.