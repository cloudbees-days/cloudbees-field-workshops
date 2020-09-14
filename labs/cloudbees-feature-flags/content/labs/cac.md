---
title: "Feature Flags and GitOps"
chapter: false
weight: 4
--- 

### Connecting to GitHub Cloud
1. Create an empty repository named ***feature-flags-configuration-as-code*** in your workshop GitHub Organization. 
2. Connect the CloudBees Feature Flags app into the Github repository
  1. Go to **App Settings > Integrations tab** (from the left Panel)
  2. Click the **Connect** button <p><img src="images/app-integrations.png" />
3. In GitHub, select to integrate the CloudBees Feature Flags GitHub app with your created repository. <p><img src="images/github-app.png" />
4. After clicking **Install** you will be redirected back to the CloudBees Feature Flags dashboard to select your app and the repository <p><img src="images/github-rollout-confirmation.png" />
5. Click **Connect** and you are done integrating CloudBees Feature Flags with GitHub.

### Using CasC and GitOps
1. In the CloudBees Feature Flags dashboard, disable the sidebar experiment in Development environment by toggling `Active` to `Killed`. <p><img src="images/sidebar_killed.png" />
2. In GitHub, go look at your `rollout-configuration-as-code` repo and note the structure. You should see an automatically generated `README.md` and a `target_groups` directory.
3. Then, switch from `master` branch to the automatically created `Development` branch and note the differences. Note the existence of an `experiments` folder that contains `default.sidebar.yml` with `enabled: false` on line 5.
4. Within the Github code editor, modify `default.sidebar.yml` by editing the line `enabled: false` to become `enabled: true` and commit to `Development` branch. Your YAML should closely resemble this:

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

5. In CloudBees Feature Flags, notice that your default.sidebar experiment is now reactivated on the Development environment.

Now that you are satisfied with the experiment in your Development environment, you want to include this experiment in your Production environment.

6. In Github, merge `Development` to `master` branch with an appropriate commit message.
7. In CloudBees Feature Flags, note the sidebar experiment is now added to the Production environment.

<p><img src="images/production_sidebar.png" />

### Lab 5 Completed!
Congratulations! You have finished Lab 5 of the CloudBees Feature Flags Workshop.

**For instructor led workshops please return to the workshop slides: https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-feature-flags/#33**
