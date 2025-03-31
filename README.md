# 🛍 Django E-commerce API

A **feature-rich** e-commerce backend API built with **Django** and **Django REST Framework**.

---

## 🚀 Project Overview

This project is a **comprehensive e-commerce RESTful API** designed to power an online store. It includes **product management, user authentication, cart functionality, order processing,** and much more!

### ✨ Features

- 🔑 **User Authentication**: Secure JWT-based authentication with Djoser
- 🛒 **Product Management**: Full CRUD with filtering, searching, and sorting
- 📦 **Collection Management**: Group products into collections
- 🛍 **Shopping Cart System**: Add, remove, and update items
- 📦 **Order Processing**: Order placement and tracking
- 👤 **Customer Profiles**: View and manage purchase history
- ⭐ **Reviews System**: Leave reviews for products
- 🔐 **Role-based Access Control**: Admin, staff, and customers
- 🏷 **Content Tagging**: Flexible product categorization
- ❤️ **Like Feature**: Users can like various content types
- 📄 **Pagination**: Efficient API responses with pagination

---

## 🛠 Tech Stack

| Technology      | Description                          |
|---------------|----------------------------------|
| **Django**        | Web framework for backend logic |
| **Django REST Framework** | API development & serialization |
| **PostgreSQL**   | Relational database for storage  |
| **Simple JWT**   | JSON Web Token authentication  |
| **Djoser**       | Prebuilt authentication endpoints |
| **Django Filter** | Advanced filtering support |
| **Django Debug Toolbar** | Debugging & performance monitoring |

---

## 🔌 API Endpoints

### 🔐 Authentication
- `POST /auth/users/` - Register new user
- `POST /auth/jwt/create/` - Get JWT token
- `POST /auth/jwt/refresh/` - Refresh JWT token

### 🛍 Products
- `GET /store/products/` - List all products
- `GET /store/products/{id}/` - Get product details
- `POST /store/products/` - Create new product (**Admin only**)
- `PUT /store/products/{id}/` - Update product (**Admin only**)
- `DELETE /store/products/{id}/` - Delete product (**Admin only**)

### 📦 Collections
- `GET /store/collections/` - List all collections
- `GET /store/collections/{id}/` - Get collection details
- `POST /store/collections/` - Create new collection (**Admin only**)
- `PUT /store/collections/{id}/` - Update collection (**Admin only**)
- `DELETE /store/collections/{id}/` - Delete collection (**Admin only**)

### 🛒 Carts
- `POST /store/carts/` - Create a cart
- `GET /store/carts/{id}/` - Get cart details
- `DELETE /store/carts/{id}/` - Delete cart

### 🛍 Cart Items
- `GET /store/carts/{id}/items/` - List cart items
- `POST /store/carts/{id}/items/` - Add item to cart
- `PATCH /store/carts/{id}/items/{id}/` - Update item quantity
- `DELETE /store/carts/{id}/items/{id}/` - Remove item from cart

### 📦 Orders
- `GET /store/orders/` - List customer orders
- `POST /store/orders/` - Create an order
- `GET /store/orders/{id}/` - Get order details
- `PATCH /store/orders/{id}/` - Update order (**Admin only**)
- `DELETE /store/orders/{id}/` - Delete order (**Admin only**)

### 👤 Customers
- `GET /store/customers/me/` - Get customer profile
- `PUT /store/customers/me/` - Update customer profile

### ⭐ Reviews
- `GET /store/products/{id}/reviews/` - List product reviews
- `POST /store/products/{id}/reviews/` - Create a review

---

## 📌 Setup & Installation

1️⃣ **Clone the repository**
```bash
git clone <repository-url>
cd django-ecommerce-api
```

2️⃣ **Create & activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Configure database settings** in `storefront2/settings.py`

5️⃣ **Apply database migrations**
```bash
python manage.py migrate
```

6️⃣ **Create an admin user**
```bash
python manage.py createsuperuser
```

7️⃣ **Run the development server**
```bash
python manage.py runserver
```

---

## 📂 Project Structure

```
📦 django-ecommerce-api
├── 📁 core/            # Authentication & base models
├── 📁 store/           # E-commerce logic (products, orders, etc.)
├── 📁 tags/            # Content tagging system
├── 📁 likes/           # Like functionality
├── 📁 storefront2/     # Project settings & configurations
├── 📁 playground/      # Development & testing space
```

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

🚀 **Happy Coding & Build Your Own E-commerce Platform!**


