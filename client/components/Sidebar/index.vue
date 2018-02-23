<template>
    <div id="sidebar" :class="{'open': active}">
        
        <el-menu theme="light" router>
            <div class="logo-container">
            </div>
            <el-menu-item index="/">Create</el-menu-item>
            <el-menu-item index="/play">Play</el-menu-item>
            <el-menu-item index="/user_dashboard">User's Dashboard</el-menu-item>    
        </el-menu>
    </div>
</template>

<script>
    export default {
        name: 'Sidebar',
        props: ['active'],
        computed() {
            active: () => {
                return this.active
            }
        }
    }
</script>

<style lang="scss">
    // You can import all your SCSS variables using webpack alias
    @import '~scss_vars';
    @import './style.scss';
</style>
