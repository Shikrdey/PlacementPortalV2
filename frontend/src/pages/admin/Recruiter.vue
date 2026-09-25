<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/services/api';


const route = useRoute() 
const router = useRouter()
const id = route.params.id;
const recruiter = ref({})

const cover = "/src/assets/cover.jpg"
const photo = "/src/assets/photo.jpg"


const loadData = async() =>{
    try{
        const response = await api.get(`/admin/view/recruiter/${id}`);
        recruiter.value = response.data
    }
    catch(error){
        alert(response.data.message)
    }
}

onMounted(async ()=>{
    try{
        const response = await api.get(`/admin/view/recruiter/${id}`);
        recruiter.value = response.data
    }
    catch(error){
        alert(response.data.message)
    }
})

const approve = async () =>{
    try{
        const response = await api.put(`/admin/approve/recruiter/${id}`, {
        })
        loadData();
        alert(response.data.message)
    }
    catch(error){
        alert(error.response.data.value)
    }
}
const block = async () =>{
    try{
        const response = await api.put(`/admin/block/recruiter/${id}`, {
        })
        loadData();
        alert(response.data.message)
    }
    catch(error){
        alert(error.response.data.value)
    }
}

const deleteUser = async (id) =>{
       const result = confirm("Are you sure you want to delete this recruiter? ")

        if(!result) return;
        const response = await api.delete(`/admin/delete/recruiter/${id}`)
        alert(response.data.message)
    router.push("/admin/view/recruiters")
}

const back = ()=>{
    router.push("/admin/view/recruiters")
}

</script>




<template>
    <div class="admin_details">
        <p class="back" @click="back()">Back</p>
        <div class="admin_head1">
            <div class="admin_img1">
                <img :src="cover" alt="" class="admin_img">
            </div>
            <img :src="photo" alt="" class="admin_img2">
            <div class="head_mid">
                <p class="head_status" :class="{
                    block: recruiter.status === 'Blocked',
                    active: recruiter.status === 'Approved',
                    pending: recruiter.status === 'Pending'
                }">{{ recruiter.status }}</p>
                <p class="mid_name"> {{ recruiter.name }}</p>
            </div>
            <p class="skills"> {{recruiter.website}} </p>
        </div>
        <div class="mid">
            <div class="admin_mid">
                <div class="item">
                    <p class="item_name">Email</p>
                    <p class="item_value">{{ recruiter.email }}</p>
                </div>
                 <div class="item">
                    <p class="item_name">Contact</p>
                    <p class="item_value">{{ recruiter.contact }}</p>
                </div>
                <div class="item">
                    <p class="item_name">Owernship Type</p>
                    <p class="item_value">{{ recruiter.ownership_type }}</p>
                </div>
                <div class="item">
                    <p class="item_name">Role</p>
                    <p class="stu">{{ recruiter.role }}</p>
                </div>
                <div class="item">
                    <p class="item_name">Offering Type</p>
                    <p class="item_value">{{recruiter.offering_type}}</p>
                </div>
            </div>
            <div class="admin_last">
                <button class="btn1" v-if="recruiter.status === 'Pending'" @click="approve()">Approve</button>
                <button class="btn1" v-if="recruiter.status === 'Approved' || recruiter.status ==='Pending'" @click="block()">Blacklist</button>
                <button class="btn2" v-if="recruiter.status=== 'Blocked'" @click="approve()">Approve</button>
                <button class="btn3" @click="deleteUser(id)">Delete</button>

            </div>
        </div>
    </div>
</template>

<style scoped>
.admin_details{
    display: flex;
    width: 100%;
    height: 100%;
    overflow: hidden;
    flex-direction: column;
    align-items: center;
    padding: 5vh 0vh 20vh 0vh;
    background-color: #F8F9FD;
}
.admin_head1{
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.admin_img1{
    width: 75%;
    height: 28vh;
    border-radius: 2vh;
    overflow: hidden;
    border: 0.5vh solid #000;
    
}
.admin_img{
    width: 100%;
    justify-self: center;
    align-self: center;
}
.admin_img2{
    width: 23vh;
    height: 23vh;
    border-radius: 50%;
    margin-top: -15vh;
    border: 0.6vh solid rgba(70, 73, 76, 0.921);
}

.mid_name{
    font-family: "Google sans";
    font-size: 3.7vh;
    font-weight: 650;
    letter-spacing: -0.1vh;
    margin-top: -1.5vh;

}
.head_status{
    font-family: "Google Sans";
    background-color: #1970d4;
    color: #fff;
    padding: 0.6vh 1.6vh;
    border-radius: 1vh;
    font-size: 1.8vh;
    font-weight: 600;
}
.small_dets{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2vh;
    margin-top: -2vh;
    background-color: #fff;
    padding: 0.5vh 1vh;
    border-radius: 2vh;
    box-shadow: 0vh 0vh 0.2vh 0vh #000;
}
.head_mid{
    display: flex;
    gap: 2vh;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.stu, .dob{
    font-family: "Google sans";
    font-size: 2vh;
    font-weight: 650;
    letter-spacing: -0.1vh;
}
.stu{
    background-color: #000;
    color: #fff;
    padding: 0.6vh 1.6vh ;
    border-radius: 1vh;
}
.dobspe{
    font-family: "Google sans";
    font-size: 1.9vh;
    font-weight: 500;
    letter-spacing: -0.1vh;
}
.admin_mid{
    width: 100vh;
    height: 100%;
    background-color: #fff;
    padding: 2vh 0vh;
    border-radius: 2vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 0.2vh solid #0000002e;
}
.admin_last{
    width: 100vh;
    height: 100%;
    background-color: #fff;
    padding: 2vh 0vh;
    border-radius: 2vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 0.2vh solid #0000002e;
}
.item{
    width: 100%;
    display: flex;
    justify-content: space-between;
    padding: 0vh 3vh;
    height: 6.8vh;
    box-sizing: border-box;
    align-items: center;
}
.item:hover{
    background-color: #f2f2f2;
}
.item_value{
    font-size: 1.9vh; 
    font-weight: 500;
    color: #1b1b1b;
    font-family: "google sans";
    letter-spacing: -0.1vh;
}
.item_name{
    font-size: 2vh; 
    font-weight: 650;
    color: #1b1b1b;
    font-family: "google sans";
    letter-spacing: -0.1vh;
}
.skills{
    margin: 1vh;
    width: 50vh;
    font-size: 1.8vh; 
    text-align: center;
    font-weight: 500;
    color: #1b1b1b;
    margin-top: 0;
    padding-bottom: 5vh;
    font-family: "google sans";
}
.back{
    position: relative;
    font-family: "google sans";
    font-size: 2.5vh; 
    text-align: center;
    font-weight: 500;
    background-color: #000;
    color: #fff;
    padding: 1vh 2.8vh;
    border-radius: 10vh;
    scale: 0.88;
    top: -2vh;
    left: -73vh;
    transition: 0.3s all ease-in-out;
    cursor: pointer;
}
.back:hover{
    color: #000;
    font-weight: 600;
    background-color: #fff;
    box-shadow: 0vh 0vh 0vh 0.4vh #000;
}
.btn1{
    width: 100%;
    height: 6.8vh;
    font-family: "google sans";
    font-size: 2vh; 
    text-align: center;
    font-weight: 650;
    letter-spacing: -0.1vh;
    background-color: #fff;
    color: #181818;
    border: none;
    
    /* display: flex;
    align-items: center;
    padding: 0vh 3vh;
    box-sizing: border-box; */
}
.btn2{
    width: 100%;
    height: 6.8vh;
    font-family: "google sans";
    font-size: 2vh; 
    text-align: center;
    font-weight: 650;
    letter-spacing: -0.1vh;
    background-color: #fff;
    color: #181818;
    border: none;

    /* display: flex;
    align-items: center;
    padding: 0vh 3vh;
    box-sizing: border-box; */
}
.btn3{
    width: 100%;
    height: 6.8vh;
    font-family: "google sans";
    font-size: 2vh; 
    text-align: center;
    font-weight: 650;
    letter-spacing: -0.1vh;
    background-color: #fff;
    color: #181818;
    border: none;

    /* display: flex;
    align-items: center;
    padding: 0vh 3vh;
    box-sizing: border-box; */
}
.btn1:hover{
    background-color: #f7ff9a;
    border: 0.5vh solid #e3cc00;
}
.btn2:hover{
    background-color: #b7ff9b;
    border: 0.5vh solid #2fa400;
}
.btn3:hover{
    background-color: #ff9b9b;
    border: 0.5vh solid #b20000;
}
.mid{
    display: flex;
    flex-direction: column;
    gap: 3vh;
}
.active {
  background-color: #198754;
}

.block {
  background-color: #dc3545;
}
.pending{
    background-color: #ffc107;
}
</style>