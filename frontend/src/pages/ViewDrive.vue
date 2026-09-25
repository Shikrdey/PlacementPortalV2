<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import api from "@/services/api";

const router = useRouter();
const route = useRoute();

const role = localStorage.getItem("role");

const bookmark = "/src/assets/bookmark.svg";

const id = route.params.id;

// const status = ref("");
const recruiterDrive = ref({});
const studentDrive = ref({});
const resume = ref("");
const resume_link = ref("");

const editDrive = (id,bool) => {
     router.push(`/recruiter/edit/drive/${id}/${bool}`)
} 

const updateDrive = async (status) => {
  try {
    const response = await api.put(`/recruiter/update/drive/${id}`, {
      status: status,
    });
    recruiterDrive.value.status = status;
    alert(response.data.message);
  } catch (error) {
    alert(error.response.data.message);
  }
};

const applydrive = async () => {
  try {
    const response = await api.post(`/student/apply/drive/${id}`, {
      resume: resume.value,
      drive_id: id,
    });
    console.log("Response:", response);

    alert(response.data.message);
    router.push("/student/dashboard");
  } catch (error) {
    alert(error.response.data.message);
  }
};

const back = () => {
  if (role === "Student") {
    router.push("/student/dashboard");
  } else {
    router.push("/recruiter/dashboard");
  }
};

const history = () => {
  router.push("/student/application/history");
};

const viewApplication = () => {
  router.push(`/recruiter/view/applications/${id}`);
};


const deleteDrive = async (id) => {
  const result = confirm("Are you sure you want to delete this drive?");

  if (!result) return;
  const response = await api.delete(`/delete/drive/${id}`);

  router.push("/recruiter/dashboard");
  alert(response.data.message);
};

onMounted(async () => {
  if (role === "Student") {
    try {
      const response = await api.get(`/student/load/drive/${id}`);

      studentDrive.value = response.data;
      resume_link.value = response.data.resume;
    } catch (error) {
      router.push("/student/dashboard")
      alert(error.response.data.message);
    }
  } else {
    try {
      const response = await api.get(`/recruiter/drive/${id}`);

      recruiterDrive.value = response.data;
    } catch (error) {
      router.push("/recruiter/dashboard")
      alert(error.response.data.message);
    }
  }
});
</script>

<template>
  <div class="main">
    <div class="head_lastdate">
      <p v-if="role === 'Student' && !studentDrive.applied" class="LDTA">
        Closing On : {{ studentDrive.deadline }}
      </p>
      <p v-if="role === 'Recruiter'" class="LDTA">
        Deadline : {{ recruiterDrive.deadline }}
      </p>
    </div>
    <div class="head_info">
      <p v-if="role === 'Student'" class="head_title">
        {{ studentDrive.title }}
      </p>
      <p v-if="role === 'Recruiter'" class="head_title">
        {{ recruiterDrive.title }}
      </p>
      <p v-if="role === 'Student'" class="head_subTitle">
        {{ studentDrive.recruiter }} || {{ studentDrive.job_type }} ||
        {{ studentDrive.location }}
      </p>
      <p v-if="role === 'Recruiter'" class="head_subTitle">
        {{ recruiterDrive.status }} || {{ recruiterDrive.job_type }} ||
        {{ recruiterDrive.location }}
      </p>
      <div class="head_btns">
        <a
          v-if="role === 'Student' && !studentDrive.applied"
          href="#application"><button class="head_btn_apply">Apply</button></a>
        <a href="#application"><button
          v-if="studentDrive.applied"
          class="status_box"
          :class="{
            applied : studentDrive.status === 'Applied',
            shortlisted : studentDrive.status === 'Shortlisted',
            selected : studentDrive.status === 'Selected',
            rejected : studentDrive.status === 'Rejected'}">
          {{ studentDrive.status }}
        </button></a>
        <button
          class="head_btn_apply"
          v-if="role === 'Recruiter' && (recruiterDrive.status === 'Ongoing' || recruiterDrive.status === 'Closed')"
          @click="viewApplication"
        >
          Applications
        </button>
        
        <button
          class="head_btn_save"
          v-if="role === 'Recruiter' && recruiterDrive.status === 'Closed'"
        >
          <img :src="bookmark" alt="" class="save_img" />
        </button>
        <button
          class="head_btn_apply"
          v-if="role === 'Recruiter' && recruiterDrive.status === 'Ongoing'"
          @click="updateDrive('Closed')"
        >
          Close
        </button>
        <button
          class="delete_btn"
          v-if="role === 'Recruiter' && recruiterDrive.status === 'Rejected'"
          @click="deleteDrive(id)"
        >
          Delete
        </button>
        <router-link :to=" `/recruiter/edit/drive/${id}/${true}`"><button
          class="edit_btn"
          v-if="role === 'Recruiter' && recruiterDrive.status === 'Pending'" @click="editDrive(id, true)"
        >
          Edit
        </button></router-link>
      </div>
    </div>
    <div class="head_body">
      <div class="main_content">
        <p class="content_title">Package</p>
        <p class="content_descrip" v-if="role === 'Student'">
          {{ studentDrive.ctc }}
        </p>
        <p class="content_descrip" v-if="role === 'Recruiter'">
          {{ recruiterDrive.ctc }}
        </p>
      </div>
      <div class="main_content">
        <p class="content_title">Description</p>
        <p class="content_descrip" v-if="role === 'Student'">
          {{ studentDrive.description }}
        </p>
        <p class="content_descrip" v-if="role === 'Recruiter'">
          {{ recruiterDrive.description }}
        </p>
      </div>
      <div class="main_content">
        <p class="content_title">Qualifications</p>
        <p class="content_descrip" v-if="role === 'Student'">
          {{ studentDrive.eligibility }}
        </p>
        <p class="content_descrip" v-if="role === 'Recruiter'">
          {{ recruiterDrive.eligibility }}
        </p>
      </div>
    </div>
    <div class="head_end">
      <button
        v-if="!studentDrive.applied"
        class="head_end_btn_back"
        @click="back"
      >
        Back
      </button>
      <button
        v-if="studentDrive.applied"
        class="head_end_btn_back"
        @click="history"
      >
        Back
      </button>
      <button class="head_end_btn_next">Next</button>
    </div>
    <section id="application">
      <div class="head_end_submiss">
        <form @submit.prevent="applydrive" v-if="role === 'Student'">
          <div class="end">
            <p v-if="!studentDrive.applied" class="end_title">
              Complete your application
            </p>
            <p v-if="studentDrive.applied" class="end_title">Application</p>
            <input
              v-if="!studentDrive.applied"
              type="url"
              v-model="resume"
              placeholder="Enter your Portfolio/Drive link"
              class="end_title_place"
              required
            />
            <input
              v-if="studentDrive.applied"
              type="url"
              v-model="resume_link"
              class="end_title_place"
              disabled
            />
          </div>
          <div class="end_buttn" v-if="!studentDrive.applied">
            <button class="last_btn">Send</button>
          </div>
        </form>
      </div>
    </section>
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
  font-family: "Google sans";
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
  border-radius: 2.5vh;
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
.head_btn_save {
  width: 8vh;
  height: 8vh;
  font-family: "Google Sans";
  font-weight: 550;
  letter-spacing: -0.1vh;
  font-size: 2.1vh;
  border: 0.5vh solid #181818;
  border-radius: 2.5vh;
  display: flex;
  justify-content: center;
  align-items: center;
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
.content_title {
  font-family: "Google Sans";
  font-weight: 550;
  letter-spacing: -0.1vh;
  font-size: 2.3vh;
  margin-left: -1vh;
}
.content_descrip {
  width: 100%;
  background-color: #f4f4f4;
  height: fit-content;
  padding: 5vh 5vh 10vh 5vh;
  border-radius: 1.5vh;
  box-sizing: border-box;
  margin-top: 0vh;
  font-family: "Google Sans";
  font-weight: 550;
  letter-spacing: -0.1vh;
  font-size: 1.8vh;
}
.head_body {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2vh;
  margin-top: 10vh;
}

.head_end_btn_next {
  width: 15vh;
  height: 6vh;
  border: none;
  background-color: #fff;
  color: #000;
  font-family: "Google Sans";
  font-weight: 600;
  font-size: 1.9vh;
  border-radius: 10vh;
  border: 0.5vh solid #000;
  cursor: not-allowed;
}

.head_end_btn_back {
  width: 15vh;
  height: 6vh;
  border: none;
  background-color: #000;
  color: #fff;
  font-family: "Google Sans";
  font-weight: 550;
  font-size: 1.9vh;
  border-radius: 10vh;
  transition: 0.2s all ease-in-out;
  cursor: pointer;
}
.head_end_btn_back:hover {
  background-color: #fff;
  color: #000;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
}
.head_end {
  /* background-color: red; */
  padding: 0vh 12vh;
  margin-top: 3vh;
  display: flex;
  gap: 1.5vh;
}
.head_end_submiss {
  /* background-color: beige; */
  margin-top: 10vh;
  display: flex;
  flex-direction: column;
  padding: 0vh 0vh 10vh 0vh;
}
.end_title {
  font-family: "Google Sans";
  font-weight: 600;
  letter-spacing: -0.3vh;
  /* text-decoration: underline; */
  font-size: 4.8vh;
  margin-left: -1vh;
  margin-left: 5vh;
}
.end_title_place {
  width: 90%;
  height: 7vh;
  display: block;
  margin: auto auto;
  border: none;
  padding: 0vh 3vh;
  box-sizing: border-box;
  font-family: "Google sans";
  background-color: #f4f4f4;
  border-radius: 1vh;
  font-size: 2vh;
}
.last_btn {
  width: 15vh;
  height: 6vh;
  border: none;
  background-color: #000;
  color: #fff;
  font-family: "Google Sans";
  font-weight: 550;
  font-size: 1.9vh;
  border-radius: 10vh;
  justify-self: end;
  transition: 0.2s all ease-in-out;
  cursor: pointer;
}
.last_btn:hover {
  background-color: #0b52c4;
  color: #fff;
  box-shadow: 0vh 0vh 0vh 0.5vh #0b52c4;
}
.end_buttn {
  /* background-color: rebeccapurple; */
  display: flex;
  justify-content: end;
  padding: 2vh 10vh;
}
.delete_btn {
  width: 27vh;
  height: 8vh;
  font-family: "Google Sans";
  font-weight: 550;
  letter-spacing: -0.1vh;
  font-size: 2.1vh;
  border-radius: 2.5vh;
  background-color: #e52c2c;
  color: #fff;
  border: none;
  transition: 0.2s all ease-in-out;
  cursor: pointer;
}
.delete_btn:hover {
  background-color: #fff;
  color: #000;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
}
.edit_btn {
  width: 27vh;
  height: 8vh;
  font-family: "Google Sans";
  font-weight: 550;
  letter-spacing: -0.1vh;
  font-size: 2.1vh;
  border-radius: 2.5vh;
  background-color: #3172d2;
  color: #fff;
  border: none;
  transition: 0.2s all ease-in-out;
  cursor: pointer;
}
.edit_btn:hover {
  background-color: #fff;
  color: #000;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
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
.status_box {
  display: inline-block;
  padding: 1vh 1.7vh;
   width: 27vh;
  height: 8vh;
  font-family: "Google Sans";
  font-weight: 600;
  font-size: 2.1vh;
  border-radius: 2.5vh;
    transition: 0.2s all ease-in-out;
  cursor: pointer;
}
.status_box:hover {
scale: 1.04;
}
</style>
