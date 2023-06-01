<template>
  <div>
    <h2>My Courses</h2>
    <ul>
      <li v-for="course in courses" :key="course.id">
        {{ course.name }} - {{ course.description }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      courses: [],
    };
  },
  mounted() {
    this.fetchCourses();
  },
  methods: {
    fetchCourses() {
      // Make an API request to fetch the courses sent to the student
      // You can use axios or any other library for making the HTTP request
      axios.get("/api/student/courses")
        .then(response => {
          this.courses = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>
