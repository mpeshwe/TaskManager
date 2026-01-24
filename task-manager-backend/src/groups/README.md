# Groups Module

Manages groups and their members.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/groups` | List all groups |
| GET | `/groups/:id` | Get group by ID |
| POST | `/groups` | Create group |
| DELETE | `/groups/:id` | Delete group (cascades tasks) |
| GET | `/groups/:id/members` | Get group members |
| POST | `/groups/:id/members` | Add member to group |
| DELETE | `/groups/:id/members/:userId` | Remove member from group |

## DTOs

### CreateGroupDto
```typescript
{
  name: string;         // required
  description?: string; // optional
}
```

### AddMemberDto
```typescript
{
  userId: number;  // required, ID of user to add
}
```

## Service Methods

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `getAllGroups()` | - | `Group[]` | Get all groups |
| `getById(id)` | `id: number` | `Group` | Get group by ID, throws `NotFoundException` if not found |
| `createGroup(data)` | `CreateGroupDto` | `Group` | Create new group |
| `deleteGroup(id)` | `id: number` | `Group` | Delete group (tasks cascade) |
| `addMember(groupId, data)` | `groupId: number, AddMemberDto` | `UserGroup` | Add user to group |
| `getMembers(id)` | `id: number` | `UserGroup[]` | Get all members with user details |
| `deleteMember(groupId, userId)` | `groupId: number, userId: number` | `UserGroup` | Remove user from group |

## Cascade Behavior

When a group is deleted:
- All tasks belonging to the group are automatically deleted (Prisma `onDelete: Cascade`)
- All UserGroup memberships are removed

## Dependencies

- `UsersService` - Used to validate user existence when adding members

## Files

- `groups.controller.ts` - HTTP request handling
- `groups.service.ts` - Business logic
- `groups.module.ts` - Module definition
- `dto/create-group.dto.ts` - Create group validation
- `dto/add-member.dto.ts` - Add member validation
