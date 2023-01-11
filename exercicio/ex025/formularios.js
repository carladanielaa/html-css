function pegarDados(evento){
    evento.preventDefault();
    const formulario = document.querySelector("from");
    console.log(formulario);

    const dados = {};

    [...formulario.querySelectorAll("input")].forEach(tag)
    =>{
        console.log(tag);
    });
}