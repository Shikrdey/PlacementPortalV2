<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/services/api';


const route = useRoute() 
const router = useRouter()
const id = route.params.id;
const application = ref({})

const cover = "/src/assets/cover.jpg"
const photo = "/src/assets/photo.jpg"


function formatDate(dateString) {
    const date = new Date(dateString);

    const day = String(date.getDate()).padStart(2, "0");
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const year = date.getFullYear();

    return `${day}-${month}-${year}`;
}

onMounted(async ()=>{
    try{
        const response = await api.get(`/admin/view/application/${id}`);
        application.value = response.data
    }
    catch(error){
        alert(response.data.message)
    }
})


const back = ()=>{
    router.push("/admin/view/applications")
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
                    selected: application.status === 'Selected',
                    applied: application.status === 'Applied',
                    shortlisted: application.status === 'Shortlisted',
                    rejected: application.status === 'rejected'
                }">{{ application.status }}</p>
                <p class="mid_name">{{ application.title }}</p>
            </div>
            <p class="skills">{{ application.student_name }}</p>
        </div>
        <div class="mid">
            <div class="admin_mid">
                <div class="item">
                    <p class="item_name">Recruiter</p>
                    <p class="item_value">{{application.recruiter_name}}</p>
                </div>
                 <div class="item">
                    <p class="item_name">Student Email</p>
                    <p class="item_value">{{ application.student_email }}</p>
                </div>
                <div class="item">
                    <p class="item_name">Rcruiter Email</p>
                    <p class="item_value">{{ application.recruiter_email}}</p>
                </div>
                <div class="item">
                    <p class="item_name">Resume</p>
                    <p class="item_value">{{application.resume}}</p>
                </div>
                <div class="item">
                    <p class="item_name">Applied On</p>
                    <p class="item_value">{{ formatDate(application.date_applied) }}</p>
                </div>
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

.dob{
    font-family: "Google sans";
    font-size: 2vh;
    font-weight: 650;
    letter-spacing: -0.1vh;
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
.mid{
    display: flex;
    flex-direction: column;
    gap: 3vh;
}
.applied {
  background-color: #1970d4;
}
.shortlisted {
  background-color: #ffc107;
}

.selected {
  background-color: #198754;
}

.rejected {
  background-color: #dc3545;
}
</style>