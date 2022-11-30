<template>
    <div>
        <div>
            <h1>Usuários</h1>
        </div>

        <div style="margin-top: 25px">
            <v-data-table :headers="headers" :items="users" class="elevation-1"
                no-data-text="Não encontramos usuários cadastrados.">
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
        this.getUsers();
    },
    methods: {
        async getUsers() {
            try {
                const response = await AuthService.getUsers();
                this.users = response.data.users_list.map(user => {
                    return {
                        id: user.id,
                        name: user.name,
                        email: user.email
                    }
                });
            } catch (err) {
                this.users = [];
            }
        }
    }
}
</script>