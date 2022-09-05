# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.settings import *
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    sitemap = [
        {
            'name': 'Index page',
            'route': 'index',
        },
        {
            'name': 'Login page',
            'route': 'login',
        },
        {
            'name': 'Name page',
            'route': 'name',
        },
        {
            'name': 'Names page',
            'route': 'names',
        },
    ]
    return render_template('index.html', url=URL, sitemap=sitemap)


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/name')
def name():
    user = {'username': 'BOSSy'}
    return render_template('name.html', title='Home', user=user)


@app.route('/names')
def names():
    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('names.html', title='Home', user=user, posts=posts)
