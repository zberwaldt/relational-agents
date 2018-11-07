---
title: "Dtask"
---

DTask: A hierarchical task decomposition-based dialogue planner
====
DTask is a dialogue planner designed to model and execute system-directed dialogue, with multiple-choice user input. Dialogue is specified declaratively, as a hierarchical task decomposition. It is designed to model and execute system-directed dialogue, where user input is performed via selection from a multiple choice menu of possible utterances, dynamically updated at each turn of the dialogue. DTask uses a [CEA-2018](http://www.ce.org/Standards/browseByCommittee_4467.asp) recipe library to plan a task decomposition for each segment of a dialogue. DTask provides support for loading and saving data and metadata represented in [Resource Description Framework (RDF)](http://www.w3.org/RDF/) at runtime.


Prerequisites
----
Instructions for setting up the DTask system:

- Requires Java 1.5 or better.  Java 1.6 is preferred.

- lib/dtask.jar is a pre-compiled version of the dialogueengine.

The following jar files must be in the same directory. Some are only required on Java 1.5 (but can be included on Java 1.6). All of these should be included with this distribution:

From [Oracle](http://www.oracle.com/) site, download the following files:

- jsr173_api.jar (required for Java 1.5)

- sjsxp.jar (required for Java 1.5)

From [Mozilla](http://www.mozilla.org/rhino/download.html) site, download the following files:

- js.jar (required for Java 1.5)

- js-engine5.jar (required for Java 1.5)

From [Thai Open Source Software Center Ltd](http://www.thaiopensource.com/relaxng/jing.html) site, download the source files to build the jar:
- jing.jar (required for all)

Running DTask in console mode
----

DTask provides a simple console mode, which is useful for testing. Put the dependencies in the same directory as dtask.jar, then run it with: ``` java -jar lib/dtask.jar ```
It responds to the following commands:

- **help:** display descriptions and details on all commands 

- **eval:** evaluate Javascript; can set variables

- **load:** load a new model file. takes a path or URL.

- **models:** show all loaded models.

- **quit:** shutdown and exit

- **run:** begin a new top-level task

    _use_ "run task; slot1=value1; slot2=value2" _syntax to set the input slots_

- **say:** respond to the current dialogue turn if called with no arguments then displays the current possible choices.

- **source:** read and execute commands from a file

- **status:** display the current plan tree

Running DTask with LiteBody
----
Most of the time you'll want to deploy DTask with [Litebody](../litebody/) in a servlet. This section assumes that you've already read the Litebody <a href="litebody-setup.html">[installation guide](../litebody/installation).

First, you'll want to add dtask.jar and all its dependencies to the WEB-INF/lib directory of your servlet.  Next, add any DTask model files somewhere within your servlet. Conventionally, we use WEB-INF/models for this purpose, but anything should work.

Finally, you'll need to include some parameters in the web.xml file. The parameter "webframe.dialogue-manager" should be set to "edu.neu.ccs.task.web.DTaskManager"; this tells Litebody to use DTask as its dialogue manager.  There are also a number of DTask-specific parameters to set:

<table class="prop">
    <tr>
        <th>Property</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>dtask.models</td>
        <td>REQUIRED</td>
        <td>a whitespace-separated list of paths (within the servlet directories) to DTask model files</td>
    </tr>
    <tr>
        <td>dtask.top-task</td>
        <td>Top</td>
        <td>the name of the top-level task for a conversations</td>
    </tr>
    <tr>
        <td>dtask.top-input.SLOT-NAME</td>
        <td>NONE</td>
        <td>allows you to bind input slots of the top-level task.</td>
    </tr>
    <tr>
        <td>dtask.persistence</td>
        <td>NONE</td>
        <td>fully-qualified name of an implementation of the Persistence interface; this is optional, but can be used to save a user model after conversations, and load it again later.</td>
    </tr>
</table>

DTask Example
----

The xml file below shows an example of a fragment of a DTask dialogue model. This example implements a task ("RitualIntro") which is a short ritualized greeting to the user. There is one recipe provided which can achieve this task ("DoRitualIntro"), consisting of two subtasks ("HowAreYou" and "RespondToIntro").

Tasks can have locally-scoped input and output parameters. The "HowAreYou" task has one output slot, which defines the semantics of the user's utterance which will be represented. In this case, the semantics is simply a boolean value representing whether the user asked a reciprocal question of the agent.

The "RespondToIntro" task has one input parameter, and constraints on the recipe are used to bind the output of the earlier task to this input. The example shows one dialogue turn which can be used to achieve this task in the case where the user requested a reciprocal response. There may be any number of other dialogue turns specified with different applicability conditions.

{{<highlight xml>}}
  <task id="RitualIntro"/>
  <subtasks id="DoRitualIntro" goal="RitualIntro">
  <step name="ask" task="HowAreYou"/>
  <step name="respond" task="RespondToIntro"/>
  <binding slot="$respond.reciprocal" value="$ask.reciprocal"/>
  </subtasks>
  <task id="HowAreYou">
  <output name="reciprocal" type="boolean"/>
  <d:turn>
  <d:agent>Hi {USER.name}. How are you?</d:agent>
  <d:user>
  <d:say>I'm good. How are you?</d:say>
  <d:result slot="reciprocal" value="true"/>
  </d:user>
  <d:user>
  <d:say>Good.</d:say>
  <d:result slot="reciprocal" value="false"/>
  </d:user>
  </d:turn>
  </task>
  <task id="RespondToIntro">
  <input name="reciprocal" type="boolean"/>
  <d:turn>
  <applicable>$this.reciprocal</applicable>
  <d:agent>Great. Thanks for asking!</d:agent>
{{< /highlight >}}

Publications
----
<ul>
<li>Bickmore, T., Schulman, D., Sidner, C. (2011) A Reusable Framework for   Health Counseling Dialogue Systems based on a Behavioral Medicine   Ontology. Journal of Biomedical Informatics, 44, 183-197. <a href="http://relationalagents.com/publications/JBI2011-ontology.pdf">PDF</a></li>
<li>Bickmore, T., Schulman, D. and Shaw, G. (2009) DTask &amp; LiteBody: Open Source, Standards-based Tools for Building Web-deployed Embodied Conversational Agents Proceedings of Intelligent Virtual Agents, Amsterdam. <a href="publications/IVA09.litebody.pdf" target="blank">PDF</a>
</li>
</ul>

Licensing
----
[![Creative Commons License](http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)<span property="dc:title" xmlns:dc="http://purl.org/dc/elements/1.1/">DTask</span> by <a href="http://relationalagents.com " property="cc:attributionName" rel="cc:attributionURL" xmlns:cc="http://creativecommons.org/ns#">Northeastern University Relational Agents Group</a> is licensed under a <a style="float: none; margin: 0;" href="http://creativecommons.org/licenses/by-nc-sa/3.0/" rel="license">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>. Based on a work at <a href="http://dtask.sourceforge.net" rel="dc:source" xmlns:dc="http://purl.org/dc/elements/1.1/">dtask.sourceforge.net</a>.

We also request that any publications covering work based on DTask cite the Bickmore, et al, 2011 JBI paper (above).

Download
----
[http://dtask.sourceforge.net/](http://dtask.sourceforge.net/)