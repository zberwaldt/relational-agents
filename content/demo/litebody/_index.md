---
title: "litebody"
layout: single
draft: false
---

<a class="back-link" href="../"><i class="fas fa-chevron-left"></i>Go Back</a>

Litebody: An Open-Source Tool for Building Lightweight, Web-deployed Embodied Conversational Agents
=======

Litebody is a set of open-source tools for building lightweight, web-deployed Embodied Conversational Agents (ECAs). Litebody is designed to have minimal hardware requirements on the client side, primarily by handling computationally-intensive tasks (such as speech synthesis) on the server. On most contemporary web browsers, no custom client installation will be required beyond Adobe Flash. The LiteBody server software will currently run on either Windows or Linux, and interoperates with either FreeTTS or Loquendo speech synthesizers. The client-server communication protocol can be secured by running over https, and additional measures are taken to ensure the security of a given user's communication with the agent. 

Components
----
Components of the Litebody system, and their features, include: 
1. **Litebody Protocol:** an http or https based client-server protocol for delivering audio and animation scripts from a server to an ECA client, and for delivering user input from client to server.

2. **Litebody Client:** a Flash-based ECA client, which supports a core set of nonverbal behavior. Our current implementations including the character animation distributed with Litebody are as small as 500K, allowing reasonable download times even on slow network connections. It can allow multiple-choice or free-text user input, and has a plug-in architecture that can be used to provide additional input methods.

3. **Litebody Server Framework:** used to build Java-based web applications which implement the Litebody Protocol. The framework abstracts low-level details of the protocol and is intended to allow the use of arbitrary dialogue engines with Litebody. We also provide an open-source dialogue engine, DTask, which is based on hierarchical task decomposition and a public standard task description language, and readily interoperates with Litebody.

4. **Litebody TTS Server:** handles text-to-speech synthesis, and is responsible for generating audio files and timing information. We provide a Java-based implementation which currently can use either FreeTTS (open-source) or Loquendo (with the addition of licensed software), with a Microsoft SAPI interface in development.

Documentation
----
- [Installation Guide](./installation/)
- [LiteBody client-server communication protocol](./protocol/)

Demo
----
- [Sample LiteBody Web Agent](../)

Licensing 
-----
![Creative Commons License](http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png) LiteBody by Northeastern University Relational Agents Group  is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. Based on a work at [litebodysuite.sourceforge.net](http://litebodysuite.sourceforge.net)


Download
-------

[http://litebodysuite.sourceforge.net/](http://litebodysuite.sourceforge.net/)

