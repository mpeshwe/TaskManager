import { Injectable, NotFoundException } from "@nestjs/common";
import { PrismaService } from "../prisma/prisma.service";
import { CreateTaskDto } from "./dto/create-task.dto";
import { UpdateTaskDto } from "./dto/update-task.dto";
import { GroupsService } from "src/groups/groups.service";

@Injectable()
export class TasksService {
    constructor(private prisma: PrismaService,private groupsService: GroupsService){}
    async findAll(){
        return this.prisma.task.findMany({
            include: {
                group : {
                    select : {
                        id : true,
                        name: true
                    }
                }
            }
        });
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
    async findByGroupId(groupId : number) {
        await this.groupsService.getById(groupId)
        return this.prisma.task.findMany(
            {
                where: {groupId}
            }
        );
    }
    async createTask(groupId: number, task: CreateTaskDto){
        
        await this.groupsService.getById(groupId)
        return this.prisma.task.create({
            data: {
                title: task.title,
                description: task.description || null,
                completed: false,
                groupId: groupId
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

        return this.prisma.task.delete({
            where:{id}
        });
    }


    async setComplete(id: number) {
        await this.getByID(id)

        return this.prisma.task.update({
            where:{id},
            data : {
                completed: true
            }
        })
    }
}