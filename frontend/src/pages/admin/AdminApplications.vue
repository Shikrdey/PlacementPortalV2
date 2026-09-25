<script setup>
import { ref,onMounted,computed } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/services/api';
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();

const router = useRouter();
const applications = ref({});

const logo = "/src/assets/frame.svg";
const logo2 = "/src/assets/logo2.jpeg";
const check = ref(false)
const id = ref("")
const name = ref("")
const search = ref("")

function formatDate(dateString) {
    const date = new Date(dateString);

    const day = String(date.getDate()).padStart(2, "0");
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const year = date.getFullYear();

    return `${day}-${month}-${year}`;
}
const viewDetail = (id)=>{
    router.push(`/admin/application/${id}`)
}
const viewName = (app_id) => {
    id.value = app_id
    check.value = !check.value
    for(const app of (applications.value)){
        if(app.id === app_id){
            name.value = app.student_name
        }
    }
}
const searchApplication = computed(()=>{
if(search.value.trim() === ""){
  return applications.value;
}
  return applications.value.filter((application)=>{
   return application.title.toLowerCase().includes(search.value.toLowerCase())
  });
});

onMounted( async ()=>{
    try{
        const response = await api.get("/admin/view/all/applications");
        applications.value = response.data
    }
    catch(error){
        alert(error.response.data.message)
        router.push("/admin/dashboard")
    }
});
const logout = () => {
  authStore.logout();
  router.push("/login");
};

</script>

<template>
    <div class="main">
        <div class="left">
            <img :src="logo" alt="logo" class="img">
            <div class="links">
                <router-link to="/admin/dashboard"><button class="btn">Dashboard</button></router-link>
                <router-link to="/admin/view/students"><button class="btn">Students</button></router-link>
                <router-link to="/admin/view/recruiters"><button class="btn">Recruiters</button></router-link>
                <router-link to="/admin/view/drives"><button class="btn">Drives</button></router-link>
                <router-link to="/admin/view/applications"><button class="btn1">Applications</button></router-link>
            </div>
            <div class="logout">
                <button class="btn2" @click="logout">Logout</button>
            </div>
        </div>
        <div class="right">
            <div class="right_left">
                <div class="right_head">
                    <p class="right-head">Applications</p>
                    <input type="search" class="search" placeholder="Search here" v-model="search">
                </div>
                 <p class="no_data" v-if="(applications.length) === 0 || searchApplication.length === 0">No Applications</p>
                <div class="right_main_body" tabindex="0" v-if="(applications.length) !== 0 && searchApplication.length !== 0">
                    <div class="titles">
                        <p>Id</p>
                        <p>Name</p>
                        <p>Title</p>
                        <p>Status</p>
                        <p>Applied On</p>
                    </div>
                    <div v-for="application in searchApplication" class="values" @click="viewName(application.id)">
                        <p>{{ application.id }}</p>
                        <p>{{ application.student_name }}</p>
                        <p>{{ application.title }}</p>
                        <p>{{ application.status }}</p>
                        <p>{{ formatDate(application.applied_at) }}</p>
                    </div>
                </div>
                
            </div>
            <div class="right_right" v-if="check">
                <img :src="logo2" alt="" class="img2">
                 <p class="name" v-if="name">{{ name }}</p>
                <div class="links3">
                    <button class="det" @click="viewDetail(id)">View Details</button>
                    <button class="det d">Blacklist</button>
                    <button class="det2 d">Delete User</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.main{
    height: 100vh;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #11191F;
    overflow: hidden;
    box-sizing: border-box;
}
.right{
    background-color: #F4F3EC;
    width: 80%;
    height: 100vh;
    border: 3vh solid #11191F;
    box-sizing: border-box;
    border-radius: 5vh;
    display: flex;
}
.left{
    background-color: #11191F;
    width: 20%;
    height: 100vh;
    /* display: flex;
    flex-direction: column; */

}
.img{
    width: 18vh;
    display: flex;
    justify-self: center;
    margin-top: 6vh;
}
.links{
    display: flex;
    flex-direction: column;
    gap: 2vh;
    /* background-color: rebeccapurple; */
    justify-self: center;
    margin-top: 7vh ;
}
.btn1{
    width: 36vh;
    height: 7vh;
    border-radius: 2vh;
    border: none;
    font-family: "Google Sans";
    font-weight: 650;
    font-size: 2vh;
    letter-spacing: -0.1vh;
    background-color: #F4F3EC;
    color: #11191F;
    text-align: left;
    padding-left: 5vh;
    cursor: pointer;
}
.btn{
    width: 36vh;
    height: 7vh;
    border-radius: 2vh;
    border: none;
    font-family: "Google Sans";
    font-weight: 650;
    font-size: 2vh;
    letter-spacing: -0.1vh;
    color: #F4F3EC;
    background-color: #11191F;
    text-align: left;
    padding-left: 5vh;
    transition: 0.1s all ease-in-out;
    cursor: pointer;
}
.btn:hover{
    box-shadow: 0vh 0vh 0vh 0.35vh #F4F3EC;
}
.btn2{
    width: 36vh;
    height: 7vh;
    border-radius: 2vh;
    border: none;
    font-family: "Google Sans";
    font-weight: 650;
    font-size: 2.2vh;
    letter-spacing: -0.1vh;
    color: #F4F3EC;
    background-color: #11191F;
    text-align: left;
    padding-left: 5vh;
    cursor: pointer;
    transition: 0.1s all ease-in-out;
}
.btn2:hover{
    background-color: #bb0000;
    color: #fff;
}

.logout{
    justify-self: center;
    margin-top: 25vh;
}
.right_left{
    height: 100%;
    width: 100%;
    background-color: #F4F3EC;
    border-radius: 2vh 0vh 0vh 2vh;
}
.right_right{
    height: 100%;
    width: 40%;
    background-color: #ffffff;
    border-radius: 0vh 2vh 2vh 0vh;
    border: 3vh solid #F4F3EC;
    box-sizing: border-box;
    border-radius: 6vh;
    display: flex;
    flex-direction: column;
    gap: 4.5vh;
    padding: 6vh 0vh 0vh 0vh;
    align-items: center;
}
.links3{
    display: flex;
    flex-direction: column;
    gap: 1.5vh;
}
.img2{
    width: 18vh;
    border-radius: 50vh;
    box-shadow: 0vh 0vh 0vh 0.6vh #F4F3EC;
    transition: 0.2s all ease-in-out;
}
.img2:hover{
    rotate: -5deg;
}
.det{
    width: 32vh;
    height: 7vh;
    border-radius: 10vh;
    border: none;
    font-family: "Google Sans";
    font-weight: 650;
    font-size: 2vh;
    letter-spacing: -0.1vh;
    background-color: #11191F;
    color: #F4F3EC;
    cursor: pointer;
    transition: 0.1s all ease-in-out;
}
.det:hover{
    background-color: #F4F3EC;
    box-shadow: 0vh 0vh 0vh 0.5vh #11191F;
    color: #11191F;
    font-weight: 700;
}
.det2{
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
.det2:hover{
    background-color: #9f0000;
}
.right_head{
    /* background-color: #9f0000; */
    display: flex;
    justify-content: space-between;
    padding: 0vh 7vh;
    align-items: center;
}
.right-head{
    font-family: "Google Sans";
    font-weight: 500;
    font-size: 4vh;
    letter-spacing: -0.2vh;
    color: #11191F;
    /* background-color: #000; */
}
.search{
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
.search:focus{
    width: 50vh;
    border: 0.3vh solid #F4F3EC;
    box-shadow: 0vh 0vh 0vh 0.3vh #11191F;
    outline: none;
}

.right_main_body{
    /* background-color: red; */
    display: flex;
    flex-direction: column;
    overflow: hidden;
}
.titles{
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
.values{
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
    margin-right: 1vh;
    cursor: pointer;
    border-radius: 0vh 5vh 0vh 5vh;
}
.values:hover{
    background-image: linear-gradient(0deg, #000, #181818);
    color: #F4F3EC;
    justify-self: center;
}
.name{
    color: #000;
    font-family: Google sans;
    font-size: 2.1vh;
    font-weight: 600vh;
    margin-top: -2vh;
    margin-bottom: -1.5vh;
}
.d{
    cursor: not-allowed;
}
.no_data{
    font-family: "Google Sans";
  font-weight: 500;
  font-size: 2.7vh;
  color: #11191f;
  padding: 21vh 0vh;
  justify-self: center;
}
</style>
