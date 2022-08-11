<template>
  <div class="login">
            <img src="@/assets/images/logo.png" alt="Logo Escola de Aprendizes" />

            <div class="container">

                <form class="form">
                    <p>Faça seu login</p>
                    <div class="buttom">  

                        <div class="box-inputs">
                            <input type="email" v-model="email" placeholder="E-mail"> 
                            <input type="password" v-model="password" placeholder="Senha">  
                        </div>

                        <div class="box-buttons">
                                <button class="btn-login" type="button" @click="login()">ENTRAR</button>
                            <select tipo="select" v-model="tipo"> 
                                <option value="Diretor">Diretor</option>
                                <option value="Professor">Professor</option>
                                <option value="Aluno">Aluno</option>
                            </select> 
                        </div>
                    </div>
                </form>
            </div>
        </div>
</template>

<script>
import AuthService from "../services/Auth";
export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
      alerta: "",
      tipo: ""
    };
  },
  mounted() {},
  methods: {
    async login() {
      try {
        const credentials = {
          email: this.email,
          senha: this.password,
        };
        if (this.tipo == "Diretor"){
        const resposta = await AuthService.loginDiretor(credentials);
        localStorage.setItem("token", resposta.data.token);
        console.log("mudar para a outra rota!");
        }
        else if (this.tipo == "Professor"){
        const resposta = await AuthService.loginProfessor(credentials);
        localStorage.setItem("token", resposta.data.token);
        console.log("mudar para a outra rota!");
        }
        else if (this.tipo == "Aluno"){
        const resposta = await AuthService.loginAluno(credentials);
        localStorage.setItem("token", resposta.data.token);
        console.log("mudar para a outra rota!");
        }
      } catch (err) {
        const mensagemErro = err.response.data;
        this.alerta = mensagemErro;
      }
    },
  },
};
</script>

<style scoped> 
.login {
    display: flex;
    align-items: center;
    flex-direction: column;
    margin-top: 80px;
}

.login img {
    width: 260px;
}

.login .container {
    padding: 0px 40px 20px 40px;
    margin-top: 30px;
    box-sizing: border-box;
    background: #1D1C1C;
    opacity: 0.6;
    border: 1px solid #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 47px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.login .container .title {
    background: #FFFFFF;
    border-radius: 7px;
    padding: 6px 12px;
    margin-top: -18px;
}

.login .container .title p {
    padding: 0;
    margin: 0;
    text-align: center;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 700;
    font-size: 20px;
    line-height: 24px;
    color: #B06B6B;
    text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.login .container .form {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}
 .login .container .form p {
    margin-top: 30px;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 700;
    font-size: 20px;
    line-height: 24px;
    color: #FFFFFF;
}

.login .container .form .buttom{
    display: flex;
}

.login .container .form .box-inputs {
    width: 80%;
    margin-top: 20px;
    margin-bottom: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-right: 20px;
}

.login .container .form .box-buttons {
    width: 20%;
    margin-top: 20px;
    margin-bottom: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.login .container .form .box-inputs input {
    width: 340px;
    background: #FFFFFF;
    font-family: 'Inter';
    color: #333333;
    border: none;
    margin-top: 5px;
    margin-bottom: 5px;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 15px;
    padding-right: 15px;
}

.login .container .form .btn-login {
    background: #4094E0;
    border-radius: 8px;
    border: none;
    color: #FFF;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 700;
    font-size: 20px;
    line-height: 24px;
    padding: 7px 20px;
    cursor: pointer;
    margin-bottom: 5px;
}

.login .container .form .btn-login:hover {
    background-color: #4094E0;
}

@media screen and (max-width: 580px) {
  
  .login .container {
        width: 90%;
    }

  
  .login .container .form .box-inputs input {
        width: 85%;
    }
}

select {
    font-size: 20px;
    background-color: #4094E0;
    border: none;
    color: #FFFFFF;
    margin-top: 10px;
    padding: 7px 20px;
    border-radius: 8px;
    cursor: pointer;
}
</style>