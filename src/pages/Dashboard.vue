<template>
  <section>
    <v-navigation-drawer
      app
      dark
      :mini-variant.sync="mini"
      src="/images/navigator.jpg"
    >
      <v-list>
        <v-list-item v-for="([icon, text, path], i) in items" :key="i" link :to="path">
          <v-list-item-icon>
            <v-icon>{{ icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click.stop="mini = !mini"></v-app-bar-nav-icon>

      <v-toolbar-title>Dashboard</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon @click="logout()">
        <v-icon>exit_to_app</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
  </section>
</template>

<script>
export default {
  name: "DashboardPage",
  data: () => ({
    mini: true,
    items: [
      ["person", "Meu perfil", "/dash/profile"],
      ["format_list_bulleted", "Conteúdo", "/dash/conteudo"],
    ],
  }),
  components: {},
  mounted() {
    if (!localStorage.getItem("token")) {
      this.logout();
    }

    const tipoUsuario = localStorage.getItem("tipo");
    if (tipoUsuario == 'professor') {
      this.items = [
        ["groups", "Alunos", "/dash/users"],
        ["person", "Meu perfil", "/dash/profile"],
        ["format_list_bulleted", "Conteúdo", "/dash/conteudo"],
        ["assignment", "Aluno e Conteúdo", "/dash/criaalunoconteudo"]
      ]
    } 
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      this.$router.push({path: '/login'});
    }
  }
};
</script>