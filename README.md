Relational Agents Website Source
===

[![Build Status](https://travis-ci.org/zberwaldt/relational-agents.svg?branch=master)](https://travis-ci.org/zberwaldt/relational-agents)

## Table Of Contents 
- [Commands You Need To Know](#commands-you-need-to-know)
- [Commands That Are Nice To Know](#commands-that-are-nice-to-know)
- [Kinds Of Content](#kinds-of-content)
- [Archtype Index File Formats](#archtype-index-file-formats)
    - [Year `_index.md`](#year-_indexmd)
        - [Year Breakdown](#year-breakdown)
    - [Publication `index.md`](#publication-indexmd)
        - [Publication Breakdown](#publication-breakdown)
    - [Project `index.md`](#project-indexmd)
        - [Project Breakdown](#project-breakdown)
- [Tasks](#tasks)


### Command(s) You Need To Know:

Commands: | Tags: | Description: | Example: | Additional Details:
--------- | ----- | ------------ | -------- | ------------------- 
`hugo`  | __additional tags:__ | Compile your source into a static site into the `\public` directory. |  `hugo` | _n/a_ 
^ | --minify | All built html code minified | `hugo --minify` | Minifying is a good way to optimize your site.
^ | --gc | Preform garbage cleaning | `hugo --gc` | Running the command will delete old cache files from previous builds.
^ | --baseURL | allows you to specify an alternative baseURL _default: `https://relationalagents.com/`_ | hugo --baseURL `http://some-other-url.com` | Just in case you want to deploy to some other URL
 `hugo server` | _n/a_ | Runs a development server on your local machine | `hugo server` | Handy for previewing your site before deployment.


### Commands That Are Nice To Know:

Commands: | Tags: | Description: | Example: | Additional Details:
--------- | ----- | ------------ | -------- | ------------------- 
`hugo new` | additional tags: | For generating a new content files | `hugo new some-markdown-file.md` | _n/a_
^       | --kind | Specify the type of content | `hugo new --kind publication publication/2019/better-listening-behavior` | See [kinds of content](#kinds-of-content) to see what types of content you can generate with the `cli`


### Kinds of Content
_addtional reference for the `hugo new --kind` command_

Kind:       | Example:                                                   | Details: 
-----       | --------                                                   | -------- 
year        | hugo new --kind year publication/2019                      |
publication | hugo new --kind publication/2019/better-listening-behavior |
project     | hugo new --kind project project/listening-behavior         |

## Archtype Index File Formats:

### Year `_index.md`
--------------------
```yaml
---
title: ""
layout: years/list
articles: []
---
```
#### Year Breakdown:
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

### Publication `index.md`
--------------------------
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
#### Publication Breakdown:

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

### Project `index.md`
---------------------------
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
#### Project Breakdown:
----------------
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
### Tasks

- [x] optimized web assets
- [x] create build process
- [ ] update content


