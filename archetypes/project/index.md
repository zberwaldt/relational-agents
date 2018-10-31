---
title: "{{ replace .Name "-" " " | title }}"
description: "Tell me about this project"
url: "/{{ lower .Name }}/"
resources:
- name: main image
  src: image.jpg
- name: demo video
  src: demo.mov
date: {{ .Date }}
related_pubs: false
draft: false
---
