<script setup>

const logo = "/src/assets/logo.svg"
const companies = "/src/assets/companies.svg"
const img1 = "/src/assets/image1.svg"
const img2 = "/src/assets/image2.svg"

</script>


<template>
    <div class="heropage">
        <div class="navbar">
            <img :src="logo" alt="" class="navbar_logo">
            <div class="navbar_links">
                <p class="nav_1">About</p>
                <p class="nav_1">Contact</p>
                <p class="nav_1">Carrers</p>
                <p class="nav_1">Plans</p>
            </div>
        </div>
        <img :src="img2" alt="" class="card1">
        <img :src="img1" alt="" class="card2">
        <div class="main_body">
            <p class="Middle_heading">Placement</p>
            <p class="Middle_heading2">Portal</p>
            <button class="btn1">Ask About a query</button>
            <div class="btns">
                <router-link to="/register"><button class="btn2">Register</button></router-link>
                <router-link to="/login"><button class="btn3">Login</button></router-link>
            </div>
        </div>
        <img :src="companies" alt="" class="landmarks">
    </div>
</template>

<style scoped>
.heropage{
    height: 100vh;
    width: 100%;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}
.navbar{
    /* background-color: red; */
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 3vh 15vh;
}
.navbar_links{
    display: flex;
    gap: 10vh;
    color: #000;
    font-family: "Google Sans";
    font-size: 1.9vh;
    font-weight: 650;

}
.nav_1:hover{
    text-decoration: underline;
}
.navbar_logo{
    width: 7vh;
}
.card1{
    position: absolute;
    width: 36vh;
    top: 30vh;
    left: 33vh;
    rotate: -4deg;
}
.card2{
    position: absolute;
    width: 40vh;
    top: 35vh;
    right: 23vh;
    rotate: 6deg;
}
.main_body{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 2vh;
}
.Middle_heading{
    color: #212121;
    font-family: "Google Sans";
    font-size: 10vh;
    font-weight: 700;
    letter-spacing: -0.5vh;
}
.Middle_heading2{
    color: #212121;
    font-family: "Google Sans";
    font-size: 10vh;
    font-weight: 700;
    letter-spacing: -0.5vh;
    margin-top: -13vh;
}
.btn1{
    border: none;
    border-radius: 10vh;
    width: 40vh;
    height: 7vh;
    color: #212121;
    font-family: "Google Sans";
    font-size: 2.2vh;
    font-weight: 550;
    letter-spacing: -0.1vh;
    margin-top: -6vh;
    transition: 0.2s all ease-in-out;
}
.btn1:hover{
    color: #fff;
    background-color: #000;
}
.btn2{
    border: none;
    border-radius: 10vh;
    width: 23vh;
    height: 7vh;
    color: #fff;
    background-color: #FF8A3D;
    font-family: "Google Sans";
    font-size: 2.2vh;
    font-weight: 550;
    letter-spacing: -0.1vh;
    transition: 0.2s all ease-in-out;
    cursor: pointer;
}
.btn2:hover{
    background-color: #e36917;
}
.btn3{
    border: none;
    border-radius: 10vh;
    width: 16vh;
    height: 7vh;
    color: #fff;
    background-color: #E15A00;
    font-family: "Google Sans";
    font-size: 2.2vh;
    font-weight: 550;
    letter-spacing: -0.1vh;
    transition: 0.2s all ease-in-out;
    cursor: pointer;
}
.btn3:hover{
    background-color: #9b3e00;
}
.btns{
    display: flex;
    width: 40vh;
    justify-content: space-between;
    margin-top: 2vh;
}

.landmarks{
    margin-top: 18vh
}
</style>