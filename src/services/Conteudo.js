import Api from './Api'

// - - - - - - - - - - - - - - - - - - - - - - - - - - -
// Controller - service at Category
// - - - - - - - - - - - - - - - - - - - - - - - - - - -
export default {
    getAll () {
        return Api({}).get('/conteudo/')
    },

    add (dados) {
        return Api({}).post('/conteudo/', dados)
    },

    delete(id) {
        return Api({}).delete('/conteudo/' + id)
    },

    getOne(id) {
        return Api({}).get('/conteudo/' + id)
    },

    update(id, dados) {
        return Api({}).put('/conteudo/' + id, dados)
    },
    
    alunoconteudo (dados) {
        return Api({}).post('/conteudo/', dados)
    }
}