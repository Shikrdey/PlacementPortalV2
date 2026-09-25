<script setup>
import { ref,onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/services/api';
import { useAuthStore } from '@/stores/auth';
const authStore = useAuthStore();

const router = useRouter();
const look = ref(false)
const check = ref(null)
const id = ref(null)
const name = ref("")
const recruiters = ref({});
const logo = "/src/assets/frame.svg";
const logo2 = "/src/assets/logo2.jpeg";

const search = ref("")


const searchRecruiter = computed(()=>{
if(search.value.trim() === ""){
  return recruiters.value;
}
  return recruiters.value.filter((recruiter)=>{
   return recruiter.name.toLowerCase().includes(search.value.toLowerCase()) || String(recruiter.id).includes(search.value)
  });
});


const loadData = async()=>{
    try{
        const response = await api.get("/admin/view/all/recruiters");
        recruiters.value = response.data
    }
    catch(error){
        alert(error.response.data.message)
        router.push("/admin/dashboard")
    }
}

onMounted( async ()=>{
    try{
        const response = await api.get("/admin/view/all/recruiters");
        recruiters.value = response.data
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
const viewName = (user_id) => {
        look.value =!look.value
    id.value = user_id
    for(const recruiter of (recruiters.value)){
        if(recruiter.id === user_id){
            name.value = recruiter.name
        }
    }
}
const viewDetail = (id)=>{
    router.push(`/admin/recruiter/${id}`)
}
const deleteUser = async (id) =>{
       const result = confirm("Are you sure you want to delete this recruiter? ")

        if(!result) return;
        const response = await api.delete(`/admin/delete/recruiter/${id}`)
        alert(response.data.message)
        name.value = ""
        await loadData();
        look.value = !look.value
}
const blockuser = async (id) =>{

        const response = await api.put(`/admin/block/recruiter/${id}`)
        alert(response.data.message)
        name.value = ""
        await loadData();
}
const checkblock = (id) => {
    for(const recruiter of recruiters.value){
        if(recruiter.id === id && recruiter.status === "Blocked" ){
        check.value = "Blocked"
        }
    }
}

</script>
<template>
    <div class="main">
        <div class="left">
            <img :src="logo" alt="logo" class="img">
            <div class="links">
                <router-link to="/admin/dashboard"><button class="btn">Dashboard</button></router-link>
                <router-link to="/admin/view/students"><button class="btn">Students</button></router-link>
                <router-link to="/admin/view/recruiters"><button class="btn1">Recruiters</button></router-link>
                <router-link to="/admin/view/drives"><button class="btn">Drives</button></router-link>
                <router-link to="/admin/view/applications"><button class="btn">Applications</button></router-link>
            </div>
            <div class="logout">
                <button class="btn2" @click="logout">Logout</button>
            </div>
        </div>
        <div class="right">
            <div class="right_left">
                <div class="right_head">
                    <p class="right-head">Recruiters</p>
                    <input type="search" class="search" placeholder="Search here" v-model="search">
                </div>
                 <p class="no_data" v-if="(recruiters.length) === 0 || searchRecruiter.length ===0">No registered recruiter</p>
                <div class="right_main_body" tabindex="0" v-if="recruiters.length !== 0 && searchRecruiter.length !== 0">
                    <div class="titles">
                        <p>Id</p>
                        <p>Name</p>
                        <p>Email</p>
                        <p>Status</p>
                        <p>Joined On</p>
                    </div>
                    <div class="values" v-for="recruiter in searchRecruiter" @click="viewName(recruiter.id); checkblock(recruiter.id)">
                        <p>{{ recruiter.id }}</p>
                        <p>{{ recruiter.name }}</p>
                        <p>{{ recruiter.email }}</p>
                        <p>{{ recruiter.status }}</p>
                        <p>{{ recruiter.joined  }}</p>
                    </div>
                </div>
            </div>
            <div class="right_right" v-if="look">
                <img :src="logo2" alt="" class="img2">
                <p class="name" v-if="name">{{ name }}</p>
                <div class="links3">
                 <button class="det" :class="{noName:!name}" @click="viewDetail(id)">View Details</button>
                    <button class="det" :class="{noName:!name || check === 'Blocked' }" @click = "blockuser(id)">Blacklist</button>
                    <button class="det2" :class="{noName:!name}" @click="deleteUser(id)">Delete User</button>
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
.noName{
    cursor: not-allowed;
}
.no_data{
    font-family: "Google Sans";
  font-weight: 500;
  font-size: 2.7vh;
  color: #11191f;
  padding: 21vh 0vh 0vh 10vh;
  justify-self: center;
}
</style>
