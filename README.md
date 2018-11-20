Relational Agents Website [![Build Status](https://travis-ci.org/zberwaldt/relational-agents.svg?branch=master)](https://travis-ci.org/zberwaldt/relational-agents)
===

## Table Of Contents 
- [Commands You Need To Know](#commands-you-need-to-know)
- [Commands That Are Nice To Know](#commands-that-are-nice-to-know)
- [Kinds Of Content](#kinds-of-content)
- [Making Updates](#making-updates)
    - [Updating Publcations](#updating-publications)
    - [Updating Projects](#updating-projects)
    - [Updating Press](#updating-press)
    - [Updating News](#updating-news)
    - [Updating Demoes](#updating-demoes)
- [Tasks](#tasks)


## Command(s) You Need To Know:

Commands: | Tags: | Description: | Example: | Additional Details:
--------- | ----- | ------------ | -------- | ------------------- 
`hugo` | __additional tags:__ | Compile your source into a static site into the `\public` directory. |  `hugo` | _n/a_ 
^ | --minify | All built html code minified | `hugo --minify` | Minifying is a good way to optimize your site.
^ | --baseURL | allows you to specify an alternative baseURL _default: `https://relationalagents.com/`_ | hugo --baseURL `http://some-other-url.com` | Just in case you want to deploy to some other URL
 `hugo server` | _n/a_ | Runs a development server on your local machine; Handy for previewing the site before deployment | `hugo server` | _n/a_


## Commands That Are Nice To Know:

Commands: | Tags: | Description: | Example: | Additional Details:
--------- | ----- | ------------ | -------- | ------------------- 
`hugo new` | additional tags: | For generating a new content files | `hugo new some-markdown-file.md` | _n/a_
^       | --kind | Specify the type of content, List of [kinds](#kinds-of-content) below. | `hugo new --kind publication publication/2019/better-listening-behavior` | See [kinds of content](#kinds-of-content) to see what types of content you can generate with the `cli`


## Kinds of Content
_addtional reference for the `hugo new --kind` command_

Kind:       | Example:                                                   | Details: 
-----       | --------                                                   | -------- 
year        | `hugo new --kind year publication/2019`                      | See [Adding years](#adding-years) to learn more about this type of content.
publication | `hugo new --kind publication/2019/better-listening-behavior` | See [Adding publications](#adding-publications) to learn more about this type of content.
project     | `hugo new --kind project project/listening-behavior`         | See [Updating projects](#updating-projects) to learn more about this type of content

There are a few other content sections that do not have predefined "archetypes": __Press, News, Demoes,__ and __People__
Click below to read how to make new content for each type.
- [Press](#updating-press)
- [News](#updating-news)
- [Demoes](#updating-demoes)
- [People](#updating-personnel)

## Making Updates

Below are sections dedicated to teaching how to update every content type for the site. Every type of content must have an `index.md`, which contains the "frontmatter" or data that describes the content you want to put on your site. Refer to the sections below to learn the format for each type of content.

__Jump To Section__

- [Publications](#updating-publication)
- [Projects](#updating-projects)
- [Press](#updating-press)
- [Personnel](#updating-personnel)
- [News](#updating-news)
- [Demoes](#updating-demoes)

### Updating Publications
--------------------

Updating publications can be a two step process. For `ragwebv6` I've organized all publications by year. If you are adding a publication from 2019, you'll need to create a new year section, which is covered [below](#adding-years). Otherwise you can just add a [publication](#adding-publications)


#### Adding Years 
The easiest way to generate a new year directory is with the hugo `cli`.
example:
```shell
:> hugo new --kind year publication/2019
```
This will create a new folder in `content/publication` named `2019` with an `_index.md` inside:

```yaml
---
title: ""
layout: years/list
articles: []
---
```



field: |  description: 
------ |  ------------
`title:` | The full title of your project
`layout:` | I've defined a special layout for lists of publications by year. This should always be set to `years/list`
`articles:` | This is an array that holds the name of each directory for publications that belong to a given year. Each entry should unique and be formatted like so: `"/unique-directory-name"`. See the example below

_excerpt from 2018 frontmatter:_

```yaml
articles: [
    "/breath-sensitive-interactive-meditation-coach",
    "/quester-a-speech-based-question-answering-support-system",
    "/relational-agent-to-provide-alcohol-intervention",
    "/embodied-conversational-agents-for-patients",
    "/predicting-user-engagement-in-longitudinal-interventions",
    "/collaborative-human-agent-oral-presentations",
    "/managing-chronic-conditions-with-a-smartphone",
    "/medical-shared-decision",
    "/user-gaze-behavior-while-discussing-substance-use",
    "/looking-the-part",
    "/a-conversational-decision-aid-to-support",
    "/creating-new-technologies-for-companionable-agents",
    "/using-relational-agents-to-promote-exercise",
    "/a-tablet-based-embodied-conversational-agent-to",
    "/patient-and-consumer-safety-risks",
]
```
Shorter is better, but ultimately it doesn't matter as long as the directory name is unique. They do not get built into pages or get published to the web. It's just a means to organize the content.

#### Adding Publications

The fastest way to add a publication is with the `cli`:

_example:_
```shell
>: hugo new --kind publication publication/2019/listening-behavior
```
You can manually do it, however whichever way you do it, as long as the frontmatter is formatted like below everything should work fine.

```yaml
---
title: "Put the full title of your paper here."
project: ["(e.g. Atrial Fibulation)"]
event: "Which event or journal was this paper for?"
authors: 
- name: "T. Bickmore"
- name: "S. O. Guy"
year: 2018
resources: 
 - name: "short name of paper file"
   src: "pdf.pdf"
external_url: null
date: {{ .Date }}
draft: false
headless: true
---
```


After you write up the frontmatter for a publication make sure you update the `articles: []` with the folder name. See _[Year _index.md](#year-_indexmd)_ for more details.

_example:_
```yaml
---
...
articles: [
    "/publication-directory-name",
]
---
```
##### Breakdown: 
field: |  description: 
------ |  ------------
`title:` | The full title of your project
`project:` | The name(s) of the project that the paper is linked to, in an array of strings. Must match exactly the title of a project on the website. This is how the generator knows to show a publication on a project page. It can belong to more than one project. 
`event:`| A list of resources that belong to the page __resources must be in the same directory.__
`authors:` | A list of the authors.
` - name:` | each author is formatted as: `"Lastname, F."`
`year:` | The year of publication.
`resources:` | If you have the pdf for a publication use this field, otherwise set it to `null`
` - name:` | The name of a given resource.
`    src: ` | The file of a given resource: (_i.e. `IVA19.pdf`_). The pdf must be in the publication directory.
`external_url:` | If the publication is hosted elsewhere, for whatever reason, put the full url here.
`date`| If you generate with the `cli` you don't have to worry about this. 
`draft:` | _default: false_. Set this to true if you don't want it to be included in the next build.
`headless:` | _default: true_ this insures that the content is not complied into html pages when you build.

### Updating Projects
-----------------
[back to top](#table-of-contents)

A project lives under the `content/project` directory. Each project has a dedicated directory.

 _example:_
```
/content
|_ /project
   |_/listening-behavior
   |_ index.md
   |_ image.jpg
```

#### Project Frontmatter Breakdown
Below is what the typical frontmatter for a project will be.
```yaml
---
title: ""
description: "Tell me about this project"
resources:
- name: main image
  src: image.jpg
date: {{ .Date }}
related_pubs: false
draft: false
---
```
field: |  description: 
------ |  ------------
`title:` | The full title of your project
`description:` | A brief description of the project
`resources:`| A list of resources that belong to the page __resources must be in the same directory.__
`- name:` | _default: main image_. The name of the primary image for a project
`   src:` | the name of the image _example:_ listening-behavior.jpg
` date`| If you generate with the `cli` you don't have to worry about this. 
`related_pubs:` | _default: false_. Set this to true so the generator knows to look for publications that have the matching project field.
`draft:` | _default: false_. Set this to true if you don't want it to be included in the next build.

### Updating Press 
-----------------
[back to top](#table-of-contents)

### Updating Personnel
-----------------
[back to top](#table-of-contents)

### Updating News
-----------------
[back to top](#table-of-contents)

### Updating Demoes
-----------------
[back to top](#table-of-contents)


### Tasks

- [x] optimized web assets
- [x] create build process
- [ ] write better documentation
- [ ] update content


