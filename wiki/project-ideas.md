---
title: Project ideas
author: Issa Rice
created: 2017-11-20
date: 2017-11-20
bigtable: yes
# documentkind:
# status:
# belief:
---

I am writing this page for various reasons. Some of these are to:

* Give people a better idea of what I might work on next. I like to make myself
  predictable so others can plan according to a good model of how I will act.
* Tell the world the things I want to see. I think the things in this list are
  useful to the world, and it doesn't need to be me who does it. It would be
  great to find out that somebody saw a sufficient need based partly on this
  page and decided to make something. Similar to request for startups or
  charities.
* Track the things I want to work on. I often think of things while daydreaming
  or working on something else. If I don't put an effort into recording things
  to work on (and training myself to notice needs that exist in the world), I
  might forget.
* Clean out some tasks from orgmode. I have a backlog of tasks in orgmode. A
  lot of these aren't for me to immediately work on, and they kind of clutter
  up my orgmode file.
* Give potential funders an idea of what they can fund. If I already want to
  see something in the world, a modest amount of funding can shift my
  priorities to work on that thing.
* Find potential collaborators. Especially for the larger projects, it can be
  helpful to have other interested parties on board to divide up the work.
* Give people a better idea of where I'm coming from. This is a broader point
  that applies to other efforts I have made to be more transparent.

Parameters: idea, description, effort, venue (Wikipedia, blog post on LW,
standalone site, etc), format (code, prose, data, etc). These parameters exist
to be helpful in scanning the list and orientation oneself, but are only
suggestive; it is often the case that as a project proceeds, details become
cleaner or change.

Effort can be rated on the following scale. In each case I assume I am the one
performing the task. I have a good programming and writing ability but I am not
exceptional by any means and I expect many people can perform at a comparable
level or even better depending on their expertise. (As a side note, even on the
project idea generation front I don't think I am exceptional -- in fact this
page so far is quite rudimentary and biased toward things I find personally
interesting rather than most useful to the world -- so I think other people can
and should also be more transparent about projects they want to see.) Days here
refer to work days, so 8 hour periods. Of course, planning fallacy blah blah,
so I list some things I have actually produced in the past to ground myself on
the kinds of tasks and their timescales.

0
:   Up to one day of effort. These are relatively quick things that can be
done. Examples are first round of timeline of Carl Shulman publications, some
global health pages like Amanda Glassman (I think)

1
:   More than one day and up to two weeks of effort. Examples on this level are
timeline of MIRI at the upper end. I think timeline of AMF at the lower end but
will have to check.

2
:   More than two weeks of effort. Examples here are my total work so far on
the donations list site (I think), my total work on Devec wiki.

This is not an exhaustive list of project ideas. In particular if I have
already done some work on a project and just want to make general improvements
to it, I won't usually list it here (*all* projects can be improved to varying
extents, and it would be tedious to list them all). If I have specific
improvements, I will try to list them here.

# Table

|Project|Description|Effort|Venue|Format|
|----------------|------------------------------------|-----:|--------|--------|
|Pandoc scripting guide|A guide to scripting with Pandoc. Probably with Lua filters now that Pandoc 2.0 is out. It would be good to cover common frustrations like how to debug your filter, some common real-life filters, and so on.|1||Prose with code samples|
|Naturalism table|A table summarizing naturalistic worldviews. The columns can be "author", "view on consciousness", "view on free will", "view on time", etc. In other words, the "[mysterious questions](http://lesswrong.com/lw/iu/mysterious_answers_to_mysterious_questions/ "Eliezer Yudkowsky. “Mysterious Answers to Mysterious Questions”. LessWrong. August 25, 2007. Retrieved November 20, 2017.")". The authors that I would like to be covered are Yudkowsky, Tomasik, Gary Drescher, and Dennett. The cells of the table can contain the works by the author that discusses the views.|0||Table|
|Table on multiverses/Big World theories|Rows could be the multiverses: many worlds interpretation, modal realism, etc. See [Tegmark's classification](https://en.wikipedia.org/wiki/Multiverse#Max_Tegmark.27s_four_levels) for example. The columns could be things like "how big?", "implications for altruism", "proponents".|1|No particular venue in mind|Table|
|Timeline of felicifia|I think quite a few EAs came from felicifia-related online presence, including Brian Tomasik, Pablo Stafforini, Ryan Carey, and Peter Hurford. Carl Shulman also has an account on the forums. It would be interesting to document its rise and decline.|1|Timelines Wiki|Timeline|
|Guide to working on wiki-like pages with Vim|I've developed some ideas about how to work on wiki-like pages in [Vim](), which is distinct from working on related program source code. Some useful options for this are `'isfname'`, `'includeexpr'`, and `'suffixesadd'`. Setting these to good values will allow for traveling between related pages on the wiki more easily. As a case study, MediaWiki could be used. Also see the [wikilink script](https://github.com/riceissa/contentcreation/blob/master/wikilink.vim) I use on one wiki.|0|Vim Tips Wiki|Prose with code samples|
|List of mysterious answers to mysterious questions|I think one reason I like the {Yudkowsky, Tomasik, Drescher, Dennett} approach to dealing with philosophy is that they treat all of the "big questions" or "mysterious questions" at once, rather than just treating one thing in isolation. But it seems like Drescher doesn't talk much about the problem of personal identity, and Yudkowsky's blog posts only pose it as a *question* (about the anthropic trilemma) rather than as an answer. I think having these all in one table would be nice, since I am tabulating a bunch these days. The columns could be "mysterious question", "mysterious answer", "resolution/dissolved answer".|1||Table|
|Timeline of web analytics|There is a stub for this [here](https://timelines.issarice.com/wiki/Timeline_of_web_analytics).|1|Timelines Wiki|Timeline|
|Improve the [Staycation § Benefits](https://en.wikipedia.org/wiki/Staycation#Benefits)|Some benefits can be framed as ways to avoid the downsides of international travel (jet lag, illness, and so on). I think Bryan Caplan discusses staycation in his kids book.|0|Wikipedia|Prose|
|A consciousness wiki|A wiki systematically exploring issues related to consciousness. See more ideas [here](https://github.com/riceissa/issarice.com/tree/master/external/consciousness.issarice.com). The wiki can have an altruism/crucial considerations bent like [Luke Muehlhauser's moral patienthood report](https://www.openphilanthropy.org/2017-report-consciousness-and-moral-patienthood "Luke Muehlhauser. “2017 Report on Consciousness and Moral Patienthood”. Open Philanthropy Project. August 5, 2017. Retrieved November 20, 2017."). It can also apply the ideas to e.g. cryonics.|2|Separate wiki|Prose and tables|
|Improve [pdftextfmt](https://github.com/riceissa/pdftextfmt) to handle more PDF madness|It's already fine for simple linebreaks and hyphens, but "word breaks" need to be handled manually (i.e. when there's a space within a word that's not supposed to be there). MuPDF also inserts strange lines containing just the character "f". Ligatures also often mess up the output.|2|GitHub|Code|
|Improve [Timeline of online dating services](https://timelines.issarice.com/wiki/Timeline_of_online_dating_services)|For example add info from [this piece](https://www.huffingtonpost.com/susie-lee/timeline-online-dating-fr_b_9228040.html). I also have a private discussion about more columns to add to the timeline (so find that before starting on this).|1|Timelines Wiki|Timeline|
|Research some trends in font usage|For instance, both Lato and Merriweather have become very popular in recent years. It seems like Minion Pro has supplanted Times New Roman as the new "boring default font". Default fonts for MS Word etc. have changed as well.|1|No particular venue in mind|Prose with maybe tables or graphs|
|Rationality blogroll graph|A graph showing which rationality community blogs have which blogs in their blogroll. To see if any patterns in e.g. subcommunities can be observed, and to uncover potentially interesting blogs.|1|GitHub for the code, no particular venue in mind for a writeup|Code with figures and maybe a writeup|

# External links

- [New article pool](https://github.com/vipulnaik/contractwork/blob/master/new-article-pool.mediawiki)
  by Vipul Naik lists article ideas