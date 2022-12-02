<template>
    <div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h1>Conteudos</h1>

            <v-btn color="blue-grey" class="ma-2 white--text" @click="goToAdd()" v-if="tipoUsuario !== 'aluno'">
                <v-icon left dark>
                    add
                </v-icon>
                Novo conteúdo
            </v-btn>
        </div>

        <div style="margin-top: 25px">
            <v-data-table :headers="headers" :items="conteudos" class="elevation-1"
                no-data-text="Não encontramos conteudos cadastrados.">

                <template v-slot:[`item.actions`]="{ item }">
                    <v-btn class="mx-2" fab dark small color="primary" :to="'/dash/edit-conteudo/' + item.id" v-if="tipoUsuario !== 'aluno'">
                        <v-icon dark>
                            edit
                        </v-icon>
                    </v-btn>

                    <v-btn class="mx-2" fab dark small color="red" @click="dialogCancelar = true; idParaCancelar = item.id;" v-if="tipoUsuario !== 'aluno'">
                        <v-icon dark>
                            delete
                        </v-icon>
                    </v-btn>
                </template>
            </v-data-table>

            <v-dialog v-model="dialogCancelar" persistent max-width="350">
                <v-card>
                    <v-card-title class="text-h5">
                        Excluindo Categoria: {{idParaCancelar}}
                    </v-card-title>

                    <v-card-text>Tem certeza que deseja excluir a categoria?</v-card-text>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="green darken-1" text @click="dialogCancelar = false; idParaCancelar = null;">
                            Cancelar
                        </v-btn>
                        <v-btn color="green darken-1" text @click="excluirConteudo(idParaCancelar)">
                            SIM
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </div>
    </div>
</template>

<script>
import ConteudoService from "../services/Conteudo";
export default {
    data() {
        return {
            headers: [
                { text: 'Nome', align: 'start', value: 'nome', },
                { text: 'Descrição', align: 'start', value: 'descricao' },
                { text: 'Professor', align: 'center', value:'professor'},
                { text: 'Ações', align: 'center', value: 'actions' }
            ],
            conteudos: [],
            dialogCancelar: false,
            idParaCancelar: null,
            tipoUsuario: null
        }
    },
    mounted() {
        this.tipoUsuario = localStorage.getItem("tipo");

        this.getConteudos();
    },
    methods: {
        async getConteudos() {
            try {
                const response = await ConteudoService.getAll();
                console.log(response)
                this.conteudos = response.data.conteudos.map(conteudo => {
                    return {
                        id: conteudo.id,
                        nome: conteudo.nome,
                        descricao: conteudo.descricao,
                        professor: conteudo.nome_professor
                    }
                });
            } catch (err) {
                this.conteudos = [];
            }
        },
        async excluirConteudo(idConteudo) {
            try {
                await ConteudoService.delete(idConteudo);
                this.dialogCancelar = false;
                this.getConteudos();
            } catch (err) {
                console.log(err)
            }
        },
        goToAdd() {
            this.$router.push({ path: '/dash/add-conteudo' });
        }
    }
}
</script>