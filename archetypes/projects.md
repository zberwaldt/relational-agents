---
title: "{{ replace .Name "-" " " | title }}"
description: "Tell me about this project"
url: "/{{ lower .Name }}/"
resources:
- src: image
  name: main image
date: {{ .Date }}
draft: true
---
