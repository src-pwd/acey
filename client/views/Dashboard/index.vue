<template>
    <div class="dashboard">
        <div v-for="element in events">
            <dashboard-element :details="element"></dashboard-element>
        </div>
        <router-view></router-view>
    </div>
</template>

<script>
    import element from './element.vue'
    export default {
        components: {
            'dashboard-element': element
        },
        data() {
            return {
                events: []
            }
        },
        created() {
            this.fetchData()
        },
        methods: {
            fetchData() {
                fetch('http://localhost:8000/api/events/', {
                        method: "GET", // or 'PUT'
                        headers: new Headers({
                            "Content-Type": "application/json"
                        })
                    })
                    .then(response => {
                        return response.json()
                    })
                    .then((el) => {
                        this.events = el
                    })
            }
        }
    }
</script>

<style lang="scss">
    .dashboard {
        width: 1200px;
        margin-left: auto;
        margin-right: auto;
        display: flex;
        flex-flow: row;
        flex-wrap: wrap;
    }
    
    .dashboard-element-block {
        width: 330px;
        height: 250px;
        margin: 30px;
        border-radius: 7px;
        background: -moz-linear-gradient(90deg, rgba(30, 30, 31, 1) 0%, rgba(82, 82, 82, 1) 100%);
        /* ff3.6+ */
        background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, rgba(82, 82, 82, 1)), color-stop(100%, rgba(30, 30, 31, 1)));
        /* safari4+,chrome */
        background: -webkit-linear-gradient(90deg, rgba(30, 30, 31, 1) 0%, rgba(82, 82, 82, 1) 100%);
        /* safari5.1+,chrome10+ */
        background: -o-linear-gradient(90deg, rgba(30, 30, 31, 1) 0%, rgba(82, 82, 82, 1) 100%);
        /* opera 11.10+ */
        background: -ms-linear-gradient(90deg, rgba(30, 30, 31, 1) 0%, rgba(82, 82, 82, 1) 100%);
        /* ie10+ */
        background: linear-gradient(0deg, rgba(30, 30, 31, 1) 0%, rgba(82, 82, 82, 1) 100%);
        /* w3c */
        filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#525252', endColorstr='#1e1e1f', GradientType=0);
        /* ie6-9 */
        border: 1px solid orange;
        transition: ease 0.3s;
        &:hover {
            transform: scale(1.03);
            box-shadow: 0 0 150px rgba(0, 0, 0, 0.25);
        }
    }
    
    .loading {
        margin-left: auto;
        text-align: center;
        margin-right: auto;
    }
</style>