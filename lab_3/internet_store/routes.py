import os
import secrets

from PIL import Image
from flask import render_template, flash, url_for, redirect, request, abort
from flask_login import login_user, current_user, logout_user, login_required

from lab_3.internet_store import app, db, bCrypt
from lab_3.internet_store.forms import RegistrationForm, LoginForm, UpdateAccountForm, GoodForm
from lab_3.internet_store.models import User, Good, Roles, UsersGoods


@app.route("/")
@app.route("/home")
def home():
    goods = Good.query.all()
    return render_template("home.html", goods=goods)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bCrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bCrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture, folder):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/', folder, picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    goods = []
    for a in current_user.stock:
        goods.append((a.number, Good.query.filter_by(id=a.good_id).first()))
    if form.validate_on_submit():
        print(form.picture.data)
        if form.picture.data:
            current_user.image_file = save_picture(form.picture.data, 'profile_pics')
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    print(goods)
    return render_template("account.html", title='Account', image_file=image_file, form=form, goods=goods)


@app.route("/good/new", methods=['GET', 'POST'])
@login_required
def new_good():
    form = GoodForm()
    if form.validate_on_submit():
        good = Good(name=form.name.data, producer=form.producer.data,
                    description=form.description.data, number_available=form.number_available.data)
        if form.picture.data:
            good.image_file = save_picture(form.picture.data, 'good_pics')
        db.session.add(good)
        db.session.commit()
        flash('The good has been added!', 'success')
        return redirect(url_for('home'))
    return render_template("new_good.html", title='New Good', form=form, legend="Add Good")


@app.route("/good/<int:good_id>")
def good_one(good_id):
    good = Good.query.get_or_404(good_id)
    return render_template('good_one.html', title=good.name, good=good)


@app.route("/good-update/<int:good_id>", methods=['GET', 'POST'])
@login_required
def good_update(good_id):
    good = Good.query.get_or_404(good_id)
    if current_user.role != Roles.ADMIN:
        abort(403)
    form = GoodForm()
    if form.validate_on_submit():
        if form.picture.data:
            good.image_file = save_picture(form.picture.data, 'good_pics')
        good.name = form.name.data
        good.producer = form.producer.data
        good.number_available = form.number_available.data
        good.description = form.description.data
        db.session.commit()
        flash('The good has been updated!', 'success')
        return redirect(url_for('good_one', good_id=good.id))
    elif request.method == 'GET':
        form.name.data = good.name
        form.producer.data = good.producer
        form.number_available.data = good.number_available
        form.description.data = good.description
    return render_template("new_good.html", title='Update ' + good.name, form=form, legend="Update Good")


@app.route("/good-delete/<int:good_id>", methods=['POST'])
@login_required
def good_delete(good_id):
    good = Good.query.get_or_404(good_id)
    if current_user.role != Roles.ADMIN:
        abort(403)
    db.session.delete(good)
    db.session.commit()
    flash('The good has been deleted!', 'danger')
    return redirect(url_for('home'))


@app.route("/good-buy/<int:good_id>", methods=['GET'])
@login_required
def good_buy(good_id):
    good = Good.query.get_or_404(good_id)
    ug = UsersGoods(user_id=current_user.id, good_id=good.id, number=1)
    for a in UsersGoods.query.all():
        if a.good_id == good.id and a.user_id == current_user.id:
            ug = a
            ug.number += 1
    good.stock.append(ug)
    current_user.stock.append(ug)
    good.number_available -= 1
    db.session.commit()
    flash('Thank you for buying ' + good.name, 'success')
    return redirect(url_for('home'))
