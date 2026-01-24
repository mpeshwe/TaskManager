import { Get, Post, Put, Delete, Controller, Param, Body } from "@nestjs/common";
import { UsersService } from "./users.service";
import { CreateUserDto } from "./dto/create-user.dto";
import { UpdateUserDto } from "./dto/update-user.dto";
// import type { CreateTaskDto } from "src/tasks/dto/create-task.dto";

@Controller('users')
export class UsersController {
    constructor(private usersService: UsersService){}
    @Get()
    getUsers() {
        return this.usersService.getUsers();
    }

    @Get(':id')
    getById(@Param('id') id: string) {
        const userId = parseInt(id);
        return this.usersService.getById(userId);
    }

    @Put(":id")
    updateUserByID(@Param('id') id : string, @Body() data: UpdateUserDto){
        const userId = parseInt(id);

        return this.usersService.updateUserByID(userId, data);
    }
    @Post()
    createUser(@Body() data: CreateUserDto) {
        return this.usersService.createUser(data);
    }

    @Get(':id/groups')
    seeUserGroups(@Param('id') userId : string) {
        return this.usersService.seeUserGroups(parseInt(userId));
    }

    @Delete(':id')
    deleteUser(@Param('id') id: string) {
        return this.usersService.deleteUser(parseInt(id));
    }
}