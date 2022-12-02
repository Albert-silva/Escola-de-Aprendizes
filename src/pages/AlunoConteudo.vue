<template>
    <div>
        <h1>Adicione um aluno a um conteúdo</h1>

        <v-alert v-if="finish" shaped outlined type="success" style=" margin: 20px">
            Aluno adicionado a conteudo com sucesso! Você será redirecionada para a pagina de listagem...
        </v-alert>

        <v-form ref="form" v-model="valid" lazy-validation
            style="background: #FFF; border-radius: 5px; padding: 20px; margin: 20px">

            <v-select v-model="aluno_selecionado" label="Aluno" :items="todos_alunos" item-text="name" item-value="id" return-object outlined></v-select>
            <v-select v-model="conteudo_selecionado" label="Conteudo" :items="todos_conteudos" item-text="name" item-value="id" return-object outlined></v-select>

            <v-btn :disabled="!valid" color="success" class="mr-4" @click="criaalunoconteudo">
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
import AuthService from "../services/Auth";

export default {
    data() {
        return {
            valid: false,
            finish: false,
            id_conteudo: '',
            numberRules: [
                v => !!v || 'Id do aluno e do conteudo são obrigatórios'
            ],
            
            aluno_selecionado: null,
            todos_alunos: [],
            
            conteudo_selecionado: null,
            todos_conteudos: []
        }
    },
    mounted() {
        // pegar a lista de alunos disponiveis
        this.getAlunos();
        // pegar a lista de conteudos disponiveis
        this.getConteudo();
    },
    methods: {
        async getAlunos() {
            try {
                const response = await AuthService.getAlunos();
                this.todos_alunos = response.data.users_list.map(user => {
                    return {
                        'id': user.id,
                        'name': user.Nome
                    }
                });

            } catch(err) {
                console.log(err);
            }
        },
        async getConteudo() {
            try {
                const response = await ConteudoService.getAll();
                this.todos_conteudos = response.data.conteudos.map(conteudo => {
                    return {
                        'id': conteudo.id,
                        'name': conteudo.nome
                    }
                })

            } catch(err) {
                console.log(err);
            }
        },
        async criaalunoconteudo() {
            try {
                const data = {
                    id_aluno: this.aluno_selecionado.id,
                    id_conteudo: this.conteudo_selecionado.id
                }
                await ConteudoService.alunoconteudo(data);
                
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