# TaskManager

A simple task manager API built with NestJS and Prisma. This repo currently contains a backend service backed by a local SQLite database for learning and iteration.

## Overview

- REST API for basic task CRUD
- Prisma ORM with SQLite persistence
- NestJS + TypeScript

## Project Structure

- `task-manager-backend/` - NestJS API
- `task-manager-backend/prisma/` - Prisma schema and migrations
- `task-manager-backend/dev.db` - local SQLite database (created by Prisma)

## Getting Started

Prerequisites:
- Node.js 18+ (recommended for NestJS 11)
- npm

Install and run the API:

```bash
cd task-manager-backend
npm install
npx prisma migrate dev
npm run start:dev
```

The server starts on `http://localhost:3000` by default.
The database connection string lives in `task-manager-backend/.env` (default is `DATABASE_URL="file:./dev.db"`).

## API Endpoints

- `GET /tasks` - list all tasks
- `GET /tasks/:id` - get a single task
- `POST /tasks` - create a task
- `PUT /tasks/:id` - replace a task
- `PATCH /tasks/:id` - update part of a task
- `DELETE /tasks/:id` - delete a task

Example request:

```bash
curl -X POST http://localhost:3000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Read docs","description":"NestJS basics"}'
```

## Scripts

From `task-manager-backend/`:

- `npm run start:dev` - development server with watch mode
- `npm run build` - build for production
- `npm run test` - run unit tests

## Notes

This project uses SQLite via Prisma for persistence; update `DATABASE_URL` in `task-manager-backend/.env` if you want a different database.
