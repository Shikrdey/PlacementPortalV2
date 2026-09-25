<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import api from "@/services/api";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const authStore = useAuthStore();

const email = ref("");
const password = ref("");
const eye = "/src/assets/eye.svg";
const image = "/src/assets/download.jpeg";

const view = ref(false);

const viewPassword = () => {
  view.value = !view.value;
};

const login = async () => {
  try {
    const response = await api.post("/login", {
      email: email.value,
      password: password.value,
    });

    authStore.setAuth(response.data.access_token, response.data.role);

    if (response.data.role === "Admin") {
      router.push("/admin/dashboard");
    } else if (response.data.role === "Recruiter") {
      const profile = await api.get("/recruiter/profile/check");

      if (profile.data.profile) {
        router.push("/recruiter/dashboard");
      } else {
        router.push("/recruiter/create/profile");
      }
    } else {
      const profile = await api.get("/student/profile/check");

      if (profile.data.profile) {
        router.push("/student/dashboard");
      } else {
        router.push("/student/create/profile");
      }
    }
  } catch (error) {
    alert(error.response.data.message);
  }
};

const register = ()=> {
  router.push("/register")
};

</script>

<template>
  <div class="main">
    <div class="img"><img class="imgcont" :src="image" alt="Image" /></div>
    <div class="box">
      <p class="login">Login</p>
      <form @submit.prevent="login">
        <div class="content">
          <div class="ema">
            <p class="email">Email</p>
            <input
              class="emailin"
              type="email"
              v-model="email"
              placeholder="Enter your email"
              required
            />
          </div>
          <div class="pass">
            <p class="password">Password</p>
            <input
              class="passin"
              :type="view?'text':'password'"
              v-model="password"
              placeholder="Enter your password"
              required
            />
             <img @click="viewPassword" :src="eye" alt="" class="eyel" />
          </div>
          <div class="submit">
            <button type="submit" class="press">Login</button>
            <p class="sug">New user? <span @click="register" class="reg">Register</span></p>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.main {
  background-color: #fafafa;
  height: 100vh;
  width: 100%;
  display: flex;
  justify-content: center;
  overflow: hidden;
}

.img {
  width: 45%;
  height: 100vh;
}

.box {
  width: 55%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #fafafa;
  flex-direction: column;
}
.imgcont {
  width: 100%;
  margin-top: -25vh;

}
.content {
  background-color: #fafafa;
  height: fit-content;
  width: fit-content;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 3vh;
}

.email {
  font-family: "Google Sans";
  font-size: 2vh;
}

.pass {
  font-family: "Google Sans";
  font-size: 2vh;
}

.emailin {
  width: 50vh;
  height: 7vh;
  background-color: #efeeee;
  border-radius: 5vh;
  margin-top: -0.2vh;
  margin-left: 1vh;
  font-family: "Google Sans";
  font-weight: 350;
  font-size: 1.9vh;
  border: none;
  color: #1e1e1e;
  padding: 0vh 3vh;
  box-sizing: border-box;
}
.passin {
  width: 50vh;
  height: 7vh;
  background-color: #efeeee;
  border-radius: 5vh;
  margin-top: -0.2vh;
  margin-left: 1vh;
  font-family: "Google Sans";
  font-weight: 350;
  font-size: 1.9vh;
  border: none;
  color: #1e1e1e;
  padding: 0vh 3vh;
  box-sizing: border-box;
  padding-right:6vh;
}
.press {
  width: 50vh;
  height: 8vh;
  margin-top: 4vh;
  background-color: #181818;
  color: #fafafa;
  font-family: "Google Sans";
  font-size: 2.5vh;
  letter-spacing: -0.1vh;
  font-weight: 600;
  border: none;
  border-radius: 5vh;
  justify-self: center;
  transition: 0.3s all ease-in-out;
  cursor: pointer;
}
.press:hover {
  background-color: #fff;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
  color: #000;
}

.login {
  font-family: "Google Sans";
  font-size: 3vh;
  font-weight: 500;
  margin-bottom: 4vh;
}
.eyel {
  position: absolute;
  right: 30.5vh;
  bottom: 42vh;
  cursor: pointer;
}
.sug{
  font-family: "Google Sans";
  font-weight: 350;
  font-size: 1.8vh;
  color: #1e1e1e;
  justify-self: center;
}
.reg{
  color: #0b52c4;
  font-size: 1.9vh;
  font-weight: 500;
  cursor: pointer;
}
</style>
