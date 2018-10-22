---
name: "{{ replace .Name "-" " " | title }}"
position: "Job position"
bio:  "Tell me about yourself."
resources:
- name: image name
  src: images/image-name.ext
date: {{ .Date }}
draft: true
---