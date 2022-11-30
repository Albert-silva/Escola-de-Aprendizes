<template>
    <div>
        <h1>Cadastre o novo conteúdo</h1>

        <v-alert v-if="finish" shaped outlined type="success" style=" margin: 20px">
            Conteudo cadastrado com sucesso! Você será redirecionada para a pagina de listagem...
        </v-alert>

        <v-form ref="form" v-model="valid" lazy-validation
            style="background: #FFF; border-radius: 5px; padding: 20px; margin: 20px">

            <v-text-field v-model="nome" :rules="nameRules" label="Nome" outlined required></v-text-field>
            <v-textarea v-model="descricao" name="input-5-1" label="Descrição" outlined></v-textarea>
            <v-text-field v-model="id_professor" :rules="numberRules" label="ID Professor" outlined required></v-text-field>

            <v-btn :disabled="!valid" color="success" class="mr-4" @click="addConteudo">
                Cadastrar
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
            id_professor: '',
            nameRules: [
                v => !!v || 'Nome é obrigatório'
            ],
            numberRules: [
                v => !!v || 'Id do professor é obrigatório'
            ],
        }
    },
    mounted() {
    },
    methods: {
        async addConteudo() {
            try {
                const data = {
                    nome: this.nome,
                    descricao: this.descricao,
                    id_professor: this.id_professor
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