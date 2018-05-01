<template>
    <div class="container">
        <p class="first-create-desc">1. Select type of prediction to create:</p>
        <div class="type-block-menu">
            <router-link tag="div" to="/create/range" class="type-block" ref="range">
                <div class="type-block-head">Range</div>
                <br>
                <div class="type-block-body">Type of prediction where you can define ranges for price of cryptocurrency</div>
            </router-link>
            <router-link tag="div" to="/create/accuracy" class="type-block" ref="accuracy">
                <div class="type-block-head">Accuracy</div>
                <br>
                <div class="type-block-body">This type is for defining accurate price for cryptocurrency in the moment</div>
            </router-link>
            <router-link tag="div" to="/create/parlay" class="type-block" ref="parlay">
                <div class="type-block-head">Parlay</div>
                <br>
                <div class="type-block-body">Bet on price of crypto!</div>
            </router-link>
        </div>
        <transition name="fade">
                <router-view></router-view>
        </transition>
    </div>
</template>

<script>
    import Accuracy from './accuracy.vue'
    import Parlay from './parlay.vue'
    import Range from './range.vue'
    
    export default {
        name: 'Dashboard',
        components: {
            Accuracy,
            Parlay,
            Range
        },
        mounted() {
            console.log(this.$refs)

        },
        computed: {
            configVal() {
                // if (this.$refs.accuracy.$el.className.indexOf("router-link-active") !== -1 || this.$refs.range.$el.className.indexOf("router-link-active") !== -1) {
                    // console.log('lol')
                // }
            }
        }
    }
</script>

<style lang="scss">
    @import '../../styles/vars.scss';
    @import './create.scss';
    .container {
        width: 1170px;
    }
    
    .type-block-menu {
        display: flex;
        flex-flow: row;
    }
    
    .soon-label {
        display: block;
        text-align: center;
        margin-top: 20px;
        background-color: #151515;
        position: relative;
        left: 50px;
        width: 155px;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid orange;
        max-width: 100%;
        -ms-transform: rotate(-20deg);
        /* IE 9 */
        -webkit-transform: rotate(-20deg);
        /* Safari 3-8 */
        transform: rotate(-20deg);
        transition: 1.2s ease;
        &:hover {
            -ms-transform: rotate(0deg);
            /* IE 9 */
            -webkit-transform: rotate(0deg);
            /* Safari 3-8 */
            transform: rotate(0deg);
        }
    }
    
    .type-block {
        margin: 25px;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #bd7125;
        width: 30%;
        transition: 0.2s;
        &:hover {
            transform: scale(1.03);
            box-shadow: 0 0 150px rgba(0, 0, 0, 0.25);
        }
    }
    
    .type-block-head {
        font-size: 20px;
        color: #fff;
    }
    
    .range-bet-head {
        width: 400px;
        padding-left: 20px;
        font-size: 24px;
        background-color: #1a1a1a;
        color: white;
        border: none;
        &:active {
            outline: none;
            border-bottom: 2px solid orange;
        }
    }
</style>