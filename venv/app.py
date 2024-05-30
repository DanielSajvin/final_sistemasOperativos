from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_content = '''
    <!doctype html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Datos del Estudiante</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                text-align: center;
                max-width: 400px;
            }
            h1 {
                color: #333;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.1em;
                color: #666;
                margin: 5px 0;
            }
            .section {
                margin-bottom: 20px;
            }
            .section:last-child {
                margin-bottom: 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="section">
                <h1>Datos del Estudiante</h1>
                <p><strong>Nombre:</strong> Mario Daniel Sajvin Gómez</p>
                <p><strong>Carnet:</strong> 1612921</p>
            </div>
            <div class="section">
                <h1>Universidad Rafael Landívar</h1>
                <p><strong>Facultad:</strong> Ingeniería</p>
                <p><strong>Curso:</strong> Sistemas operativos</p>
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
