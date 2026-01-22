import { Injectable, NotFoundException } from "@nestjs/common";
import { PrismaService } from "../prisma/prisma.service";
import { CreateTaskDto } from "./dto/create-task.dto";
import { UpdateTaskDto } from "./dto/update-task.dto";

/**
 * TasksService - The "Workers" or "Business Logic Layer"
 * This is where all the actual work happens (CRUD operations, validations, etc.)
 * Think of this as the chef in a restaurant - doing the actual cooking
 */

@Injectable()
export class TasksService {
    constructor(private prisma: PrismaService){}
    async findAll(){
        //return this.tasks;
        return this.prisma.task.findMany();
    }

    async getByID(id: number){
         const task = await this.prisma.task.findUnique({
            where: {id}
        })
        if (!task) {
            throw new NotFoundException(`Task with id ${id} not found!`);
        }

        return task
    }

    async createTask(task: CreateTaskDto){
        return this.prisma.task.create({
            data: {
                title: task.title,
                description: task.description || null,
                completed: false
            }
        });
    }

    async updateTask(id: number , data: UpdateTaskDto){
        await this.getByID(id);

        return this.prisma.task.update({
            where: {id},
            data
        });
    }
    async deleteTask(id: number){

        await this.getByID(id)

        await this.prisma.task.delete({
            where:{id}
        });
    }


    async setComplete(id: number) {
        await this.getByID(id)

        await this.prisma.task.update({
            where:{id},
            data : {
                completed: true
            }
        })
    }
}