<template>
    <div>
        <h1>Atualizando o conteúdo</h1>

        <v-alert v-if="finish" shaped outlined type="success" style=" margin: 20px">
            Conteúdo atualizado com sucesso! Você será redirecionada para a pagina de listagem...
            <a @click="goToList()">Ir Agora</a>
        </v-alert>

        <v-form ref="form" v-model="valid" lazy-validation
            style="background: #FFF; border-radius: 5px; padding: 20px; margin: 20px">

            <v-text-field v-model="nome" :rules="nameRules" label="Nome" outlined required></v-text-field>
            <v-textarea v-model="descricao" name="input-5-1" label="Descrição" outlined></v-textarea>

            <v-btn :disabled="!valid" color="success" class="mr-4" @click="updateConteudo">
                Atualizar
            </v-btn>

            <v-btn color="error" class="mr-4" @click="reset">
                Limpar
            </v-btn>
        </v-form>
    </div>
</template>

<script>
import ConteudoService from "../services/Conteudo";
export default {
    data() {
        return {
            valid: false,
            finish: false,
            nome: '',
            descricao: '',
            nameRules: [
                v => !!v || 'Nome é obrigatório'
            ],
            id: null
        }
    },
    mounted() {
        this.id = this.$route.params.id;
        this.getConteudo();
    },
    methods: {
        async getConteudo() {
            try {
                const response = await ConteudoService.getOne(this.id);
                this.nome = response.data.nome;
                this.descricao = response.data.descricao;
            } catch (err) {
                this.conteudos = [];
            }
        },
        async updateConteudo() {
            try {
                const data = {
                    nome: this.nome,
                    descricao: this.descricao
                }
                await ConteudoService.update(this.id, data);
                this.finish = true;
                this.reset();
                setTimeout(() => {
                    this.goToList();
                }, 5000);
            } catch (err) {
                console.log(err);
            }
        },
        goToList() {
            this.$router.push({ path: '/dash/conteudo' });
        },
        reset() {
            this.$refs.form.reset();
        },
    }
}
</script>