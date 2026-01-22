# TaskManager

A simple task manager API built with NestJS. This repo currently contains a backend service with in-memory data storage for learning and iteration.

## Overview

- REST API for basic task CRUD
- In-memory task list (resets on server restart)
- NestJS + TypeScript

## Project Structure

- `task-manager-backend/` - NestJS API

## Getting Started

Prerequisites:
- Node.js 18+ (recommended for NestJS 11)
- npm

Install and run the API:

```bash
cd task-manager-backend
npm install
npm run start:dev
```

The server starts on `http://localhost:3000` by default.

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

This project uses in-memory data for simplicity; add a database if you want persistence.
