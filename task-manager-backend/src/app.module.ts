import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import {TasksController} from './tasks.controller';
import { TasksService } from './tasks.service';
import { PrismaModule } from './prisma/prisma.module';
@Module({
  imports: [PrismaModule],
  controllers: [AppController, TasksController],
  providers: [AppService, TasksService],
})
export class AppModule {}
