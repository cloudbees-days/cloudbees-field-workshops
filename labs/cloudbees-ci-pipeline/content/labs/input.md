---
title: "Pipelines with Interactive Input"
chapter: false
weight: 7
--- 

In this lab, we will see how you can capture interactive input in your Jenkins Pipeline while it is running by using the `input` step and some pitfalls you will want to avoid when using the `input` step.

1. Use the GitHub file editor to update the **Jenkinsfile** file in the **main** branch of your copy of the **helloworld-nodejs** repository and update the **Deploy** `stage` by adding the following between `environment` directive and `steps` block:

```
          when {
            environment name: 'FAVORITE_COLOR', value: 'BLUE'
          }
          input {
            message "Should we continue with deployment?"
          }
```

Note that we added a new `when` condition that will result in the **Deploy** stage being skipped. We also added an `input` directive instead of an `input` step in the `steps` block. This ensures that the `input` will be displayed before the agent is used. *Also note that even though we are setting the `FAVORITE_COLOR` environment variable value to `BLUE` in the **Deploy** stage that does not get executed until after the `when` condition is checked; so the value is still `RED` for the `when` condition.* 

2. Commit the changes and then navigate to the **main** branch of your **helloworld-nodejs** project on your Managed Controller.
3. There will be an `input` prompt for the `Deploy` stage (*the `input` prompt is also available in the Console log*). ![Configure Notification Link](input-prompt.png?width=50pc) Go ahead and click the **Proceed** button and you will see that the **Deploy** stage is skipped. 
4. Return to the the **Jenkinsfile** file in the **main** branch of your copy of the **helloworld-nodejs** repository in GitHub and use the GitHub file editor to update the **Deploy** `stage` by adding a special `[beforeInput](https://www.jenkins.io/doc/book/pipeline/syntax/#evaluating-when-before-the-input-directive)` `when` condition set to `true` after the `environment` condition. The updated `when` directive should match the following:
```
          when {
            environment name: 'FAVORITE_COLOR', value: 'BLUE'
            beforeInput true
          }
```

5. Commit the changes and then navigate to the **main** branch of your **helloworld-nodejs** project on your Managed Controller. The **Deploy** stage will be skipped before prompting for input.
6. Return to the the **Jenkinsfile** file in the **main** branch of your copy of the **helloworld-nodejs** repository in GitHub and use the GitHub file editor to update the **Deploy** `stage`. Replace the entire **Deploy** stage with the following:
```
        stage('Deploy') {
          agent any
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }
          input {
            message "Should we continue with deployment?"
          }
          steps {
            sh 'echo TODO - deploy to $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW'
          }
        }
```

7. Commit the changes, navigate to the **main** branch of your **helloworld-nodejs** project on your Managed Controller and you will eventually see a `input` prompt for the `Deploy` stage.
8. If you don't click on either the **Proceed** or **Abort** button in the `input` prompt, the Managed Controller would have waited indefinitely for a user response. Let's fix that by setting a timeout for the **Deploy** stage. We will add a `timeout` `option` for the **Deploy** `stage` using the [`stage` `options` directive](https://jenkins.io/doc/book/pipeline/syntax/#stage-options). Update the **Deploy** `stage` to match the following in the **main** branch and then commit the changes:

```
        stage('Deploy') {
          agent any
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }
          options {
            timeout(time: 30, unit: 'SECONDS') 
          }
          input {
            message "Should we continue with deployment?"
          }
          steps {
            sh 'echo TODO - deploy to $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW'
          }
        }
```

9. Navigate to the **main** branch of your **helloworld-nodejs** project on your Managed Controller and wait at least 30 seconds after the 'Deploy' `stage` starts. Your pipeline will be automatically **aborted** 30 seconds after the 'Deploy' `stage` starts. ![Input Timeout](input-timeout.png?width=50pc)

## Input Approval for Team Members

The `input` directive supports a [number of interesting configuration options](https://jenkins.io/doc/book/pipeline/syntax/#configuration-options). In this exercise we are going to use the `submitter` option to control what team member is allowed to submit the `input` directive. But first you need to provide access to your Managed Controller and the **helloworld-nodejs** job. 

We want to add a deployment approver to our Managed Controllers and then set that approver as the `submitter` for our `input` directive. Before you begin, pick a person to pair up with. The two of you will share each other's Jenkins account names (your GitHub username). You will use that account name when adding a new member to the **Approvers** Group on your Managed Controller. **NOTE:** If you don't have another person to pair up with then you can use the admin user that was created for you. It will be your GitHub username with the suffix `-admin` and the password will be the same, just use that in place of the approvers account username.

1. Go to the top-level of your Managed Controller and click on the **Groups** link in the left menu. ![Groups Link](groups-link.png?width=50pc)
2. On the next screen
3. Click on the ***Members*** link in the left menu and then click on the ***Add a user or group*** link. <p><img src="img/input/input_submitter_members_link.png" width=800/>
4. Select **Team Guest** from the role drop-down, enter the account name for the person next to you in the ***Add user or group*** input (I will use **beedemo-ops**), press your ***enter/return*** key, and then click the **Save changes** button.  <p><img src="img/input/input_submitter_add_team_guest.png" width=600/>
5. Click on the ***Pipelines*** link in the top menu. <p><img src="img/input/input_submitter_pipelines_link.png" width=600/>
6Now that we all have a new team member, you can add them as a `submitter` for the `input` directive in your `Jenkinsfile` Pipeline script. Use the GitHub file editor to update the **Jenkinsfile** file in the **main** branch of your copy of the **helloworld-nodejs** repository - updating the `input` directive of the **Deploy** `stage` with the following changes (replacing **beedemo-dev-admin** with the Jenkins username of your approver). Also, update the `timeout` duration to give your approver plenty of time to submit the `input`:

```
      options {
        timeout(time: 60, unit: 'SECONDS') 
      }
      input {
        message "Should we deploy?"
        submitter "beedemo-ops"
        submitterParameter "APPROVER"
      }
```

2. So, we added one additional configuration option for our `input` directive: `submitterParameter`. Setting the  `submitterParameter` option will result in a Pipeline environmental variable named `APPROVER` being set with the value being the username of the user that submitted the `input`. In the example above it will be **beedemo-ops**. Update the `steps` section so the `echo` step in your `Jenkinsfile` Pipeline script will print the `APPROVER` environmental variable and then commit the changes:

```
      steps {
        echo "Continuing with deployment - approved by ${APPROVER}"
      }
```

3. Navigate to the **master** branch of your **helloworld-nodejs** job in Blue Ocean on your Team Master. The job should be waiting for `input`: <p><img src="img/input/input_submitter_pending.png" width=800/>
4. The ***submitter*** needs to navigate to the **master** branch of your **helloworld-nodejs** job on your Team Master to approve the `input` of your **helloworld-nodejs** Pipeline. You can use the *Team switcher* to quickly navigate to another Team Master that you are a member. The *Team switcher* drop-down will appear in the top right of your screen once you have been added as a member to another Team Master. The ***submitter*** needs to switch to the Team where they are a *Team Guest* member by selecting that team from the *Team switcher* drop-down. <p><img src="img/input/input_submitter_team_switcher.png" width=600/>
5. As the ***submitter*** navigate to the **helloworld-nodejs** job on your new team and approve the `input`. Note the output of the `echo` step. <p><img src="img/input/input_submitter_approved_by.png" width=850/>

>**NOTE:** If you select a Pipeline job as a *favorite* you will be able to see things like jobs awaiting `input` submission in the Blue Ocean **Dashboard**. 

<p><img src="img/input/input_submitter_favorite.png" width=800/>

Before moving on to the next lesson make sure that your **Jenkinsfile** Pipeline script is correct by comparing to or copying from [below]().

### Finished Jenkinsfile for *Pipeline Approvals with Interactive Input*
```
pipeline {
  agent none
  options { 
    buildDiscarder(logRotator(numToKeepStr: '2'))
    skipDefaultCheckout true
  }
  stages {
    stage('Test') {
      agent {
        kubernetes {
          label 'nodejs-app-pod-2'
          yamlFile 'nodejs-pod.yaml'
        }
      }
      steps {
        checkout scm
        container('nodejs') {
          echo 'Hello World!'   
          sh 'node --version'
        }
      }
    }
    stage('Build and Push Image') {
      when {
        beforeAgent true
        beforeInput true
        branch 'master'
      }
      steps {
        echo "TODO - build and push image"
      }
    }
    stage('Deploy') {
      when {
        beforeAgent true
        branch 'master'
      }
      options {
        timeout(time: 60, unit: 'SECONDS') 
      }
      input {
        message "Should we deploy?"
        submitter "beedemo-ops"
        submitterParameter "APPROVER"
      }
      steps {
        echo "Continuing with deployment - approved by ${APPROVER}"
      }
    }
  }
}
```
