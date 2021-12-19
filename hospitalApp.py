from config import *
import reset_db, add, edit, delete, listar, extras

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)