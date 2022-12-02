<template>
    <div>
        <div>
            <h1>Alunos</h1>
        </div>

        <div style="margin-top: 25px">
            <v-data-table :headers="headers" :items="users" class="elevation-1"
                no-data-text="Não encontramos alunos cadastrados.">
            </v-data-table>
        </div>
    </div>
</template>

<script>
import AuthService from "../services/Auth";
export default {
    data() {
        return {
            headers: [
                { text: 'Nome', align: 'start', value: 'name', },
                { text: 'Email', align: 'start', value: 'email'}
            ],
            users: []
        }
    },
    mounted() {
        const tipoUsuario = localStorage.getItem("tipo");
        if (tipoUsuario != "professor" && tipoUsuario != "diretor") {
            alert('Você nao tem permissão!');
            this.$router.push({path: '/dash/profile'});
        }

        this.getAlunos();
    },
    methods: {
        async getAlunos() {
            try {
                const response = await AuthService.getAlunos();
                this.users = response.data.users_list.map(user => {
                    return {
                        id: user.id,
                        name: user.Nome,
                        email: user.Email
                    }
                });
            } catch (err) {
                this.users = [];
            }
        }
    }
}
</script>