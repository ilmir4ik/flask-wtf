from flask import Flask, render_template
from werkzeug.utils import redirect

from data.loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/index/<title>')
@app.route('/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def train(prof):
    if 'врач' in prof.lower() or 'учен' in prof.lower() or 'учён' in prof.lower() or 'ном' in prof.lower():
        res = 'Научные симуляторы'
    elif 'инжен' in prof.lower() or 'строит' in prof.lower():
        res = 'Инженерные тренажеры'
    else:
        res = 'Другое'
    title = host + ':' + str(port) + '/training/' + prof
    return render_template('index.html', title=title, text=res)


@app.route('/list-prof/<mode>')
def list_prof(mode):
    return render_template('list_prof.html', mode=mode)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    users = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']


if __name__ == '__main__':
    port = 8080
    host = '127.0.0.1'
    app.run(port=port, host=host)