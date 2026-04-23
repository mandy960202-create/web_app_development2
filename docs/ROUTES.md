# 路由設計文件 - 個人記帳簿

本文件定義了系統中所有的 URL 路徑、HTTP 請求方法與對應的 Jinja2 模板，做為前後端對接的參考。

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 登入頁面 | GET | `/login` | `auth/login.html` | 顯示登入表單 |
| 執行登入 | POST | `/login` | — | 驗證帳密，成功則重導向 `/dashboard` |
| 註冊頁面 | GET | `/register` | `auth/register.html` | 顯示註冊表單 |
| 執行註冊 | POST | `/register` | — | 建立帳號，成功則重導向 `/login` |
| 登出系統 | GET | `/logout` | — | 清除 session 並重導向 `/login` |
| 儀表板 | GET | `/dashboard` | `dashboard/index.html` | 顯示總資產與當月收支圖表 |
| 歷史紀錄 | GET | `/transaction` | `transaction/history.html` | 列出所有收支明細 |
| 新增收支頁面 | GET | `/transaction/new` | `transaction/form.html` | 顯示新增收支的表單 |
| 執行新增收支 | POST | `/transaction` | — | 寫入資料庫，重導向 `/dashboard` |
| 編輯收支頁面 | GET | `/transaction/<id>/edit` | `transaction/form.html` | 顯示編輯收支的表單 |
| 執行更新收支 | POST | `/transaction/<id>/update` | — | 更新資料，重導向 `/transaction` |
| 執行刪除收支 | POST | `/transaction/<id>/delete` | — | 刪除資料，重導向 `/transaction` |
| 帳戶列表與新增 | GET, POST | `/account` | `account/index.html` | 顯示所有帳戶並提供新增表單 |
| 預算與分類設定 | GET, POST | `/category` | `category/index.html` | 顯示分類並設定預算與新增表單 |

## 2. 每個路由的詳細說明

### Auth 模組 (`/login`, `/register`, `/logout`)
- **輸入**：`username`, `password` (POST)
- **處理邏輯**：
  - 登入：透過 `User.get_by_username()` 查詢並驗證密碼，若成功將 user_id 存入 Flask `session`。
  - 註冊：透過 `User.create()` 寫入資料庫。
- **輸出**：登入成功重導向 `/dashboard`。錯誤則透過 `flash()` 提示訊息並重新渲染表單。

### Dashboard 模組 (`/dashboard`)
- **處理邏輯**：檢查 session 是否登入。透過 `Account.get_all_by_user()` 加總總餘額，透過 `Transaction.get_all_by_user()` 計算當月收支。
- **輸出**：渲染 `dashboard/index.html`。

### Transaction 模組 (`/transaction/...`)
- **輸入**：`account_id`, `category_id`, `type`, `amount`, `tx_date`, `description` (POST)
- **處理邏輯**：
  - 新增 (`POST /transaction`)：呼叫 `Transaction.create()` 與 `Account.update_balance()`，若資料驗證失敗則 `flash()` 錯誤並返回表單。
  - 刪除 (`POST /transaction/<id>/delete`)：確認擁有權後呼叫 `Transaction.delete()`，還原帳戶餘額。
- **輸出**：成功後重導向 `/transaction` 或 `/dashboard`。

### Account 模組 (`/account`)
- **輸入**：`name`, `type`, `balance` (POST)
- **處理邏輯**：建立新帳戶 `Account.create()`。
- **輸出**：渲染 `account/index.html`，POST 後重導向回同頁面。

### Category 模組 (`/category`)
- **輸入**：`name`, `type`, `budget` (POST)
- **處理邏輯**：建立新分類 `Category.create()`。
- **輸出**：渲染 `category/index.html`，POST 後重導向回同頁面。

## 3. Jinja2 模板清單

所有模板皆繼承自 `base.html`，共用導覽列 (Navbar) 與 footer：

- `templates/base.html`：基底版型。
- `templates/auth/login.html`：登入頁面。
- `templates/auth/register.html`：註冊頁面。
- `templates/dashboard/index.html`：首頁儀表板。
- `templates/transaction/history.html`：歷史明細列表。
- `templates/transaction/form.html`：共用的新增與編輯表單。
- `templates/account/index.html`：帳戶管理頁面。
- `templates/category/index.html`：分類與預算管理頁面。
