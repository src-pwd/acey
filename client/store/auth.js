/*eslint-disable*/
import jwt_decode from 'jwt-decode'
import fetch from "isomorphic-fetch";
import store from './index'

const state = {
  username:localStorage.getItem("u"),
  password: "",
  email: "",
  loggedIn: false,
  jwt: "",
  endpoints: {
    obtainJWT: "http://localhost:8000/api/login/",
    refreshJWT: "http://localhost:8000/api/login/refresh/"
  }
};

const mutations = {
  updateToken(state, newToken) {
    localStorage.setItem("u", state.username);    
    localStorage.setItem("h", state.loggedIn);
    state.jwt = newToken;
    this.commit("loggingIn");
  },
  removeToken(state) {
    localStorage.removeItem("u");    
    localStorage.removeItem("t");
    localStorage.removeItem("h");    
    state.jwt = null;
  },
  updateUsername(state, value) {
    state.username = value;
  },
  updatePassword(state, value) {
    console.log(value);

    state.password = value;
  },
  updateEmail(state, value) {
    console.log(value);
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
    fetch("http://localhost:8000/api/users/", {
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
        console.log(responseJson);
      })
      .then(data => {
        console.log(data);
      })
      .catch(data => {
        console.log(data);
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
      token: state.jwt
    };
    fetch(state.endpoints.refreshJWT, {
      method: "POST", // or 'PUT'
      body: JSON.stringify(payload), // data can be `string` or {object}!
      headers: new Headers({
        "Content-Type": "application/json",
      })
    }).then(response => {
      response.json().then(el => {
        this.commit("updateToken", el.token);
      })
    });
  },
  
  inspectToken(store) {
    console.log('evocated')
    const token = state.jwt;
    if (token) {
      const decoded = jwt_decode(token);
      const exp = decoded.exp;
      const orig_iat = decoded.orig_iat;
      if (
        exp - Date.now() / 1000 < 900 &&
        Date.now() / 1000 - orig_iat < 628200
      ) {
        this.dispatch("refreshToken");
      } else if (exp - Date.now() / 1000 < 1800) {
        // DO NOTHING, DO NOT REFRESH
       
      }  else {
        // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
        alert('please relogin!')
      }
    }
   
  }
};

export default {
  state,
  actions,
  mutations
};
