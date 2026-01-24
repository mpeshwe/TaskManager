import { Module } from "@nestjs/common";
import { PrismaModule } from "src/prisma/prisma.module";
import {GroupsController} from "./groups.controller"
import {GroupsService} from "./groups.service"
import { UsersModule } from "src/users/users.module";
@Module({
    imports: [PrismaModule, UsersModule],
    controllers: [GroupsController],
    providers: [GroupsService],
    exports: [GroupsService]
})
export class GroupsModule{}