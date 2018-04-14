<template>
    <div class="header">
    
        <div class="container">
            <div class="app-main-nav">
                <div class="main-nav-logo">
                    <img class="logo-main-nav" src="Acey_logo.png" alt="">
                </div>
                <div class="app-main-nav-links">
                    <router-link tag="div" class="app-main-nav-link" to="/dashboard"><span>Dashboard</span></router-link>
                    <router-link tag="div" class="app-main-nav-link" to="/create"><span>Create</span></router-link>
                    <router-link tag="div" class="app-main-nav-link" to="/user_dashboard"><span>User's dashboard</span></router-link>
                </div>
                
            </div>
    
        </div>
    
    </div>
</template>

<script>
    export default {
        data() {
            return {
    
            }
        }
    }
</script>


<style lang="scss">
    .app-main-nav {
        padding-top: 20px;
        width: 100%;
        display: flex;
        flex-flow: row;
        justify-content: space-around;
        
        &-links {
            margin-left: -110px;
        }
        
        &-links > div {
            padding: 30px;
            padding-right: 20px;
            
            
        }
        &-links > div > span {
           
        }
        
        &-links > div  {
            color: white;
        }
    }
    
    .app-main-nav-link {
        transition: 0.2s;
        border-bottom: 1px solid #fff;
        &:hover {
            transform: scale(1.03);
            box-shadow: 0 0 150px rgba(0,0,0,0.25);
        }
    }
    .app-main-nav-links {
        display: flex;
        flex-flow: row;
    }
    
    .app-user-face {
           display: flex;
    float: right;
    margin-right: 20px;
    margin-top: 15px;
    max-height: 50px;
    max-width: 50px;
        & > img {
        border-radius: 50px;
            
            max-width: 100%;
        }
        & > p {
        color: white;
        float: left;
        margin-right: 20px;    
        
        }
    }
    
    
    .router-link-active {
    border-top: 1px solid white;
    
    
   -webkit-box-shadow: -5px 4px 100px 2px rgba(0,0,0,0.75);
-moz-box-shadow: -5px 4px 100px 2px rgba(0,0,0,0.75);
box-shadow: -5px 4px 100px 2px rgba(0,0,0,0.75);
    color: orange !important;
}
    .logo-main-nav {
        padding-top: 30px;
        max-width: 100%;
    }
    
</style>
