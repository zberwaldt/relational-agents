---
name: "{{ replace .Name "-" " " | title }}"
position: "Job position"
bio:  "Tell me about yourself."
resource: 
 - name: "{{ replace .Name "-" " " | title }}"
   src: "image.jpg"
date: {{ .Date }}
draft: false
---