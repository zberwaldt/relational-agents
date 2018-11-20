Relational Agents Website Source
===

[![Build Status](https://travis-ci.org/zberwaldt/relational-agents.svg?branch=master)](https://travis-ci.org/zberwaldt/relational-agents)

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


### Command(s) You Need To Know:

Commands: | Tags: | Description: | Example: | Additional Details:
--------- | ----- | ------------ | -------- | ------------------- 
`hugo`  | __additional tags:__ | Compile your source into a static site into the `\public` directory. |  `hugo` | _n/a_ 
^ | --minify | All built html code minified | `hugo --minify` | Minifying is a good way to optimize your site.
^ | --baseURL | allows you to specify an alternative baseURL _default: `https://relationalagents.com/`_ | hugo --baseURL `http://some-other-url.com` | Just in case you want to deploy to some other URL
 `hugo server` | _n/a_ | Runs a development server on your local machine; Handy for previewing the site before deployment | `hugo server` | _n/a_


### Commands That Are Nice To Know:

Commands: | Tags: | Description: | Example: | Additional Details:
--------- | ----- | ------------ | -------- | ------------------- 
`hugo new` | additional tags: | For generating a new content files | `hugo new some-markdown-file.md` | This example will create a generic page, should not use for this site
^       | --kind | Specify the type of content, List of [kinds](#kinds-of-content) below. | `hugo new --kind publication publication/2019/better-listening-behavior` | See [kinds of content](#kinds-of-content) to see what types of content you can generate with the `cli`


### Kinds of Content
_addtional reference for the `hugo new --kind` command_

Kind:       | Example:                                                   | Details: 
-----       | --------                                                   | -------- 
year        | hugo new --kind year publication/2019                      |
publication | hugo new --kind publication/2019/better-listening-behavior |
project     | hugo new --kind project project/listening-behavior         |

There are a few other content sections that do not have predefined "archetypes": __Press, News, Demoes, and People__
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

Updating can be a two step process. For `ragwebv6` I've organized all publications by year. If you are adding a publication from 2019, you'll need to create a new year section, which is covered [below](#adding-years). Otherwise you can just add a [publication](#adding-publications)


#### Adding Years 
--------------------
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
`layout:` | 
`articles:` |

#### Adding Publications
--------------------------

The fastest way to add a publication is with the `cli`:

_example:_
```shell
>: hugo new --kind publication publication/2019/listening-behavior
```
You can manually do it, however whichever way you do it, as long as the frontmatter is formatted like below everything should work fine.

```yaml
---
title: "Put the full title of your paper here."
project: "Put the name of the project that served as the basis for this publication (e.g. Atrial Fibulation)"
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


