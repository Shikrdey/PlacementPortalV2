<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

import api from "@/services/api";

const authStore = useAuthStore();
const router = useRouter();

const drives = ref([]);
const search = ref("");

const grad_b = "/src/assets/b.svg";
const grad_p = "/src/assets/p.svg";
const grad_s = "/src/assets/s.svg";

const image = "/src/assets/logo.svg";
const pfp = "/src/assets/Nagi.jpeg";

const searchDrive = computed(()=>{
if(search.value.trim() === ""){
  return drives.value;
}
  return drives.value.filter((drive)=>{
   return drive.title.toLowerCase().includes(search.value.toLowerCase())
  });
});

const scrollToResults = () =>{
  document.getElementById("rec_das_sec").scrollIntoView({
    behavior: "smooth"
  });
}

const logout = () => {
  authStore.logout();
  router.push("/");
};
const viewDrive = (drive_id) =>{
  router.push(`/drive/${drive_id}`)
}
onMounted(async() => {
   try {
    const response = await api.get("/student/dashboard");

    drives.value = response.data.drives;
  } catch (error) {
    console.error(error);
  }
});
</script>
<template>
  <img :src="grad_p" alt="" class="grdp" />
  <img :src="grad_s" alt="" class="grds" />
  <img :src="grad_b" alt="" class="grdb" />
  <div class="rec_das_main">
    <div class="rec_das_nav">
      <div class="rec_das_log">
        <img :src="image" alt="" class="rec_das_img" />
      </div>
      <div class="rec_das_but">
        <router-link to="/student/application/history"
          ><p class="but1">Applications</p></router-link
        >
        <a href="#rec_das_sec"><p class="but1">Drives</p></a>
        <a href="#" @click="logout"><p class="but1">Logout</p></a>
        <router-link to="/student/profile"
          ><img :src="pfp" alt="" class="rec_das_pfp"
        /></router-link>
      </div>
    </div>
    <div class="rec_das_box1">
      <img
        src="https://i.pinimg.com/1200x/a2/08/4f/a2084fe2f8dd5e851b6ca504b4664613.jpg"
        alt=""
        class="rec_das_ban"
      />
    </div>
    <div class="rec_das_box3">
      <input class="rec_das_inp" type="search"  placeholder="Search drives here" v-model="search" />
      <button class="rec_das_sea" @click="scrollToResults">Search</button>
    </div>
    <div class="nodrive_div" v-if="drives.length === 0">
      <p class="nodrive">No ongoing drives yet</p>
    </div>
    <section id="rec_das_sec" v-if="drives.length !==0">
      <div class="rec_das_box4">
        <div class="rec_das_dri" v-for="drive in searchDrive">
          <div class="rec_das_head">
            <img
              src="https://i.pinimg.com/736x/1f/26/89/1f26894a486fa212816e8f1c773a65bb.jpg"
              alt=""
            />
          </div>
          <div class="rec_das_cont">
            <p class="title">{{ drive.recruiter }}</p>
            <p class="title2">{{ drive.title }}</p>
            <p class="title">Closing On {{ drive.deadline }}</p>
          </div>
        
            <button class="rec_das_dri_but" @click="viewDrive(drive.id)">View</button>
    
        </div>
      </div>
    </section>
  </div>
</template>
<style scoped>
.rec_das_main {
  background-color: #fafafa;
  height: 100vh;
  width: 100%;
}
.rec_das_nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0vh 10vh;
}
.rec_das_log {
  margin-top: 3vh;
  margin-left: 3vh;
}
.rec_das_pfp {
  height: 7vh;
  width: 7vh;
  object-fit: cover;
  border-radius: 10vh;
}
.rec_das_img {
  height: 9vh;
  width: 9vh;
}
.rec_das_but {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-right: 3vh;
  margin-top: 3vh;
  gap: 6vh;
  z-index: 2;
}
.rec_das_box1 {
  width: 160vh;
  height: 35vh;
  display: flex;
  justify-content: center;
  justify-self: center;
  align-items: center;
  margin-top: 6vh;
  overflow: hidden;
  border-radius: 2.7vh;
}
.rec_das_ban {
  width: 100%;
  rotate: 90deg;
  filter: contrast(200);
  filter: brightness(0.92);
  object-fit: cover;
  border-radius: 2.7vh;
}
.rec_das_box2 {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 5vh;
}
.cp {
  width: 160vh;
  height: 10vh;
  border-radius: 2.7vh;
  background-color: #181818;
  color: #fafafa;
  font-family: "Google Sans";
  font-size: 2.5vh;
  letter-spacing: -0.1vh;
  font-weight: 600;
  border: none;
  justify-self: center;
  transition: 0.3s all ease-in-out;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1vh;
}
.cp:hover {
  background-color: #fff;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
  color: #000;
}
.rec_das_box3 {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 5vh;
}
.rec_das_inp {
  height: 8.5vh;
  width: 160vh;
  border-radius: 2.7vh;
  font-family: "Google Sans";
  font-weight: 350;
  font-size: 1.9vh;
  border: 0.5vh solid #000;
  color: #1e1e1e;
  padding: 0vh 23vh 0vh 3vh;
  box-sizing: border-box;
  z-index: 2;
}
.rec_das_sea {
  height: 8.5vh;
  width: 20vh;
  margin-left: -20vh;
  background-color: #181818;
  color: #fafafa;
  font-family: "Google Sans";
  font-size: 2.5vh;
  letter-spacing: -0.1vh;
  font-weight: 600;
  border: 0.5vh solid #000;
  border-radius: 0vh 2.7vh 2.7vh 0vh;
  justify-self: center;
  transition: 0.15s all ease-in-out;
  z-index: 2;
  cursor: pointer;
}
.rec_das_sea:hover {
  background-color: #fff;
  color: #000;
}
.rec_das_box4 {
  padding: 10vh 8vh;
  width: 90%;
  display: flex;
  justify-self: center;
  align-items: center;
  gap: 5vh;
  flex-wrap: wrap;
  box-sizing: border-box;
}

.rec_das_dri {
  height: 50vh;
  width: 50vh;
  display: flex;
  flex-direction: column;
  border-radius: 2.7vh;
  box-shadow: 0vh 0vh 0vh 0.2vh #000;
  scale: 0.9;
}
.rec_das_head {
  height: 21vh;
  width: 100%;
  overflow: hidden;
  border-radius: 2.7vh 2.7vh 0vh 0vh;
}
.but1 {
  font-family: "Google Sans";
  color: #181818;
  font-size: 1.8vh;
  font-weight: 550;
  transition: 0.2s all ease-in-out;
}
.but1:hover {
  text-decoration: underline;
  scale: 1.05;
}
.title {
  height: 3vh;
  font-family: "Google Sans";
  font-size: 2vh;
  font-weight: 500;
  padding: 0vh 3vh;
  margin: 0.8vh 0vh;
}
.title2 {
  height: 6vh;
  font-family: "Google Sans";
  font-size: 5vh;
  font-weight: 550;
  padding: 0vh 3vh;
  margin: 0vh;
}
.rec_das_dri_but {
  height: 8vh;
  width: 80%;
  background-color: #181818;
  color: #fafafa;
  font-family: "Google Sans";
  font-size: 2.5vh;
  letter-spacing: -0.1vh;
  font-weight: 600;
  border: none;
  border-radius: 2.7vh;
  justify-self: center;
  transition: 0.3s all ease-in-out;
  display: block;
  margin: auto auto;
  margin-top: 2.1vh;
  cursor: pointer;
}
.rec_das_dri_but:hover {
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
  color: #fff;
}

.plus {
  font-size: 3vh;
  margin-top: -0.5vh;
}
.nodrive_div{
  display: flex;
  justify-content: center;
  margin-top: 7vh;
}
.nodrive{
  font-family: "Google Sans";
  font-size: 2.5vh;
  font-weight: 500;
  color: #181818;

}
.grdp {
  position: absolute;
  height: 80vh;
  width: 80vh;
  right: -45vh;
  top: 25vh;
  z-index: 0;
}
.grds {
  position: absolute;
  left: 35vh;
  top: -70vh;
  z-index: 0;
}
.grdb {
  position: absolute;
  height: 80vh;
  width: 80vh;
  left: -60vh;
  top: 60vh;
  z-index: 0;
}
.divphoto {
  width: 100%;
  object-fit: cover;
  /* height: 100%; */
}
.pila{
  z-index: 2;
}
</style>
