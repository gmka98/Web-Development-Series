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
          </tr>
        </thead>
        <tbody>
          <tr v-for="student in students" :key="student.id">
            <td>{{ student.id }}</td>
            <td>{{ student.email }}</td>
            <td>{{ student.status }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
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
        this.students.push(student);
        this.nextId++;
        this.newStudent.email = ''; // clear the input field
        this.newStudent.status = 'junior'; // reset the select field
      }
    }
  }
  </script>
  