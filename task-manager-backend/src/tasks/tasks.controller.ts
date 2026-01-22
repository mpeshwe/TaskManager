import {Controller , Get, Post, Put ,Delete, Patch,Body,  Param, NotFoundException} from '@nestjs/common';
import {TasksService} from './tasks.service'
import type {CreateTaskDto ,UpdateTaskDto} from './tasks.service'


@Controller('tasks')
export class TasksController {
    constructor(
        private readonly tasksService: TasksService
    ){}
    @Get()
    getAllTasks(){
        return this.tasksService.findAll()
    };

    @Get(':id')
    getByID(@Param('id')taskid: string){
        const taskId = parseInt(taskid);
        return this.tasksService.getByID(taskId); 
    }

    @Post()
    createTask(@Body() taskD : CreateTaskDto){
        return this.tasksService.createTask(taskD);
    }

    // @Put(':id')
    // replaceTaskById(@Param('id') taskid : string , @Body() data: ReplaceTaskDTO) {
    //     // parse taskID
    //     const taskID = parseInt(taskid)
    //     return this.tasksService.replaceTask(taskID, data);
    // }

    @Delete(':id')
    deleteTask(@Param('id') taskid: string) {
        const taskID = parseInt(taskid);
        return this.tasksService.deleteTask(taskID);
    }
    @Put(':id') 
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