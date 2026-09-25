<script setup>
import { ref, onMounted } from "vue";
import router from "@/router";
import api from "@/services/api";

const applications = ref([]);
const name = ref("");
const arrow = "/src/assets/arrow.svg";

const exportCSV = async () => {
  try {

        const response = await api.get("/student/export");

        alert(response.data.message);

    
        await new Promise(resolve => setTimeout(resolve, 2000));

        const fileResponse = await api.get(
            "/student/export/download",
            {
                responseType: "blob"
            }
        );

        const url = window.URL.createObjectURL(
            new Blob([fileResponse.data], {
                type: "text/csv"
            })
        );

        const link = document.createElement("a");

        link.href = url;
        link.download = "my_applications.csv";

        document.body.appendChild(link);
        link.click();

        link.remove();

        window.URL.revokeObjectURL(url);

    } catch (error) {

        console.error("Export error:", error);

        alert("Unable to export CSV");
    }
};

onMounted(async () => {
  try {
    const response = await api.get("/student/applications/history");

    applications.value = response.data.applications;
    name.value = response.data.name;
  } catch (error) {
    alert(error.response.data.message);
  }
});

const back = () => {
  router.push("/student/dashboard");
};

const view = (id) => {
  router.push(`/drive/${id}`);
};
</script>

<template>
  <div class="main">
    <div class="back">
      <button class="back_btn" @click="back">Back</button>
    </div>
    <p class="no_application" v-if="applications.length===0">No applications yet</p>
    <div class="head_info" v-if="applications.length !==0">
      <p class="head_title">History</p>
      <p class="head_subTitle">
        {{ name }}
      </p>
      <div class="head_btns">
        <div class="head_btn_save" @click="exportCSV">
          <button class="export">Export</button>
          <button class="save_btn">
            <img :src="arrow" alt="" class="save_img" />
          </button>
        </div>
      </div>
    </div>
    <div class="head_body">
      <div class="main_content" v-for="(application, index) in applications">
        <div class="content">
          <p class="value1">{{ index + 1 }}</p>
          <p class="value2">{{ application.title }}</p>
          <p class="value">{{ application.recruiter }}</p>
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
          <button class="view" @click="view(application.drive_id)">View</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
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
  font-size: 2.1vh;
  margin: 0vh;
}

.head_btn_save {
  font-family: "Google Sans";
  font-weight: 550;
  letter-spacing: -0.1vh;
  font-size: 2.1vh;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.save_img {
  width: 4vh;
}
.head_btns {
  /* background: pink; */
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2vh;
  margin-top: 2vh;
}
.main_content {
  width: 90%;
  /* background-color: purple; */
  display: flex;
  flex-direction: column;
  /* align-items: center; */
}
.back {
  margin-top: 11vh;
  margin-left: 9vh;
}

.back_btn {
  width: 10vh;
  height: 4vh;
  font-family: "Google Sans";
  font-weight: 550;
  letter-spacing: -0.1vh;
  font-size: 2.1vh;
  border-radius: 2.5vh;
  background-color: #000;
  color: #fff;
  border: none;
  transition: 0.2s all ease-in-out;
  cursor: pointer;
}
.back_btn:hover {
  background-color: #fff;
  color: #000;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
}
.head_body {
  width: 80%;
  display: flex;
  flex-direction: column;
  justify-self: center;
  align-items: center;
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
.content:hover {
  background-image: linear-gradient(0deg, #000, #181818);
  color: #f4f3ec;
  justify-self: center;
  .view {
    background-color: #fff;
    color: #000;
    box-shadow: 0vh 0vh 0vh 0.5vh #000;
  }
}
.export {
  width: 30vh;
  height: 9vh;
  display: flex;
  align-items: center;
  padding: 0vh 0vh 0vh 8vh;
  font-family: "Google sans";
  font-size: 2.2vh;
  font-weight: 600;
  border: none;
  border-radius: 3vh 2vh 2vh 3vh;
  background-color: #000;
  color: #fff;
  cursor: pointer;
}

.save_btn {
  width: 9vh;
  height: 9vh;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1vh solid #000;
  margin-left: -9vh;
  font-family: "Google sans";
  font-size: 2.2vh;
  font-weight: 600;
cursor: pointer;
  border-radius: 2vh;
  background-color: #f1f1f1;
  color: #000;
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
.no_application{
  font-family: "Google Sans";
  font-size: 2.7vh;
  font-weight: 550;
  display: flex;
  justify-content: center;
  margin-top: 25vh;
}
</style>
