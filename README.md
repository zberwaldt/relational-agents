Relational Agents Website Source
===

[![Build Status](https://travis-ci.org/zberwaldt/relational-agents.svg?branch=master)](https://travis-ci.org/zberwaldt/relational-agents)

### Commands You Need To Know:

Commands | Tags | Description | Example | Notes
-------- | ---- | ----------- | ------- | ----- 
`hugo new --kind year publication/year-of-publication` | | For generating a new section for publications.
`hugo new --kind publication publication/year-of-publication/unique-title` | | this will generate a new publication.
`hugo`  | additional tags: | compile your source into a static site |  `hugo` | __IMPORTANT:__ by default you should always use: `hugo --minify`
 - | --minify | adding this tag will output the site with all html code minified | `hugo --minify`
 - | --gc | adding this tag will preform garbage cleaning on | hugo --gc
 - | --baseURL | allows you to specify an alternative baseURL _default: https<span></span>://relationalagents.com/_ | hugo --baseURL http<span></span>://some-other-url.com

### tasks

- [x] optimized web assets
- [x] create build process
- [ ] update content