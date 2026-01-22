import { Injectable, NotFoundException } from "@nestjs/common";

export interface Task {
    id: number;
    title: string;
    description: string;
    completed: boolean;
}

export interface CreateTaskDto {
    title: string; 
    description: string
}

export interface ReplaceTaskDTO {
    title: string;
    description: string;
    completed: boolean;
}

export interface UpdateTaskDto {
    title? : string;
    description?: string;
    completed? : boolean
}

@Injectable()
export class TasksService {
    private tasks: Task[] = [
        {id: 1 , title: 'sample1', description:'okay',completed: false},
        {id: 2 , title: 'sample2', description:'okay',completed: false},
        {id: 3 , title: 'sample3', description: 'hmm', completed: false}
    ];

    findAll() : Task[]{
        return this.tasks;
    }

    getByID(id: number) : Task{
        // return this.tasks.find(t => t.id === id);
        const task = this.tasks.find(task => task.id === id);
        if (!task) {
            throw new NotFoundException(`Task with id ${id} not found!`);
        }

        return task
    }

    createTask(task: CreateTaskDto): Task{
        const newID = this.tasks.length +1;
        const newTask: Task = {
            id : newID,
            completed: false,
            ...task
        };

        this.tasks.push(newTask);
        return newTask;
    }

    replaceTask(taskID: number , data: ReplaceTaskDTO) :Task{
        // find task 
        const index = this.tasks.findIndex(task => task.id === taskID);
        if (index === -1) {
            // Not found
            throw new NotFoundException(`Task with ${taskID} not found!`);
        };
        this.tasks[index] = {
            ...this.tasks[index],
            ...data
        }
        return this.tasks[index];
    }
    private findTaskIndex(taskID: number) {
        return this.tasks.findIndex(task => task.id === taskID);
    }
    deleteTask(taskID: number) :boolean{
        const index = this.findTaskIndex(taskID);
        if (index === -1) {
            // Not found
            throw new NotFoundException(`Task with ${taskID} not found!`);
        };
        this.tasks.splice(index,1)

        return true
    }

    updateTask(taskID : number, data: UpdateTaskDto) : Task{
        const index = this.findTaskIndex(taskID);
        if (index === -1) {
            // Not found
            throw new NotFoundException(`Task with ${taskID} not found!`);
        };

        this.tasks[index] = {
            ...this.tasks[index],
            ...data
        }

        return this.tasks[index]
    }
}