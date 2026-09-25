<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import api from "@/services/api";

const router = useRouter();
const authStore = useAuthStore();

const grad_b = "/src/assets/b.svg";
const grad_p = "/src/assets/p.svg";
const grad_s = "/src/assets/s.svg";

const image = "/src/assets/logo.svg";
const pfp = "/src/assets/pfp.jpeg";
const banner = "/src/assets/banner.jpeg";

const search = ref("");
const drives = ref([]);

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

onMounted( async () => {
 try {
    const response = await api.get("/recruiter/dashboard");
    drives.value = response.data ;
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
        <a href="#"><p class="but1">Applications</p></a>
        <a @click="scrollToResults"><p class="but1">Drives</p></a>
        <a @click="logout"><p class="but1">Logout</p></a>
        <router-link to="/recruiter/profile"
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
    <div class="rec_das_box2">
      <router-link to="/create/drive" class="pila"
        ><button class="cp">
          <span class="plus">+</span>Create drive
        </button></router-link
      >
    </div>
    
    <div class="rec_das_box3">
      <input type="search" class="rec_das_inp" placeholder="Search drives here" v-model="search"/>
     <button class="rec_das_sea" @click="scrollToResults">Search</button>
    </div>
    <section id="rec_das_sec">
      <div class="rec_das_box4">
        <div v-for="(drive, index) in searchDrive" class="rec_das_dri" :key="drive.id">
          <div class="rec_das_head">
            <img
              class="divphoto"
              src="https://i.pinimg.com/736x/a6/07/b8/a607b88eb45c08918a823b622f8ab1f8.jpg"
              alt=""
            />
          </div>
          <div class="rec_das_cont">
            <p class="title">N°{{ index + 1 }}</p>
            <p class="title2">{{ drive.title }}</p>
            <div class="frame">
              <p class="title">{{ drive.status }}</p>
            </div>
          </div>
          <router-link :to="`/drive/${drive.id}`"
            ><button class="rec_das_dri_but">View</button></router-link
          >
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
  z-index: 999;
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
  z-index: 0;
}
.rec_das_box2 {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 5vh;
  router-link {
    z-index: 9;
  }
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
  z-index: 5;
  cursor: pointer;
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
  background-color: #f4f4f4;
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
  background-color: #fefefe;
  z-index: 2;
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
  cursor: pointer;
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
  text-wrap: nowrap;
  overflow-x: hidden;
  overflow-y: hidden;
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
  z-index: 2;
}

.grdp {
  position: absolute;
  right: -100vh;
  height: 70vh;
  top: 25vh;
  z-index: 0;
}
.grds {
  position: absolute;
  left: 30vh;
  top: -70vh;
  z-index: 0;
}
.grdb {
  position: absolute;
  left: -60vh;
  height: 70vh;
  top: 90vh;
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
