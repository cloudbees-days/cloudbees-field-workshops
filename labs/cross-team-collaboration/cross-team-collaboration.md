# <img src="images/cloudbeescore_logo.png" alt="CloudBees Core Logo" width="40" align="top"> CloudBees Core - Cross Team Collaboration

# WORK IN PROGRESS

The `simpleEvent` and `simpleMatch` are great for a lot of situations, but for this workshop we are going to want to be able to pass some data along (in this case, the new image tag).

Thankfully we have another type which lets us do just that. Instead of the simpleEvent we can now use the jsonEvent:

```groovy
publishEvent jsonEvent('{"eventName":"helloWorld"}')
```

And instead of simpleMatch trigger, we can use the jmespathQuery:

```groovy
    triggers {
        eventTrigger jmespathQuery("eventName=='helloWorld'")
    }
```

A JMESPath expression allows us to check a value against the JSON body we receive with the event.

## Adding the trigger to our pipeline

First, to figure out what we're dealing with, let's look at the actual Dockerfile for the microblog-frontend application:

```Dockerfile
ARG NODE_IMAGE=node:lts-alpine

# build stage
FROM $NODE_IMAGE as build-stage
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install
COPY . .
RUN yarn run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

We can see in the build stage, by default, it is using this `node:lts-alpine` image. This `lts-alpine` image is great, but we actually want to use our own internal version of the image since it goes through our rigorous security scanning process.

If you were to build this locally with Docker, you could run something like `docker build -t microblog-frontend NODE_IMAGE=internal-node:tag .` to use a specific `NODE_IMAGE`.

What we need to do is update our pipeline template catalog to 1) listen for the trigger and 2) modify the docker build to use the argument.

### The trigger

In any pub/sub relationship, it's important to understand the format of the data being sent and received. So let's take a look at the data the instructors job will be sending. 

```groovy
publishEvent jsonEvent('{
  "imageName": "node",
  "image": "{registry}/node:version"
}')
```

With this, we're going to want to trigger our job based on a search match on `imageName=='node'`.

Let's add this trigger block to our vuejs-app pipeline template catalog. If you haven't forked the catalog repo in the previous labs, you can do it [here](https://github.com/cloudbees-days/pipeline-template-catalog).

In your forked repo, navigate to `templates/vuejs-app/Jenkinsfile`.

Currently we have no defined triggers in this template:

```groovy
library 'cb-days@master'
def testPodYaml = libraryResource 'podtemplates/vuejs/vuejs-test-pod.yml'
pipeline {
  agent none
  options { 
    buildDiscarder(logRotator(numToKeepStr: '2'))
    skipDefaultCheckout true
    preserveStashes(buildCount: 2)
  }
  environment {
    repoOwner = "${repoOwner}"
    credId = "${githubCredentialId}"
  }
  stages('VueJS Test and Build')
...
```

To get this job to trigger on the event, we simply need to add the following block below the `agent none`:

```groovy
triggers {
  eventTrigger jmespathQuery("imageName=='node'")
}
```

For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/core/#33).

You may proceed to the next lab: [*Preview Environments with Core*](../core-preview-environment/catalog-templates.md) or choose another lab on the [main page](../../README.md#workshop-labs).