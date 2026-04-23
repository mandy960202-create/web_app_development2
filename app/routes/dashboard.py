from flask import Blueprint, render_template, session, redirect, url_for

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
def index():
    """
    GET: 檢查登入狀態。取得該用戶的總資產餘額、當月收支統計，並渲染首頁儀表板。
    """
    pass
