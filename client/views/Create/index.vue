<template>
    <div class="container">
        <p>Select type of prediction to create:</p>
        <div class="type-block-menu">
            <router-link tag="div" to="/range" class="type-block">
                <div class="type-block-head">Range</div>
                <br>
                <div class="type-block-body">huengzh</div>
            </router-link>
            <router-link tag="div" to="/accuracy" class="type-block">
                <div class="type-block-head">Accuracy</div>
                <br>
                <div class="type-block-body">huyakuracy</div>
            </router-link>
            <router-link tag="div" to="#" class="type-block">
                <div class="type-block-head">Parlay</div>
                <br>
                <div class="type-block-body">soon nahuy</div>
            </router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Dashboard',
        components: {}
    }
</script>

<style scoped>
    .container {
        width: 1170px;
    }
    
    .type-block-menu {
        display: flex;
        flex-flow: row;
    }
    
    .type-block {
        margin: 25px;
        height: 300px;
        border: 5px solid pink;
        width: 30%;
    }
</style>