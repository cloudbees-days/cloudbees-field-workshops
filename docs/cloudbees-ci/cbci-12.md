name: cbci-thanks
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# Thank You!

---

name: cbci-appendix
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI<br>Workshop Appendix

---
name: appendix

#### GitHub App Credential
Using the GitHub App credential type with the CloudBees SCM Reporting plugin offers the following additional benefits:
* **Larger rate limits** - The rate limit for a GitHub app scales with your organization size, whereas a user based token has a limit of 5000 regardless of how many repositories you have.
* **User-independent authentication** - Each GitHub app has its own user-independent authentication. No more need for 'bot' users or figuring out who should be the owner of 2FA or OAuth tokens.
* **Improved security and tighter permissions** - GitHub Apps offer much finer-grained permissions compared to a service user and its personal access tokens. This lets the Jenkins GitHub app require a much smaller set of privileges to run properly.
* **GitHub Checks API** - allows the CloudBees SCM Reporting plugin to use the GitHub Checks API to create check runs and check suites from Jenkins jobs and provide detailed feedback on commits as well as detailed code annotations.