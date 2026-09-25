<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import api from "@/services/api";

const router = useRouter();
const editMode = ref(false);

const name = ref("");
const dob = ref("");
const sex = ref("");
const linkedin = ref("");
const department = ref("");
const degree = ref("");
const passing_year = ref("");
const skills = ref("");
const cgpa = ref("");
const email = ref("");
const joined_on = ref("");

const updateProfile = async () => {
  try {
    const response = await api.put("/student/edit/profile", {
      name: name.value,
      dob: dob.value,
      sex: sex.value,
      linkedin: linkedin.value,
      degree: degree.value,
      department: department.value,
      skills: skills.value,
      cgpa: cgpa.value,
      passing_year: passing_year.value,
    });
    alert(response.data.message);
    router.push("/student/dashboard");
    editMode = false;
  } catch (error) {
    alert(error.response.data.message);
  }
};
onMounted(async()=>{
    try {
    const response = await api.get("/student/view/profile");

    name.value = response.data.name;
    dob.value = response.data.dob;
    sex.value = response.data.sex;
    linkedin.value = response.data.linkedin;
    department.value = response.data.department;
    degree.value = response.data.degree;
    passing_year.value = response.data.passing_year;
    skills.value = response.data.skills;
    cgpa.value = response.data.cgpa;
    email.value = response.data.email;
    joined_on.value = response.data.joined_on;
  } catch (error) {
    alert(error.response.data.messagge);
  }
});
</script>
<template>

    <div class="view_prof_stu_main">
      <div class="view_prof_stu_box">
        <p class="svph">Profile</p>
        <div class="view_prof_stu_field1">
          <div class="view_prof_stu_name">
            <p class="view_prof_stu_namel">Name</p>
            <input
              class="view_prof_stu_namein"
              type="text"
              v-model="name"
              :disabled="!editMode"
              required
            />
          </div>
          <div class="view_prof_stu_dob">
            <p class="view_prof_stu_dobl">Date of Birth</p>
            <input
              class="view_prof_stu_dobin"
              type="date"
              v-model="dob"
              :disabled="!editMode"
              required
            />
          </div>
        </div>
        <div class="view_prof_stu_field2">
          <div class="view_prof_stu_sex">
            <p class="view_prof_stu_sexl">Gender</p>
            <input
              class="view_prof_stu_sexin"
              v-if="!editMode"
              type="text"
              v-model="sex"
              :disabled="!editMode"
            />
            <select v-if="editMode" v-model="sex" class="view_prof_stu_sexin" required>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </select>
          </div>
          <div class="view_prof_stu_link">
            <p class="view_prof_stu_linkl">Linkedin</p>
            <input
              class="view_prof_stu_linkin"
              type="url"
              v-model="linkedin"
              :disabled="!editMode"
              required
            />
          </div>
        </div>
        <div class="view_prof_stu_field3">
          <div class="view_prof_stu_dept">
            <p class="view_prof_stu_dptl">Department</p>
            <input
              class="view_prof_stu_dptin"
              v-if="!editMode"
              type="text"
              v-model="department"
              :disabled="!editMode"
            />
            <select
              v-model="department"
              v-if="editMode"
              class="view_prof_stu_dptin"
            >
              <option value="Data Science & Applications">
                Data Science & Applications
              </option>
              <option value="Electronic Systems">Electronic Systems</option>
              <option value="Aeronautics and Space Technology">
                Aeronautics and Space Technology
              </option>
              <option value="Management and Data Science">
                Management and Data Science
              </option>
            </select>
          </div>
          <div class="view_prof_stu_deg">
            <p class="view_prof_stu_degl">Degree</p>
            <input
              class="view_prof_stu_dptin"
              v-if="!editMode"
              type="text"
              v-model="degree"
              :disabled="!editMode"
            />
            <select v-if="editMode" v-model="degree" id="degree" class="view_prof_stu_degin">
              <option value="Bachelor of Science (BS)">
                Bachelor of Science (BS)
              </option>
              <option value="Bachelor of Science (BSc)">
                Bachelor of Science (BSc)
              </option>
              <option value="Diploma">Diploma</option>
              <option value="Diploma in Data Science">
                Diploma in Data Science
              </option>
              <option value="Diploma in Programming">
                Diploma in Programming
              </option>
              <option value="PG Diploma in AL and ML">
                PG Diploma in AL and ML
              </option>
              <option value="M.Tech in AI and ML">M.Tech in AI and ML</option>
            </select>
          </div>
        </div>
        <div class="view_prof_stu_field4">
          <div class="view_prof_stu_year">
            <p class="view_prof_stu_yearl">Graduation Year</p>
            <input
              class="view_prof_stu_yearin"
              type="text"
              v-model="passing_year"
              :disabled="!editMode"
              required
            />
          </div>
          <div class="view_prof_stu_cg">
            <p class="view_prof_stu_cgl">CGPA</p>
            <input
              class="view_prof_stu_cgin"
              type="text"
              v-model="cgpa"
              :disabled="!editMode"
              required
            />
          </div>
        </div>
        <div class="view_prof_stu_field5">
          <p class="view_prof_stu_skillsl">Skills</p>
          <input
            class="view_prof_stu_skillsin"
            type="text"
            v-model="skills"
            :disabled="!editMode"
            required
          />
        </div>
        <div class="view_prof_stu_field6">
          <div class="view_prof_stu_sts">
            <p class="view_prof_stu_stsl">Email</p>
            <input
              class="view_prof_stu_stsin"
              type="text"
              v-model="email"
              disabled
            />
          </div>
          <div class="view_prof_stu_joi">
            <p class="view_prof_stu_joil">Joined At</p>
            <input
              class="view_prof_stu_joiin"
              type="text"
              v-model="joined_on"
              disabled
            />
          </div>
        </div>
         <div class="view_prof_stu_field7">
          <button class="vpsp1" v-if="!editMode" @click="editMode = true">
            Edit Profile
          </button>

          <button class="vpsp1" v-if="editMode" @click="updateProfile">
            Save
          </button>

          <button class="vpsp2" @click="router.push('/student/dashboard')">
            Back
          </button>
        </div>
      </div>
  </div>
</template>
<style scoped>

.view_prof_stu_main {
  background-color: #fafafa;
  overflow: hidden;
  height: 100vh;
  width: 100%;
}
.view_prof_stu_box {
  display: flex;
  margin-top: 2vh;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  align-self: center;
}
.view_prof_stu_field1 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.view_prof_stu_field2 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}

.view_prof_stu_field3 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}

.view_prof_stu_field4 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.view_prof_stu_field6 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.view_prof_stu_field7 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.view_prof_stu_cgl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_stu_yearl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_stu_skillsl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_stu_dptl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_stu_degl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_stu_linkl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_stu_sexl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_stu_dobl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_stu_namel {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_stu_stsl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_stu_joil {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_stu_cgin {
  width: 50vh;
  height: 6vh;
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
.view_prof_stu_dobin {
  width: 50vh;
  height: 6vh;
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
.view_prof_stu_namein {
  width: 50vh;
  height: 6vh;
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
.view_prof_stu_yearin {
  width: 50vh;
  height: 6vh;
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
.view_prof_stu_skillsin {
  width: 110vh;
  height: 6vh;
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
.view_prof_stu_sexin {
  width: 50vh;
  height: 6vh;
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
.view_prof_stu_linkin {
  width: 50vh;
  height: 6vh;
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
.view_prof_stu_dptin {
  width: 50vh;
  height: 6vh;
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
.view_prof_stu_degin {
  width: 50vh;
  height: 6vh;
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
.view_prof_stu_stsin {
  width: 50vh;
  height: 6vh;
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
.view_prof_stu_joiin {
  width: 50vh;
  height: 6vh;
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
.svph {
  font-family: "Google Sans";
  font-size: 3vh;
  font-weight: 500;
  margin-bottom: 2vh;
}
.vpsp2 {
  width: 50vh;
  height: 7vh;
  margin-top: 3vh;
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
}
.vpsp2:hover {
  background-color: #fff;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
  color: #000;
}
.vpsp1 {
  width: 50vh;
  height: 7vh;
  margin-top: 3vh;
  background-color: #FF8A3D;
  color: #fafafa;
  font-family: "Google Sans";
  font-size: 2.5vh;
  letter-spacing: -0.1vh;
  font-weight: 600;
  border: none;
  border-radius: 5vh;
  justify-self: center;
  transition: 0.3s all ease-in-out;
}
.vpsp1:hover {
  background-color: #fff;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
  color: #000;
}
.vsph {
  font-family: "Google Sans";
  font-size: 3vh;
  font-weight: 500;
  margin-bottom: 1vh;
}


</style>