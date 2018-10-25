---
name: "{{ replace .Name "-" " " | title }}"
title: "Put the full title of your paper here."
event: "Which event or journal was this paper for?"
authors: 
- name: "T. Bickmore"
- name: "S. O. Guy"
year: 2018
resources: 
 - name: "short name of paper file"
   src: "name of file with extention (i.e: pdf)"
external_url: null
date: {{ .Date }}
draft: false
---