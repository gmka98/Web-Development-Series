<template>
    <div>
        <h2>Evaluations</h2>
        <div v-for="(evaluation, index) in evaluations" :key="index">
            <h3>Evaluation {{ index + 1 }}</h3>
            <p>Date: {{ evaluation.date }}</p>
            <p>Active participation: {{ evaluation.activeParticipation }}</p>
            <p>behavior during the course: {{ evaluation.behavior }}</p>
            <p>Acquisition of knowledge: {{ evaluation.acquisition }}</p>
            <p>Additional comments: {{ evaluation.comments }}</p>
        </div>
    </div>
</template>

<script>
 export default {
    name: 'EvaluationList',
    props: {
        evaluations: {
            type: Array,
            required: true
        }
    }
 }   
</script>