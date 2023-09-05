let username = window.localStorage.getItem("username")
if (!username) {
  username = "REPLACE_WITH_YOUR_USERNAME"
}

const elements = document.getElementsByTagName("code")

Array.from(elements).forEach(el => {
  const inner = el.innerHTML
  const replaced = inner.replaceAll("my-username", username)
  el.innerHTML = replaced
})

