<template>
    <div>
        <div>
            <h1>Profile</h1>
        </div>

        <div class="profile">
            <div class="profile_content d-flex align-start flex-wrap">
                <p><b>Nome:</b> {{ user_infos.Nome }}</p>
                <p><b>E-mail:</b> {{ user_infos.Email }}</p>
            </div>

            <hr />
        </div>
    </div>
</template>

<script>
import AuthService from "../services/Auth";
export default {
    data() {
        return {
            user_id: null,
            user_infos: {}
        }
    },
    mounted() {
        this.user_id = localStorage.getItem("userId");
        this.getUser();
    },
    methods: {
        async getUser() {
            try {
                const response = await AuthService.getUser(this.user_id);
                this.user_infos = response.data;
            } catch (err) {
                this.user_infos = {};
            }
        }
    }
}
</script>

<style>
.profile {
    margin-top: 25px;
    background-color: #FFF;
    padding: 20px;
    border-radius: 10px;
}
.profile .profile_content {
    border-color: 1px solid #CCC;
    width: 100%;
}
.profile .profile_content p {
    min-width: 33%;
}
</style>