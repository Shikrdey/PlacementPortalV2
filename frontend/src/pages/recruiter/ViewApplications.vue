<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import api from "@/services/api";

const router = useRouter();
const route = useRoute();

const drive_id = route.params.id;
const bookmark = "/src/assets/bookmark.svg";

const applications = ref([]);
const drive = ref({});

// const updateApplication = async ()=> {
//     try{
//         const response = await api.put(`/recruiter/update/application/${app_id}`, {
//             status: status.value,
//         });
//         alert(response.data.message);
//         router.push("`recruiter/view/drive/${drive_id}`")
//     }
//     catch(error){
//         alert(error.response.data.message);
//     }
// }

const go_to_drive = (drive_id) => {
  router.push(`/drive/${drive_id}`);
};

const view = (app_id) => {
  router.push(`/recruiter/view/application/${app_id}`);
};

onMounted(async () => {
  try {
    const response = await api.get(
      `/recruiter/view/all/applications/${drive_id}`,
    );
    applications.value = response.data.data;
    drive.value = response.data.drive_detail;
  } catch (error) {
    alert(error.response.data.message);
  }
});
</script>

<template>
  <div class="main">
    <div class="head_lastdate">
      <p class="LDTA">Applications</p>
    </div>
    <div class="head_info">
      <p class="head_title">{{ drive.title }}</p>
      <p class="head_subTitle">{{ drive.job_type }} || {{ drive.location }}</p>
      <div class="head_btns">
        <button class="head_btn_apply" @click="go_to_drive(drive.drive_id)">
          View Details
        </button>
      </div>
    </div>
    <div class="head_body">
      <div class="content" v-for="application, index in applications">
        <p class="value1">{{ index+1 }}</p>
        <p class="value2">{{ application.student_name }}</p>
        <p class="value">{{ application.student_email }}</p>
        <p
            class="status_box"
            :class="{
              applied: application.status === 'Applied',
              shortlisted: application.status === 'Shortlisted',
              selected: application.status === 'Selected',
              rejected: application.status === 'Rejected',
            }"
          >
            {{ application.status }}
          </p>
        <button class="view" @click="view(application.application_id)">View</button>
      </div>
    </div>
  </div>
</template>
<style scoped>
.head_lastdate {
  /* background: red; */
  display: flex;
  justify-content: end;
  padding: 0vh 5vh 0vh 0vh;
  margin-top: 10vh;
}

.LDTA {
  border-radius: 5vh;
  background-color: #eeeeee;
  border: 0.4vh solid #dfdfdf;
  width: fit-content;
  font-family: "Google Sans";
  font-weight: 550;
  font-size: 1.7vh;
  padding: 0.5vh 2vh;
  box-sizing: border-box;
}

.head_title {
  font-family: "Google Sans";
  font-weight: 700;
  letter-spacing: -0.4vh;
  justify-self: center;
  font-size: 7vh;
  margin: 4vh 0vh 0vh 0vh;
}
.head_info {
  margin-top: 9vh;
}
.head_subTitle {
  font-family: "Google Sans";
  font-weight: 550;
  letter-spacing: -0.1vh;
  justify-self: center;
  font-size: 1.8vh;
  margin: 0vh;
}
.head_btn_apply {
  width: 27vh;
  height: 8vh;
  font-family: "Google Sans";
  font-weight: 550;
  letter-spacing: -0.1vh;
  font-size: 2.1vh;
  border-radius: 0.5vh;
  background-color: #000;
  color: #fff;
  border: none;
  transition: 0.2s all ease-in-out;
  cursor: pointer;
}
.head_btn_apply:hover {
  background-color: #fff;
  color: #000;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
}

.head_btns {
  /* background: pink; */
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2vh;
  margin-top: 2vh;
}
.application_div {
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.main_content {
  width: 90%;
  /* background-color: purple; */
  display: flex;
  flex-direction: column;
  /* align-items: center; */
}
.name {
  font-family: "Google sans";
}

.head_body {
  width: 80%;
  display: flex;
  flex-direction: column;
  justify-self: center;
  padding: 5vh 0vh;
  gap: 4vh;


}
.content {
  height: 15vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-radius: 0.5vh;
  background-color: #f1f1f1;
  padding: 0vh 3vh 0vh 3vh;
  cursor: pointer;
  transition: 0.2s all ease-in-out;

}
.content:hover{
    background-image: linear-gradient(0deg, #000, #181818);
    color: #F4F3EC;
    justify-self: center;
    .view{
      background-color: #fff;
  color: #000;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
    }
}

.value {
  align-items: center;
  font-family: "Google Sans";
  font-weight: 500;
  font-size: 2.1vh;
}
.value1 {
  align-items: center;
  font-family: "Google Sans";
  font-weight: 400;
  font-size: 2.1vh;
}
.value2 {
  align-items: center;
  font-family: "Google Sans";
  font-weight: 650;
  font-size: 2.7vh;
}

.view {
  width: 27vh;
  height: 7vh;
  font-family: "Google Sans";
  font-weight: 550;
  letter-spacing: -0.1vh;
  font-size: 2.1vh;
  border-radius: 0.5vh;
  background-color: #000;
  color: #fff;
  border: none;
  transition: 0.2s all ease-in-out;
  cursor: pointer;
}
.status_box {
  display: inline-block;
  padding: 1vh 1.7vh;
  font-family: "Google Sans";
  font-weight: 550;
  border-radius: 0.5vh;
  font-size: 1.9vh;
  font-weight: 600;
}
.applied {
  background-color: #dbeafe;
  color: #1d4ed8;
}
.shortlisted {
  background-color: #fff3cd;
  color: #856404;
}

.selected {
  background-color: #d4edda;
  color: #155724;
}

.rejected {
  background-color: #f8d7da;
  color: #721c24;
}
</style>
