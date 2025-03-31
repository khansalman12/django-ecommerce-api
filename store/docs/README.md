# Store App

The core e-commerce functionality module of the Django E-commerce API project.

## Overview

The Store app handles all the essential e-commerce functionality including products, collections, carts, orders, and customers. It provides a complete set of API endpoints for building an e-commerce platform.

## Models

- **Product**: Represents products available in the store
- **Collection**: Groups of related products
- **Customer**: User profile with purchase history and membership status
- **Cart**: Shopping carts for storing items before purchase
- **CartItem**: Individual items in a cart with quantities
- **Order**: Customer orders with payment status
- **OrderItem**: Individual items within an order
- **Address**: Customer shipping addresses
- **Review**: Product reviews submitted by customers
- **Promotion**: Product promotions and discounts

## Key Features

### Product Management
- Full CRUD operations for products
- Search, filter, and sorting capabilities
- Product inventory tracking
- Product reviews and ratings

### Collection Management
- Organize products into collections
- Featured products in collections
- Collection product counts

### Shopping Cart System
- Create and manage shopping carts
- Add, update and remove items
- Calculate totals and track quantities

### Order Processing
- Convert carts to orders
- Track order status and payment status
- Order history per customer

### Customer Profiles
- Membership tiers (Bronze, Silver, Gold)
- Customer purchase history
- Custom admin view for orders

## API Endpoints

### Products
- `GET /store/products/` - List all products with filtering
- `GET /store/products/{id}/` - Get product details
- `POST /store/products/` - Create new product (admin only)
- `PUT /store/products/{id}/` - Update product (admin only)
- `DELETE /store/products/{id}/` - Delete product (admin only)

### Collections
- `GET /store/collections/` - List all collections
- `GET /store/collections/{id}/` - Get collection details
- `POST /store/collections/` - Create new collection (admin only)
- `PUT /store/collections/{id}/` - Update collection (admin only)
- `DELETE /store/collections/{id}/` - Delete collection (admin only)

### Carts
- `POST /store/carts/` - Create a cart
- `GET /store/carts/{id}/` - Get cart details
- `DELETE /store/carts/{id}/` - Delete cart

### Cart Items
- `GET /store/carts/{id}/items/` - List items in cart
- `POST /store/carts/{id}/items/` - Add item to cart
- `PATCH /store/carts/{id}/items/{id}/` - Update cart item quantity
- `DELETE /store/carts/{id}/items/{id}/` - Remove item from cart

### Orders
- `GET /store/orders/` - List customer orders
- `POST /store/orders/` - Create an order
- `GET /store/orders/{id}/` - Get order details
- `PATCH /store/orders/{id}/` - Update order status (admin only)
- `DELETE /store/orders/{id}/` - Delete order (admin only)

### Customers
- `GET /store/customers/` - List all customers (admin only)
- `GET /store/customers/me/` - Get customer profile
- `PUT /store/customers/me/` - Update customer profile

### Reviews
- `GET /store/products/{id}/reviews/` - List reviews for a product
- `POST /store/products/{id}/reviews/` - Create review for a product

## Custom Admin Features

- Custom inventory filter for products
- Inline order items in order admin
- Actions for bulk updating inventory
- Custom display for product inventory status
- Links between related models in admin