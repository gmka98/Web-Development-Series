<template>
  <div>
    <form @submit.prevent="createStudent">
      <label for="email">Email:</label>
      <input type="email" id="email" v-model="newStudent.email">
      <br>
      <label for="status">Status:</label>
      <select id="status" v-model="newStudent.status">
        <option value="junior">Junior</option>
        <option value="medior">Medior</option>
        <option value="senior">Senior</option>
      </select>
      <br>
      <button type="submit">Add Student</button>
    </form>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Email</th>
          <th>Status</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id">
          <td>{{ student.id }}</td>
          <td>{{ student.email }}</td>
          <td>{{ student.status }}</td>
          <td><button @click="createEvaluation(student.id)">Create Evaluation</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        newStudent: {
          email: '',
          status: 'junior'
        },
        students: [],
        nextId: 1
      };
    },
    methods: {
      createStudent() {
        const student = {
          email: this.newStudent.email,
          status: this.newStudent.status,
          id: this.nextId
        };
        
        axios.post('/api/students', student)
          .then(response => {
            this.students.push(student);
            this.nextId++;
            this.newStudent.email = ''; // clear the input field
            this.newStudent.status = 'junior'; // reset the select field
          })
          .catch(error => {
            console.error(error);
          });
      },
      createEvaluation(studentId) {
        const evaluation = {
          studentId: studentId
          // Include other evaluation data as needed
        };
  
        axios.post('/api/evaluations', evaluation)
          .then(response => {
            // Handle successful creation of evaluation
          })
          .catch(error => {
            console.error(error);
          });
      },
      fetchStudents() {
        axios.get('/api/students')
          .then(response => {
            this.students = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      }
    },
    mounted() {
      this.fetchStudents();
    },
  };
  </script>