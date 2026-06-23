from fastapi.responses import HTMLResponse

@app.get('/exercicio-html', response_class=HTMLResponse)
def Viajei_zero():
    return """
    <html>
      <header>
        <title>Nosso ola mundo!</title>
      </header>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""