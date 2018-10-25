---
name: "{{ replace .Name "-" " " | title }}"
position: "Job position"
bio:  "Tell me about yourself."
image: images/image-name.ext
date: {{ .Date }}
draft: false
---