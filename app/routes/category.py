from flask import Blueprint, render_template, request, redirect, url_for, flash, session

category_bp = Blueprint('category', __name__, url_prefix='/category')

@category_bp.route('/', methods=['GET', 'POST'])
def index():
    """
    GET: 顯示所有收支分類，以及新增分類與設定預算的表單。
    POST: 接收資料並新增一個分類（可包含預算），重導向 /category。
    """
    pass
