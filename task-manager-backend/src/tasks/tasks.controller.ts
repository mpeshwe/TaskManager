import {Controller , Get, Post, Put ,Delete, Patch,Body,  Param} from '@nestjs/common';
import {TasksService} from './tasks.service'
import type { CreateTaskDto } from './dto/create-task.dto';
import type {UpdateTaskDto } from './dto/update-task.dto';

@Controller('groups/:groupId/tasks')
export class TasksController {
    constructor(
        private readonly tasksService: TasksService
    ){}
    @Get()
    getTasksByGroup(@Param('groupId') groupId: string) {
        const groupID = parseInt(groupId)
        return this.tasksService.findByGroupId(groupID)
    }
    @Get(':id')
    getByID(@Param('id')taskid: string){
        const taskId = parseInt(taskid);
        return this.tasksService.getByID(taskId); 
    }

    @Post()
    createTask(@Param('groupId') groupId: string, @Body() taskD : CreateTaskDto){
        return this.tasksService.createTask(parseInt(groupId),taskD);
    }

    
    @Delete(':id')
    deleteTask(@Param('id') taskid: string) {
        const taskID = parseInt(taskid);
        return this.tasksService.deleteTask(taskID);
    }
    @Patch(':id/complete') 
    setComplete(@Param('id') id: string) {
        const taskID = parseInt(id)
        return this.tasksService.setComplete(taskID);
    }
    @Patch(':id') 
    partialUpdateTask(@Param('id') taskid : string, @Body() data: UpdateTaskDto) {
        const taskID = parseInt(taskid);
        return this.tasksService.updateTask(taskID , data);
    }
}