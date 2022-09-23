let username = window.localStorage.getItem("username");
if (username) {
  const qaEl = document.getElementById("qa-env-link");
  const qaLink = document.createElement("a");
  qaLink.innerText = "Access your QA Environment";
  qaLink.className = "btn btn-default";
  qaLink.href = `https://${username}-qa.cdro-workshop.cb-demos.io`
  qaLink.target = "_blank"
  qaEl.appendChild(qaLink);

  const prodEl = document.getElementById("prod-env-link");
  const prodLink = document.createElement("a");
  prodLink.innerText = "Access your Production Environment";
  prodLink.className = "btn btn-default";
  prodLink.href = `https://${username}-prod.cdro-workshop.cb-demos.io`
  prodLink.target = "_blank"
  prodEl.appendChild(prodLink);
}
