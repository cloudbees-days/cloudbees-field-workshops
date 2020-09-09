# Instructions on updating slides

Slide content is broken up by workshop product with each product folder containing a Markdown file for each lab/section and an `index.html` used to load those slides and custom CSS for the theme. The purpose of the slides is to provide an overview of the product and of the differentiating feature(s) being highlighted in each lab.

There is also a top-level slide that provides navigation to the product specific slides.

To create a new slide, wrap some content inside some `---` like this example below and to add speaker notes add `???` before the next slide.

```markdown
---

# This is page 1

???
Speaker notes can go here.

---

# This is page 2

---
```

If you are unfamiliar with markdown syntax [here is a good cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

## Viewing Rendered Slides
The fastest way to see your changes is to run a web server from the `docs` directory. If you have Python 3 installed it is as easy as running this command `python3 -m http.server` in that directory and then navigating to http://localhost:8000 

## Presenting Slides
To present the slides so you can use the notes, press 'C' to first clone the opened slideshow in another browser window and the press 'P' in the browser window you would like to use for notes.

## Styling

Styling is based on the excellent work done by the Apron styling extension for remark.js - customizations are in the ./css/apron.css file.