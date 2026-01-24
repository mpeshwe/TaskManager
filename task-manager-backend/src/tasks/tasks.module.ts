import { Module} from "@nestjs/common";
import { TasksService } from "./tasks.service";
import { TasksController } from "./tasks.controller";
import { PrismaModule } from "../prisma/prisma.module";
import { GroupsModule } from "src/groups/groups.module";


@Module({
    imports: [PrismaModule, GroupsModule],
    controllers: [TasksController],
    providers: [TasksService],
    exports: [TasksService]
})
export class TasksModule{}