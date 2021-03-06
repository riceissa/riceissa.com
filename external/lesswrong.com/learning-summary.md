# My current thoughts on learning how to learn, educational psychology, and spaced repetition

For the past two or so years, one of my side interests has been to figure out how effective learning works (especially with regard to highly technical and confusing subjects such as math and AI safety), both as an autodidact myself and as someone who wants to produce clear written explanations. This post is a summary of my current take on this area.

## Summary of my views

Here are my basic conclusions:

### Small number of core techniques

- There are a small core of learning techniques that have been found to basically work. These are: spaced repetition, interleaving, active recall, generation.

### High level learning strategies are trickier

- I'm pretty uncertain about higher level learning strategies

e.g. moore method, project-based learning vs drilling vs other things.

### Illusions of understanding are insightful

- in addition, there are several "illusions" of understanding that I think are insightful and good to be familiar with: illusion of transparency, double illusion of transparency, illusion of understanding.

### Educational psychology literature does not provide any guidance beyond telling me things like spaced repetition exists

i think i'm less optimistic about optimizing learning these days than back when i started learning subwiki stuff
back then it felt like there were all these low-hanging fruit that nobody was making use of (e.g. spaced repetition, feynman technique, interleaving)
i think these things do give a boost to learning, but there's still something really hard about learning, and i think it might be a "fundamental" difficulty (either the act of learning is just really hard/takes time, or it can be made easy but only in not-easily-scalable ways like 1-on-1 tutoring)
i think there are "learning boosts" on the order of spaced repetition that are still undiscovered, but discovering these will take time (e.g. lots of messing around to find what works). i am sort of naturally doing this just by experimenting with anki
i think there is some sort of deep connection between learning things and debating things, and that the difficulty of reconciling views even among smart people (e.g. eliezer vs paul) says something about the fundamental difficulties of learning

I get the feeling that i've already exhausted the low-hanging fruit of the "education literature"
i think testing, interleaving, and spacing are the main effects
my feeling is that like a typical spacing study just uses it for simple vocab memorization and similar, instead of, like, teaching a whole course on real analysis using spaced repetition and seeing what works

I think there must be something preventing these psychology researchers from doing more interesting experiments
like maybe it's hard to keep subjects around for several years
or they can't be too selective about the subjects they use, so e.g. they can't filter to people who have some good level of math ability
or they don't want to/can't make the subjects do elaborate preparatory work (e.g. making them learn Anki well)
so then, instead of refining the learning technique (e.g. figuring out the "parameters" I talked about), they just "spread out" their studies by doing the same thing over and over again but using different materials (paintings, nonsense syllables, foreign vocabulary, math word problems, physics problems, etc. etc.)
also in most of the studies i'm seeing they're still comparing spacing vs no spacing, rather than like spacing A vs spacing B vs spacing C

https://youtu.be/7_DA-hbuafU?t=197
anna says here that academic research is good but slow so it comes up with a single technique over some long period of time (the comparison to CFAR is that CFAR tries to do things more quickly and by mixing techniques)

from a comment on [this video](https://www.youtube.com/watch?v=-TIDDKswpLM): "I was in total agreement with Andy's sentiments here. Most research papers barely move beyond memorisation of Ebbinghaus-esque nonsense syllables. The goal of this is of course understandable - to control for the confounding interference of prior knowledge and meaning, similar to how Ebbinghaus chose nonsense syllables over poem stanzas. But this insistence on scientific rigour eliminates any relation the research could have to the most interesting applications of spaced repetition: in creative domains where there MUST be rich interactions between new material and prior knowledge."

TODO: copy quotes from the papers i looked at into a separate page.



## History of my interest in the area

I first heard about spaced repetition sometime around 2011-2013, probably from LessWrong or gwern's website. I used Anki to memorize pretty random things, including Spanish vocabulary, English vocabulary, facts from history, literary techniques, random quotes, and kanji. Most of these things were related to my high school classes, and when I started college in 2014 it became clear that I didn't care about most of my decks. Even my non-school interests changed a bunch, which made my decks less useful. So I eventually stopped using Anki, probably sometime in 2014.

Around mid-2018, I began ramping up my self-study of math as part of my entry into AI safety. I realized how much of the math I had learned a couple of years ago I had forgotten, and resolved to figure out some way to make my forgetting less drastic and also to make my learning more effective in general. So I started using Anki again, and shortly after that Michael Nielsen's "[Augmenting Long-term Memory](http://augmentingcognition.com/ltm.html)" was published, which influenced my thinking a lot.

Since mid-2018, I've continuously used Anki, playing around with it to see how to get the most out of it. I've also read a bunch of things related to learning in general.

specifically, with spaced repetition software, i've had the following experience: i used it for a while  a few years ago and thought it was pretty cool, but then i stopped using it. Then around a year ago when michael nielsen's SRS essay came out, i realized that i hadn't really understood SRS very well and that i hadn't been using it anywhere near as well as e.g. nielsen was using it. Since then, i feel like i've gotten much better at using it and have gotten a lot out of it (and also i've kept using it)

In other words, there's the distinction between "the tool failing the user" and "the user failing the tool" and it can be pretty hard to tell which one it is

## Inputs to my thinking

I want to list some of the main inputs to my thinking, so people can judge me on how I process evidence. Of course, even if you think I processed the evidence correctly, you might still think I sought out evidence in a biased way (and so disagree with my conclusions). I'm not aware of a way to convince people that I sought out evidence in a good way.

- Work by Michael Nielsen and Andy Matuschak, including [Quantum Country](https://quantum.country/) (all four essays plus reviews), ["Augmenting Long-term Memory"](http://augmentingcognition.com/ltm.html), ["Using spaced repetition systems to see through a piece of mathematics"](http://cognitivemedium.com/srs-mathematics), ["Reinventing explanation"](http://michaelnielsen.org/reinventing_explanation/index.html), [Andy's working notes](https://notes.andymatuschak.org/), ["How can we develop transformative tools for thought?"](https://numinous.productions/ttft/), ["Toward an exploratory medium for mathematics"](http://cognitivemedium.com/emm/emm.html), and ["Magic Paper"](http://cognitivemedium.com/magic_paper/index.html): I think Michael and Andy have done the most to influence my views on learning, particularly by promoting to my attention the idea that Anki usage has a lot of [scope for improvement](https://learning.subwiki.org/wiki/Scope_for_improvement).
- gwern's [spaced repetition page](https://www.gwern.net/Spaced-repetition): I read this a long time ago, so I don't actually remember what I thought.
- The [Anki subreddit](https://www.reddit.com/r/Anki/): very low quality on average, but in some threads people share tips on how to make cards, and some of those things are somewhat useful.
- Dunlosky 2013 paper https://pcl.sitehost.iu.edu/rgoldsto/courses/dunloskyimprovinglearning.pdf
- Richard Reitz, especially his [learning omega](https://docs.google.com/document/d/1Qu21SMy0DgQzYQBt1jCi416xeK6A-8eg84WA-kqamSM/edit) Google Doc.
- Lots of questions on Math Stack Exchange and Reddit about how to study math
- Lara Alcock's books about how to study math
- Cal Newport's _How to Become a Straight-A Student_
- Barbara Oakley's _A Mind For Numbers_
- Brown et al's _Make It Stick_
- Hans Freudenthal's writings about math education: I tried to understand what he was saying/what his main point is, but I never figured it out. https://www.quora.com/What-is-a-summary-of-Hans-Freudenthals-work-on-mathematical-education
- ["Making Things Hard on Yourself, But in a Good Way: Creating Desirable Difficulties to Enhance Learning"](https://teaching.yale-nus.edu.sg/wp-content/uploads/sites/25/2016/02/Making-Things-Hard-on-Yourself-but-in-a-Good-Way-2011.pdf)
- Piotr Wozniak, especially his [SuperMemo Guru](https://supermemo.guru/wiki/SuperMemo_Guru) wiki.
- The [Master How To Learn](https://www.masterhowtolearn.com/) website.
- My own informal experiments by using Anki.

This means I have *not* used the following as inputs:

- Educational psychology papers reporting on specific experiments: I've trusted other people to do this work for me, including Michael Nielsen, gwern, and the Dunlosky paper. For spaced repetition in particular, I've also found through my own experience that it basically works. I have not searched for, but also have not found, any disagreements with these results (on the order of "all of these papers are fraudulent and you shouldn't trust any of this"). I *have* briefly looked through a bunch of papers in order to figure out if they can teach me more about specific techniques to level up my Anki usage, but have mostly come away disappointed.


## How important is any of this, really?

Currently I think the biggest problems are scale and concept dependency tracking.

## Next steps

I think the way to make progress isn't to read more of the literature. The literature tends to test for basic effects but doesn't give you any help on how to take that basic effect and turn it into an effective learning procedure. It tells you that spaced repetition is real, but doesn't tell you the best way to create cards for mathematical proofs in Anki.

Given this, my plans are something like:

- Keep an eye on Michael Nielsen and Andy Matuschak (actually, apparently just Andy now)
- Occasionally check r/Anki and some learning blogs, to see if someone has come up with something new
- Continue playing with Anki
- for math in particular, I'm currently organizing my thoughts at https://wiki.issarice.com/wiki/Spaced_proof_review
