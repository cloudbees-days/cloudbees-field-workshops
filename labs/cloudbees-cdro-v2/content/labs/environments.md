---
title: "Environments"
chapter: false
weight: 5
--- 

Application modeling is only one part of managing deployment automation with CloudBees CD/RO. The other main part is environment modeling. 

With application modeling you describe what the processes are that can be run against an application. Now with the environment modeling you are defining where these processes can occur.

It is important that these two be separate or else there would be a lot of repetition of effort. With this setup you only need to define the application processes once and then point them at the target environments. Properties from the environment can then be passed along to the application process during runtime.

In the previous lab we took a look at the application modeling process and setup a microservice definition. As part of this we created our first environment in which we would deploy our application.

## Reviewing the environment we've created

