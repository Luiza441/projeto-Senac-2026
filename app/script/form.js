const form = document.getElementById('post-form');

form.addEventListener('submit', function(event) {

        event.preventDefault();

        const autorInput = document.getElementById('autor')
        const tituloInput = document.getElementById('titulo')
        const historiaInput = document.getElementById('historia')
        const historiasContainer = document.getElementById('historias')

        const autor = autorInput.value;
        const titulo = tituloInput.value;
        const historia = historiaInput.value;

        if (!autor || !historia) { //verificação de campos vazios
                alert("Os campos `Autor` e `Historia` são obrigatórios!")
        }

        const article = document.createElement('article');
        article.className = "artigo";

        article.innerHTML =
                `<h3>${titulo}</h3>
         <p><strong> Autor: ${autor} </strong></p>
         <p>${historia.replace('/\n/g', '<br />')}</p>
         <hr />`;


        historiasContainer.appendChild(article);
        event.target.reset()
})