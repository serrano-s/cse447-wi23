---
layout: home
title: Natural Language Processing
nav_exclude: true
toc: true
seo:
  type: Course
  name: Natural Language Processing
---

# {{ site.tagline }}
{: .fs-7 .fw-350 }
MWF 1:30-2:20pm, CSE2 G01
{: .fs-6 .fw-300 }

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

{% assign teaching_assistants = site.staffers | where: 'role', 'Teaching Assistant' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}

{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}

<!-- Office hours are available on Zoom by appointment. -->

## Announcements

- Have anything you'd like to anonymously let the course staff know? You are of course welcome to email us, but feel free to use [this anonymous feedback form](https://docs.google.com/forms/d/e/1FAIpQLSfHu8vkapQJql7S7T15y4_DGT0_Ylrpi587ImnWzO83EgJHPQ/viewform) instead if you'd prefer.
  
## Summary

This course will explore foundational statistical techniques for the automatic analysis of natural (human) language text. Towards this end the course will introduce pragmatic formalisms for representing structure in natural language, and algorithms for annotating raw text with those structures. The dominant modeling paradigm is corpus-driven statistical learning, covering both supervised and unsupervised methods. Algorithms for NLP is a lab-based course. This means that instead of homeworks and exams, you will mainly be graded based on three hands-on coding projects.

This course assumes a good background in basic probability and a strong ability to program in Python. Experience using numerical libraries such as NumPy and neural network libraries such as PyTorch are a plus. Prior experience with machine learning is important. Prior experience in linguistics or natural languages is helpful, but not required. There will be a lot of statistics, algorithms, and coding in this class.

## Calendar

Calendar is tentative and subject to change. More details will be added as the quarter continues.

<table>
  <thead>
  <tr>
    <th>Week</th>
    <th>Date</th>
    <th width="30%">Topics</th>
    <th width="20%">Readings</th>
    <th width="13%">Homeworks</th>
  </tr>
  </thead>
  <tbody>
  {% for week in site.data.calendar %}
    {% for day in week.days %}
      <tr>
        {% if forloop.index == 1 %}
        <td rowspan="{{week.size}}">{{week.week}}</td>
        {% endif %}
        <td>{{day.date}}</td>
        <td class="cal-content">
          {{day.topics}}
          <br>
          {% if day.slides %}
            <a href="{{day.slides}}" class="cal-content-link">[slides]</a>
          {% endif %}
          {% if day.recording %}
            <a href="{{day.recording}}" class="cal-content-link">[recording]</a>
          {% endif %}
          {% if day.supplement %}
            <a href="{{day.supplement}}" class="cal-content-link">[supplementary recording]</a>
          {% endif %}
        </td>
        <td class="cal-content">
          {% for reading in day.readings %}
            {% if reading.link %}<a href="{{reading.link}}" class="cal-content-link">{% endif %}
              {{reading.title}}{% if forloop.last == false %};{% endif %}
            {% if reading.link %}</a>{% endif %}
          {% endfor %}
        </td>
        <td class="cal-content">{{day.due}}</td>
      </tr>
    {% endfor %}
  {% endfor %}
  </tbody>
</table>

## Resources

* Readings
  - [Eis](https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes.pdf): Natural Language Processing (Jacob Eisenstein)
  - [J&M III](https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf): Speech and Language Processing (Dan Jurafsky and James H. Martin)
* [Ed discussion board](https://edstem.org/us/courses/32306/)
<!-- * Zoom link -->
* [Canvas](https://canvas.uw.edu/courses/1610941)
* [GitLab](https://gitlab.cs.washington.edu/cse447-wi23)

## Assignments/Grading

* Project 1 (sequence classification): 30%
    - We will build a system for automatically classifying song lyrics comments by era. 
    - Specifically, we build machine learning _text classifiers_, including both generative and discriminative models, and explore techniques to improve the models.
* Project 2 (sequence labeling): 30%
    - We focus on sequence labeling with _Hidden Markov Models_ and some simple deep learning based models. 
    - Our task is part-of-speech tagging on English and Norwegian from the Universal Dependencies dataset.
    - We will cover the _Viterbi algorithm_.
* Project 3 (dependency parsing): 30%
    - We will implement a transition-based _dependency parser_.
    - The algorithm would be new and specific to the dependency parsing problem, but the underlying building blocks of the method are still some neural network modules covered in P1 and P2.
* Quizzes: 10%
    - Starting from the 3rd week, we will have quizzes on Wednesdays.
    - There will be 8 quizzes in total.
    - Quizzes will be released at the end of class on Canvas and be available for twelve hours. They should take approximately ten minutes to complete.
    - 5 best quizzes will be counted into final score. Each quiz will occupy 2% of final score. 

* Participation: 10% bonus

## Policies

* **Late policy.** Each student will be granted **5 late days** to use over the duration of the quarter. You can use a **maximum of 3 late days** on any one project. Weekends and holidays are also counted as late days. Late submissions are automatically considered as using late days. Using late days will not affect your grade. However, projects submitted late after all late days have been used will receive no credit. Be careful!

* **Academic honesty.** Homework assignments are to be completed individually. Verbal collaboration on homework assignments is acceptable, as well as re-implementation of relevant algorithms from research papers, but everything you turn in must be your own work, and you must note the names of anyone you collaborated with on each problem and cite resources that you used to learn about the problem. Suspected violations of academic integrity rules will be handled in accordance with [UW guidelines](https://www.washington.edu/cssc/for-students/overview-of-the-student-conduct-process/) on academic misconduct. See also the [academic integrity form posted to Canvas](https://canvas.uw.edu/courses/1610941/files?preview=100173898).

* **Accommodations.** If you have a disability and have an accommodations letter from the Disability Resources office, I encourage you to discuss your accommodations and needs with me as early in the semester as possible. I will work with you to ensure that accommodations are provided as appropriate. If you suspect that you may have a disability and would benefit from accommodations but are not yet registered with the office of Disability Resources for Students, I encourage you to apply [here](https://denali.accessiblelearning.com/Washington/ApplicationStudent.aspx).

## Note to Students

Take care of yourself! As a student, you may experience a range of challenges that can interfere with learning, such as strained relationships, increased anxiety, substance use, feeling down, difficulty concentrating and/or lack of motivation. All of us benefit from support during times of struggle. There are many helpful resources available on campus and an important part of having a healthy life is learning how to ask for help. Asking for support sooner rather than later is almost always helpful. UW services are available, and treatment does work. You can learn more about confidential mental health services available on campus [here](https://www.washington.edu/counseling/). Crisis services are available from the counseling center 24/7 by phone at +1 (866) 743-7732 ([more details here](https://www.washington.edu/counseling/services/crisis/)).

## COVID-19 Safety

In accordance with [UW guidelines](https://www.washington.edu/coronavirus/), we are implementing the following policies to ensure the safety of our students and instructors to the maximum extent possible:

* **Course instruction** The course will be taught in-person only, following the UW guidelines. However, links to recordings of each lecture will be posted on this site by the day following class.

* **Remote access.** If you are sick or have potentially been exposed to COVID-19, **stay home**! While we encourage everyone to attend class in-person when they are well, there will always be a Zoom meeting for the class and there is no penalty for attending remotely. Office hours are also available both in-person and over Zoom (by appointment).

<!-- When in public, indoor spaces occupied by other people, **you must wear a mask**. This includes class sections and office hours. See more about UW's masking requirements [here](https://www.ehs.washington.edu/covid-19-prevention-and-response/face-covering-requirements). The instructors will abide by the same masking policy.

  For the purposes of this policy, a face covering must fit snugly against the sides of the face and completely cover the nose and mouth. Bandanas and gaiters are not considered face coverings under this policy. Students who do not wear a face mask will be asked to leave the classroom. Repeated failure to wear a face covering may result in being referred to the Student Conduct Office for possible disciplinary action.

  UW has approved a hydration exemption which allows students and instructors to briefly move aside their mask if they are drinking water even in class. This exemption is meant be used only for a brief moment to hydrate, and does not allow talking with one's mask off or having one's mask removed for a prolonged period of time. This exemption does not allow for eating food in classes.

  --- -->

* **Masking.**  In accordance with UW's masking policy, masks are strongly recommended the first two weeks of the quarter and will be recommended after that, so long as we stay in the CDC’s "low" community level. Given the flexibility in choosing whether to wear a mask or not, please be respectful of others’ choices. Read more about UW's policy [here](https://www.ehs.washington.edu/covid-19-prevention-and-response/face-covering-requirements).

  If you would like a mask, please feel free to stop by the reception desk in the Allen Center, where they can provide you your choice of either a KN95/N95 mask or a cloth mask. Additionally, UW mask distribution will continue at various library locations, the Health Sciences Center, the HUB, and testing sites.
  
* **Social distancing.** Currently, UW does not require social distancing in the classroom or office hours for students who are vaccinated and wearing a mask; it can also make it difficult to navigate and interact in such spaces. We do not mandate social distancing, but ask that if another student asks you to maintain distance from them, that you respect their request.

* **What if you get sick?** Stay home if you are sick! The [COVID-19 Public Health Flowchart](https://www.ehs.washington.edu/system/files/resources/COVID-19-public-health-flowchart.pdf) indicates what you should do if you test positive, have been exposed to COVID-19, or have symptoms. Also see [this FAQ](https://www.washington.edu/coronavirus/faq/) for what to do.

* **What if we get sick?** We will reschedule class, hold it remotely, or bring in a substitute lecturer/facilitator if necessary to prevent exposing students. We will try to give notice as far in advance as possible if an in-person event is moving to be held remotely, but please check your email beforehand to be sure you don't miss anything.
