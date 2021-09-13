---
title: 👋
hide:
  - toc
  - navigation
---
<script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
<script>
  var typed = new Typed('h1', {
    startDelay: 000,
    showCursor: false,
    typeSpeed: 50,
    strings: {{ salutation_permutations() }},
  });
  // todo: cycle avatar
</script>

## Michael Joseph

![avatar](media/shaggy.svg){ align=left height=200px width=200px }

I've [worked](/resume) in the computer / internet industry for the last {{ now().year - 1999}} years, primarily as a backend software engineer for web applications.

For most of that time, I've either been the lead of a small developer team or provided technical leadership and engineering management roles.

*[Michael Joseph]: yes, two first names, I know. MJ works as an internet handle, for people into the whole brevity thing as well as for disambiguation purpose

{{ skills_badge_urls() }}








