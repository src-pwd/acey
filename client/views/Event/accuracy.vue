<template>
<div class="accuracy-control">
    <input type="range" v-model="currentValue">
    or
    <input type="number" min="0" v-model="currentValue"> 
</div>
</template>


<script>
    export default {
        data() {
            return {
                currentValue:0
            }
        }
    }
</script>

<style lang="scss">
    
</style>