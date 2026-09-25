<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import api from "@/services/api";

const router = useRouter();

const grad_b = "/src/assets/b.svg";
const grad_p = "/src/assets/p.svg";
const grad_s = "/src/assets/s.svg";
const editMode = ref(false);

const name = ref("");
const email = ref("");
const contact = ref("");
const website = ref("");
const ownership_type = ref("");
const offering_type = ref("");
const joined_on = ref("");

const updateProfile = async () => {
  try {
    const response = await api.put("/recruiter/edit/profile", {
      name: name.value,
      contact: contact.value,
      website: website.value,
      ownership_type: ownership_type.value,
      offering_type: offering_type.value,
    });
    alert(response.data.message);
    router.push("/recruiter/dashboard");

    editMode.value = false;
  } catch (error) {
    alert(error.response.data.message);
  }
};

onMounted(async () => {
  try {
    const response = await api.get("/recruiter/profile");

    name.value = response.data.name;
    email.value = response.data.email;
    contact.value = response.data.contact;
    website.value = response.data.website;
    ownership_type.value = response.data.ownership_type;
    offering_type.value = response.data.offering_type;
    joined_on.value = response.data.joined_on;
  } catch (error) {
    alert(error.response.data.message);
  }
});
</script>

<template>
  <div class="view_prof_rec_main">
    <img :src="grad_p" alt="" class="grdp" />
    <img :src="grad_s" alt="" class="grds" />
    <img :src="grad_b" alt="" class="grdb" />
    <div class="view_prof_rec_box">
      <p class="vrph">Profile</p>
      <div class="view_prof_rec_field1">
        <p class="view_prof_rec_namel">Name</p>
        <input
          class="view_prof_rec_namein"
          type="text"
          v-model="name"
          :disabled="!editMode"
          required
        />
      </div>
      <div class="view_prof_rec_field2">
        <div class="view_prof_rec_cont">
          <p class="view_prof_rec_contl">Contact</p>
          <input
            class="view_prof_rec_contin"
            type="text"
            v-model="contact"
            :disabled="!editMode"
            required
          />
        </div>
        <div class="view_prof_rec_web">
          <p class="view_prof_rec_webl">Website</p>
          <input
            class="view_prof_rec_webin"
            type="url"
            v-model="website"
            :disabled="!editMode"
            required
          />
        </div>
      </div>
      <div class="view_prof_rec_field3">
        <div class="view_prof_rec_own">
          <p class="view_prof_rec_ownl">Ownership</p>
          <input
            class="view_prof_rec_ownin"
            v-if="!editMode"
            type="text"
            v-model="ownership_type"
            :disabled="!editMode"
          />
          <select
            v-if="editMode"
            v-model="ownership_type"
            class="view_prof_rec_ownin"
          >
            <option value="Private Limited">Private Limited</option>
            <option value="Public Limited">Public Limited</option>
            <option value="PSU">PSU</option>
            <option value="MNC">MNC</option>
            <option value="Startup">Startup</option>
            <option value="Partnership">Partnership</option>
          </select>
        </div>
        <div class="view_prof_rec_bus">
          <p class="view_prof_rec_busl">Business Offering</p>
          <input
            class="view_prof_rec_webin"
            v-if="!editMode"
            type="text"
            v-model="offering_type"
            :disabled="!editMode"
          />
          <select
            v-if="editMode"
            v-model="offering_type"
            class="view_prof_rec_busin"
          >
            <option value="Product-Based">Product-Based</option>
            <option value="Service-Based">Service-Based</option>
            <option value="Hybrid">Hybrid</option>
          </select>
        </div>
      </div>
      <div class="view_prof_rec_field4">
        <div class="view_prof_rec_sts">
          <p class="view_prof_rec_stsl">Email</p>
          <input
            class="view_prof_rec_stsin"
            type="text"
            v-model="email"
            :disabled="true"
          />
        </div>
        <div class="view_prof_rec_joi">
          <p class="view_prof_rec_joil">Joined At</p>
          <input
            class="view_prof_rec_joiin"
            type="text"
            v-model="joined_on"
            :disabled="true"
          />
        </div>
      </div>
      <div class="view_prof_rec_field5">
        <button class="vprp1" v-if="!editMode" @click="editMode = true">
          Edit Profile
        </button>

        <button class="vprp1" v-if="editMode" @click="updateProfile">
          Save
        </button>

        <button class="vprp2" @click="router.push('/recruiter/dashboard')">
          Back
        </button>
      </div>
    </div>
  </div>
</template>
<style scoped>
.view_prof_rec_main {
  background-color: #fafafa;
  overflow: hidden;
  height: 100vh;
  width: 100%;
}
.view_prof_rec_box {
  display: flex;
  margin-top: 7vh;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  align-self: center;
  gap: 2vh;
}
.view_prof_rec_field2 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.view_prof_rec_field3 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.view_prof_rec_field4 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.view_prof_rec_field5 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.view_prof_rec_namel {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_rec_contl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_rec_webl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_rec_ownl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_rec_busl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_rec_stsl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_rec_joil {
  font-family: "Google Sans";
  font-size: 2vh;
}
.view_prof_rec_namein {
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
.view_prof_rec_webin {
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
.view_prof_rec_contin {
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
.view_prof_rec_ownin {
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
.view_prof_rec_busin {
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
.view_prof_rec_stsin {
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
.view_prof_rec_joiin {
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
.vprp2 {
  width: 50vh;
  height: 8vh;
  margin-top: 5vh;
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
  cursor:pointer;
}
.vprp2:hover {
  background-color: #fff;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
  color: #000;
}
.vprp1 {
  width: 50vh;
  height: 8vh;
  margin-top: 5vh;
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
  cursor:pointer;
}
.vprp1:hover {
  background-color: #fff;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
  color: #000;
}
.vrph {
  font-family: "Google Sans";
  font-size: 3vh;
  font-weight: 500;
  margin-bottom: 1vh;
  z-index: 2;
}
.grdp {
  position: absolute;
  height: 80vh;
  right: -65vh;
  top: 5vh;
  z-index: 0;
}
.grds {
  position: absolute;
  left: 35vh;
  top: -83vh;
  z-index: 0;
}
.grdb {
  height: 80vh;
  position: absolute;
  left: -55vh;
  top: 20vh;
  z-index: 0;
}
.view_prof_rec_field1{
  z-index: 2;
}
</style>
