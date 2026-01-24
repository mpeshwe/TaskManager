import { Injectable, NotFoundException } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import { CreateUserDto } from "./dto/create-user.dto";
import { UpdateUserDto } from "./dto/update-user.dto";


@Injectable()
export class UsersService{
    constructor(private prisma: PrismaService){}

    async getUsers(){
        return this.prisma.user.findMany();
    }

    async getById(id: number) {
        const user = await this.prisma.user.findUnique({
            where: {id}
        });

        if (!user) {
            throw new NotFoundException(`User with id ${id} not found!`);
        }

        return user
    }

    async createUser(data: CreateUserDto) {
        return this.prisma.user.create({
            data: {
                name: data.name,
                email: data.email
            }
        })
    }

    async updateUserByID(id: number, data: UpdateUserDto) {
        await this.getById(id);

        return this.prisma.user.update({
            where: {id},
            data : {
                ...data
            }
        })
    }
    async seeUserGroups(userId : number) {
        await this.getById(userId)

        return this.prisma.user.findUnique({
            where: {id: userId},
            select : {
                groups : {
                    select :{ 
                        group : {
                            select : {
                                id: true,
                                name: true
                            }
                        }
                    }
                }
            }
        })
    }
    async deleteUser(userId: number) {
        await this.getById(userId)

        const userGroups = await this.prisma.userGroup.findMany({
            where: {userId: userId},
            select: {groupId: true}
        });

        const groupIds = userGroups.map(ug => ug.groupId)

        // remove user from all these groups 

        await this.prisma.userGroup.deleteMany({
            where: {userId}
        });


        for (const groupId of groupIds) {
            const memberCount = await this.prisma.userGroup.count({
                where : {groupId}
            });

            if (memberCount === 0 ) {
                await this.prisma.group.delete(
                    {
                        where: {id: groupId}
                    }
                );
            }
        }

        return this.prisma.user.delete({
            where: { id : userId}
        });
    }
}