---
title: "Feature Flags and GitOps"
chapter: false
weight: 4
--- 

### Connecting to GitHub Cloud
1. Create an empty repository named ***feature-flags-configuration-as-code*** in your workshop GitHub Organization. 
2. Connect the CloudBees Feature Flags app into the Github repository by:
  - Going to **App Settings > Integrations tab** (from the left Panel) in the CLoudBees Feature Flags dashboard.
  - Click the **Connect** button in the **GitHub** panel. ![GitHub App](images/app-integrations.png?width=50pc)
3. In GitHub, select your workshop GitHub Organization to integrate with CloudBees Feature Flags GitHub app. On the next screen select the ***Only select repositories*** and then select the `feature-flags-configuration-as-code` repository you just created. ![GitHub App](images/github-app-repo.png?width=50pc)
4. After clicking the **Install** button you will be redirected back to the CloudBees Feature Flags dashboard to select your app and the repository you just created. ![GitHub App](images/github-rollout-confirmation.png?width=50pc) 
5. Click **Connect** and you are done integrating CloudBees Feature Flags with GitHub. ![Connected](images/connected.png?width=50pc) 

### Using CasC and GitOps
1. In the CloudBees Feature Flags dashboard, disable the sidebar experiment in Development environment by toggling `Active` to `Killed`. ![Connected](images/sidebar_killed.png?width=50pc)
2. In GitHub, navigate to your `feature-flags-configuration-as-code` repository and note the structure. You should see an automatically generated `README.md` and a `target_groups` directory.
3. Switch from `master` branch to the automatically created `Development` branch and note the differences. Note the existence of an `experiments` folder that contains `default.sidebar.yml` with `enabled: false` on line 5.
4. Within the GitHub code editor, modify `default.sidebar.yml` by editing the line `enabled: false` to become `enabled: true` and commit to `Development` branch. Your YAML should closely resemble this:

```YAML
# This file was edited by rollout.io
# URL: https://app.rollout.io/ex/<YOUR_EXPERIMENT_URL>
type: experiment
name: sidebar
flag: default.sidebar
enabled: true
conditions:
  - group:
      name: LoggedInUsers
    value: true
value: false
```
5. In the CloudBees Feature Flags dashboard, notice that your **default.sidebar** experiment is now reactivated in the **Development** environment.
6. Now that you are satisfied with the experiment in your Development environment, you want to include this experiment in your Production environment. In Github, merge the `Development` branch to `master` branch by creating and merging a pull request. Make sure not to delete the `Development` branch after confirming the merge.
7. In CloudBees Feature Flags dashboard, note the **sidebar** and **title** experiments have now added to your **Production** environment. ![Connected](images/production_sidebar.png?width=50pc)

### Lab 5 Completed!
Congratulations! You have finished Lab 5 of the CloudBees Feature Flags Workshop.

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-feature-flags/#33">return to the workshop slides</a>**
