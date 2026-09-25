<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import api from "@/services/api";

const router = useRouter();
const authStore = useAuthStore();
const dashboard = ref({
  pending_drives: [],
  pending_recruiters: [],
  total_students: 0,
  total_recruiters: 0,
  total_drives: 0,
  total_applications: 0,
});

const logo = "/src/assets/frame.svg";
const logo2 = "/src/assets/logo2.jpeg";
const check = ref(false);
const id = ref("");
const name = ref("");
const conf = ref("");


const viewName = (user_id, role) => {
  check.value = !check.value;
  id.value = user_id;
  if (role === "recruiter") {
    for (const recruiter of dashboard.value.pending_recruiters) {
      if (recruiter.id === user_id) {
        name.value = recruiter.name;
        conf.value = role
      }
    }
  } else if (role === "drive") {
    for (const drive of dashboard.value.pending_drives) {
      if (drive.id === user_id) {
        name.value = drive.title;
        conf.value = role
      }
    }
  }
};

const logout = () => {
  authStore.logout();
  router.push("/login");
};

onMounted(async () => {
  try {
    const response = await api.get("/admin/dashboard");
    console.log(response.data);
    dashboard.value = response.data;
  } catch (error) {
    alert(error.response.data.message);
    router.push("/login");
  }
});

const viewDetail = (id)=>{
  if(conf.value ==='drive'){
    router.push(`/admin/drive/${id}`)
  }
  else if (conf.value ==='recruiter'){
    router.push(`/admin/recruiter/${id}`)
  }
}
</script>

<template>
  <div class="main">
    <div class="left">
      <img :src="logo" alt="logo" class="img" />
      <div class="links">
        <button class="btn1">Dashboard</button>
        <router-link to="/admin/view/students"
          ><button class="btn">Students</button></router-link
        >
        <router-link to="/admin/view/recruiters"
          ><button class="btn">Recruiters</button></router-link
        >
        <router-link to="/admin/view/drives"
          ><button class="btn">Drives</button></router-link
        >
        <router-link to="/admin/view/applications"
          ><button class="btn">Applications</button></router-link
        >
      </div>
      <div class="logout">
        <button class="btn2" @click="logout">Logout</button>
      </div>
    </div>
    <div class="right">
      <div class="right_left">
        <div class="right_head">
          <p class="right-head">Dashboard</p>
          <input type="search" class="search" placeholder="Search here" />
        </div>
        <div class="stats">
          <div class="stu">
            <p class="text">Students</p>
            <p class="subtext">{{ dashboard.total_students }}</p>
          </div>
          <div class="stu">
             <p class="text">Recruiters</p>
            <p class="subtext">{{ dashboard.total_recruiters }}</p>
          </div>
          <div class="stu">
             <p class="text">Drives</p>
            <p class="subtext">{{ dashboard.total_drives }}</p>
          </div>
          <div class="stu">
            <p class="text">Applications</p>
            <p class="subtext">{{ dashboard.total_applications }}</p>
          </div>
        </div>
        <p
          class="no_data"
          v-if="
            dashboard.pending_drives.length === 0 &&
            dashboard.pending_recruiters.length === 0
          "
        >
          No pending drive or recruiter
        </p>
        <div class="table_grp">
          <div v-if="dashboard.pending_drives.length !== 0">
            <p class="tb_head">Pending Drives</p>
            <div class="right_main_body" tabindex="0">
              <div class="titles">
                <p>Id</p>
                <p>Title</p>
                <p>Recruiter</p>
                <p>Status</p>
                <p>Deadline</p>
              </div>
              <div
                class="values"
                v-for="(drive, index) in dashboard.pending_drives"
                @click="viewName(drive.id, 'drive')"
              >
                <p>{{ index + 1 }}</p>
                <p>{{ drive.title }}</p>
                <p>{{ drive.recruiter }}</p>
                <p>{{ drive.status }}</p>
                <p>{{ drive.deadline }}</p>
              </div>
            </div>
          </div>
          <div v-if="dashboard.pending_recruiters.length !== 0">
            <p class="tb_head">Pending Recruiters</p>
            <div class="right_main_body" tabindex="0">
              <div class="titles">
                <p>Id</p>
                <p>Name</p>
                <p>Email</p>
                <p>Status</p>
                <p>Joined On</p>
              </div>
              <div
                class="values"
                v-for="(recruiter, index) in dashboard.pending_recruiters"
                @click="viewName(recruiter.id, 'recruiter')"
              >
                <p>{{ index + 1 }}</p>
                <p>{{ recruiter.name }}</p>
                <p>{{ recruiter.email }}</p>
                <p>{{ recruiter.status }}</p>
                <p>{{ recruiter.joined }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="right_right">
        <img :src="logo2" alt="" class="img2" />
        <p class="name" v-if="name">{{ name }}</p>
        <div class="links3">
          <button class="det" @click = viewDetail(id)>View Details</button>
          <button class="det">Approve</button>
          <button class="det2">Reject</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main {
  height: 100vh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #11191f;
  overflow: hidden;
  box-sizing: border-box;
}
.right {
  background-color: #f4f3ec;
  width: 80%;
  height: 100vh;
  border: 3vh solid #11191f;
  box-sizing: border-box;
  border-radius: 5vh;
  display: flex;
}
.left {
  background-color: #11191f;
  width: 20%;
  height: 100vh;
  /* display: flex;
    flex-direction: column; */
}
.img {
  width: 18vh;
  display: flex;
  justify-self: center;
  margin-top: 6vh;
}
.links {
  display: flex;
  flex-direction: column;
  gap: 2vh;
  /* background-color: rebeccapurple; */
  justify-self: center;
  margin-top: 7vh;
}
.btn1 {
  width: 36vh;
  height: 7vh;
  border-radius: 2vh;
  border: none;
  font-family: "Google Sans";
  font-weight: 650;
  font-size: 2vh;
  letter-spacing: -0.1vh;
  background-color: #f4f3ec;
  color: #11191f;
  text-align: left;
  padding-left: 5vh;
  cursor: pointer;
}
.btn {
  width: 36vh;
  height: 7vh;
  border-radius: 2vh;
  border: none;
  font-family: "Google Sans";
  font-weight: 650;
  font-size: 2vh;
  letter-spacing: -0.1vh;
  color: #f4f3ec;
  background-color: #11191f;
  text-align: left;
  padding-left: 5vh;
  transition: 0.1s all ease-in-out;
  cursor: pointer;
}
.btn:hover {
  box-shadow: 0vh 0vh 0vh 0.35vh #f4f3ec;
}
.btn2 {
  width: 36vh;
  height: 7vh;
  border-radius: 2vh;
  border: none;
  font-family: "Google Sans";
  font-weight: 650;
  font-size: 2.2vh;
  letter-spacing: -0.1vh;
  color: #f4f3ec;
  background-color: #11191f;
  text-align: left;
  padding-left: 5vh;
  cursor: pointer;
  transition: 0.1s all ease-in-out;
}
.btn2:hover {
  background-color: #bb0000;
  color: #fff;
}

.logout {
  justify-self: center;
  margin-top: 25vh;
}
.right_left {
  height: 100%;
  width: 70%;
  background-color: #f4f3ec;
  border-radius: 2vh 0vh 0vh 2vh;
}
.right_right {
  height: 100%;
  width: 30%;
  background-color: #ffffff;
  border-radius: 0vh 2vh 2vh 0vh;
  border: 3vh solid #f4f3ec;
  box-sizing: border-box;
  border-radius: 6vh;
  display: flex;
  flex-direction: column;
  gap: 4.5vh;
  padding: 6vh 0vh 0vh 0vh;
  align-items: center;
}
.links3 {
  display: flex;
  flex-direction: column;
  gap: 1.5vh;
}
.img2 {
  width: 18vh;
  border-radius: 50vh;
  box-shadow: 0vh 0vh 0vh 0.6vh #f4f3ec;
  transition: 0.2s all ease-in-out;
}
.img2:hover {
  rotate: -5deg;
}
.det {
  width: 32vh;
  height: 7vh;
  border-radius: 10vh;
  border: none;
  font-family: "Google Sans";
  font-weight: 650;
  font-size: 2vh;
  letter-spacing: -0.1vh;
  background-color: #11191f;
  color: #f4f3ec;
  cursor: pointer;
  transition: 0.1s all ease-in-out;
}
.det:hover {
  background-color: #f4f3ec;
  box-shadow: 0vh 0vh 0vh 0.5vh #11191f;
  color: #11191f;
  font-weight: 700;
}
.det2 {
  width: 32vh;
  height: 7vh;
  border-radius: 10vh;
  border: none;
  font-family: "Google Sans";
  font-weight: 650;
  font-size: 2vh;
  letter-spacing: -0.1vh;
  background-color: #bb0000;
  color: #fff;
  cursor: pointer;
  transition: 0.1s all ease-in-out;
}
.det2:hover {
  background-color: #9f0000;
}
.right_head {
  /* background-color: #9f0000; */
  display: flex;
  justify-content: space-between;
  padding: 0vh 7vh;
  align-items: center;
}
.right-head {
  font-family: "Google Sans";
  font-weight: 500;
  font-size: 4vh;
  letter-spacing: -0.2vh;
  color: #11191f;
  /* background-color: #000; */
}
.search {
  width: 30vh;
  height: 5vh;
  border: none;
  border-radius: 10vh;
  border: 0.3vh solid #363636;
  background-color: #fffefa;
  padding: 0vh 3vh;
  font-family: "Google Sans";
  font-weight: 600;
  font-size: 1.8vh;
  transition: 0.3s all ease-in-out;
}
.search:focus {
  width: 50vh;
  border: 0.3vh solid #f4f3ec;
  box-shadow: 0vh 0vh 0vh 0.3vh #11191f;
  outline: none;
}

.right_main_body {
  /* background-color: red; */
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.titles {
  display: flex;
  /* background-color: pink; */
  justify-content: space-between;
  padding: 0vh 6vh;
  align-items: center;
  font-family: "Google Sans";
  font-weight: 500;
  font-size: 1.6vh;
  opacity: 0.8;
}
.values {
  display: flex;
  /* background-color: blue; */
  justify-content: space-between;
  padding: 0vh 6vh;
  align-items: center;
  font-family: "Google Sans";
  font-weight: 650;
  font-size: 1.8vh;
  transition: 0.1s all ease-in-out;
  margin-left: 1vh;
  cursor: pointer;
  border-radius: 0vh 5vh 0vh 5vh;
}
.values:hover {
  background-image: linear-gradient(0deg, #000, #181818);
  color: #f4f3ec;
  justify-self: center;
}

.tb_head {
  font-family: "Google Sans";
  font-weight: 500;
  font-size: 2.5vh;
  /* letter-spacing: -0.1vh; */
  color: #11191f;
  padding: 0vh 5vh;
}
.table_grp {
  display: flex;
  flex-direction: column;
  gap: 3vh;
}
.no_data {
  font-family: "Google Sans";
  font-weight: 500;
  font-size: 2.7vh;
  color: #11191f;
  padding: 21vh 0vh;
  justify-self: center;
}
.name {
  color: #000;
  font-family: Google sans;
  font-size: 2.1vh;
  font-weight: 600vh;
  margin-top: -2vh;
  margin-bottom: -1.5vh;
}
.stats{
  display: flex;
  justify-content:space-between;
  align-items: center;
  margin-left: 5vh;
  margin-right: 2vh;
}
.stu{
  display: flex;
  flex-direction: column;
  align-items: center;
}

.text{
  font-family: "Google sans";
  font-size: 1.9vh;
  font-weight:600;
}
.subtext{
  font-family: "Google sans";
  margin: 0;
  font-size: 1.9vh;
  font-weight: 600;
}
</style>
