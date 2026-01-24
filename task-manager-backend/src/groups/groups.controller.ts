import { Controller , Get, Post, Delete , Param, Body} from "@nestjs/common";
import {GroupsService} from "./groups.service"
import { CreateGroupDto } from "./dto/create-group.dto";
import { AddMemberDto } from "./dto/add-member.dto";
@Controller('groups') 
export class GroupsController{
    constructor(
        private groupsService: GroupsService
    ){}
    @Get()
    getAllGroups(){
        return this.groupsService.getAllGroups()
    }

    @Get(':id')
    getById(@Param('id') id : string) {
        const groupID = parseInt(id)

        return this.groupsService.getById(groupID);
    }

    @Post()
    createGroup(@Body() data: CreateGroupDto) {
        return this.groupsService.createGroup(data)
    }


    @Delete(':id') 
    deleteGroup(@Param('id') id: string) {
        const groupID = parseInt(id)

        return this.groupsService.deleteGroup(groupID)
    }

    @Post(':id/members')
    addMember(@Param('id') groupid: string, @Body() userData: AddMemberDto) {
        const groupID = parseInt(groupid)
        return this.groupsService.addMember(groupID, userData)
    }

    @Get(':id/members') 
    getMembers(@Param('id') id : string){
        const groupID  = parseInt(id) 
        return this.groupsService.getMembers(groupID)
    }

    @Delete(':id/members/:userId')
    deleteMember(@Param('id') groupId: string , @Param('userId') userId : string) {
        return this.groupsService.deleteMember(  parseInt(groupId), parseInt(userId))
    }
}