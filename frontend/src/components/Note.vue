<template>
    <div>
      <h2>Evaluations</h2>
      <div v-for="(student, index) in students" :key="index">
        <h3>{{ student.email }}</h3>
        <table>
          <thead>
            <tr>
              <th>Date</th>
              <th>Active participation</th>
              <th>Behavior during the course</th>
              <th>Acquisition of knowledge</th>
              <th>Additional comments</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(evaluation, index) in student.evaluations" :key="index">
              <td>{{ evaluation.date }}</td>
              <td>{{ evaluation.activeParticipation }}</td>
              <td>{{ evaluation.behavior }}</td>
              <td>{{ evaluation.acquisition }}</td>
              <td>{{ evaluation.comments }}</td>
            </tr>
          </tbody>
        </table>
        <form @submit.prevent="createEvaluation(student.id)">
          <label for="date">Date:</label>
          <input type="date" id="date" v-model="newEvaluation.date">
          <br>
          <label for="activeParticipation">Active participation:</label>
          <input type="number" id="activeParticipation" v-model="newEvaluation.activeParticipation">
          <br>
          <label for="behavior">Behavior during the course:</label>
          <input type="number" id="behavior" v-model="newEvaluation.behavior">
          <br>
          <label for="acquisition">Acquisition of knowledge:</label>
          <input type="number" id="acquisition" v-model="newEvaluation.acquisition">
          <br>
          <label for="comments">Additional comments:</label>
          <input type="text" id="comments" v-model="newEvaluation.comments">
          <br>
          <button type="submit">Add Evaluation</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        newEvaluation: {
          date: '',
          activeParticipation: '',
          behavior: '',
          acquisition: '',
          comments: ''
        },
        students: [
          // Add your student objects here
        ]
      };
    },
    methods: {
      createEvaluation(studentId) {
        const evaluation = { ...this.newEvaluation }; // create a copy of newEvaluation
        const student = this.students.find((s) => s.id === studentId);
        if (student) {
          student.evaluations.push(evaluation);
        }
        this.newEvaluation = {
          date: '',
          activeParticipation: '',
          behavior: '',
          acquisition: '',
          comments: ''
        }; // reset newEvaluation after adding the evaluation
      }
    }
  };
  </script>
  