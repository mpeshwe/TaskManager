# Tasks Module

Manages tasks within groups.

## Endpoints

All task endpoints are nested under groups: `/groups/:groupId/tasks`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/groups/:groupId/tasks` | List all tasks in group |
| GET | `/groups/:groupId/tasks/:id` | Get task by ID |
| POST | `/groups/:groupId/tasks` | Create task in group |
| PATCH | `/groups/:groupId/tasks/:id` | Update task fields |
| PATCH | `/groups/:groupId/tasks/:id/complete` | Mark task as complete |
| DELETE | `/groups/:groupId/tasks/:id` | Delete task |

## DTOs

### CreateTaskDto
```typescript
{
  title: string;        // required
  description?: string; // optional
}
```

### UpdateTaskDto
```typescript
{
  title?: string;       // optional
  description?: string; // optional
  completed?: boolean;  // optional
}
```

## Service Methods

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `findAll()` | - | `Task[]` | Get all tasks with group info |
| `getByID(id)` | `id: number` | `Task` | Get task by ID, throws `NotFoundException` if not found |
| `findByGroupId(groupId)` | `groupId: number` | `Task[]` | Get all tasks in a group |
| `createTask(groupId, data)` | `groupId: number, CreateTaskDto` | `Task` | Create task in group |
| `updateTask(id, data)` | `id: number, UpdateTaskDto` | `Task` | Partial update of task |
| `setComplete(id)` | `id: number` | `Task` | Mark task as completed |
| `deleteTask(id)` | `id: number` | `Task` | Delete task |

## Task Properties

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `id` | `number` | auto | Primary key |
| `title` | `string` | - | Task title |
| `description` | `string?` | `null` | Optional description |
| `completed` | `boolean` | `false` | Completion status |
| `groupId` | `number` | - | Foreign key to group |
| `createdAt` | `DateTime` | `now()` | Creation timestamp |

## Dependencies

- `GroupsService` - Used to validate group existence when creating tasks

## Files

- `tasks.controller.ts` - HTTP request handling
- `tasks.service.ts` - Business logic
- `tasks.module.ts` - Module definition
- `dto/create-task.dto.ts` - Create task validation
- `dto/update-task.dto.ts` - Update task validation
