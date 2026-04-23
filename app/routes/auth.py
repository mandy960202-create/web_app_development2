from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    GET: 顯示登入表單。
    POST: 接收 username 與 password，驗證身分並設定 session。成功重導向 /dashboard，失敗顯示錯誤。
    """
    pass

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    GET: 顯示註冊表單。
    POST: 接收 username 與 password，建立新帳號。成功重導向 /login。
    """
    pass

@auth_bp.route('/logout', methods=['GET'])
def logout():
    """
    清除 session 登入狀態，重導向至 /login。
    """
    pass
