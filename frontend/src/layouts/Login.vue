<template link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  
    <body>
    <div class="login_form">
   
  <div class="left">
    <h2>Profesionnal Development Series</h2>
    <p>Adimian App for his members
    </p>
  </div>
  
  <div>

  </div>
  <div class="right">
    <img src="adimian-logo.jpg">

    <h1>Login</h1>
   <form action="/dashboard">
    <label id="email" for="fname">Email Address</label><br>
    <input type="text" id="fname" name="fname" placeholder="Enter your email"><br>
    <label id="password" for="lname">Password</label><br>
    <input type="text" id="lname" name="lname" placeholder="Enter password"><br><br>
    <input type="checkbox"><span>Remember me</span>
    <br>
    <input type="submit" id="login_btn" value="Login">
  </form> 
  <button class="btn-google">
    <i class="material-icons">google</i> Connexion avec Google
  </button>
  <img id="adimian-text" src="Adimian-name.jpg">
  </div>
    </div>
  </body>
  </template>
  <style scoped>
   body{
    background-color: #25ca0f;
   }
    .login_form{
      display: inline-flex;
      background-color: rgba(82, 82, 82, 0.137);
      
    }
    #login_btn{
      width: 70px;
      height: 35px;
      color: white;
      background-color: green;
    }
    button{
      width:350px;
      background-color: red;
      margin-top: 50px;
    }
    h2{
      color: white;
      text-align: center;
    }
    p{
      color: white;
      font-size: 20px;
    }
    .left{
      background-image: url("../../public/green.jpg");
      padding: 10%;
      margin-left: 5cm;
      margin-top: 5cm;
      margin-bottom: 5cm;
    }
    .right{
      background-color: rgb(255, 255, 255);
      padding: 10%;
      margin-right: 3cm;
      margin-top: 5cm;
      margin-bottom: 5cm;
      width: 50%;
    }
    .btn-google {
  background-color: #c51919;
  color: #ffffff;
  border: 1px solid #757575;
  border-radius: 4px;
  padding: 8px 16px;
  font-size: 14px;
  text-transform: uppercase;
  font-weight: 500;
  letter-spacing: 0.025em;
  cursor: pointer;
  text-align: center;
}

.btn-google:hover {
  background-color: #25ca0f;
}

    #fname{
      width: 350px;
      height: 35px;
  
    }
    #lname{
      height: 35px;
      width: 350px;
    }
    #email{
      font-weight: bold;
    }
    #password{
      font-weight: bold
}
#adimian-text{
  
}
  </style>
<script>
import {defineComponent} from 'vue'
export default defineComponent({
    name: "Log"
})
</script>