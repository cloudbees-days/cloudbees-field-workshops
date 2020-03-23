## Setting Up CloudBees Rollout
1. Navigate to the CloudBees Rollout [sign-up](https://app.rollout.io/signup).
2. Fill out the form, agree to the Terms of Service, and click Sign Up.
3. In order to control feature flags from the Rollout dashboard, we have to connect it to our code. On the far left side of the dashobard, click the App Settings option. From the resulting App Settings page, navigate to the "Environments" tab, and copy your unique key associated with the Production environment. This will be the `<ROLLOUT_ENV_KEY>` used in our set-up later on.

* NEED TO ADD CALLOUTS TO IMG BELOW
<p><img src="img/rollout/RolloutEnvKey.png" />

4. In Github, navigate to the microblog-frontend repository previously forked to the organization.
5. Click `Branch: master`
6. Type `initRollout` then click "Create branch: initRollout from master" to finish creating a new branch.
<p><img src="img/rollout/initRolloutBranch.gif" />

7. Ensure you are within the initRollout branch, then click the `src` folder. On the resulting page, click the "Create new file" button.
* NEED TO ADD CALLOUT TO IMG BELOW
<p><img src="img/rollout/srcCreateNewFile.png" />

8. In the textbox next to `microblog-frontend/src/`, type: `utils/flag.js`
<p><img src="img/rollout/utilsFlagJS.gif" />

9. Within the Github code editor, enter the following code, replacing `<ROLLOUT_ENV_KEY>` with the key copied from step 3:
```javascript
import Rox from 'rox-browser'

export const Flags = {
	sidebar: new Rox.Flag(false)
};

Rox.register('default', Flags);

Rox.setup("<ROLLOUT_ENV_KEY>");
```
10. Create a commit message (Create flag.js) and select "Commit directly to the `initRollout` branch" radio button. The file and its directory path should look similar to the picture below. Complete this lab by clicking "Commit new file."
<p><img src="img/rollout/flagJSCommit.png" />