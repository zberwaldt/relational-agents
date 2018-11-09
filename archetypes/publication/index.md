---
name: "{{ replace .Name "-" " " | title }}"
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