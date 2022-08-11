<template>
    <div class="header">
        <h1>Cabeçalho da Página, abaixo o titulo dinamico:</h1>
        <p>{{ titulo }}</p>

        <p>Data: {{ dataAtual }}</p>
    </div>
</template>

<script>
export default {
    name: 'HeaderTest',

    props: ['titulo'],

    data() {
        return {
            dataAtual: new Date()
        }
    }
}
</script>

<style scoped>
.header {
    padding: 15px;
    background: rgb(212, 210, 210);
    border-radius: 10px;
}
</style>