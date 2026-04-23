from flask import Blueprint, render_template, request, redirect, url_for, flash, session

account_bp = Blueprint('account', __name__, url_prefix='/account')

@account_bp.route('/', methods=['GET', 'POST'])
def index():
    """
    GET: 顯示所有帳戶與新增帳戶的表單。
    POST: 接收資料並新增一個資金帳戶，重導向 /account。
    """
    pass
