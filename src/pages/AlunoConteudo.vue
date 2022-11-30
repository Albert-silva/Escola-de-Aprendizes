<template>
    <div>
        <h1>Adicione um aluno a um conteúdo</h1>

        <v-alert v-if="finish" shaped outlined type="success" style=" margin: 20px">
            Aluno adicionado a conteudo com sucesso! Você será redirecionada para a pagina de listagem...
        </v-alert>

        <v-form ref="form" v-model="valid" lazy-validation
            style="background: #FFF; border-radius: 5px; padding: 20px; margin: 20px">

            <v-text-field v-model="id_aluno" :rules="numberRules" label="ID Aluno" outlined required></v-text-field>
            <v-text-field v-model="id_conteudo" :rules="numberRules" label="ID Conteudo" outlined required></v-text-field>

            <v-btn :disabled="!valid" color="success" class="mr-4" @click="alunoconteudo">
                Adicionar
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
            id_aluno: '',
            id_conteudo: '',
            numberRules: [
                v => !!v || 'Id do aluno e do conteudo são obrigatórios'
            ],
        }
    },
    mounted() {
    },
    methods: {
        async alunoconteudo() {
            try {
                const data = {
                    id_aluno: this.id_aluno,
                    id_conteudo: this.id_conteudo
                }
                await ConteudoService.add(data);
                
                this.finish = true;
                this.reset();
                setTimeout(() => {
                    this.$router.push({path: '/dash/conteudo'});
                }, 5000);
            } catch (err) {
                console.log(err);
            }
        },
        reset() {
            this.$refs.form.reset();
        },
    }
}
</script>