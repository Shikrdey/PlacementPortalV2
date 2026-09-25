<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import api from "@/services/api";

const router = useRouter();


const name = ref("");
const contact = ref("");
const website = ref("");
const ownership_type = ref("Private Limited");
const offering_type = ref("Product-Based");

const CreateProfile = async () => {
  try {
    const response = await api.post("/recruiter/create/profile", {
      name: name.value,
      contact: contact.value,
      website: website.value,
      ownership_type: ownership_type.value,
      offering_type: offering_type.value,
    });
    alert(response.data.message);

    router.push("/recruiter/dashboard");
  } catch (error) {
    alert(error.response.data.message);
  }
};
</script>

<template>
  <div class="create_prof_rec_main">
    <form @submit.prevent="CreateProfile">
      <div class="create_prof_rec_box">
        <p class="rph">Profile</p>
        <div class="create_prof_rec_field1">
          <p class="create_prof_rec_namel">Name</p>
          <input
            class="create_prof_rec_namein"
            type="text"
            v-model="name"
            placeholder="Enter company name"
            required
          />
        </div>
        <div class="create_prof_rec_field2">
          <div class="create_prof_rec_cont">
            <p class="create_prof_rec_contl">Contact</p>
            <input
              class="create_prof_rec_contin"
              type="text"
              v-model="contact"
              placeholder="Enter contact number"
              required
            />
          </div>
          <div class="create_prof_rec_web">
            <p class="create_prof_rec_webl">Website</p>
            <input
              class="create_prof_rec_webin"
              type="url"
              v-model="website"
              placeholder="Enter recruiter website URL"
              required
            />
          </div>
        </div>
        <div class="create_prof_rec_field3">
          <div class="create_prof_rec_own">
            <p class="create_prof_rec_ownl">Ownership</p>
            <select v-model="ownership_type" class="create_prof_rec_ownin">
              <option value="Private Limited">Private Limited</option>
              <option value="Public Limited">Public Limited</option>
              <option value="PSU">PSU</option>
              <option value="MNC">MNC</option>
              <option value="Startup">Startup</option>
              <option value="Partnership">Partnership</option>
            </select>
          </div>
          <div class="create_prof_rec_bus">
            <p class="create_prof_rec_busl">Business Offering</p>
            <select v-model="offering_type" class="create_prof_rec_busin">
              <option value="Product-Based">Product-Based</option>
              <option value="Service-Based">Service-Based</option>
              <option value="Hybrid">Hybrid</option>
            </select>
          </div>
        </div>
        <button class="cprp" type="submit">Save Profile</button>
      </div>
    </form>
  </div>
</template>

<style scoped>
.create_prof_rec_main {
  background-color: #fafafa;
  overflow: hidden;
  height: 100vh;
  width: 100%;
}
.create_prof_rec_box {
  display: flex;
  margin-top: 10vh;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  align-self: center;
  gap: 3vh;
}
.create_prof_rec_field2 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.create_prof_rec_field3 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 9vh;
}
.create_prof_rec_namel {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_rec_contl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_rec_webl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_rec_ownl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_rec_busl {
  font-family: "Google Sans";
  font-size: 2vh;
}
.create_prof_rec_namein {
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
.create_prof_rec_contin {
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
.create_prof_rec_webin {
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
.create_prof_rec_ownin {
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
.create_prof_rec_busin {
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
.cprp {
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
}
.cprp:hover {
  background-color: #fff;
  box-shadow: 0vh 0vh 0vh 0.5vh #000;
  color: #000;
}
.rph {
  font-family: "Google Sans";
  font-size: 3vh;
  font-weight: 500;
  margin-bottom: 3vh;
}
</style>
