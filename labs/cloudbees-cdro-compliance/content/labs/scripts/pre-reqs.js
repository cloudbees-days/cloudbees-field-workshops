import Rox from 'https://cdn.skypack.dev/rox-browser'

const fmEnvToken = "621cd5c5e03b4a3cd33a99d5"

const flags = {
  isOpen: new Rox.Flag(),
  registrationEndpoint: new Rox.RoxString(""),
  workshopUrl: new Rox.RoxString("")
};

const content = document.getElementById("content")


async function initRollout() {
  const options = {};

  Rox.register('docs', flags);

  await Rox.setup(fmEnvToken, options);

  if (flags.isOpen.isEnabled()) {
    if (window.localStorage.getItem("username")) {
      content.innerHTML = `
        <h3>Success</h3>
        <p>You've now got an account with username <strong>${window.localStorage.getItem("username")}</strong> and your chosen password.</p>
        <a class="btn btn-default" href="${flags.workshopUrl.getValue()}" target="_blank">Open the workshop environment</a>
        <button class="btn btn-default" onclick="window.localStorage.removeItem('username'); window.location.reload()">Create a new user</button>
      `
    } else {
      content.innerHTML = `
    <h3>Register for an account</h3>
    <form id="registrationForm">
      <label>Username
        <input type="text" required name="username" />
      </label>
      <label>Password
        <input type="password" required name="password" />
      </label>
      <label>Confirm password
        <input type="password" required name="confirm_password" />
      </label>
      <label>EMail
        <input type="text" required name="email" />
      </label>
      <button type="submit" class="btn btn-default">Register</button>
    </form>
    <div id="errors" ></div>
    `

      const form = document.getElementById("registrationForm")
      form.addEventListener('submit', async e => {
        e.preventDefault()
        const formData = new FormData(form)
        const username = formData.get("username")
        const pw = formData.get("password")
        const pw2 = formData.get("confirm_password")
        const email = formData.get("email")
        const errors = document.getElementById("errors")
        if (pw !== pw2) {
          errors.innerText = "The passwords you entered do not match. Please try again."
          return
        } else {
          errors.innerText = ""
        }
        var patt = new RegExp("[^A-Z a-z0-9]");
        var isUsernameOK = ! patt.test(username);
        if ( ! isUsernameOK ) {
          errors.innerText = "Special characters are not allowed in the username."
          return
        } else {
          errors.innerText = ""
        }
        const serverUrl = flags.registrationEndpoint.getValue()
        const resp = await fetch(serverUrl, {
          method: "POST",
          body: JSON.stringify({
            "username": username,
            "password": pw,
            "email": email
          }),
          headers: {
            "Content-Type": "application/json"
          }
        })
        const data = await resp.json()
        console.log(data)
        if (resp.status === 400) {
          errors.innerText = data.message
        }
        if (resp.status === 201) {
          window.localStorage.setItem("username", data.user)
          content.innerHTML = `
          <h3>Success</h3>
          <p>You've now got an account with username <strong>${window.localStorage.getItem("username")}</strong> and your chosen password.</p>
          <a class="btn btn-default" href="${flags.workshopUrl.getValue()}" target="_blank">Open the workshop environment</a>
        `
        }

      })
    }
  } else {
    content.innerHTML = `
    <h3>Registration is currently closed</h3>
    <p>We run a workshop every month. If you'd like to join the next one, you can find more details here.</p>
    `
  }
}



initRollout().then(function () {
  console.log('Done loading Rollout');
});

