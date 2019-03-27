Relational Agents Website [![Build Status](https://travis-ci.org/zberwaldt/relational-agents.svg?branch=master)](https://travis-ci.org/zberwaldt/relational-agents)
===

Table Of Contents
---

- [Important Thing to Know](#important-things-to-know)
- [Where is content located?](#where-is-the-content)
  - [Creating or Editing Demoes](#creating-or-editing-demoes)
  - [Creating or Editing People](#creating-or-editing-people)
  - [Creating or Editing Press](#creating-or-editing-press)
  - [Creating or Editing Projects](#creating-or-editing-projects)
    - [Archiving Old Projects](#archiving-old-projects)
  - [Creating or Editing Publications](#creating-or-editing-publications)
    - [Scaffolding Publication Year](#scaffolding-publication-year)
    - [Scaffolding Publications](#scaffolding-publications)
- [Modifying Hero Images On The Homepage](#modifying-hero-images-on-the-homepage)
- [Modifying Styles](#modifying-styles)
- [Modifying Layouts](#modifying-layouts)
- [How Do I Preview The Site?](#previewing-the-site)
- [I have questions](#i-have-questions)

Important Things to Know
----

The Hugo static site generator makes extensive use of Markdown as the basis for
the content of the site. You will have to write it. Fortunately is very simple
and easy to learn. Hugo uses a particular flavor called BlackFriday that has a
few extra features that are listed [here](https://gohugo.io/content-management/formats#configure-blackfriday-markdown-rendering) in the documenatation.
However, You shouldn't have to ever mess with the configuration.

Resources for learning Markdown are [here](https://gohugo.io/content-management/formats/#learn-markdown).

Where Is The Content
----------

All content files are located in the `content` directory. Each content type is 
housed in their own dedicated directory. There are five content types:

- demo
- people
- press
- project
- publication

Creating or Editing Demoes
---

To create a new demo page, simple create a Markdown file in the `demo` directory.
Name the file the same as the project or product it's for. Look to the other demoes
for reference if you need more than a single page demo. 

**If you need to add a demo video:**

Add the embed code to the `_index.md` file in the `demo` directory. Format the 
code as html, and also follow the other demoes on the page as reference.

Creating or Editing People
---

To create or edit new personnel, open the `_index.md` file. In the `resources` 
field you will see all listed employees and candidates. Using the other entries
as reference, create a new employee or candidate. Or simply edit the content of
the sub-fields of each entry. Lastly, add the image for that person to the 
`people` directory.

Creating or Editing Press
---

Creating or editing press is similar to editing personnel. Open the `index.md` 
contained within the `press` directory and edit the entries in the press field 
or create a new entry using the others as reference.

Creating or Editing Projects
---

**This section assumes you have the hugo generator installed on your machine.**

Because projects get their own page on the site, generating new projects is a 
little different. In your terminal use this command:

    \:> hugo new --kind project project/name-of-project

This will scaffold a project directory that is prepopulated with the basic 
components for generating a given project page.

### Archiving Old Projects

To archive a project, all you have to do is move the project folder you want to
archive and place it in the `archive` subdirectory in the `project` directory. 
On the next build, the project will now appear in the archive section.

Creating or Editing Publications
---

**This section assumes you have the hugo generator installed on your machine.**

### Scaffolding Publication year

Publications are organized together by year. If the year of your publication doesn't
exist you will need to scaffold a publication year directory with the following
command:

    hugo new --kind year publication/year-of-publication

with `/year-of-publicaiton` as the actual year. For example:

    /2019

Within that directory will be a `_index.md`. This file is used to manage and track
all your publications for that year. There is a technical reason for this, that will
not be covered in this documenation.

There is only one field you need to be concerned with in the `_index.md` file,
the `articles` field. Every entry should reference a publication subdirectory
like so:

    "/pepper-a-robot"

With `publication-subdirectory` being replace with the _exact_ subdirectory name.
Additionally, you should list each directory in the order you want them to appear
on the site.

Use the `_index.md` files from other publication years as reference.

### Scaffolding Publications

**IMPORTANT** If the year directory hasn't been scaffolded, you must do that first!
please refer to [previous section](#scaffolding-publication-year)

To scaffold a directory for a publication use this command:

    \:> hugo new --kind publication/year-of-publication/publication-folder

With `year-of-publication` replaced with the year. Example: `2019`

And, with `publication-folder` replaced with your desired name. **_IT MUST BE UNIQUE_**
Example: `pepper-a-robot`. 

The final command will look like this:

    \:> hugo new --kind publication/2019/pepper-a-robot

A new publication subdirectory will be scaffolded. It will contain two files

- index.md
- pdf.pdf

`index.md` is responsible for managing the metadata for the given publication.

You should refer to other publication `index.md` for reference.

`pdf.pdf` should be removed if there is no pdf. If there is one associated with
the publication add that file to the subdirectory and reference it in the metadata
in `index.md`. Again, use other publication `index.md` as reference.

[back to top](#table-of-contents)

Modifying Hero Images On The Homepage
---

Managing the hero images seen on the home page is relatively straightforward.
There are only three hero images you should be concerned with located in the below
directory path.

    project-directory
    |_themes
      |_rag-theme
        |_static
          |_img

those images are, in order of appearance on the page:

- jumbotron.png
- explore.png
- team-photo.jpg

Name the replacement image the same as it's match and place it in the previously mentioned directory path.

[back to top](#table-of-contents)

Modifying Styles
---

If you want to make changes to the style of the website you can find the stylesheet
In the following directory path:
  
    project-directory
    |_themes
      |_rag-theme
        |_static
          |_css
            |_style.css

I tried to write efficient and unified css, so if you don't like css editing this
file isn't for the feint of heart. In hindsight, I 

[back to top](#table-of-contents)

Modifying Layouts
---

You can find the layouts in the `layouts` directory. They are organized by page
or content type. Some knowledge of how hugo organizes [layouts](https://gohugo.io/categories/templates) for content in required
Additionally, you will need to know the syntax for hugo layouts. It is very well
documented on [gohugo.io](https://gohugo.io)

[back to top](#table-of-contents)

Previewing The Site
---

**This section assumes you have the hugo generator installed on your machine.**

Hugo comes with a development server that will enable you to preview the site
as close to how it will appear on the real web.

    \:> hugo server -D

You can omit the `-D` flag. It just allows the server to auto refresh when you make
changes to files.

[back to top](#table-of-contents)

Building The Site
---

I have setup a build process that builds the site for you. However, you have to 
use the version of the code base that is hosted on Github. Make your changes to
the code base, then push, then after a few moments you can download the latest
build from the `build` branch. However, if you choose to not use this functionality
you can still generate the site manually.

### Manually Building The Site.

**This section assumes you have the hugo generator installed on your machine.**

To initiate a manual build of your site make sure you are in the top level of
your project directory in your terminal. Then enter in the following command:

    \:> hugo --baseURL https://relationalagents.com

There is one additional tag that will generate an optimized site, meaning the code will
be minified. However, it will not be human readable. the tag is `--minify` and
is used like so:

    \:> hugo --minify --baseURL https://relationalagents.com

I recommend using the latter version of the command. Regardless of which one used,
the site will be compiled into the `\public` directory. The files there are the ones
you want to put on your hosting server.

[back to top](#table-of-contents)

I Have Questions
---

Email me [here](mailto:zberwaldt@gmail.com?Subject=I%20Have%20Questions). I will
do my best to get back to you as soon as possible.

[back to top](#table-of-contents)

