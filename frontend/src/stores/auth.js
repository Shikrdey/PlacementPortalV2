import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useAuthStore = defineStore("auth", () => {
    const token = ref(localStorage.getItem("token") || "");
    const role = ref(localStorage.getItem("role") || "");
    const isLoggedIn = computed(() => token.value !== "");

    function setAuth(authToken, userRole){
        token.value = authToken;
        role.value = userRole;

        localStorage.setItem("token", authToken);
        localStorage.setItem("role", userRole);
    }
    function logout() {
        token.value = "";
        role.value = "";

        localStorage.removeItem("token");
        localStorage.removeItem("role");
    }
    return {
        token,
        role,
        isLoggedIn,
        setAuth,
        logout,
    };
});