<script setup>
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import api from "@/services/api";

const router = useRouter();
const route = useRoute();
const edit = ref(false);

if (route.params.bool) {
  edit.value = route.params.bool;
} else {
  edit.value = false;
}
// edit.value = route.params.bool;
const id = route.params.id;

const title = ref("");
const job_type = ref("Full Time");
const description = ref("");
const eligibility = ref("");
const ctc = ref("");
const location = ref("");
const deadline = ref("");

const back = (id) => {
  router.push(`/drive/${id}`);
};

const createDrive = async () => {
  try {
    const response = await api.post("/recruiter/create_drive", {
      title: title.value,
      job_type: job_type.value,
      description: description.value,
      eligibility: eligibility.value,
      ctc: ctc.value,
      location: location.value,
      deadline: deadline.value,
    });
    alert(response.data.message);

    router.push("/recruiter/dashboard");
  } catch (error) {
    alert(error.response.data.message);
  }
};

const editDrive = async () => {
  try {
    const response = await api.put(`/recruiter/edit/drive/${id}`, {
      title: title.value,
      job_type: job_type.value,
      description: description.value,
      eligibility: eligibility.value,
      ctc: ctc.value,
      location: location.value,
      deadline: deadline.value,
    });
    alert(response.data.message);
    edit.value = !edit.value;
    router.push("/recruiter/dashboard");
  } catch (error) {
    alert(error.response.data.message);
  }
};

onMounted(async () => {
  if (edit) {
    const response = await api.get(`/recruiter/drive/${id}`);
    title.value = response.data.title;
    job_type.value = response.data.job_type;
    description.value = response.data.description;
    eligibility.value = response.data.eligibility;
    location.value = response.data.location;
    ctc.value = response.data.ctc;
    const [day, month, year] = response.data.deadline.split("-");
    deadline.value = `${year}-${month}-${day}`;
  }
});
</script>
<template>
  <div class="create_dri_main">
    <form @submit.prevent="edit ? editDrive() : createDrive()">
      <div class="create_dri_box">
        <p class="cdh">{{ edit ? "Edit Drive" : "Create" }}</p>
        <div class="create_dri_field1">
          <div class="create_dri_name">
            <p class="create_dri_namel">Job Title</p>
            <input
              class="create_dri_namein"
              type="text"
              v-model="title"
              placeholder="Enter job title"
              required
            />
          </div>
          <div class="create_dri_role">
            <p class="create_dri_rolel">Employment Type</p>
            <select v-model="job_type" class="create_dri_rolein" required>
              <option value="Full Time">Full Time</option>
              <option value="Internship">Intership</option>
            </select>
          </div>
        </div>
        <div class="create_dri_field2">
          <div class="create_dri_loc">
            <p class="create_dri_locl">Location</p>
            <input
              class="create_dri_locin"
              type="text"
              v-model="location"
              required
              placeholder="Enter recruiter location"
            />
          </div>
          <div class="create_dri_elg">
            <p class="create_dri_elgl">Qualifications</p>
            <input
              class="create_dri_elgin"
              type="text"
              v-model="eligibility"
              placeholder="Enter qualification required"
              required
            />
          </div>
        </div>
        <div class="create_dri_field3">
          <div class="create_dri_des">
            <p class="create_dri_desl">Job Description</p>
            <input
              class="create_dri_desin"
              type="text"
              v-model="description"
              placeholder="Enter job description"
              required
            />
          </div>
        </div>
        <div class="create_dri_field4">
          <div class="create_dri_ctc">
            <p class="create_dri_ctcl">Salary</p>
            <input
              class="create_dri_ctcin"
              type="text"
              v-model="ctc"
              placeholder="Enter ctc"
              required
            />
          </div>
          <div class="create_dri_ded">
            <p class="create_dri_dedl">Closing on</p>
            <input
              class="create_dri_dedin"
              type="date"
              v-model="deadline"
              required
            />
          </div>
        </div>
        <button class="cdp" type="submit" v-if="edit === false">Create</button>
        <div class="btn_grp" v-if="edit">
          <button class="edit_btn" type="submit">Edit</button>
          <button class="back_btn" @click="back(id)">Back</button>
        </div>
      </div>
    </form>
  </div>
</template>

<style scoped>
.create_dri_main {
  background-color: #fafafa;
  overflow: hidden;
  height: 100vh;
  width: 100%;
}
.create_dri_box {
  display: flex;
  margin-top: 7vh;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  align-self: center;
  gap: 1.5vh;
}
.create_dri_field1 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.create_dri_field2 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.create_dri_field3 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.create_dri_field4 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.create_dri_namel {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_dri_rolel {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_dri_locl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_dri_elgl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_dri_desl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_dri_ctcl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_dri_dedl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_dri_namein {
  width: 50vh;
  height: 7vh;
  background-color: #efeeee;
  border-radius: 5vh;
  margin-top: -0.2vh;
  margin-left: 1vh;
  font-family: "Google Sans";
  font-weight: 350;
  font-size: 1.9vh;
  border: none;
  color: #1e1e1e;
  padding: 0vh 3vh;
  box-sizing: border-box;
}
.create_dri_rolein {
  width: 50vh;
  height: 7vh;
  background-color: #efeeee;
  border-radius: 5vh;
  margin-top: -0.2vh;
  margin-left: 1vh;
  font-family: "Google Sans";
  font-weight: 350;
  font-size: 1.9vh;
  border: none;
  color: #1e1e1e;
  padding: 0vh 3vh;
  box-sizing: border-box;
}
.create_dri_locin {
  width: 50vh;
  height: 7vh;
  background-color: #efeeee;
  border-radius: 5vh;
  margin-top: -0.2vh;
  margin-left: 1vh;
  font-family: "Google Sans";
  font-weight: 350;
  font-size: 1.9vh;
  border: none;
  color: #1e1e1e;
  padding: 0vh 3vh;
  box-sizing: border-box;
}
.create_dri_elgin {
  width: 50vh;
  height: 7vh;
  background-color: #efeeee;
  border-radius: 5vh;
  margin-top: -0.2vh;
  margin-left: 1vh;
  font-family: "Google Sans";
  font-weight: 350;
  font-size: 1.9vh;
  border: none;
  color: #1e1e1e;
  padding: 0vh 3vh;
  box-sizing: border-box;
}
.create_dri_desin {
  width: 110vh;
  height: 7vh;
  background-color: #efeeee;
  border-radius: 5vh;
  margin-top: -0.2vh;
  margin-left: 1vh;
  font-family: "Google Sans";
  font-weight: 350;
  font-size: 1.9vh;
  border: none;
  color: #1e1e1e;
  padding: 0vh 3vh;
  box-sizing: border-box;
}
.create_dri_ctcin {
  width: 50vh;
  height: 7vh;
  background-color: #efeeee;
  border-radius: 5vh;
  margin-top: -0.2vh;
  margin-left: 1vh;
  font-family: "Google Sans";
  font-weight: 350;
  font-size: 1.9vh;
  border: none;
  color: #1e1e1e;
  padding: 0vh 3vh;
  box-sizing: border-box;
}
.create_dri_dedin {
  width: 50vh;
  height: 7vh;
  background-color: #efeeee;
  border-radius: 5vh;
  margin-top: -0.2vh;
  margin-left: 1vh;
  font-family: "Google Sans";
  font-weight: 350;
  font-size: 1.9vh;
  border: none;
  color: #1e1e1e;
  padding: 0vh 3vh;
  box-sizing: border-box;
}
.cdp {
  width: 50vh;
  height: 8vh;
  margin-top: 4vh;
  background-color: #181818;
  color: #fafafa;
  font-family: "Google Sans";
  font-size: 2.5vh;
  letter-spacing: -0.1vh;
  font-weight: 600;
  border: none;
  border-radius: 5vh;
  justify-self: center;
  transition: 0.3s all ease-in-out;
  cursor: pointer;
}
.cdp:hover {
  background-color: #fff;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
  color: #000;
}
.btn_grp {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 5vh;
}

.edit_btn {
  width: 30vh;
  height: 8vh;
  margin-top: 4vh;
  background-color: #2168db;
  color: #fafafa;
  font-family: "Google Sans";
  font-size: 2.5vh;
  letter-spacing: -0.1vh;
  font-weight: 600;
  border: none;
  border-radius: 5vh;
  justify-self: center;
  transition: 0.3s all ease-in-out;
  cursor: pointer;
}
.edit_btn:hover {
  background-color: #fff;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
  color: #000;
}
.back_btn {
  width: 30vh;
  height: 8vh;
  margin-top: 4vh;
  background-color: #181818;
  color: #fafafa;
  font-family: "Google Sans";
  font-size: 2.5vh;
  letter-spacing: -0.1vh;
  font-weight: 600;
  border: none;
  border-radius: 5vh;
  justify-self: center;
  transition: 0.3s all ease-in-out;
  cursor: pointer;
}
.back_btn:hover {
  background-color: #fff;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
  color: #000;
}
.cdh {
  font-family: "Google Sans";
  font-size: 3vh;
  font-weight: 500;
  margin-bottom: 4vh;
}
</style>
