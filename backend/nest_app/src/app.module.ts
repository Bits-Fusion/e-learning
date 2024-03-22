import { Module } from '@nestjs/common';
import {VideoStreamModule} from './video-stream/video-stream.module';


@Module({
  imports: [VideoStreamModule],
})
export class AppModule {}
