import AdminApplications from '@/pages/admin/AdminApplications.vue'
import AdminDrives from '@/pages/admin/AdminDrives.vue'
import AdminRecruiters from '@/pages/admin/AdminRecruiters.vue'
import AdminStudents from '@/pages/admin/AdminStudents.vue'
import AdminDashboard from '@/pages/admin/Dashboard.vue'
import Hero from '@/pages/Hero.vue'
import Student from '@/pages/admin/Student.vue'
import Login from '@/pages/Login.vue'
import Application from '@/pages/recruiter/Application.vue'
import CreateDrive from '@/pages/recruiter/CreateDrive.vue'
import RecruiterCreateProfile from '@/pages/recruiter/CreateProfile.vue'
import RecruiterDashboard from '@/pages/recruiter/Dashboard.vue'
import ViewApplications from '@/pages/recruiter/ViewApplications.vue'
import RecruiterViewProfile from '@/pages/recruiter/ViewProfile.vue'
import Register from '@/pages/Register.vue'
import StudentCreateProfile from '@/pages/student/CreateProfile.vue'
import StudentDashboard from '@/pages/student/Dashboard.vue'
import ViewHistory from '@/pages/student/ViewHistory.vue'
import StudentViewProfile from '@/pages/student/ViewProfile.vue'
import ViewDrive from '@/pages/ViewDrive.vue'
import { createRouter, createWebHistory } from 'vue-router'
import Drive from '@/pages/admin/Drive.vue'
import AdminApplication from '@/pages/admin/Application.vue'
import Recruiter from '@/pages/admin/Recruiter.vue'




const routes = [
  {
    path : "/",
    component : Hero
  },
  {
    path: "/register",
    component : Register
  },
  {
    path : "/login",
    component : Login
  },
  {
    path : "/admin/dashboard",
    component : AdminDashboard,
    meta : {
      requiresAuth: true
    }
  },
  {
    path : "/admin/view/applications",
    component : AdminApplications,
    meta : {
      requiresAuth: true
    }
  },
  {
    path : "/admin/view/drives",
    component : AdminDrives,
    meta : {
      requiresAuth: true
    }
  },
  {
    path : "/admin/view/recruiters",
    component : AdminRecruiters,
    meta : {
      requiresAuth: true
    }
  },
  {
    path : "/admin/view/students",
    component : AdminStudents,
    meta : {
      requiresAuth: true
    }
  },
   {
    path : "/admin/view/:id",
    component : Student,
    meta : {
      requiresAuth: true
    }
  },
   {
    path : "/admin/recruiter/:id",
    component : Recruiter,
    meta : {
      requiresAuth: true
    }
  },
   {
    path : "/admin/application/:id",
    component : AdminApplication,
    meta : {
      requiresAuth: true
    }
  },
   {
    path : "/admin/drive/:id",
    component : Drive,
    meta : {
      requiresAuth: true
    }
  },
  {
    path : "/recruiter/create/profile",
    component : RecruiterCreateProfile,
    meta : {
      requiresAuth: true
    }
  },
  {
    path : "/recruiter/dashboard",
    component : RecruiterDashboard,
    meta : {
      requiresAuth: true
    }
  },
  {
    path : "/create/drive",
    component : CreateDrive,
    meta : {
      requiresAuth: true
    }
  },
  {
    path : "/recruiter/profile",
    component : RecruiterViewProfile,
    meta : {
      requiresAuth: true
    }
  },
  {
    path : "/recruiter/edit/drive/:id/:bool",
    component : CreateDrive,
    meta : {
      requiresAuth: true
    }
  },
  {
    path : "/recruiter/view/applications/:id",
    component : ViewApplications,
    meta : {
      requiresAuth: true
    }
  },
  {
    path : "/recruiter/view/application/:id",
    component : Application,
    meta : {
      requiresAuth: true
    }
  },
  {
    path : "/student/create/profile",
    component : StudentCreateProfile,
    meta : {
      requiresAuth: true
    }
  },
  
  {
    path : "/student/dashboard",
    component : StudentDashboard,
    meta : {
      requiresAuth: true
    }
  },
  {
    path: "/student/profile",
    component: StudentViewProfile,
    meta : {
      requiresAuth: true
    }
  },
  {
    path: "/drive/:id",
    component: ViewDrive,
    meta : {
      requiresAuth: true
    }
  },
  {
    path: "/student/application/history",
    component: ViewHistory,
    meta : {
      requiresAuth: true
    }
  },
]
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    }

    return { top: 0 };
  }
})

router.beforeEach((to, from, next) => {

  const token = localStorage.getItem("token");
  const role = localStorage.getItem("role");

  if(to.meta.requiresAuth && !token){
    next("/login");
  }
  if((to.path === "/login" || to.path === "/register") && token ){
    if(role === "Student") return next("/student/dashboard");
    else if (role === "Recruiter") return next("/recruiter/dashboard");
    else return next("/admin/dashboard");
  }
  else{
    next();
  }
});

export default router
