# Identity Service Design

> **Service:** Identity Service
>
> **Current Scope:** Milestone 2 - Authentication
>
> This document evolves as new milestones are completed.

---

# 1. Responsibilities

Identity Service

├── Authentication
│   ├── Register User
│   ├── Login
│   ├── Logout
│   ├── Refresh Access Token
│   └── Change Password

---

# 2. Database Design

## Tables

### User

Purpose

Stores the identity and authentication information of every platform user.

| Field | Type | Description |
|---------|------|-------------|
| id | UUID / BigAutoField | Primary Key |
| email | Email | Unique Email Address |
| username | String | Unique Username |
| password | String | Hashed Password |
| first_name | String | First Name |
| last_name | String | Last Name |
| phone_number | String | Mobile Number |
| is_active | Boolean | User Active Status |
| created_at | DateTime | Record Creation Time |
| updated_at | DateTime | Last Updated Time |

---

## Relationships

```text
User

(No relationships in Milestone 2)
```

---

## Tables Overview

| Table | Purpose |
|---------|----------|
| User | Stores user identity and authentication details |

---

# 3. API Design

## Authentication APIs

| Method | Endpoint | Purpose | Authentication | Authorization |
|----------|-------------------------|-----------------------------|----------------|----------------|
| POST | /api/v1/auth/register | Register a new user | No | Public |
| POST | /api/v1/auth/login | Authenticate user | No | Public |
| POST | /api/v1/auth/logout | Logout current user | Yes | Authenticated User |
| POST | /api/v1/auth/refresh | Refresh JWT Access Token | Yes | Authenticated User |
| POST | /api/v1/auth/change-password | Change current user's password | Yes | Authenticated User |

---

# Milestone Coverage

✅ Authentication

- Register User
- Login
- Logout
- Refresh Token
- Change Password

---

# Future Milestones

The following sections will be added later.

## User Management

- View Profile
- Update Profile
- Activate User
- Deactivate User

Additional Tables

- UserStatusHistory

Additional APIs

- GET /users/me
- PATCH /users/me
- PATCH /users/{id}/activate
- PATCH /users/{id}/deactivate

---

## Authorization

Additional Tables

- Role
- Permission
- UserRole
- RolePermission

Additional APIs

- Role Management
- Permission Management
- RBAC

---

## Audit

Additional Tables

- LoginHistory

Additional APIs

- Login History
- User Status History

---