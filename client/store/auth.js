/*eslint-disable*/
import jwt_decode from 'jwt-decode'
import fetch from "isomorphic-fetch";
import store from './index'

const state = {
  username:localStorage.getItem("u"),
  password: "",
  email: "",
  loggedIn: JSON.parse(localStorage.getItem("h")) || false,
  jwt: localStorage.getItem("t"),
  endpoints: {
    obtainJWT: "http://app.acey.it/api/login/",
    refreshJWT: "http://app.acey.it/api/login/refresh/"
  }
};

const mutations = {
  updateToken(state, newToken) {
    localStorage.setItem("u", state.username);    
    localStorage.setItem("h", state.loggedIn);
    localStorage.setItem("t", state.jwt);
    state.jwt = newToken;
    this.commit("loggingIn");
  },
  removeToken(state) {
    localStorage.removeItem("u");    
    localStorage.removeItem("t");
    localStorage.setItem("h", "false");  
    localStorage.removeItem("about");          
    state.jwt = null;
  },
  updateUsername(state, value) {
    state.username = value;
  },
  removeCreds(state) {
    state.email = ''
    state.password  = ''
    state.username = ''
  },
  updatePassword(state, value) {
    state.password = value;
  },
  updateEmail(state, value) {
    state.email = value;
  },
  loggingIn() {
    state.loggedIn = true;
  },
  loggingOut() {
    state.loggedIn = false;
    state.username = "";
    state.password = "";
    store.state.user.details = {}
  },
  saveToken(state, value) {
    state.saveToken = value;
  }
};

const actions = {
  register(store) {
    fetch("http://app.acey.it/api/users/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        user: {
          username: state.username,
          password: state.password,
          email: state.email
        }
      })
    })
      .then(responseJson => {
      })
      .then(data => {
        this.commit("removeCreds")        
      })
      .catch(data => {
      });
  },
  obtainToken(store) {
    var data = {
      username: state.username,
      password: state.password
    };

    fetch(state.endpoints.obtainJWT, {
      method: "POST", // or 'PUT'
      body: JSON.stringify(data), // data can be `string` or {object}!
      headers: new Headers({
        "Content-Type": "application/json"
      })
    })
    .then(response => {
      if(!response.ok) alert('something bad happend maybe try another creds')
      else {
         response.json().then(el => {
       this.commit("updateToken", el.token);
       store.dispatch("getUserInfo");
      })
      }
     
    })
      // repsonses with status < 400 get resolved. you can access response.status and response.data here
  },
  
  refreshToken(store) {
    var payload = {
      token: state.jwt || ''
    };
    fetch(state.endpoints.refreshJWT, {
      method: "POST", // or 'PUT'
      body: JSON.stringify(payload), // data can be `string` or {object}!
      headers: new Headers({
        "Content-Type": "application/json",
      })
    }).then(response => {
      response.json().then(el => {
        if (!el.token)  {this.commit("removeToken")
          this.commit("loggingOut")}
        this.commit("updateToken", el.token);
      })
    });
  },
  
  inspectToken(store) {
    const token = state.jwt || '';
    if (token) {
      token === "null" ? 
         this.commit("removeToken") :
          console.log('vy zdes')
      const decoded = jwt_decode(token);
      const exp = decoded.exp;
      const orig_iat = decoded.orig_iat;
      if (
        exp - Date.now() / 1000 < 900 &&
        Date.now() / 1000 - orig_iat < 628200
      ) {
        console.log('fi')
        this.dispatch("refreshToken");
      } else if (exp - Date.now() / 1000 < 1800) {
        // DO NOTHING, DO NOT REFRESH
       console.log('se')
      }  else {
       console.log('la')
        
        // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
        this.commit("removeToken")
        alert('please relogin!')
        localStorage.clear
      }
    }
   
  }
};

export default {
  state,
  actions,
  mutations
};
