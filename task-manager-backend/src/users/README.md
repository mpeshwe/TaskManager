# Users Module

Manages user accounts and their group memberships.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users` | List all users |
| GET | `/users/:id` | Get user by ID |
| POST | `/users` | Create user |
| PUT | `/users/:id` | Update user |
| GET | `/users/:id/groups` | Get user's groups |
| DELETE | `/users/:id` | Delete user (with cascade) |

## DTOs

### CreateUserDto
```typescript
{
  name: string;    // required
  email: string;   // required, must be valid email format
}
```

### UpdateUserDto
```typescript
{
  name?: string;   // optional
  email?: string;  // optional
}
```

## Service Methods

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `getUsers()` | - | `User[]` | Get all users |
| `getById(id)` | `id: number` | `User` | Get user by ID, throws `NotFoundException` if not found |
| `createUser(data)` | `CreateUserDto` | `User` | Create new user |
| `updateUserByID(id, data)` | `id: number, UpdateUserDto` | `User` | Update user fields |
| `seeUserGroups(userId)` | `userId: number` | `{groups: Group[]}` | Get groups user belongs to |
| `deleteUser(userId)` | `userId: number` | `User` | Delete user with cascade logic |

## Cascade Behavior

When a user is deleted:
1. User is removed from all groups (UserGroup entries deleted)
2. Any group that becomes empty (0 members) is automatically deleted
3. Tasks belonging to deleted groups are also deleted (via Prisma cascade)
4. Finally, the user record is deleted

## Files

- `users.controller.ts` - HTTP request handling
- `users.service.ts` - Business logic
- `users.module.ts` - Module definition
- `dto/create-user.dto.ts` - Create user validation
- `dto/update-user.dto.ts` - Update user validation
