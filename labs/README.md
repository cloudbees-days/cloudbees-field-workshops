To build and view the labs locally [install Hugo](https://gohugo.io/getting-started/installing/) and then run the corresponding commands from the `base` directory. This allows us to reuse the same theme from the `base` directory for both workshop lab sites.

For the CloudBees CI Workshop labs:
```sh
hugo server --config ../cloudbees-ci/config.toml --contentDir ../cloudbees-ci/content/
```

For the CloudBees Feature Management Workshop labs: 
```sh
hugo server --config ../cloudbees-feature-flags/config.toml --contentDir ../cloudbees-feature-flags/content/
```

If you create a PR in the https://github.com/cloudbees-days/cloudbees-field-workshops/ repository then a preview site will be built and deployed for you with the link provided as a PR comment once the site is ready. 

In order to render the workshops locally, you will need to ensure the theme is pulled locally. These are configured as git submodules, so you will need to pull those. You can do this by running:

```bash
git submodule update --init --recursive
```