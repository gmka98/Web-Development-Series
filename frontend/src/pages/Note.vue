<template>
  <div>
    <h2>Students</h2>
    <student-form v-bind:students="students" v-on:student-created="onStudentCreated"></student-form>
    <h2>Evaluations</h2>
    <!-- evaluations code goes here -->
    
  </div>
</template>

<script>

export default {
  components: {
    StudentForm
  },
  data() {
    return {
      students: []
    };
  },
  methods: {
    onStudentCreated(student) {
      this.students.push(student); // add new student to the students array
    }
  }
};
</script>
