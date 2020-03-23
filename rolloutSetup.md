## Create a Rollout Account
1. Navigate to the [sign-up form](https://app.rollout.io/signup).
2. Fill out the form, agree to the Terms of Service, and click Sign Up.
3. Within the navigation menu, located on the far left side of the dashobard, click the App Settings option.
4. From the resulting App Settings page, navigate to the "Environments" tab, and copy your unique key associated with the Production environment. This will be the <ROLLOUT_ENV_KEY> used in our set-up later on.
5. In Github, navigate to the microblog-frontend repository previously forked to the organization.
6. Click Branch: master
7. Type "initRollout" to create a new branch.
8. Click "Create a new file"
9. Type "utils/flag.js"
10. Within the Github code editor, enter the following code:
```javascript
import Rox from 'rox-browser'

export const Flags = {
	sidebar: new Rox.Flag(false)
};

Rox.register('default', Flags);

Rox.setup("<ROLLOUT_ENV_KEY>");
```
11. Create a commit message and select "Commit directly to the initRollout branch." option before clicking "Commit new file.""