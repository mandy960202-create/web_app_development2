from flask import Blueprint, render_template, request, redirect, url_for, flash, session

transaction_bp = Blueprint('transaction', __name__, url_prefix='/transaction')

@transaction_bp.route('/', methods=['GET'])
def history():
    """
    GET: 列出所有收支歷史明細。
    """
    pass

@transaction_bp.route('/new', methods=['GET'])
def new_transaction():
    """
    GET: 顯示新增收支的表單。
    """
    pass

@transaction_bp.route('/', methods=['POST'])
def create_transaction():
    """
    POST: 接收表單資料，寫入 Transaction 與更新 Account 餘額，重導向 /dashboard。
    """
    pass

@transaction_bp.route('/<int:id>/edit', methods=['GET'])
def edit_transaction(id):
    """
    GET: 顯示編輯特定收支的表單。
    """
    pass

@transaction_bp.route('/<int:id>/update', methods=['POST'])
def update_transaction(id):
    """
    POST: 接收表單資料，更新特定收支，重導向 /transaction。
    """
    pass

@transaction_bp.route('/<int:id>/delete', methods=['POST'])
def delete_transaction(id):
    """
    POST: 刪除特定收支，並還原 Account 餘額，重導向 /transaction。
    """
    pass
