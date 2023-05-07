<template>
<div>
    <q-badge :color="rateColor">{{ratePresence}}</q-badge>
</div>
</template>
<script>
export default {
    props: {
        presence: {

        
        type: Number,
        required: true
    }
},

computed: {
    ratePresence(){
        return this.presence * 10;
    },
    rateColor(){
        //Calculate the color based on the rate presence value
        if (this.ratePresence >=60) {
            return 'positive';
        }else if (this.ratePresence >= 60) {
            return 'warning';
        }else {
            return 'negative';
        }
    }
}
}
    
</script>