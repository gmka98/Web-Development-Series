<template>
    <body>
    <div class="login_form">
   <div class="left">
    <h1>Login</h1>
   <form action="/dashboard">
    <label for="fname">Email:</label><br>
    <input type="text" id="fname" name="fname" placeholder="Enter your email"><br>
    <label for="lname">Password:</label><br>
    <input type="text" id="lname" name="lname" placeholder="Enter password"><br><br>
    <input type="checkbox"><span>Remember me</span>
    <br><br>
    <input type="submit" id="login_btn" value="Login">
  </form> 
  <button href="localhost:8080/dashboard">sign up</button>
  <img src="Adimian.jpg">
  </div>
  <div class="right">
    <img src="adimian_logo.jpg">
    <h2>Profesionnal Development Series</h2>
  </div>
    </div>
  </body>
  </template>
  <style scoped>
   body{
    background-color: rgba(82, 82, 82, 0.137);
   }
    .login_form{
      display: inline-flex;
      background-color: rgba(82, 82, 82, 0.137);
      
    }
    #login_btn{
      width: 350px;
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
    .left{
      padding: 10%;
      background-color: rgba(255, 255, 255, 0.438);
      margin-left: 5cm;
      margin-top: 5cm;
      margin-bottom: 5cm;
      border-radius: 15px;
    }
    .right{
      background-color: rgb(0, 83, 14);
      padding: 10%;
      margin-right: 3cm;
      margin-top: 5cm;
      margin-bottom: 5cm;
      width: 50%;
    }
    #fname{
      border-radius: 15px;
      width: 350px;
  
    }
    #lname{
      border-radius: 15px;
      width: 350px;
    }
  </style>
<script>
import {defineComponent} from 'vue'
export default defineComponent({
    name: "Log"
})
</script>