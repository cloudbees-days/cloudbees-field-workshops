To build and view the labs locally [install Hugo](https://gohugo.io/getting-started/installing/) and then run the corresponding commands from the `base` directory. This allows us to reuse the same theme from the `base` directory for both workshop lab sites.

For the CloudBees CI Workshop labs:
```sh
hugo --config ../cloudbees-ci/config.toml --contentDir ../cloudbees-ci/content/
```

For the CloudBees Feature Flags Workshop labs: 
```sh
hugo --config ../cloudbees-feature-flags/config.toml --contentDir ../cloudbees-feature-flags/content/
```

If you create a PR in the https://github.com/cloudbees-days/core-rollout-flow-workshop/ repository then a preview site will be built and deployed for you with the link provided as a PR comment once the site is ready. 