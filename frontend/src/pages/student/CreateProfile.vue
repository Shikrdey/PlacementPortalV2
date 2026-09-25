<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import api from "@/services/api";

const router = useRouter();

const name = ref("");
const dob = ref("");
const sex = ref("Male");
const linkedin = ref("");
const department = ref("Data Science & Applications");
const degree = ref("Bachelor of Science (BS)");
const passing_year = ref("");
const skills = ref("");
const cgpa = ref("");

const CreateProfile = async () => {
  try {
    const response = await api.post("/student/create/profile", {
      name: name.value,
      dob: dob.value,
      sex: sex.value,
      linkedin: linkedin.value,
      department: department.value,
      degree: degree.value,
      passing_year: passing_year.value,
      skills: skills.value,
      cgpa: cgpa.value,
    });
    alert(response.data.message);

    router.push("/student/dashboard");
  } catch (error) {
    alert(error.response.data.message);
  }
};
</script>

<template>
  <div class="create_prof_stu_main">
    <form @submit.prevent="CreateProfile">
      <div class="create_prof_stu_box">
        <p class="sph">Profile</p>
        <div class="create_prof_stu_field1">
          <div class="create_prof_stu_name">
            <p class="create_prof_stu_namel">Name</p>
            <input
              class="create_prof_stu_namein"
              type="text"
              v-model="name"
              placeholder="Enter your name"
              required
            />
          </div>
          <div class="create_prof_stu_dob">
            <p class="create_prof_stu_dobl">Date of Birth</p>
            <input
              class="create_prof_stu_dobin"
              type="date"
              v-model="dob"
              required
            />
          </div>
        </div>
        <div class="create_prof_stu_field2">
          <div class="create_prof_stu_sex">
            <p class="create_prof_stu_sexl">Gender</p>
            <select v-model="sex" class="create_prof_stu_sexin" required>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </select>
          </div>
          <div class="create_prof_stu_link">
            <p class="create_prof_stu_linkl">Linkedin</p>
            <input
              class="create_prof_stu_linkin"
              type="url"
              v-model="linkedin"
              placeholder="Enter your linkedin URL"
              required
            />
          </div>
        </div>
        <div class="create_prof_stu_field3">
          <div class="create_prof_stu_dept">
            <p class="create_prof_stu_dptl">Department</p>
            <select
              v-model="department"
              id="department"
              class="create_prof_stu_dptin"
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
          <div class="create_prof_stu_deg">
            <p class="create_prof_stu_degl">Degree</p>
            <select v-model="degree" id="degree" class="create_prof_stu_degin">
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
        <div class="create_prof_stu_field4">
          <div class="create_prof_stu_year">
            <p class="create_prof_stu_yearl">Graduation Year</p>
            <input
              class="create_prof_stu_yearin"
              type="text"
              v-model="passing_year"
              placeholder="Enter your graduation year"
              required
            />
          </div>
          <div class="create_prof_stu_cg">
            <p class="create_prof_stu_cgl">CGPA</p>
            <input
              class="create_prof_stu_cgin"
              type="text"
              v-model="cgpa"
              placeholder="Enter your CGPA"
              required
            />
          </div>
        </div>
        <div class="create_prof_stu_field5">
          <p class="create_prof_stu_skillsl">Skills</p>
          <input
            class="create_prof_stu_skillsin"
            type="text"
            v-model="skills"
            placeholder="Enter your skills"
            required
          />
        </div>

        <button class="cpp" type="submit">Save Profile</button>
      </div>
    </form>
  </div>
</template>

<style scoped>
.create_prof_stu_main {
  background-color: #fafafa;
  overflow: hidden;
  height: 100vh;
  width: 100%;
}
.create_prof_stu_box {
  display: flex;
  margin-top: 4vh;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  align-self: center;
}
.create_prof_stu_field1 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.create_prof_stu_field2 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.create_prof_stu_field3 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.create_prof_stu_field4 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.create_prof_stu_cgl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_stu_yearl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_stu_skillsl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_stu_dptl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_stu_degl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_stu_linkl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_stu_sexl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_stu_dobl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_stu_namel {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_stu_cgin {
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
.create_prof_stu_dobin {
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
.create_prof_stu_namein {
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
.create_prof_stu_yearin {
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
.create_prof_stu_skillsin {
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
.create_prof_stu_sexin {
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
.create_prof_stu_linkin {
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
.create_prof_stu_dptin {
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
.create_prof_stu_degin {
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
.cpp {
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
}
.cpp:hover {
  background-color: #fff;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
  color: #000;
}
.sph {
  font-family: "Google Sans";
  font-size: 3vh;
  font-weight: 500;
  margin-bottom: 4vh;
}
</style>
