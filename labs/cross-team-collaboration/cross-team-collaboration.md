# <img src="images/cloudbeescore_logo.png" alt="CloudBees Core Logo" width="40" align="top"> CloudBees Core - Cross Team Collaboration

The [Cross Team Collaboration](https://docs.cloudbees.com/docs/cloudbees-core/2.204.2.2/cloud-admin-guide/cross-team-collaboration) functionality in CloudBees Core allows you to create events and listeners to trigger jobs across the cluster. It gives you effectively a pub/sub relationship where jobs can send an event with data, and the jobs listening for it can trigger and process the data.

![Cross Team Collaboration diagram](https://docs.cloudbees.com/docs/cloudbees-common/latest/_images/cross-team-collaboration-screenshots/cross-team-diagram.abf4b33.png)

In this lab we're going to take advantage of cross team collaboration by adding an event trigger listener so that when the job for our base image is complete, it will kick off our frontend application job. This is a common real world scenario where your container base image may receive security patches or minor updates and you want all applications using that base image to be updated. 

Rather than asking everyone to make sure their application containers are rebuilt with the new base image version, we can trigger this automatically. For this workshop, the instructor will kick off a job which sends an event which will kick off your frontend job. 

## Taking a brief look at event trigger syntax

At its most basic, publishing an event is as simple as adding the the following step:
`publishEvent simpleEvent('helloWorld')`. In this case, we're using the string 'helloWorld' and any matching listeners will receive it.

```groovy
pipeline {
    agent any
    stages {
        stage('Publish event') {
            steps {
                publishEvent simpleEvent('helloWorld')
            }
        }
    }
}
```

Now we just need another job which has a listener listening for 'helloWorld'. We can see there is a new eventTrigger type of trigger specific for cross team collaboration.

```groovy
pipeline {
    agent any

    triggers {
        eventTrigger simpleMatch("helloWorld")
    }
    stages {
        stage('Example') {
            steps {
                echo 'received helloWorld'
            }
        }
    }
}
```

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

We can see in the build stage, by default, it is using this `node:lts-alpine` image. This lts-alpine image is great, but we actually want to use our own internal version of the image since it goes through our rigorous security scanning process.

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

---

That completes this lab, please choose another lab on the [main page](../../README.md#workshop-labs).