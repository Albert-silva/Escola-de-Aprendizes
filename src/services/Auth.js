import Api from './Api'

// - - - - - - - - - - - - - - - - - - - - - - - - - - -
// Controller - service at Authentication
// - - - - - - - - - - - - - - - - - - - - - - - - - - -
export default {
    loginDiretor (data) {
        return Api({}).post('/login/diretor', data)
    },
    loginProfessor (data){
        return Api({}).post('/login/professor', data)
    },
    loginAluno (data){
        return Api({}).post('/login/aluno', data)
    },
}
