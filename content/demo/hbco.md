---
title: "hbco"
draft: false
---

HBCO: Open Source Ontology and Task Models for Deploying Health Behavior Change Dialogue Systems
=======

The Health Behavior Change Ontology (HBCO) is an ontology, knowledge base, and set of task models that can be used to drive health behavior change counseling systems. The system models the theory-driven therapeutic planning processes of a human health advisor during a counseling session, and is designed to be reusable. To address issues of reuse, we have built the system on public standard formalisms for computerized ontologies ([OWL](http://www.w3.org/TR/owl-features/) and [RDF](http://www.w3.org/TR/2004/REC-rdf-concepts-20040210/)) and hierarchical task models ([ANSI/CEA-2018](http://ce.org/Standards/browseByCommittee_4467.asp)).

HBCO is based on a "domain ontology", which specifies the conceptualization of the domain of theory-driven, conversational agent-based behavior change interventions. Domain ontologies contain concrete categories that are of direct relevance to inference. Our ontology is "theory-driven" because only psychological states and therapeutic actions (such as counseling dialogue) that are sanctioned by a theory or method of health behavior change counseling are included in the model. We assume that the "counselor" (conversational agent) may have multiple conversations with a given "patient" (user) over time, and that its only means of effecting change is through dialogue. The ontology does not make any assumptions about the underlying dialogue model, and only makes reference to "Dialogue Actions" that can be realized as discourse segments consisting of one or more consecutive utterances by the counselor and patient. Thus, the knowledge in the ontology is not sufficient to produce a counseling dialogue; it must be augmented with information about how to produce specific utterances and how multiple utterances and Dialogue Actions should be sequenced. In our system, this information is encoded in our task model.

HBCO contains task models for transtheoretical-model-based dialog to promote physical activity (walking, based on pedometer steps) and diet (fruit and vegetable consumption). The models include emphasis on motivational interviewing techniques for early stages of change and social cognitive techniques for later stages of change, encompassing rapport building, assessment, feedback and negotiation within counseling sessions, and homework assignments and behavioral goals between counseling sessions.

HBCO is designed to be used in conunction with and interpreted by the [DTask](../dtask/) dialogue engine and the [LiteBody](../litebody/) web-based conversational agent interface.

Publications
----
- Bickmore, T., Schulman, D., Sidner, C. (2011) A Reusable Framework for Health Counseling Dialogue Systems based on a Behavioral Medicine Ontology. Journal of Biomedical Informatics, 44, 183-197. PDF

- Bickmore, T., Schulman, D. and Shaw, G. (2009) DTask & LiteBody: Open Source, Standards-based Tools for Building Web-deployed Embodied Conversational Agents Proceedings of Intelligent Virtual Agents, Amsterdam. PDF

Licensing 
----
[![Creative Commons License](http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) HBCO by <a xmlns:cc="http://creativecommons.org/ns#" href="http://relationalagents.com " property="cc:attributionName" rel="cc:attributionURL">Northeastern University Relational Agents Group</a> is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. Based on a work at [tbd.sourceforge.net](http://litebody.sourceforge.net).

We also request that any publications covering work based on HBCO cite the Bickmore, et al, 2011 JBI paper (above).

Download
----

[http://hbco.courceforge.net](http://hbco.courceforge.net)