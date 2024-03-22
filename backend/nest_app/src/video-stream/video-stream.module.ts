/* eslint-disable prettier/prettier */
import { Module } from '@nestjs/common';
import { VideoStreamController } from './video-stream.controller';
 
@Module({
    controllers:[VideoStreamController],
    providers:[],
})
export class VideoStreamModule {}
