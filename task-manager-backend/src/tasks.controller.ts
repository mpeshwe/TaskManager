import {Controller , Get, Post, Put ,Delete, Patch,Body,  Param, NotFoundException} from '@nestjs/common';
import {TasksService} from './tasks.service'
import type {Task , ReplaceTaskDTO , CreateTaskDto ,UpdateTaskDto} from './tasks.service'


@Controller('tasks')
export class TasksController {
    constructor(
        private readonly tasksService: TasksService
    ){};
    @Get()
    getAllTasks(): Task[]{
        return this.tasksService.findAll()
    };

    @Get(':id')
    getByID(@Param('id')taskid: string) : Task{
        const taskId = parseInt(taskid);
        return this.tasksService.getByID(taskId); 
    }

    @Post()
    createTask(@Body() taskD : CreateTaskDto): Task {
        return this.tasksService.createTask(taskD);
    }

    @Put(':id')
    replaceTaskById(@Param('id') taskid : string , @Body() data: ReplaceTaskDTO) : Task {
        // parse taskID
        const taskID = parseInt(taskid)
        return this.tasksService.replaceTask(taskID, data);
    }

    @Delete(':id')
    deleteTask(@Param('id') taskid: string): boolean {
        const taskID = parseInt(taskid);
        return this.tasksService.deleteTask(taskID);
    }

    @Patch(':id') 
    partialUpdateTask(@Param('id') taskid : string, @Body() data: UpdateTaskDto): Task {
        const taskID = parseInt(taskid);
        return this.tasksService.updateTask(taskID , data);
    }
}