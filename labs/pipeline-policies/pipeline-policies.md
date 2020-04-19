# <img src="images/cloudbeescore_logo.png" alt="CloudBees Core Logo" width="40" align="top"> CloudBees Core - Pipeline Policies

## Create a Pipeline Policy

In this lab you will create a [Pipeline Policy](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines-user-guide/pipeline-policies) to ensure that all Pipeline jobs that run on your Team Master have a `timeout` set.

1. Navigate to team master level and click on "Pipeline Policies"<p><img src="images/policies_click.png" width=800/>
2. Click on "New Policy"<p><img src="images/newpolicy_click.png" width=800/>
3. Fill out the Pipeline Policy parameters:
   1. **Name**: Timeout policy
   2. **Action**: Fail
   3. Click on **Add Rule** and select **Pipeline Timeout**
   4. **Timeout**: 30 MINUTES
   5. Click the **Save** button<p><img src="images/pipe_timeout_fail.png" width=800/>
4. Navigate back to your master branch job inside of the **Template Jobs** folder and hit **Build Now**
5. In the logs of the last run master branch job you should see the following error:<p><img src="images/pipeline_policy_error.png" width=800/>

Congratulations! You have created a Pipeline Policy and updated a Pipeline template to conform to the policy.

You may proceed to the next lab: [*Cross Team Collaboration*](../cross-team-collaboration/cross-team-collaboration.md) or choose another lab on the [main page](../../README.md#workshop-labs).