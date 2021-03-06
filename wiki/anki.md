---
title: Anki
author: Issa Rice
created: 2019-11-22
date: 2019-11-22
# documentkind:
# status:
# belief:
---

Here are some Anki-related things I have written:

* [Ramblings about my experience using Anki](https://github.com/riceissa/issarice.com/blob/master/drafts/spaced-repetition.md)
* [Resetting ease factor for a deck in Anki](https://gist.github.com/riceissa/9616621772754a94e4254e1590a44afd)
* [An implementation of the Anki scheduling algorithm](https://gist.github.com/riceissa/1ead1b9881ffbb48793565ce69d7dbdd)
* [Comment thread on LessWrong](https://www.greaterwrong.com/posts/xDWGELFkyKdBpySAf/an1lam-s-short-form-feed/comment/6Qt29YZAtRiE9zWhe)
* [Imagining a world where spaced repetition is commonplace](https://raw.githubusercontent.com/riceissa/issarice.com/master/drafts/spaced-repetition-world.txt)
* <https://wiki.issarice.com/wiki/Category:Spaced_repetition>
* <https://github.com/riceissa/spaced-inbox>

Anki defaults to CommonHTML for MathJax, which doesn't work when using mathbf fonts (e.g. $\mathbf R$) -- they show up as mathrm instead. To fix this on Linux, edit `/usr/share/anki/web/mathjax/conf.js` and change `jax: ["input/TeX", "output/CommonHTML"],` to `jax: ["input/TeX", "output/HTML-CSS"],`.
This will be overridden whenever Ubuntu upgrades to the next version, so you will have to edit this again at that time (unless the bug in MathJax is fixed).

On older versions of Android, the default fonts for kanji use the Chinese
variants. To correct this, you can change the templates to have
`<span lang="ja">...</span>` around the kanji parts.
