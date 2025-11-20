{% extends "base.html" %}

{% block sidebar %}
<div class="list-group list-group-flush py-3">
  <button type="submit" form="main-form"
          class="list-group-item list-group-item-action {% if active_tab == 'timetable' %}active{% endif %}"
          onclick="document.getElementById('tab').value='timetable';">
    🗓 Timetable
  </button>
  <button type="submit" form="main-form"
          class="list-group-item list-group-item-action {% if active_tab == 'lesson_plan' %}active{% endif %}"
          onclick="document.getElementById('tab').value='lesson_plan';">
    📚 Lesson Plan
  </button>
  <button type="submit" form="main-form"
          class="list-group-item list-group-item-action {% if active_tab == 'test' %}active{% endif %}"
          onclick="document.getElementById('tab').value='test';">
    ✏️ Test / Worksheet
  </button>
  <button type="submit" form="main-form"
          class="list-group-item list-group-item-action {% if active_tab == 'parent_message' %}active{% endif %}"
          onclick="document.getElementById('tab').value='parent_message';">
    👨👩👧 Parent Message
  </button>
  <button type="submit" form="main-form"
          class="list-group-item list-group-item-action {% if active_tab == 'behaviour' %}active{% endif %}"
          onclick="document.getElementById('tab').value='behaviour';">
    🧠 Behaviour Note
  </button>
  <button type="submit" form="main-form"
          class="list-group-item list-group-item-action {% if active_tab == 'emergency' %}active{% endif %}"
          onclick="document.getElementById('tab').value='emergency';">
    🚨 Emergency Plan
  </button>
  <button type="submit" form="main-form"
          class="list-group-item list-group-item-action {% if active_tab == 'heatmap' %}active{% endif %}"
          onclick="document.getElementById('tab').value='heatmap';">
    📊 Progress Heatmap
  </button>
</div>
{% endblock %}

{% block content %}
<div class="card shadow-sm mb-4">
  <div class="card-body">
    <h3 class="card-title mb-2">Welcome, Teacher</h3>
    <p class="card-text text-muted mb-0">
      Choose a feature from the left, fill the form, and let your AI assistant handle the work.
    </p>
  </div>
</div>

<form id="main-form" method="post" class="card shadow-sm mb-4">
  <div class="card-body">
    <input type="hidden" id="tab" name="action" value="{{ active_tab }}">

    {% if active_tab == 'timetable' %}
      <h4 class="mb-3">🗓 Generate Timetable</h4>
      <div class="mb-3">
        <label class="form-label">Classes (comma-separated)</label>
        <input type="text" name="classes" class="form-control"
               placeholder="Class 6-A, Class 6-B, Class 7-A">
      </div>
      <div class="mb-3">
        <label class="form-label">Periods per day</label>
        <input type="number" name="periods_per_day" class="form-control" value="6">
      </div>
      <div class="mb-3">
        <label class="form-label">Days (comma-separated)</label>
        <input type="text" name="days" class="form-control"
               value="Monday, Tuesday, Wednesday, Thursday, Friday">
      </div>

    {% elif active_tab == 'lesson_plan' %}
      <h4 class="mb-3">📚 Generate Lesson Plan</h4>
      <div class="mb-3">
        <label class="form-label">Grade</label>
        <input type="text" name="grade" class="form-control" placeholder="6">
      </div>
      <div class="mb-3">
        <label class="form-label">Subject</label>
        <input type="text" name="subject" class="form-control" placeholder="English">
      </div>
      <div class="mb-3">
        <label class="form-label">Topic</label>
        <input type="text" name="topic" class="form-control" placeholder="Past Tense">
      </div>
      <div class="mb-3">
        <label class="form-label">Duration (minutes)</label>
        <input type="number" name="duration" class="form-control" value="40">
      </div>

    {% elif active_tab == 'test' %}
      <h4 class="mb-3">✏️ Generate Test / Worksheet</h4>
      <div class="mb-3">
        <label class="form-label">Grade</label>
        <input type="text" name="grade_test" class="form-control" placeholder="7">
      </div>
      <div class="mb-3">
        <label class="form-label">Subject</label>
        <input type="text" name="subject_test" class="form-control" placeholder="Science">
      </div>
      <div class="mb-3">
        <label class="form-label">Topic</label>
        <input type="text" name="topic_test" class="form-control" placeholder="Photosynthesis">
      </div>
      <div class="mb-3">
        <label class="form-label">Question type</label>
        <select name="question_type" class="form-select">
          <option value="MCQ">MCQ</option>
          <option value="short">Short Questions</option>
          <option value="long">Long Questions</option>
        </select>
      </div>
      <div class="mb-3">
        <label class="form-label">Number of questions</label>
        <input type="number" name="count" class="form-control" value="5">
      </div>

    {% elif active_tab == 'parent_message' %}
      <h4 class="mb-3">👨👩👧 Generate Parent Message</h4>
      <div class="mb-3">
        <label class="form-label">Student name</label>
        <input type="text" name="student_name_msg" class="form-control" placeholder="Ali Ahmed">
      </div>
      <div class="mb-3">
        <label class="form-label">Issue / reason</label>
        <input type="text" name="issue_msg" class="form-control"
               placeholder="Homework not completed regularly">
      </div>
      <div class="mb-3">
        <label class="form-label">Tone</label>
        <select name="tone_msg" class="form-select">
          <option value="polite">Polite</option>
          <option value="firm but kind">Firm but kind</option>
          <option value="appreciative">Appreciative</option>
        </select>
      </div>

    {% elif active_tab == 'behaviour' %}
      <h4 class="mb-3">🧠 Generate Behaviour / Observation Note</h4>
      <div class="mb-3">
        <label class="form-label">Student name</label>
        <input type="text" name="student_name_beh" class="form-control" placeholder="Fatima">
      </div>
      <div class="mb-3">
        <label class="form-label">Behaviour issue</label>
        <input type="text" name="issue_beh" class="form-control"
               placeholder="Talking in class, disturbing others">
      </div>
      <div class="mb-3">
        <label class="form-label">Positives (optional)</label>
        <input type="text" name="positives_beh" class="form-control"
               placeholder="Participates actively, helps classmates">
      </div>

    {% elif active_tab == 'emergency' %}
      <h4 class="mb-3">🚨 Generate Emergency Lesson Plan</h4>
      <div class="mb-3">
        <label class="form-label">Grade</label>
        <input type="text" name="grade_em" class="form-control" placeholder="8">
      </div>
      <div class="mb-3">
        <label class="form-label">Subject</label>
        <input type="text" name="subject_em" class="form-control" placeholder="Maths">
      </div>
      <div class="mb-3">
        <label class="form-label">Topic</label>
        <input type="text" name="topic_em" class="form-control"
               placeholder="Fractions revision">
      </div>

    {% elif active_tab == 'heatmap' %}
      <h4 class="mb-3">📊 Generate Progress Heatmap</h4>
      <div class="mb-3">
        <label class="form-label">Class name</label>
        <input type="text" name="class_name_heat" class="form-control"
               placeholder="Class 7-B">
      </div>
      <div class="mb-3">
        <label class="form-label">Subjects (comma-separated)</label>
        <input type="text" name="subjects_heat" class="form-control"
               placeholder="Maths, English, Science">
      </div>
      <p class="text-muted small">
        After you submit once, you can extend this form to accept percentages per subject.
      </p>
    {% endif %}

    <button type="submit" class="btn btn-primary mt-2">
      Generate
    </button>
  </div>
</form>

{% if result_text %}
  <div class="card shadow-sm">
    <div class="card-header bg-primary text-white">
      {{ result_title }}
    </div>
    <div class="card-body">
      <pre class="result-block">{{ result_text }}</pre>
    </div>
  </div>
{% endif %}
{% endblock %}
