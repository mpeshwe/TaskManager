import {Injectable, NotFoundException } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import { CreateGroupDto } from "./dto/create-group.dto";
import { AddMemberDto } from "./dto/add-member.dto";
import { UsersService } from "src/users/users.service";

@Injectable() 
export class GroupsService {
    constructor(
        private prisma : PrismaService,
        private userService : UsersService
    ){}

    async getAllGroups () {
        return this.prisma.group.findMany()
    }

    async getById(id: number) {
        const group = await this.prisma.group.findUnique({
            where: {id}
        })
        if (!group) {
            throw new NotFoundException(`Group with ID ${id} not found!`);
        }

        return group
    }

    async createGroup(data: CreateGroupDto){
        return this.prisma.group.create({
            data:{
                ...data
            }
        })
    }

    async deleteGroup(id: number) {
        await this.getById(id);

        return this.prisma.group.delete({
            where:{id}
        })
    }

    async addMember(groupID: number, userData: AddMemberDto) {
        await this.getById(groupID)
        const user = await this.userService.getById(userData.userId)

        return this.prisma.userGroup.create({
            data:{
                groupId: groupID,
                userId : user.id
            }
        })
    }

    async getMembers (id : number) {
        await this.getById(id)
        
        return this.prisma.userGroup.findMany({
            where: {groupId : id},
            include : {
                user: true
            }
        })
    }

    async deleteMember(groupID: number , userID :number) {
        const group = await this.getById(groupID)
        const user  = await this.userService.getById(userID)

        return this.prisma.userGroup.delete ({
            where: {
                userId_groupId: {
                    userId: userID,
                    groupId: groupID
                }
            }
        })
    }
}