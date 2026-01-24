# Task Manager API

A RESTful API for managing users, groups, and tasks built with NestJS and Prisma.

## Tech Stack

- **Framework**: NestJS
- **ORM**: Prisma
- **Database**: SQLite

## Setup

```bash
npm install
npx prisma generate
npx prisma db push
npm run start:dev
```

## API Endpoints

### Users

| Method | Endpoint | Description | Body |
|--------|----------|-------------|------|
| GET | `/users` | List all users | - |
| GET | `/users/:id` | Get user by ID | - |
| POST | `/users` | Create user | `{name, email}` |
| PUT | `/users/:id` | Update user | `{name?, email?}` |
| GET | `/users/:id/groups` | Get user's groups | - |
| DELETE | `/users/:id` | Delete user | - |

### Groups

| Method | Endpoint | Description | Body |
|--------|----------|-------------|------|
| GET | `/groups` | List all groups | - |
| GET | `/groups/:id` | Get group by ID | - |
| POST | `/groups` | Create group | `{name, description?}` |
| DELETE | `/groups/:id` | Delete group | - |
| GET | `/groups/:id/members` | Get group members | - |
| POST | `/groups/:id/members` | Add member | `{userId}` |
| DELETE | `/groups/:id/members/:userId` | Remove member | - |

### Tasks

| Method | Endpoint | Description | Body |
|--------|----------|-------------|------|
| GET | `/groups/:groupId/tasks` | List tasks in group | - |
| GET | `/groups/:groupId/tasks/:id` | Get task by ID | - |
| POST | `/groups/:groupId/tasks` | Create task | `{title, description?}` |
| PATCH | `/groups/:groupId/tasks/:id` | Update task | `{title?, description?, completed?}` |
| PATCH | `/groups/:groupId/tasks/:id/complete` | Mark complete | - |
| DELETE | `/groups/:groupId/tasks/:id` | Delete task | - |

## Data Model

```
User <---> Group (many-to-many via UserGroup)
             |
             v
           Task (one-to-many)
```

## Cascade Behavior

- **Delete User**: Removes from all groups, deletes empty groups and their tasks
- **Delete Group**: Deletes all tasks in the group
