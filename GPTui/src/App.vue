<template>
    <div class="">
    <!-- header section strats -->
    <header class="header_section">
      <div class="container-fluid">
        <nav class="navbar navbar-expand-lg custom_nav-container ">
          <a class="navbar-brand" href="index.html">
            <img src="/images/drGPTicon.png" alt="">
            <span style="text-transform: none;" >
              Dr.GPT
            </span>
          </a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <div class="d-flex mx-auto flex-column flex-lg-row align-items-center">
              <ul class="navbar-nav  ">
                <li class="nav-item active">
                  <a class="nav-link" href="index.html">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="/app">Consult Dr.GPT </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#contact">Contact us</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="Signup.html"> Sign-Up </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="Login.html"> Login </a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </header>
  </div>
  <v-app>
    <v-main>
      <!-- route outlet -->
      <!-- component matched by the route will render here -->
      <router-view></router-view>
    </v-main>
  </v-app>
</template>
<style>
  @import url('@/assets/css/bootstrap.css');
  @import '@/assets/css/style.css';
  @import '@/assets/css/responsive.css';
</style>

<script setup lang="ts">
  import Diagnosis from '@/components/Diagnosis.vue'
  import router from '@/router'
</script>
